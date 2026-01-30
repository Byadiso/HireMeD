# 🤖 Autonomous IT Career Discovery Engine

[![Job Search Bot](https://github.com/Byadiso/HireMeD/actions/workflows/job_hunt.yml/badge.svg)](https://github.com/Byadiso/HireMeD/actions/workflows/job_hunt.yml)
![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Market](https://img.shields.io/badge/Market-Poland-red.svg)

A sophisticated Python-based automation pipeline that uses **Natural Language Processing (NLP)** and **Cloud Computing** to identify high-value career opportunities in the Polish IT market.

---

## 🛠️ The Technology Stack

| Category | Tools | Badges |
| :--- | :--- | :--- |
| **Language** | Python 3.10 | ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) |
| **Automation** | Playwright | ![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=Playwright&logoColor=white) |
| **Cloud/DevOps** | GitHub Actions | ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=flat&logo=githubactions&logoColor=white) |
| **NLP** | Scikit-Learn | ![SciKit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white) |
| **Data** | Pandas, Openpyxl | ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white) |
| **UI** | Streamlit | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white) |

---

## 🔄 How It Works



1. **Sourcing:** The script fetches live job data from Adzuna APIs.
2. **Scraping:** Headless Chromium (**Playwright**) extracts full job descriptions, bypassing superficial snippets and handling complex redirects.
3. **Cross-Language Match:** Integrated `deep-translator` converts Polish descriptions to English in real-time to match my English resume.
4. **Scoring:** An NLP algorithm calculates the **Cosine Similarity** between provided resume and the job requirements, applying weighted bonuses for key technical skills like Python, SQL, and Active Directory.
5. **Alerting:** High-match roles (Score > 50%) are instantly pushed to the mobile via a custom **Telegram Bot**.
6. **Persistence:** Data is logged into an Excel database, which powers a live analytics dashboard.

---

## ☁️ Cloud Deployment (GitHub Actions)

This project is deployed using **GitHub Actions**. It runs on a headless Ubuntu environment every 30 minutes. 



- **Secrets Management:** Sensitive keys (API IDs, Bot Tokens) are handled via GitHub encrypted secrets.
- **Automated Commits:** The pipeline automatically commits updated job listings back to the repository, keeping the database current without manual intervention.

---

## 🚀 Impact

By treating the job search as a technical engineering problem, you will:
- **Reduce manual search time by 90%.**
- **Eliminate language barriers** between  EN resume and PL job postings.
- **Improve accuracy** by focusing only on roles where technical background provides the highest value.

---

## 📂 Quick Start

1. **Clone:** `git clone https://github.com/Byadiso/HireMeD.git`
2. **Setup Secrets:** Add `ADZUNA_APP_ID`, `ADZUNA_APP_KEY`, `TELEGRAM_TOKEN`, and `TELEGRAM_CHAT_ID` to your GitHub Repo Secrets.
3. **Resume:** Replace `my_resume.pdf` with your own.
4. **Run UI:** `streamlit run dashboard.py`
