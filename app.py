import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model & tokenizer once
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("vennify/t5-base-grammar-correction")
    model = AutoModelForSeq2SeqLM.from_pretrained("vennify/t5-base-grammar-correction")
    return tokenizer, model

tokenizer, model = load_model()

def polish_text(text):
    input_text = f"grammar: {text}"
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    outputs = model.generate(**inputs, max_length=512, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# UI Setup
st.markdown("# 📬 Email Toxicity Auto-Polisher")
st.markdown("Paste a message and we'll help rewrite it more politely.")

# Input
user_input = st.text_area("✉️ Enter your email message:", height=150)

# Detect tone (placeholder — extend later with real model)
def detect_tone(text):
    # Placeholder: integrate a model like detoxify later
    return "toxic", 0.00

if st.button("Polish Text"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        with st.spinner("Analyzing and polishing your message..."):
            tone, confidence = detect_tone(user_input)
            polished = polish_text(user_input)

        st.markdown(f"### 🧪 Detected Tone: **{tone}** — Confidence: `{confidence:.2f}`")
        st.markdown("### ✅ Polished Version:")
        st.success(polished)
