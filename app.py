import streamlit as st
from toxic_detector import is_toxic
from polite_rewriter import polish_text

# Page config
st.set_page_config(page_title="Email Toxicity Auto-Polisher", layout="wide")

st.markdown("""
    <style>
        .main { background-color: #f5f7fa; }
        .title { font-size: 2.5rem; font-weight: bold; color: #1f77b4; }
        .sub { font-size: 1.2rem; color: #4a4a4a; }
        .tox-box { background-color: #fff3f3; border-left: 5px solid #ff4d4f; padding: 10px 15px; border-radius: 8px; }
        .success-box { background-color: #f6ffed; border-left: 5px solid #52c41a; padding: 10px 15px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📬 Email Toxicity Auto-Polisher</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Paste a message and we\'ll help rewrite it more politely.</div>', unsafe_allow_html=True)

st.markdown("---")

# Input field
email_text = st.text_area("✉️ Enter your email message:", height=150)

# Button
if st.button("✨ Polish it!"):
    if email_text.strip() == "":
        st.warning("Please enter an email.")
    else:
        label, score = is_toxic(email_text)

        st.markdown("### 🧪 Detected Tone")
        st.markdown(f"**Tone:** `{label.upper()}`  &nbsp;&nbsp;&nbsp; 🎯 **Confidence:** `{score:.2f}`")
        st.progress(min(score, 1.0))

        if label == "toxic":
            polished = polish_text(email_text)

            st.markdown("### ✅ Result")
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 🟥 Original")
                st.markdown(f'<div class="tox-box">{email_text}</div>', unsafe_allow_html=True)

            with col2:
                st.markdown("#### 🟩 Polished")
                st.markdown(f'<div class="success-box">{polished}</div>', unsafe_allow_html=True)
        else:
            st.info("Your email already looks polite 😊")


