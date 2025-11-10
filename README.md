# 🤖 AI Developer Crew

**AI Developer Crew** is an intelligent software development assistant that orchestrates a team of AI agents for **planning, coding, reviewing, and testing software projects**. Using **LangGraph**, **LangChain**,**CrewAI** and local LLMs via **Ollama** (e.g., `gemma:2b`), it automates the software development lifecycle from requirement gathering to tested, production-ready code.

---

## 🚀 Project Overview

This project combines several powerful tools:

* **LangGraph** – Define and manage stateful workflows of AI agents.
* **LangChain** – Interact with local LLMs using prompt templates and chains.
* **CrewAI** - Coordinate multiple specialized AI agents (Planner, Coder, Reviewer, Tester) to collaboratively automate the software development process.
* **Streamlit** – Provides a **user-friendly web interface** for interacting with the AI Crew.
* **Ollama** – Run local LLMs like `gemma:2b` **without cloud dependencies**.

The AI Developer Crew simulates a team of software engineers to automate **end-to-end software development tasks**.

---

## ✨ Features

* Accepts **natural language software requirements**.
* Generates a **structured project plan**.
* Writes **clean, modular Python code**.
* Reviews code for **bugs and improvements**.
* Generates **unit tests** for the code.
* Displays all outputs in an **interactive Streamlit dashboard**.

---

## 🛠️ Setup Instructions

### Prerequisites

* Python **3.8+**
* **Ollama** installed and running locally
* Required Python packages:

  * `streamlit`
  * `langchain`
  * `langgraph`
  * `langchain-community`

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-developer-crew.git
cd ai-developer-crew

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# macOS / Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### Running the App

```bash
streamlit run app.py
```

* Open your browser at [http://localhost:8501](http://localhost:8501)
* Enter your software requirements in **natural language**
* Click **Generate Project Plan & Code** to see the AI Crew in action

---

## 🧩 How It Works

1. **Planner Agent** – Creates a structured project plan from user requirements.
2. **Coder Agent** – Writes Python code based on the project plan.
3. **Reviewer Agent** – Reviews the generated code for bugs, issues, and improvements.
4. **Tester Agent** – Generates and runs unit tests for the code.

All outputs are displayed clearly in the **Streamlit dashboard** for easy inspection.

---

## 📂 Project Structure

```
ai-developer-crew/
├─ app.py                 # Streamlit frontend
├─ crew_setup.py          # Creates the AI crew (planner, coder, reviewer, tester)
├─ langgraph_flow.py      # Defines the LangGraph workflow
├─ agents/
│  ├─ coder.py
│  ├─ reviewer.py
│  ├─ tester.py
│  └─ planner.py
├─ coderunner.py          # Utility to run Python scripts
├─ requirements.txt
└─ README.md
```

## Built With ❤️ using LangGraph, LangChain, CrewAI, Ollama (gemma:2b)

---
