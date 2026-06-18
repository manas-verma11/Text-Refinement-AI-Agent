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

### Privacy Guard Example

Input:

hello my email is manas@gmail.com and my phone number is 9876543210 please make this professional

Detected Sensitive Data:

Email Address, Phone Number

Text Sent to AI:

hello my email is [EMAIL] and my phone number is [PHONE_NUMBER] please make this professional

## Evaluation & Benchmarking

The project includes a benchmarking script to evaluate refinement quality across multiple real-world communication scenarios.

### Benchmark Coverage

The benchmark evaluates:

- Client email refinement
- Incident communication
- Project status updates
- Meeting summaries
- Executive updates
- Privacy guard and sensitive data masking

### Metrics Used

- Output generation success
- Change detection
- Expected term preservation
- Placeholder safety
- Reasonable output length
- Privacy detection
- Privacy masking
- Sensitive data leakage prevention
- Processing time

### Benchmark Results

| Metric | Result |
|---|---|
| Total Test Cases | 6 |
| Passed Cases | 6/6 |
| Average Auto Score | 97.92% |
| Average Processing Time | 0.71 seconds |

### Case-Level Results

| Case ID | Score | Processing Time |
|---|---:|---:|
| client_email_001 | 100.0% | 1.20 sec |
| incident_001 | 87.5% | 0.59 sec |
| project_status_001 | 100.0% | 0.64 sec |
| meeting_summary_001 | 100.0% | 0.51 sec |
| executive_update_001 | 100.0% | 0.72 sec |
| privacy_guard_001 | 100.0% | 0.61 sec |

The benchmark results are saved in:

```text
benchmark_results.csv

## Deployment Readiness

The project includes a deployment guide covering:

- Local deployment
- Production-style deployment
- Environment variables
- API health check
- Security considerations
- Scalability plan
- Operational support
- Analytics and feedback logs
- Benchmarking results
- Deployment checklist

See:

```text
DEPLOYMENT.md

## Run with Docker

Build and start the full application:

```bash
docker compose up --build

## Author

Manas Verma