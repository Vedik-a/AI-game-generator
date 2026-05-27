# 🎮 AI Game Generator

AI-powered browser game generator using FastAPI, Streamlit, Playwright, and LLMs.

## 🚀 Features

- Generate playable browser games using AI
- FastAPI backend
- Streamlit frontend
- Runtime validation with Playwright
- Automatic self-repair loop
- Gameplay critic system
- View generated game source code
- HTML/CSS/JS game generation

---

# 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- Playwright
- HTML/CSS/JavaScript
- NVIDIA NIM API

---

# 📁 Project Structure

```text
aigame/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── streamlit_app.py
│   ├── api_client.py
│   └── requirements.txt
│
├── generated_games/
│
└── README.md
```

---

# ⚙️ Backend Setup

```bash
cd backend

python -m venv venv
```

## Activate venv

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Playwright

```bash
pip install playwright
playwright install
```

## Run Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

# 🌐 Frontend Setup

Open new terminal:

```bash
cd frontend
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Frontend

```bash
streamlit run streamlit_app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# 🔑 Environment Variables

Create `.env` inside `backend/`

```env
NVIDIA_API_KEY=your_api_key_here
```

---

# 🎮 Usage

Enter prompts like:

```text
Create a snake game
Create a racing game
Create a flappy bird clone
Create a tic tac toe game
```

AI generates a playable browser game automatically.

---

# 🤖 AI Pipeline

```text
User Prompt
    ↓
LLM Game Generation
    ↓
HTML Cleaning
    ↓
Runtime Testing
    ↓
Gameplay Critic
    ↓
Self Repair Loop
    ↓
Frontend Rendering
```

---

# ✅ Features Implemented

- Runtime testing
- Gameplay validation
- Auto-repair loop
- Keyboard/mouse support
- HTML sanitization
- Playable game rendering

---
