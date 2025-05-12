# test-suite-generator


An AI-powered backend system that automatically generates, validates, and tests input/output for coding problems using OpenAI and FastAPI Designed for developers, educators, and problem setters.

---

What It Does
**Generate** diverse test cases for any problem statement
**Validate** test cases using constraints and format rules
**Compute expected outputs** (via GPT or reference logic)
**Validate outputs** manually or through AI
Full API & simple web UI
Easily deployable using Docker

---

#Tech Stack

- **Backend**: FastAPI, Python 3.10
- **AI Integration**: OpenAI GPT-4o
- **Testing**: Pytest + Mock
- **Frontend**: Basic HTML/CSS form
- **DevOps**: Docker, CircleCI

---

## Installation

```bash
# 1. Clone this repo
https://github.com/YOUR_USERNAME/test-suite-generator.git
cd test-suite-generator

# 2. Set up a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your OpenAI key
echo "OPENAI_API_KEY=sk-..." > .env

# 5. Run the app
uvicorn main:app --reload
```

Access the app at [http://localhost:8000/ui](http://localhost:8000/ui)  
API docs at [http://localhost:8000/docs](http://localhost:8000/docs)

---

##  Docker Support

```bash
# Build the Docker image
docker build -t test-suite-api .

# Run the container
docker run -p 8000:8000 --env-file .env test-suite-api
```

---


## 🗂 Project Structure

```
src/
├── generate.py              # Test case generator (LLM)
├── validate.py              # Validates test cases
├── output.py                # Generates outputs via LLM or ref
├── output_validation.py     # Validates outputs
├── ref_solution.py          # Logic-based fallback solutions
├── test/                    # Unit tests for each component
│   ├── test_generate.py
│   ├── test_validate.py
│   ├── test_output.py
│   ├── test_output_validation.py
│   └── test_ref_solution.py
public/
└── index.html               # Simple frontend UI
```





