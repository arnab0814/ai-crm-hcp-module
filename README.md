# 🧠 AI-First CRM HCP Module

## 🚀 Overview

This project is an **AI-first Customer Relationship Management (CRM) system** designed specifically for managing interactions with Healthcare Professionals (HCPs).

It enables field representatives to log, update, and retrieve interactions using both:

* 📋 Structured Form Input
* 💬 AI-Powered Conversational Interface

The system leverages an **LLM-driven agent (LangGraph)** to intelligently interpret user input and execute appropriate actions.

---

## 🎯 Key Features

### 🔹 Dual Interaction Logging

* Manual entry via structured form
* Natural language logging via AI chat

### 🔹 AI-Powered Data Extraction

* Converts unstructured text into structured CRM records
* Extracts doctor name, product, notes, follow-up date

### 🔹 LangGraph Agent Orchestration

* Dynamically decides actions:

  * Log Interaction
  * Edit Interaction
  * Fetch Interaction History

### 🔹 Real-Time CRUD Operations

* Store, update, and retrieve interaction data from database

### 🔹 Clean UI Experience

* Chat-based interaction flow
* Structured form interface
* Human-readable output (not raw JSON)

---

## 🏗️ System Architecture

User (React UI)
→ FastAPI Backend
→ LangGraph Agent
→ LLM (Groq)
→ SQLite Database

---

## 🧠 AI Agent Design (LangGraph)

The system uses a **LangGraph-based AI agent** to interpret user intent and trigger appropriate tools.

### 🔧 Tools Implemented

1. **Log Interaction**

   * Extracts structured data using LLM
   * Stores interaction in database

2. **Edit Interaction**

   * Updates existing interaction details

3. **Get Interactions**

   * Retrieves stored interaction records

4. **Summarize Interaction**

   * Generates concise summaries

5. **Suggest Next Action**

   * Recommends follow-up steps

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Axios

### Backend

* FastAPI (Python)
* SQLAlchemy

### AI & Agent

* LangGraph
* Groq LLM (llama-3.3-70b-versatile)

### Database

* SQLite

---

## ⚙️ Installation & Setup

### 🔹 Clone Repository

```bash
git clone https://github.com/arnab0814/ai-crm-hcp-module.git
cd ai-crm-hcp-module
```

---

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run backend:

```bash
python -m uvicorn main:app --reload
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 🧪 Sample Inputs

### 🟢 Log Interaction

```
Met Dr Sharma, discussed insulin, follow up next Monday
```

### 🔵 Fetch Data

```
show all interactions
```

### 🟡 Edit Interaction

```
update follow up to next Friday
```

---

## 🎥 Demo Highlights

* Structured form-based logging
* AI chat-based interaction logging
* Intelligent action selection via agent
* Real-time database updates
* Clean formatted outputs

---

## ⚠️ Important Note

The originally specified model (`gemma2-9b-it`) was deprecated.
Therefore, `llama-3.3-70b-versatile` was used as a replacement.

---

## 🔐 Security Consideration

* API keys are managed using environment variables
* `.env` file is excluded using `.gitignore`
* Keys are not exposed in source code

---

## 🎯 Conclusion

This project demonstrates how **AI agents can enhance CRM systems** by:

* Automating data entry
* Reducing manual effort
* Enabling natural language interaction
* Improving workflow efficiency

---

## 👨‍💻 Author

Arnab Das
