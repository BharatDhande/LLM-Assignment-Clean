from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from utils import search_and_scrape, process_text, generate_response

# Load environment variables from .env file
load_dotenv()

# Flask app setup
app = Flask(__name__)
CORS(app)

@app.route('/query', methods=['POST'])
def query():
    """
    Handles POST requests to '/query'. Extracts the query from the request,
    performs search, scraping, processing, and LLM generation (or fallback),
    and returns the response in JSON format.
    """
    data = request.get_json()
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    print(f"\nReceived query: {user_query}")

    # Step 1: Search and scrape
    print("→ Step 1: Searching and scraping articles...")
    articles = search_and_scrape(user_query)

    if not articles:
        return jsonify({"error": "No relevant content found."}), 404

    # Step 2: Process scraped content
    print("→ Step 2: Processing content...")
    context = process_text(articles)

    # Step 3: Generate LLM response (with fallback)
    print("→ Step 3: Generating response from LLM...")
    answer = generate_response(user_query, context, articles)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
