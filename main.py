
import openai
import streamlit as st

openai.api_key = "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"
model_engine = "gpt-3.5-turbo"

def generate_text(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text
    return message.strip()

def main():
    st.title(" ChatGPT Test")

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        bot_response = generate_text(user_input)
        st.text_area("Bot:", value=bot_response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    main()

