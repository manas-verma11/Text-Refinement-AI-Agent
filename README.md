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
- Multiple refinement tones: Professional, Formal, Concise, Email, LinkedIn, Academic, and Casual
- Input validation for empty, invalid, and long text inputs
- Logging for workflow execution and debugging
- Retry mechanism for LLM API calls
- FastAPI backend with REST endpoint
- Streamlit frontend for user interaction
- Test cases for validating different tone outputs

---

## Sample Test Cases

The project was tested with multiple refinement tones to verify output consistency and quality.

| Test Case | Input | Tone | Output |
|---|---|---|---|
| 1 | heloo i hope your doing well can u help me | Email | I hope you are doing well. Could you possibly assist me? |
| 2 | i want job in ai and i am learning python | LinkedIn | I am currently pursuing a career in Artificial Intelligence and am actively developing my skills in Python programming. |
| 3 | this project is good and i made it using ai | Professional | This project is of high quality and was developed utilizing artificial intelligence. |
| 4 | can u send me the file asap | Formal | Could you please forward the file to me as soon as possible? |
| 5 | i have completed the work and now testing it | Concise | I've completed the work and am currently testing it. |

## Author

Manas Verma