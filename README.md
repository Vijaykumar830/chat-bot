💳 Online Banking System
📌 Description
The Online Banking System is a web-based platform built using Django, Bootstrap, and AI-powered chatbot functionalities. It allows users to manage their accounts, perform transactions, and interact with an intelligent chatbot.

📁 Project Structure
graphql
Copy
Edit
online_banking/
│── accounts/              # User authentication & account management
│── admin_panel/           # Admin dashboard (Django Admin)
│── chatbot/               # AI chatbot-related files
│── online_bank/           # Main Django project files
│── transactions/          # Transaction-related logic
│── base.html              # Base template (Navbar, Footer, Layout)
│── chat_responses.csv     # Chatbot predefined responses
│── chatbot_messages.csv   # Chatbot training data
│── chatbot_responses.csv  # Chatbot response dataset
│── db.sqlite3             # SQLite database file
│── dna.py                 # AI/ML-related script
│── llmtest.py             # Large Language Model (LLM) test script
│── mainML.py              # Main AI/ML model script
│── manage.py              # Django management script
│── modified_chat_responses.csv # Modified chatbot responses
│── qna_chitchat_profile.csv # QnA and Chitchat dataset
│── Small_talk_Intents.csv # Small talk dataset for chatbot
🛠️ Tech Stack
Frontend: HTML, CSS, Bootstrap

Backend: Django, Python

Database: SQLite

AI/ML: AI-powered chatbot using datasets (chat_responses.csv, Small_talk_Intents.csv)

🚀 Features
✅ User Authentication - Secure login and profile management
✅ Deposit & Withdraw Money - Perform transactions in a secure way
✅ Fund Transfer - Transfer money between accounts
✅ Transaction History - View detailed transaction records
✅ AI Chatbot - Answer user queries using ML models
✅ Admin Panel - Manage users and transactions




🤖 AI Chatbot Integration
The system includes a chatbot that answers user queries. It is trained using:

chat_responses.csv - Predefined responses

qna_chitchat_profile.csv - Q&A dataset

Small_talk_Intents.csv - Small talk dataset

Chatbot scripts:

dna.py

mainML.py

llmtest.py

🙌 Contributors
Vijay


📜 License
This project is open-source under the MIT License.

