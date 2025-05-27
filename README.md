# 🎓 University FAQ Assistant — LangChain + Gemini + Streamlit

An interactive, memory-aware chatbot built using **LangChain**, **Google Gemini**, and **Streamlit**. Designed to answer university-related questions while remembering past conversations using LangChain's memory modules.

---

## 🚀 Features

* 🤖 Powered by **Google Gemini**

  
* 🧱 Uses **LangChain components**:
  * 🧱 **PromptTemplate** – a flexible prompt with placeholders for dynamic user inputs.
    
  * 🔗 **LLMChain** – a structured pipeline that connects the prompt to the language model and captures the output.
    
  * 🧠 **ConversationBufferMemory** – short-term memory that gives the bot context across multiple turns.



* 💬 **Multi-session support** – switch between chats or start fresh
* 🌐 Clean UI with **Streamlit**
* 🔐 Secure key loading via `.env`

---

### 🖼️ Interface Preview

<div align="center">
  <img src="https://github.com/user-attachments/assets/98d22259-7b37-4689-bdd8-13c92785a97e" alt="Chat Window View 1"  />
  <img src="https://github.com/user-attachments/assets/ae85a9ff-c163-46b0-89b7-ec6dabe1f2cf" alt="Chat Window View 2"  />
</div>

---

## 🧠 Technologies

* `langchain`
* `langchain-google-genai`
* `streamlit`
* `python-dotenv`

---

## 📦 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/sai-sujan/university-faq-bot.git
cd university-faq-bot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Gemini API key
echo "GOOGLE_API_KEY=your-api-key-here" > .env

# 4. Run the app
streamlit run app.py
