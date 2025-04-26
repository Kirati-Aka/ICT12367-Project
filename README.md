# ICT12367 Project - Online Polling System

An educational project built for the **ICT12367** course.  
It is a web application that allows users to create polls, vote, and view voting results dynamically, with a clean modern interface.

---

## 🚀 Project Overview

This system simulates an **online polling/voting platform**.  
It consists of:

- A **Django backend** to handle poll creation, voting logic, and data management.
- A **Bootstrap 5 frontend** to provide a responsive and user-friendly interface.
- Real-time update patterns (simple, without WebSocket) using Django views and modals.

Users can:
- Create new polls (questions + multiple choices)
- Vote for available options
- View results immediately after voting

---

## 🏛️ Project Structure

```plaintext
ICT12367-Project/
├── manage.py
├── ICT12367_Project/        # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── polls/                   # Core app: Polls management
│   ├── migrations/
│   ├── static/               # Static assets (CSS/JS/Images if any)
│   ├── templates/            # HTML templates
│   │   └── polls/
│   │       ├── index.html    # Home page - list of polls
│   │       ├── detail.html   # Poll detail & voting page
│   │       ├── results.html  # Poll result page
│   ├── admin.py              # Django admin registration
│   ├── apps.py
│   ├── models.py             # Data Models (Question, Choice)
│   ├── tests.py
│   ├── urls.py               # App-specific routes
│   └── views.py              # Views controlling the logic
├── db.sqlite3                # SQLite database
└── requirements.txt          # Python dependencies
⚙️ How It Works (เบื้องหลังระบบ)
Polls & Choices Models

Question: Represents a single poll (question + publication date)

Choice: Represents an option tied to a Question, with a vote counter.

User Interaction Flow

On the homepage (index.html), users see a list of available polls.

Clicking on a poll opens a modal to vote without leaving the page.

After voting, the app redirects or refreshes to show results immediately.

Voting Mechanism

Each vote updates the Choice model's votes field (+1).

Django automatically saves changes to the database.

Templates

Use Bootstrap modals for voting

Display cards for each poll dynamically

🧑‍💻 How to Run Locally
1. Clone the repository
bash
คัดลอก
แก้ไข
git clone https://github.com/Kirati-Aka/ICT12367-Project.git
cd ICT12367-Project
2. Install dependencies
bash
คัดลอก
แก้ไข
pip install -r requirements.txt
3. Apply database migrations
bash
คัดลอก
แก้ไข
python manage.py migrate
4. Start the development server
bash
คัดลอก
แก้ไข
python manage.py runserver
5. Access the application
Open your browser at: http://127.0.0.1:8000/

📚 Key Files Explained

File / Folder	Purpose
polls/models.py	Defines database structure (Questions, Choices)
polls/views.py	Handles logic for listing polls, voting, showing results
polls/templates/	HTML files that render the frontend UI
ICT12367_Project/urls.py	Maps URLs to corresponding views
requirements.txt	Lists required Python libraries
🛠️ Features To Improve (Ideas)
Add authentication (users must log in to vote)

Add real-time result updates (WebSocket / Django Channels)

Add poll closing dates (expire polls)

Improve voting UI with AJAX (without page reload)

📷 Screenshots (optional)
![image](https://github.com/user-attachments/assets/e70e37a5-3a81-4e26-8e46-f2a05030d722)
<img width="1470" alt="Screenshot 2568-04-25 at 08 01 06" src="https://github.com/user-attachments/assets/e87f2a03-9b74-4f53-9f48-a92695116e05" />
<img width="1470" alt="Screenshot 2568-04-26 at 00 30 31" src="https://github.com/user-attachments/assets/06ecb33c-0542-4719-98f9-8ba234039894" />



📜 License
This project is created for educational purposes under the ICT12367 course.
