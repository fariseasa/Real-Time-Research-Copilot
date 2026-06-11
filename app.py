import streamlit as st
import os

from search import (
    web_search,
    format_results
)

from llm import generate_answer

from rag import (
    load_pdf,
    chunk_text,
    build_faiss_index,
    rag_answer
)

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Real-Time Research Copilot",
    page_icon="🔍",
    layout="wide"
)

# ---------------------------
# HEADER
# ---------------------------

st.title("🔍 Real-Time Research Copilot")

st.caption(
    "AI-powered research assistant using Tavily, FAISS, RAG and Groq"
)

# ---------------------------
# SIDEBAR
# ---------------------------

st.sidebar.title("🔍 Research Copilot")

st.sidebar.markdown("---")

mode = st.sidebar.radio(
    "Choose Mode",
    ["🌐 Web Research", "📄 PDF Research"]
)

st.sidebar.markdown("---")

# ==================================================
# WEB RESEARCH MODE
# ==================================================

if mode == "🌐 Web Research":

    st.info(
        "Ask questions and get answers using real-time web search."
    )

    question = st.chat_input(
        "Ask anything..."
    )

    if question:

        with st.chat_message("user"):
            st.write(question)

        with st.spinner("Researching..."):

            search_results = web_search(question)

            context = format_results(
                search_results
            )

            answer = generate_answer(
                question,
                context
            )

        with st.chat_message("assistant"):
            st.write(answer)

        st.divider()

        st.subheader("📚 Sources")

        for item in search_results["results"]:

            st.markdown(
                f"- [{item['title']}]({item['url']})"
            )

# ==================================================
# PDF RESEARCH MODE
# ==================================================

elif mode == "📄 PDF Research":

    st.sidebar.subheader(
        "Upload PDF"
    )

    uploaded_file = st.sidebar.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    # Clear old PDF data if removed

    if uploaded_file is None:

        st.session_state.pop(
            "index",
            None
        )

        st.session_state.pop(
            "chunks",
            None
        )

        st.session_state.pop(
            "current_pdf",
            None
        )

    # New PDF uploaded

    if uploaded_file:

        if (
            "current_pdf"
            not in st.session_state
            or
            st.session_state["current_pdf"]
            != uploaded_file.name
        ):

            st.session_state.pop(
                "index",
                None
            )

            st.session_state.pop(
                "chunks",
                None
            )

            st.session_state[
                "current_pdf"
            ] = uploaded_file.name

        st.sidebar.success(
            f"Loaded: {uploaded_file.name}"
        )

        if st.sidebar.button(
            "Process PDF"
        ):

            os.makedirs(
                "data",
                exist_ok=True
            )

            pdf_path = os.path.join(
                "data",
                uploaded_file.name
            )

            with open(
                pdf_path,
                "wb"
            ) as f:

                f.write(
                    uploaded_file.getbuffer()
                )

            with st.spinner(
                "Processing PDF..."
            ):

                text = load_pdf(
                    pdf_path
                )

                chunks = chunk_text(
                    text
                )

                index, embeddings = (
                    build_faiss_index(
                        chunks
                    )
                )

                st.session_state[
                    "chunks"
                ] = chunks

                st.session_state[
                    "index"
                ] = index

            st.success(
                "PDF processed successfully!"
            )

    # No PDF processed

    if "index" not in st.session_state:

        st.info(
            "Upload and process a PDF to start asking questions."
        )

    # PDF Ready

    else:

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Chunks Created",
                len(
                    st.session_state[
                        "chunks"
                    ]
                )
            )

        with col2:

            st.metric(
                "Status",
                "Ready"
            )

        pdf_question = st.chat_input(
            "Ask a question about the PDF..."
        )

        if pdf_question:

            with st.chat_message(
                "user"
            ):
                st.write(
                    pdf_question
                )

            with st.spinner(
                "Searching PDF..."
            ):

                answer = rag_answer(
                    pdf_question,
                    st.session_state[
                        "index"
                    ],
                    st.session_state[
                        "chunks"
                    ]
                )

            with st.chat_message(
                "assistant"
            ):
                st.write(
                    answer
                )