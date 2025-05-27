import streamlit as st
from toxic_detector import is_toxic
from polite_rewriter import polish_text

st.set_page_config(page_title="Email Toxicity Auto-Polisher", layout="wide")

# Custom CSS for UI
st.markdown("""
    <style>
        .title { font-size: 2.3rem; font-weight: bold; color: #2f80ed; }
        .subtitle { font-size: 1.1rem; color: #666; }
        .box {
            padding: 1rem;
            border-radius: 10px;
            background-color: #f9f9f9;
            border-left: 5px solid #2f80ed;
            color: #111; /* Set text color to dark */
            font-size: 1rem;
        }
        .toxic {
            background-color: #fff1f0;
            border-left-color: #ff4d4f;
        }
        .polite {
            background-color: #f6ffed;
            border-left-color: #52c41a;
        }
        .label {
            font-weight: 600;
            font-size: 1rem;
            margin-top: 1rem;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📬 Email Toxicity Auto-Polisher</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Detects rude tone and rewrites it more politely using AI.</div>', unsafe_allow_html=True)

email_text = st.text_area("✉️ Enter your email message:", height=150)

if st.button("✨ Polish it!"):
    if not email_text.strip():
        st.warning("Please enter an email.")
    else:
        label, score = is_toxic(email_text)
        st.markdown(f"**🧪 Detected Tone:** `{label.upper()}` — Confidence: `{score:.2f}`")
        st.progress(score)

        if label.lower() == "toxic":
            polished = polish_text(email_text)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="label">🟥 Original</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="box toxic">{email_text}</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="label">🟩 Polished</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="box polite">{polished}</div>', unsafe_allow_html=True)
        else:
            st.success("🎉 Your email already sounds polite!")
