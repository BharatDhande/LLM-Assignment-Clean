import streamlit as st
import requests

st.set_page_config(page_title="LLM-based RAG Search", layout="centered")
st.title("🧠 LLM-based RAG Search Engine")

# Input for user query
query = st.text_input("Enter your query:")

if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        # Call the Flask API
        flask_url = "http://localhost:5001/query"  # Update if running on different host/port
        print("Accessing", flask_url, "with query", query)

        try:
            response = requests.post(flask_url, json={"query": query})

            if response.status_code == 200:
                # Display the generated answer
                answer = response.json().get('answer', "No answer received.")
                st.success("Generated Answer:")
                st.write(answer)
            else:
                st.error(f"Error {response.status_code}: Could not retrieve a valid response from the backend.")

        except Exception as e:
            st.error(f"Request failed: {e}")
