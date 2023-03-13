import openai
import streamlit as st
from streamlit_chat import message

def generate_response(prompt, api_key):
    openai.api_key = api_key
    completion=openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.3,
    )

    message=completion.choices[0].text
    return message

def main():
    st.title("ChatGPT Web App by Sayon")

    # get user API key
    api_key = st.text_input("Enter OpenAI API Key:", type="password")

    if api_key:
        # storing the chat
        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []

        user_input=st.text_input("You:",key='input')

        if user_input:
            output=generate_response(user_input, api_key)

            #store the output
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

        if st.session_state['generated']:

            for i in range(len(st.session_state['generated'])-1, -1, -1):
                message(st.session_state["generated"][i], key=str(i))
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

if __name__ == '__main__':
    main()
