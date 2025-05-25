# CI/CD Pipeline with GitHub Actions

This repository demonstrates a simple implementation of a CI/CD pipeline using **GitHub Actions**. It includes basic Python functions for arithmetic operations and sets up an automated workflow to test and validate the code on every push.

## 🔧 Features

* ✅ Basic Python functions (`add`, `sub`, `mul`)
* 🔁 Automated testing with GitHub Actions
* 🔍 Continuous Integration pipeline that runs on every push
* 🧪 Unit tests using `unittest`

---

## 📂 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml       # GitHub Actions workflow
├── main.py              # Python file with functions
├── test_main.py         # Unit tests for the functions
└── README.md
```

---

## 📜 Operations Included

```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b
```

---

## 🚀 CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) is triggered on every push and pull request to the main branch. It:

1. Sets up a Python environment
2. Installs dependencies
3. Runs unit tests
4. Validates the code automatically

### 🛠 Sample Workflow

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt || true
    - name: Run tests
      run: |
        python -m unittest discover
```

---

## ✅ Running Locally

You can run the tests locally using:

```bash
python -m unittest test_main.py
```

---

## 📈 Skills Demonstrated

* CI/CD concepts with GitHub Actions
* Writing clean, testable Python code
* Automating workflows in software development
* Unit testing in Python

---

## 📎 Repository Link

🔗 [CI-CD-Pipeline-and-GitHub-Action](https://github.com/alihassanml/CI-CD-Pipeline-and-GitHub-Action.git)
