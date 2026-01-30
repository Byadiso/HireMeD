import os
import requests
import pandas as pd
import time
from playwright.sync_api import sync_playwright
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
from dotenv import load_dotenv
from deep_translator import GoogleTranslator

# Load local .env (only used when running on your computer)
load_dotenv()

# --- CONFIGURATION ---
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

RESUME_PATH = "my_resume.pdf"
EXCEL_FILE = "job_listings.xlsx"
COUNTRY_CODE = "pl" 

# --- 1. NLP & TRANSLATION ---
def get_resume_text(path):
    try:
        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            return " ".join([page.extract_text() for page in reader.pages if page.extract_text()]).lower()
    except: return ""

def translate_text(text):
    try:
        if len(text) > 4000: text = text[:4000]
        return GoogleTranslator(source='auto', target='en').translate(text)
    except: return text

def get_match_score(resume_text, job_desc):
    if not job_desc or not resume_text: return 0
    translated_desc = translate_text(job_desc).lower()
    
    try:
        vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
        vectors = vectorizer.fit_transform([resume_text, translated_desc])
        base_score = cosine_similarity(vectors)[0][1] * 100

        # Technical Keyword Boost
        boost_keywords = ["python", "sql", "active directory", "linux", "helpdesk", "support"]
        bonus = sum(7 for word in boost_keywords if word in translated_desc)
        
        return round(min((base_score * 0.6) + bonus, 100), 2)
    except: return 0

# --- 2. PIPELINE ---
def run_pipeline():
    print("🚀 Starting Cloud Pipeline...")
    resume_text = get_resume_text(RESUME_PATH)
    if not resume_text: return

    # Fetch Jobs
    all_jobs = []
    roles = ["IT Specialist", "IT Support"]
    for role in roles:
        url = f"https://api.adzuna.com/v1/api/jobs/{COUNTRY_CODE}/search/1"
        params = {'app_id': ADZUNA_APP_ID, 'app_key': ADZUNA_APP_KEY, 'results_per_page': 5, 'what': role}
        try:
            res = requests.get(url, params=params).json()
            all_jobs.extend(res.get('results', []))
        except: continue

    processed = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        
        for job in all_jobs:
            link = job.get('redirect_url')
            try:
                page.goto(link, timeout=20000, wait_until="domcontentloaded")
                time.sleep(2)
                full_text = page.inner_text("body")
            except: full_text = job.get('description', '')

            score = get_match_score(resume_text, full_text)
            entry = {"id": job.get('id'), "Title": job.get('title'), "Company": job.get('company', {}).get('display_name'), "Match_Score": score, "Link": link}
            processed.append(entry)

            if score >= 50:
                msg = f"🔥 Match {score}%: {entry['Title']} @ {entry['Company']}\n{link}"
                requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": msg})
        browser.close()

    if processed:
        df_new = pd.DataFrame(processed)
        if os.path.exists(EXCEL_FILE):
            df_old = pd.read_excel(EXCEL_FILE)
            df_final = pd.concat([df_old, df_new]).drop_duplicates(subset=['id'], keep='last')
            df_final.to_excel(EXCEL_FILE, index=False)
        else:
            df_new.to_excel(EXCEL_FILE, index=False)
    print("✅ Done.")

if __name__ == "__main__":
    run_pipeline()