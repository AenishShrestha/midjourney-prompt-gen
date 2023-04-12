import streamlit as st
from transformers import pipeline, set_seed
import random
import re

gpt2_pipe = pipeline('text-generation', model='succinctly/text2image-prompt-generator')

def generate(starting_text):
    for count in range(6):
        seed = random.randint(100, 1000000)
        set_seed(seed)
    
        if starting_text == "":
            starting_text: str = line[random.randrange(0, len(line))].replace("\n", "").lower().capitalize()
            starting_text: str = re.sub(r"[,:\-–.!;?_]", '', starting_text)
            print(starting_text)
    
        response = gpt2_pipe(starting_text, max_length=random.randint(60, 90), num_return_sequences=8)
        response_list = []
        for x in response:
            resp = x['generated_text'].strip()
            if resp != starting_text and len(resp) > (len(starting_text) + 4) and resp.endswith((":", "-", "—")) is False:
                response_list.append(resp)
    
        response_end = "\n".join(response_list)
        response_end = re.sub('[^ ]+\.[^ ]+','', response_end)
        response_end = response_end.replace("<", "").replace(">", "")
        if response_end != "":
            return response_end
        if count == 5:
            return response_end

st.set_page_config(page_title="Midjourney Prompt Generator", page_icon=":rocket:", layout="centered")
st.title("Midjourney Prompt Generator")
st.subheader("This is an unofficial demo for Midjourney Prompt Generator. To use it, simply send your text, or click one of the examples to load them. Read more at the links below.")
st.write("Model: [Hugging Face](https://huggingface.co/succinctly/text2image-prompt-generator)")
st.write("Telegram bot: [Prompt Generator Bot](https://t.me/prompt_generator_bot)")
st.write("[![](https://img.shields.io/twitter/follow/DoEvent?label=@DoEvent&style=social)](https://twitter.com/DoEvent)")

starting_text = st.text_input("English", "English Text here")
if st.button("Generate"):
    generated_text = generate(starting_text)
    st.write("Generated Text:")
    st.write(generated_text)
