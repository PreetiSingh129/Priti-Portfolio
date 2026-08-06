![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql)
![License](https://img.shields.io/badge/License-MIT-green)
# 👩‍💻 Priti Portfolio

A dynamic and interactive **Portfolio Management System** built using **Python, Streamlit, and MySQL**.

The project includes a beautiful public portfolio website along with a secure **Admin Dashboard** that allows dynamic management of portfolio content such as projects, skills, certificates, achievements, profile details, and more without modifying the source code.

---

# 🚀 Live Demo

🔗 **Portfolio Website**

https://priti-portfolio-6wqwrgedegffycxklkkndy.streamlit.app/

---

# ✨ Features

## 🌐 Portfolio

- Responsive Portfolio UI
- Hero Section
- About Section
- Skills Section
- Projects Showcase
- Certificates Section
- Achievements & Leadership
- Contact Section
- Resume Download
- Visitor Counter

---

## 🔐 Admin Dashboard

Manage the portfolio dynamically through an Admin Panel.

Features include:

- Add / Edit / Delete Projects
- Add / Edit / Delete Skills
- Add / Edit / Delete Certificates
- Add / Edit / Delete Achievements
- Update Profile Information
- Update About Section
- View Visitor Count
- Manage Contact Messages

---

# 🛠 Tech Stack

### Frontend

- Streamlit
- HTML
- CSS

### Backend

- Python

### Database

- MySQL

### Libraries

- Streamlit
- streamlit-option-menu
- mysql-connector-python
- pandas

---

# 📂 Folder Structure

```
Priti-Portfolio
│
├── admin/
├── assets/
│   ├── images/
│   └── certificates/
├── components/
├── database/
├── styles/
├── app.py
├── requirements.txt
└── README.md
```

---

# 🗄 Database

The application uses MySQL for storing all portfolio data.

Tables:

- profile
- about
- skills
- projects
- certificates
- achievements
- messages
- visitors

---

# 🔐 Streamlit Secrets Configuration

Create a `.streamlit/secrets.toml` file:

```toml
[mysql]

host = "your_host"
user = "your_username"
password = "your_password"
database = "your_database"
port = 3306
```

For **Streamlit Cloud Deployment**, open:

**App Settings → Secrets**

and paste the same configuration there.

> **Note:** Never upload your actual database credentials to GitHub.

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/PreetiSingh129/Priti-Portfolio.git
```

Move into the project folder

```bash
cd Priti-Portfolio
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🎯 Key Features

- Dynamic Portfolio Management
- CRUD Operations
- Image Upload Support
- MySQL Integration
- Streamlit Cloud Deployment
- Visitor Tracking
- Responsive Design
- Clean Admin Dashboard

---

# 📸 Screenshots

You can add screenshots of:

- Home Page
- About Section
- Projects
- Skills
- Certificates
- Admin Dashboard

---

# 👩‍💻 Author

**Priti Kumari**

B.Tech (Artificial Intelligence & Machine Learning)

### Skills

- Python
- MySQL
- Streamlit
- Machine Learning
- Power BI
- SQL
- Data Analysis

---
# 🚀 How to Use

## 1. Clone the Repository

```bash
git clone https://github.com/PreetiSingh129/Priti-Portfolio.git
```

---

## 2. Go to the Project Folder

```bash
cd Priti-Portfolio
```

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## 4. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 5. Configure MySQL Database

Create a MySQL database and import the required tables.

Then create a **.streamlit/secrets.toml** file:

```toml
[mysql]
host = "your-host"
user = "your-username"
password = "your-password"
database = "your-database"
port = 3306
```

> **Note:** Never commit your `secrets.toml` file to GitHub.

---

## 6. Run the Application

```bash
streamlit run app.py
```

---

## 7. Open in Browser

After running the command, Streamlit will automatically open:

```
http://localhost:8501
```

You can now:

- 👤 View the Portfolio
- 🔐 Login to the Admin Panel
- ➕ Add Projects
- 🛠 Manage Skills
- 🏆 Upload Certificates
- 🎯 Update Achievements
- 📝 Edit Profile & About Section
- 📩 View Contact Messages
- ------------------------------
# 🌟 Future Improvements

- Cloud Image Storage (Cloudinary / AWS S3)
- Better Authentication System
- Email Notifications
- Dashboard Analytics
- Performance Optimization

---

## ⭐ If you like this project, don't forget to give it a Star!
