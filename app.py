import streamlit as st
from toxic_detector import is_toxic
from polite_rewriter import polish_text

# Page configuration
st.set_page_config(page_title="Email Toxicity Auto-Polisher", layout="wide")

# Custom styles
st.markdown("""
    <style>
        .title { font-size: 2.2rem; font-weight: bold; color: #2f80ed; }
        .subtitle { font-size: 1.1rem; color: #444; }
        .box {
            padding: 1rem;
            border-radius: 12px;
            background-color: #f9f9f9;
            border-left: 5px solid #2f80ed;
        }
        .toxic-box {
            background-color: #fff1f0;
            border-left: 5px solid #ff4d4f;
        }
        .polite-box {
            background-color: #f6ffed;
            border-left: 5px solid #52c41a;
        }
        .output-label {
            font-weight: bold;
            font-size: 1rem;
            color: #555;
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown('<div class="title">📬 Email Toxicity Auto-Polisher</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Paste a message and we\'ll help rewrite it more politely.</div>', unsafe_allow_html=True)
st.markdown("---")

# Input
email_text = st.text_area("✉️ Enter your email message:", height=150)

if st.button("✨ Polish it!"):
    if email_text.strip() == "":
        st.warning("Please enter an email message.")
    else:
        label, score = is_toxic(email_text)
        st.markdown("### 🧪 Detected Tone")
        st.markdown(f"**Tone:** `{label.upper()}`  &nbsp;&nbsp; 🎯 **Confidence:** `{score:.2f}`")
        st.progress(min(score, 1.0))

        # Output section
        if label.lower() == "toxic":
            polished = polish_text(email_text)

            st.markdown("### ✅ Result Comparison")
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="output-label">🟥 Original Message</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="box toxic-box">{email_text}</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="output-label">🟩 Polished Message</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="box polite-box">{polished}</div>', unsafe_allow_html=True)

        else:
            st.success("🎉 Your email already sounds polite!")
