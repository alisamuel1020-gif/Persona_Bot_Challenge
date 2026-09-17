import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
    "Content-Type": "application/json"
}

PERSONAS = {
    "1": {
        "name": "Math Tutor",
        "prompt": (
            "You are a strict secondary-school maths tutor. "
            "CRITICAL RULE: You must NEVER give the direct answer to a math problem. "
            "Instead, you must guide the student to the answer by asking leading questions, "
            "breaking the problem into smaller steps, and offering hints. "
            "Keep your tone encouraging but firm. Do not solve it for them."
        )
    },
    "2": {
        "name": "Naija Chef",
        "prompt": (
            "You are a friendly Nigerian chef who loves to cook. "
            "You explain recipes using local Nigerian ingredients and substitutes. "
            "You must speak with a distinct Nigerian Pidgin English flavor. "
            "Use phrases like 'wetin dey happen', 'abeg', 'chop', 'no wahala', and 'make we'. "
            "Be warm, energetic, and passionate about local food."
        )
    },
    "3": {
        "name": "PayPoint Support",
        "prompt": (
            "You are a customer support representative for a fictional fintech company called PayPoint. "
            "Your tone must be professional, patient, and highly helpful. "
            "You handle issues like failed transfers, account verification, and app glitches. "
            "Always apologize for any inconvenience and provide clear, step-by-step solutions. "
            "Never break character. You are a representative of PayPoint."
        )
    }
}

def run_persona_chat(persona_key):
    
    persona = PERSONAS[persona_key]
    
    memory = [
        {"role": "system", "content": persona["prompt"]}
    ]
    
    print(f"\n{'='*50}")
    print(f"Starting chat with: {persona['name']}")
    print(f"Type 'exit' or 'quit' to stop.")
    print(f"{'='*50}\n")
    
    turn_count = 1 

    while True:
        
        question = input(f"What would like to know? : ")
        
        if question.lower().strip() in ["nah", "no", "n", "nope", "exit", "quit"]:
            break

        memory.append({"role": "user", "content": question})
        
        response = requests.post(url, headers=headers, json={
            "messages": memory,
            "model": "qwen/qwen3.8-27b", 
        })

        if response.status_code != 200:
            print("Error: ", response.status_code)
            print(response.json())
            continue

        result = response.json()
        ai_reply = result["choices"][0]["message"]["content"]
        print(f"AI: {ai_reply}\n")
        
        memory.append({"role": "assistant", "content": ai_reply})
        



def main():
    while True:
        print("\n" + "-"*60)
        print("                 PERSONA BOT CHALLENGE   ")
        print("-"*60)
        print("1. Math Tutor")
        print("2. Naija Chef")
        print("3. PayPoint Support")
        print("4. Quit Program")  
        print("-"*60)

        choice = input("Select an option (1-4): ")

        if choice in PERSONAS:
            run_persona_chat(choice)
        elif choice == "4":

            print("Session ended Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()




