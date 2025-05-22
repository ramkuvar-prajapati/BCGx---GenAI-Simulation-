import pandas as pd

# Load financial data
df = pd.read_csv('financial_data.csv')

# Extract the latest year's data
latest_year = df['Year'].max()
latest_data = df[df['Year'] == latest_year]

# Define chatbot function
def simple_chatbot(user_query):
    if user_query.lower() == "what is the total revenue?":
        return f"The total revenue for {latest_year} is ${latest_data['Total Revenue'].values[0]:,.2f}."
    elif user_query.lower() == "how has net income changed over the last year?":
        prev_year = latest_year - 1
        prev_data = df[df['Year'] == prev_year]
        if not prev_data.empty:
            net_income_change = latest_data['Net Income'].values[0] - prev_data['Net Income'].values[0]
            return f"The net income has changed by ${net_income_change:,.2f} from {prev_year} to {latest_year}."
        else:
            return "Net income data for the previous year is unavailable."
    elif user_query.lower() == "what is the total assets value?":
        return f"The total assets value for {latest_year} is ${latest_data['Total Assets'].values[0]:,.2f}."
    elif user_query.lower() == "what is the total liabilities value?":
        return f"The total liabilities value for {latest_year} is ${latest_data['Total Liabilities'].values[0]:,.2f}."
    elif user_query.lower() == "what is the cash flow from operating activities?":
        return f"The cash flow from operating activities for {latest_year} is ${latest_data['Cash Flow from Operating Activities'].values[0]:,.2f}."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Testing the chatbot
test_queries = [
    "What is the total revenue?",
    "How has net income changed over the last year?",
    "What is the total assets value?",
    "What is the total liabilities value?",
    "What is the cash flow from operating activities?",
    "What is the stock price?"  # An invalid query for testing
]

test_results = {query: simple_chatbot(query) for query in test_queries}

# Save test results
with open("test_results.txt", "w") as f:
    for query, response in test_results.items():
        f.write(f"Query: {query}\nResponse: {response}\n\n")

print("Chatbot testing completed. Results saved in 'test_results.txt'.")
