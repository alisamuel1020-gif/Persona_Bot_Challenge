import requests

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": "Bearer load.env('GROQ_API_KEY')",
    "Content-Type": "application/json"
}

memory = []

while True:
    user_input = input("Enter your Question here (or type 'exit' to quit): ")
    if user_input.lower().strip() == 'exit':
        break

    memory.append({
        "role": "user",
        "content": user_input
    })
