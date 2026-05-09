import streamlit as st
import pandas as pd

from utils.extract_text import extract_text_from_pdf
from utils.claims import extract_claims
from utils.verify import verify_claim

st.title("AI Fact-Check Agent")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    st.info("Extracting text from PDF...")

    text = extract_text_from_pdf(uploaded_file)

    st.info("Finding factual claims...")

    claims = extract_claims(text)

    results = []

    for item in claims:

        claim = item["claim"]

        with st.spinner(f"Verifying: {claim}"):

            verdict = verify_claim(claim)

            results.append({
                "Claim": claim,
                "Verification": verdict
            })

    df = pd.DataFrame(results)

    st.dataframe(df)