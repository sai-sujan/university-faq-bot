import os
import streamlit as st
import uuid
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv
load_dotenv()  # 👈 Load environment variables from .env

# === Set Your Gemini API Key === #
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# === Initialize Gemini Model === #
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)

# === Prompt Template === #
faq_prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="""
You are a helpful and knowledgeable assistant for a university website.
Use the previous chat history and the new question to provide a clear and accurate answer.

Chat History:
{chat_history}

Question: {question}

Answer:"""
)

# === PAGE CONFIG === #
st.set_page_config(page_title="University FAQ Bot", page_icon="🎓")
st.title("🎓 University FAQ Assistant")

# === MEMORY EXPLANATION === #
with st.expander("🧠 How Memory Works", expanded=True):
    st.markdown("""
This chatbot uses **ConversationBufferMemory** from LangChain to keep track of everything you and the assistant say.
- The `memory_key` used is **`"chat_history"`**, which holds all previous messages.
- This allows the bot to respond with full awareness of past interactions.
- You can start new chats or switch between sessions anytime.
""")

# === INIT CHAT MANAGEMENT === #
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}

if "active_chat_id" not in st.session_state:
    default_id = "default"
    st.session_state.chat_sessions[default_id] = {
        "memory": ConversationBufferMemory(memory_key="chat_history", return_messages=True),
        "history": []
    }
    st.session_state.active_chat_id = default_id

# === FUNCTIONS === #
def create_new_chat():
    new_id = f"chat_{str(uuid.uuid4())[:8]}"
    st.session_state.chat_sessions[new_id] = {
        "memory": ConversationBufferMemory(memory_key="chat_history", return_messages=True),
        "history": []
    }
    st.session_state.active_chat_id = new_id

def get_active_chain():
    active_id = st.session_state.active_chat_id
    memory = st.session_state.chat_sessions[active_id]["memory"]
    return LLMChain(llm=llm, prompt=faq_prompt, memory=memory, verbose=False)

# === CHAT CONTROLS === #
cols = st.columns([4, 2])
with cols[0]:
    # Temporary variable to capture user selection
    chat_ids = list(st.session_state.chat_sessions.keys())
    selected_chat = st.selectbox(
        "💬 Select Chat Session",
        options=chat_ids,
        index=chat_ids.index(st.session_state.active_chat_id)
    )

# Only update active chat if changed
if selected_chat != st.session_state.active_chat_id:
    st.session_state.active_chat_id = selected_chat

with cols[1]:
    if st.button("➕ New Chat"):
        create_new_chat()

# === MAIN CHAT === #
user_input = st.chat_input("Ask a question...")
if user_input:
    chain = get_active_chain()
    response = chain.run(user_input)

    # Update history
    active_id = st.session_state.active_chat_id
    st.session_state.chat_sessions[active_id]["history"].append(("user", user_input))
    st.session_state.chat_sessions[active_id]["history"].append(("bot", response))

# === DISPLAY CHAT HISTORY === #
for sender, message in st.session_state.chat_sessions[st.session_state.active_chat_id]["history"]:
    st.chat_message("user" if sender == "user" else "assistant").markdown(message)
