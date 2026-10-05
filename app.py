import streamlit as st
import re

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Missing Information Detection System",
    page_icon="🔍",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------
st.title("🔍 AI Missing-Information Detection System")
st.write(
    "Enter a document or personal-information text below. "
    "The system will detect available and missing information."
)

# -------------------------------
# Required Information
# -------------------------------
required_fields = {
    "Name": r"\b(name|full name)\s*[:\-]\s*\S+",
    "Email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "Phone": r"\b(?:\+91[\s-]?)?[6-9]\d{9}\b",
    "Address": r"\b(address|location)\s*[:\-]\s*\S+",
    "Date of Birth": r"\b(date of birth|dob)\s*[:\-]\s*\S+",
    "Gender": r"\b(gender|sex)\s*[:\-]\s*(male|female|other)\b",
    "College": r"\b(college|university|institution)\s*[:\-]\s*\S+",
    "Qualification": r"\b(qualification|degree|education)\s*[:\-]\s*\S+",
    "Skills": r"\b(skills?)\s*[:\-]\s*\S+"
}

# -------------------------------
# Text Input
# -------------------------------
text = st.text_area(
    "📄 Enter your document information:",
    height=300,
    placeholder="""Example:

Name: Harika
Age: 19
Email: harika@gmail.com
Phone:
Address: Hyderabad
Date of Birth:
Gender: Female
College: ABC Engineering College
Qualification: B.Tech
Skills: Python, Java"""
)

# -------------------------------
# Detection Function
# -------------------------------
def detect_missing_information(text):

    available = []
    missing = []

    for field, pattern in required_fields.items():

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            available.append(field)
        else:
            missing.append(field)

    return available, missing


# -------------------------------
# Analyze Button
# -------------------------------
if st.button("🔎 Detect Missing Information"):

    if not text.strip():

        st.warning("⚠️ Please enter some information first.")

    else:

        available, missing = detect_missing_information(text)

        st.subheader("📊 Detection Result")

        # -------------------------------
        # Statistics
        # -------------------------------
        total = len(required_fields)
        available_count = len(available)
        missing_count = len(missing)

        completeness = (available_count / total) * 100

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Information Available",
                available_count
            )

        with col2:
            st.metric(
                "Information Missing",
                missing_count
            )

        with col3:
            st.metric(
                "Completeness",
                f"{completeness:.1f}%"
            )

        # -------------------------------
        # Available Information
        # -------------------------------
        st.subheader("✅ Available Information")

        if available:

            for field in available:
                st.success(f"✓ {field}")

        else:

            st.info("No required information detected.")

        # -------------------------------
        # Missing Information
        # -------------------------------
        st.subheader("❌ Missing Information")

        if missing:

            for field in missing:
                st.error(f"✗ {field}")

        else:

            st.success(
                "🎉 No required information is missing!"
            )

        # -------------------------------
        # Completeness Progress
        # -------------------------------
        st.subheader("📈 Information Completeness")

        st.progress(completeness / 100)

        if completeness == 100:

            st.success(
                "The document appears to contain all required information."
            )

        elif completeness >= 70:

            st.warning(
                "The document is mostly complete, but some information is missing."
            )

        else:

            st.error(
                "The document contains significant missing information."
            )