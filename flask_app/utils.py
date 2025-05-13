import os
import openai
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from dotenv import load_dotenv

load_dotenv() 

openai.api_key = os.getenv("OPENAI_API_KEY")


def search_and_scrape(query, num_results=3):
    """Search Google and scrape top articles."""
    links = list(search(query, num_results=num_results))
    articles = []

    for url in links:
        try:
            print(f"Fetching content from: {url}")
            res = requests.get(url, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')
            title = soup.title.string.strip() if soup.title else "Untitled"
            paragraphs = soup.find_all('p')
            content = "\n".join(p.get_text() for p in paragraphs)
            articles.append({
                "title": title,
                "link": url,
                "content": content
            })
        except Exception as e:
            print(f"Failed to fetch from {url}: {e}")
            continue

    return articles

def process_text(articles, max_chars=4000):
    """Concatenate article content into a single context string (for LLM)."""
    context = ""
    for article in articles:
        content = article.get("content", "")
        if len(context) + len(content) < max_chars:
            context += content + "\n\n"
        else:
            break
    return context.strip()

def generate_response(query, context, articles):
    """Generate a response using OpenAI, or fallback to scraped content."""
    try:
        print("→ Using OpenAI GPT model...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are an expert assistant."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
            ],
            max_tokens=500,
            temperature=0.7
        )

        generated = response.choices[0].message['content'].strip()
        result = f"🔍 **Answer from OpenAI:**\n\n{generated}\n\n"

        result += "📚 **Sources Used:**\n"
        for article in articles:
            result += f"- [{article.get('title', 'Untitled')}]({article.get('link', '')})\n"

        return result

    except Exception as e:
        print(f"[OpenAI API ERROR] {e}")
        print("Falling back to displaying scraped content.\n")

        fallback = "⚠️ **OpenAI failed. Showing scraped content only.**\n\n"
        for article in articles:
            fallback += f"📖 **{article.get('title', 'Untitled')}**\n🔗 {article.get('link', '')}\n\n"
            content = article.get("content", "No content available.")[:800]
            fallback += content.strip() + "\n\n---\n\n"
        return fallback
