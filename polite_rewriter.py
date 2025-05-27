from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Model for grammar correction
model_name = "vennify/t5-base-grammar-correction"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def polish_text(text):
    input_text = f"grammar: {text}"

    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding="max_length"
    )

    outputs = model.generate(
        **inputs,
        max_length=512,
        num_beams=4,
        early_stopping=True
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example
text = "This are a sentence with bad grammar and also extra word."
print("Original:", text)
print("Polished:", polish_text(text))
