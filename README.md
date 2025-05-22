# Overview:
This project is a simple Python-based chatbot designed to provide financial insights from company 10-K reports. It uses structured data in CSV format containing financial figures for companies like Microsoft, Tesla, and Apple.

# Functionality:
**The chatbot answers specific, predefined financial questions such as:**

What is the total revenue?
How has net income changed over the last year?
What is the total assets value?
What is the total liabilities value?
What is the cash flow from operating activities?

It extracts the most recent year's data using pandas, performs basic calculations (e.g., net income difference), and returns user-friendly responses. The chatbot also writes test query outputs to a text file (test_results.txt).

# How to Use:
Ensure the financial_data.csv file is present in the working directory.
Run the chatbot script (chatbot.py) using Python.
Input one of the predefined financial queries.
The chatbot will return the corresponding response and save all test results in a .txt file.

# Deliverables:
**chatbot.py:** The main script containing chatbot logic.
**documentation.txt:** User guide and system overview.
**test_results.txt:** Results of automated test queries.

# Limitations:
Only supports predefined queries.
Cannot interpret or process free-form or complex financial questions.
Based on static CSV data; does not fetch live data.

# Future Scope:
Integrate NLP to understand a wider range of financial queries.
Build a web or API interface for real-time user interaction.
Extend data support to multiple years or sectors.

