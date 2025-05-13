
# LLM-Powered Search Assistant

This project is a prototype system designed to retrieve relevant information from the internet and generate user-friendly answers using a Large Language Model (LLM). It combines web scraping, text processing, and LLM-based summarization — all presented through a clean Streamlit interface.

---

## 🔧 Project Structure

- **Backend**: Fetches top search results from the web, extracts meaningful content, and optionally sends it to an LLM.
- **Frontend (Streamlit)**: Allows users to enter queries and view either LLM-generated answers or raw scraped content.

---

## ⚙️ How It Works

1. **User submits a query** through the web interface.
2. **The backend searches the web** for that query and retrieves relevant pages.
3. **Scraped content** is processed and cleaned (headings, paragraphs, etc.).
4. **The system attempts to generate an answer using OpenAI GPT**, but due to limitations (no paid OpenAI account), this step currently returns fallback content.
5. **Final output** (either scraped or LLM-generated) is shown to the user.

---

## ❗ Note on OpenAI Usage

Although the system is integrated with OpenAI's GPT model, **response generation is disabled** in this version due to the absence of a valid (paid) OpenAI API key. This has been intentionally left this way to avoid misuse or billing issues.

> 🟡 Instead of the LLM response, the system gracefully falls back to displaying the processed, scraped content.

---

## 🚀 Features

- Web search and scraping using `serpapi` and `BeautifulSoup`
- Clean text extraction: removes ads, scripts, and irrelevant content
- Option to generate an answer using GPT (if API key is added)
- Simple and responsive Streamlit interface
- Error handling for missing API keys or content

---

## 🧪 Setup Instructions

1. **Clone the repo**

```bash
git clone https://https://github.com/BharatDhande/LLM-Assignment-Clean
cd llm_search_template

