import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

import streamlit as st
import requests

# API_URL = "http://localhost:8000/research"
# API_URL = "http://127.0.0.1:8000/research"
API_URL = "https://autonomous-research-assistant-c47v.onrender.com/research"
st.set_page_config(page_title="Autonomous Research Assistant", layout="wide")

st.title("🧠 Autonomous Research Assistant")
st.write("Agentic RAG System with Verification & Citations")

query = st.text_area("Enter your research question:", height=100)

if st.button("Generate Report"):

    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        with st.spinner("Running multi-agent research pipeline..."):
            response = requests.post(API_URL, json={"query": query})

            if response.status_code == 200:
                data = response.json()

                st.success("Research Complete ✅")

                st.markdown("## 📄 Research Report")
                st.markdown(data["report"], unsafe_allow_html=True)

                st.markdown("## 🔗 Sources")
                for src in data["sources"]:
                    st.write(src)
            else:
                st.error(f"Backend error: {response.status_code}")
                st.write(response.text)