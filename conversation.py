import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv
load_dotenv()

# From here down is all the StreamLit UI.
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat GPT")

if "sessionMessages" not in st.session_state:
     st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]
     

def load_answer(question):

    st.session_state.sessionMessages.append(HumanMessage(content=question))

    assistant_answer  = chat(st.session_state.sessionMessages )

    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))

    return assistant_answer.content


def get_text():
    input_text = st.text_input("You: ", key= input)
    return input_text

key = os.getenv('OPENAI_API_KEY')
chat = ChatOpenAI(api_key= key, temperature=0)

user_input=get_text()
submit = st.button('Generate')  

if submit:
    
    response = load_answer(user_input)
    st.subheader("Answer:")

    st.write(response,key= 1)
