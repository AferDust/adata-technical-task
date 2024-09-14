# Task-2 Python Script

This project scrapes data from the [Goszakup Registry](https://www.goszakup.gov.kz/ru/registry/rqc) website using **Selenium**. The scraped data is saved to a file for further use.

---

## ⚙️ Setting Up and Running the Project
Follow these steps to set up the environment and run the Python script.

### 1. Create a Virtual Environment
To isolate dependencies, create a virtual environment by running:
```bash
python -m venv venv
# OR (for systems where Python 3 is the default)
python3 -m venv venv
```

### 2. Activate the Virtual Environment
Activate the virtual environment based on your operating system:
```bash
    venv\Scripts\activate # For Windows
    source venv/bin/activate # For Linux / macOS
```

### 3. Install Required Packages
Install the necessary dependencies listed in the requirements.txt file:
```bash
    pip install -r requirements.txt
```

### 4. Run the Python Script
After the environment is set up and packages are installed, you can run the scraping script:
```bash
    python scripts.py
    # OR (for systems with Python 3)
    python3 scripts.py
```

## 📄 Result
***Once the script has finished running, the scraped data will be saved in a file named ``organization_data.txt``.***