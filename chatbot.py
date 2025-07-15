import openai

openai.api_key = "AIzaSyAG24E9jAIEgL3APlndewtOnBjb0CR0jp4"
def chatbot_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    print("Bot:", chatbot_response(user_input))
