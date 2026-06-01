import streamlit as st

from search import web_search
from llm import generate_answer

st.title("Real-Time Research Copilot")

question = st.text_input(
    "Ask a question"
)

if st.button("Search"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        with st.spinner("Researching..."):

            search_results = web_search(question)

            answer = generate_answer(
                question,
                search_results["results"]
            )

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        for item in search_results["results"]:
            st.markdown(
                f"- [{item['title']}]({item['url']})"
        )