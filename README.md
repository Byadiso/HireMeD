# 🤖 Autonomous IT Career Discovery Engine

A sophisticated Python-based automation pipeline that uses **Natural Language Processing (NLP)** and **Cloud Computing** to identify high-value career opportunities in the Polish IT market.



## 🛠️ The Technology Stack
* **Engine:** Python 3.10
* **Web Automation:** Playwright (Dynamic scraping & redirect handling)
* **NLP:** Scikit-Learn (TF-IDF Vectorization & Cosine Similarity)
* **Cloud/DevOps:** GitHub Actions (Automated scheduling & execution)
* **Translation:** Deep Translator (Cross-language matching for PL/EN)
* **UI:** Streamlit (Visual Analytics Dashboard)

## 🔄 How It Works
1.  **Sourcing:** The script fetches live job data from Adzuna APIs.
2.  **Scraping:** Headless Chromium (Playwright) extracts full job descriptions, bypassing superficial snippets.
3.  **Cross-Language Match:** Polish descriptions are translated to English in real-time.
4.  **Scoring:** An NLP algorithm calculates the similarity between my resume and the job requirements, applying weighted bonuses for key technical skills.
5.  **Alerting:** High-match roles (Score > 50%) are instantly pushed to my mobile via a Telegram Bot.
6.  **Persistence:** All data is logged into an Excel-based database, which powers the live Streamlit dashboard.



## ☁️ Cloud Deployment (GitHub Actions)
This project is deployed using GitHub Actions. It runs on a headless Ubuntu environment every 30 minutes, ensuring that I am the first to know when a relevant "IT Specialist" or "Support" role is posted. 

## 🚀 Impact
By treating my job search as a technical engineering problem, I reduced manual searching time by 90% and ensured that I only focus on roles where my technical background provides the highest value to the employer.