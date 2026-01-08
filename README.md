---

# ⏳ Decision Matrix: Time Asset Allocation System

### **"Treating Time as Capital with ROI-based Allocation"**

**Decision Matrix** is a Django-based productivity tool that gamifies time management. Instead of a traditional To-Do list, it functions as an **Asset Allocation Model for Time**. By quantifying subjective tasks using three key financial metrics—Urgency, Risk (Cost of Inaction), and Reward (ROI)—the system calculates a weighted priority score and automatically allocates a user's finite daily hours to the highest-impact activities.

---

## 🚀 Core Features

* **Weighted Scoring Engine:** Algorithms calculate a "Priority Score" based on user inputs (1-10 scale) for Timeframe, Cost of Inaction, and Reward.
* **The Inverted Pyramid Visualization:** A dynamic UI that renders tasks visually based on weight—the most critical tasks form the wide foundation at the top.
* **Auto-Time Budgeting:** Users input their available daily hours (e.g., 8 hours), and the system automatically distributes this time proportionally based on the task's calculated importance %.
* **Industry-Standard Architecture:** Built with a "Fat Model, Service Layer" approach to keep business logic testable and decoupled from views.

## 🧮 The Logic (Math Model)

The system uses a weighted sum formula to determine the "Market Cap" of your total workload:

*If a task constitutes 40% of the total "Context Score," it automatically receives 40% of the daily time budget.*

---

## 🛠 Tech Stack

* **Language:** Python 3.12+
* **Framework:** Django 6.x
* **Dependency Management:** `uv` (Modern, high-performance Python package manager)
* **Database:** SQLite (Dev) / PostgreSQL (Ready)
* **Frontend:** Django Templates (Jinja2) + CSS Flexbox

---

## ⚡ Getting Started (Local Development)

This project uses **[uv](https://github.com/astral-sh/uv)** for ultra-fast dependency management.

### 1. Clone the Repository

```bash
git clone https://github.com/SatyajitKumar123/Decision-Matrix.git

```

### 2. Initialize Environment

```bash
# Install dependencies and create venv in one step
uv sync

```

*(If you don't have `uv` installed, run `pip install uv` first).*

### 3. Apply Migrations

```bash
# Activate the environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Initialize database
python manage.py migrate

```

### 4. Create Superuser (Admin)

```bash
python manage.py createsuperuser

```

### 5. Run the Server

```bash
python manage.py runserver

```

Visit `http://127.0.0.1:8000` to access the dashboard.

---

## 📂 Project Structure

```text
decision_matrix/
├── config/             # Django Project Settings
├── core/               # Main Business Logic App
│   ├── models.py       # Database Schema (Validators & Structure)
│   ├── services.py     # Pure Python Math Engine (The Brain)
│   ├── forms.py        # Input Validation
│   └── views.py        # HTTP Request Handling
├── manage.py           # Django CLI
├── pyproject.toml      # Dependency Manifest (uv)
└── README.md           # Documentation

```