# LifeOS – AI Personal Productivity Agent

## Overview
LifeOS is an AI-powered multi-agent productivity assistant that automates inbox management using natural language. It can clean promotional emails, unsubscribe from newsletters, and summarize important emails through a modular agent-based workflow.

This project demonstrates how AI agents can serve as the foundation of a **LifeOS platform** by turning plain-English user requests into coordinated productivity actions.

---

## Problem Statement
Users receive large volumes of emails every day, making it difficult to identify important messages, remove clutter, and manage newsletters efficiently. Existing tools are often manual, fragmented, or rule-based.

There is a need for an intelligent system that can:
- Understand natural language requests
- Classify inbox content intelligently
- Execute multiple productivity actions in a single workflow
- Return clear, human-readable results

---

## Why This Matters for LifeOS
LifeOS is envisioned as an intelligent personal operating system that helps users manage their digital lives more efficiently.

Email is one of the most universal and time-consuming personal workflows. By automating inbox cleanup, newsletter unsubscription, and important email summarization, this project demonstrates how LifeOS can become a foundational layer for broader personal productivity automation across:

- Email
- Tasks
- Calendar
- Reminders
- Follow-ups
- Daily planning

---

## Target Users
- Busy professionals
- Students managing academic and internship/job emails
- Job seekers handling mixed inboxes
- Founders and freelancers
- Anyone overwhelmed by promotional clutter and newsletters

---

## Key Features
- Natural language inbox automation
- AI-based email classification
- Inbox cleanup for promotional emails
- Newsletter unsubscription simulation
- Important email summarization
- Multi-agent orchestration
- Human-readable output (instead of raw JSON)
- User-friendly Streamlit dashboard

---

## System Architecture

### High-Level Flow
```text
User Request (Natural Language)
        ↓
     Streamlit UI
        ↓
    FastAPI Backend
        ↓
     Orchestrator
        ↓
 ┌─────────────────────────────────────────────┐
 │ Intent Agent → Planning Agent → Email Analysis Agent │
 └─────────────────────────────────────────────┘
        ↓
 ┌─────────────────────────────────────────────┐
 │ Email Action Agent | Unsubscribe Agent | Summary Agent │
 └─────────────────────────────────────────────┘
        ↓
 Human-readable Output in UI
```

---

## Agent Roles and Responsibilities

### 1. Intent Agent
**Responsibility:**
- Understands the user’s natural language request
- Detects the requested productivity action(s)

**Examples:**
- `"Clean my inbox"` → `inbox_cleanup`
- `"Unsubscribe me from newsletters"` → `unsubscribe_newsletters`
- `"Summarize my important emails"` → `summarize_important`
- Combined requests → `full_email_optimization`

---

### 2. Planning Agent
**Responsibility:**
- Converts the detected intent into an execution plan
- Decides which downstream agents should run

**Possible plans:**
- Cleanup only
- Unsubscribe only
- Summary only
- Full optimization (cleanup + unsubscribe + summary)

---

### 3. Email Analysis Agent
**Responsibility:**
- Classifies emails into:
  - `important`
  - `newsletter`
  - `promotional`
- Uses LLM-based classification with fallback logic

---

### 4. Email Action Agent
**Responsibility:**
- Simulates inbox cleanup
- Identifies promotional emails as removable clutter

---

### 5. Unsubscribe Agent
**Responsibility:**
- Detects newsletter emails
- Simulates unsubscribe actions for newsletters

---

### 6. Summary Agent
**Responsibility:**
- Filters important emails
- Generates a concise summary of key emails

---

### 7. Orchestrator
**Responsibility:**
- Coordinates all agents
- Runs the correct workflow based on the plan
- Combines results into a final human-readable response

---

## Execution Flow

1. User enters a natural language request in the Streamlit UI  
2. The frontend sends the request to the FastAPI backend  
3. The Orchestrator invokes the Intent Agent  
4. The Intent Agent detects the user’s intent  
5. The Planning Agent creates an execution plan  
6. The Email Analysis Agent classifies the inbox emails  
7. Based on the plan:
   - Email Action Agent performs inbox cleanup
   - Unsubscribe Agent processes newsletter unsubscriptions
   - Summary Agent generates important email summaries
8. The Orchestrator merges outputs into one response  
9. The final human-readable result is shown in the UI  

---

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Language:** Python
- **AI Layer:** OpenAI API / LLM-based intent and classification
- **Architecture:** Multi-Agent System
- **Data Layer:** Mock email dataset (prototype/demo-safe)

---



## Setup & Run Instructions

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd lifeos-ai-agent
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 6. Run FastAPI backend
```bash
uvicorn main:app --reload
```

### 7. Run Streamlit frontend
```bash
streamlit run streamlit_app.py
```

---

## Example Requests and Expected Outputs

### Example 1
**Request:**  
`Clean my inbox`

**Expected Output:**  
- Detects promotional emails  
- Shows which emails were cleaned  
- Displays count of removed clutter  

---

### Example 2
**Request:**  
`Unsubscribe me from newsletters`

**Expected Output:**  
- Detects newsletter emails  
- Simulates unsubscribe actions  
- Shows which newsletters were unsubscribed  

---

### Example 3
**Request:**  
`Summarize my important emails`

**Expected Output:**  
- Filters important emails  
- Generates a concise summary  
- Displays key email insights  

---

### Example 4 (Best Demo)
**Request:**  
`Clean my inbox, unsubscribe from newsletters, and summarize important emails`

**Expected Output:**  
- Removes promotional clutter  
- Unsubscribes newsletter emails  
- Summarizes important emails  
- Returns a combined human-readable result  

---

## Product & Architecture Explanation

### Problem Being Solved
Modern inboxes are cluttered with promotional emails, newsletters, and critical messages mixed together. This causes:
- Information overload
- Missed important communication
- Repetitive manual work
- Reduced productivity

LifeOS addresses this by allowing users to issue plain-English requests and letting AI agents handle the workflow.

---

### Why This Matters for a LifeOS Platform
This project represents a strong starting point for a broader **LifeOS ecosystem** because:
- Email is a universal productivity workflow
- It is a high-frequency user pain point
- It demonstrates trust-based AI task delegation
- The same architecture can expand into tasks, reminders, calendar, and follow-up automation



## Future Scope
- Gmail / Outlook API integration
- One-click archive / delete actions
- Smart labels and categories
- Task extraction from emails
- Calendar event detection
- AI-generated follow-up drafts
- Cross-agent productivity support (tasks, reminders, scheduling)

---

## Demo 
https://drive.google.com/file/d/1Zal-vChfZFop6D8FHiA2bTJxTZEeHxIM/view?usp=sharing

## Conclusion
LifeOS demonstrates how natural language + modular AI agents can transform repetitive inbox management into an intelligent, scalable productivity experience.

This is not just an email automation tool — it is a prototype for a future **AI-powered personal operating system**.
