# Multi-Agent CM Using CrewAI

## Project Setup

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)
- API keys for OpenAI, Groq, and Serper

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yazanrisheh/Crisis-Management.git
cd into folder
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate

CTRL + SHIFT + P >>> Select Python Interpreter
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create .env file

```bash
Add all 3 API as shown in the .env.example
```

### Step 5: Fix CSV file path
```bash
Locate to tools.py and fix the copy path of volunteers.csv
```

### Step 6: Run the program
```bash
streamlit run main.py
```

