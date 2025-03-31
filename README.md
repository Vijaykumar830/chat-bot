# 💳 Online Banking System

This is a **modern, secure, and user-friendly** online banking system built using **Django** and **Bootstrap**. It includes essential banking functionalities such as **deposit, withdraw, transfer, transaction history, and chatbot assistance**.

## 🚀 Features

- 🏦 User Authentication (Login/Logout)
- 💰 Deposit & Withdraw Money
- 🔄 Transfer Funds Between Accounts
- 📜 View Transaction History
- 🤖 AI Chatbot for Assistance
- 🎨 Modern UI with Bootstrap

## 🏗 Project Structure

```
online_banking/
│-- accounts/                 # User authentication (Login, Register, Profile)
│-- banking/                  # Banking transactions (Deposit, Withdraw, Transfer)
│-- chatbot/                  # Chatbot integration
│-- templates/                # HTML templates
│-- static/                   # CSS, JS, Images
│-- db.sqlite3                # Database file (SQLite)
│-- manage.py                 # Django management script
│-- requirements.txt          # Dependencies
│-- README.md                 # Project Documentation
```

## 🛠 Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/online-banking.git
   cd online-banking
   ```

2. **Create & Activate a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create Superuser (Admin)**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```sh
   python manage.py runserver
   ```

7. **Access the App**
   - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## 📷 Screenshots

![Homepage](screenshots/homepage.png)
![Deposit](screenshots/deposit.png)
![Transaction History](screenshots/history.png)

## 🛡 Security

- Uses Django’s built-in authentication & CSRF protection.
- Secure password hashing & validation.

## 📜 License

This project is licensed under the MIT License.

---

### 🌟 Star this repo if you found it helpful! 😊
