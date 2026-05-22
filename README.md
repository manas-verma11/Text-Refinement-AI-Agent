# Text Refinement AI Agent

An AI-powered Text Refinement Agent built using LangGraph and Groq LLM APIs.  
The system takes raw user text input and refines it into professional and grammatically correct text using an LLM workflow pipeline.

---

## Features

- AI-powered text refinement
- LangGraph workflow integration
- Groq LLM API integration
- Modular graph-based architecture
- Prompt engineering for professional output
- Easy to extend with additional nodes and workflows

---

## Tech Stack

- Python
- LangGraph
- Groq API
- dotenv
- Virtual Environment (.venv)

---

## Project Structure

```bash
text-refinement-agent/
│
├── src/
│   ├── agent/
│   │   ├── graph.py
│   │   ├── nodes.py
│   │   └── state.py
│   │
│   └── api/
│
├── .env
├── requirements.txt
├── test_graph.py
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Text-Refinement-AI-Agent.git
cd Text-Refinement-AI-Agent
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

#### Windows

```bash
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create .env File

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run Project

```bash
python test_graph.py
```

---

## Example

### Input

```text
heloo how are u doing today
```

### Output

```text
Hello, how are you doing today?
```

---

## Current Progress

- Completed LangGraph workflow setup
- Integrated Groq LLM
- Implemented text refinement node
- Successfully tested graph execution

---

## Future Improvements

- Multi-node workflows
- Tone customization
- Memory support
- Frontend UI
- Streaming responses
- Validation and retry logic

---

## Author

Manas Verma