from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3")

template = """
You are a helpful hotel assistant.

User will mention a destination they are going to
(for example: 'I am going to Kochi, Kerala').

Your job:
- Understand the destination (city/area)
- Suggest popular tourist attractions nearby
- Give short descriptions and approximate distance from the city center
- If the user asks follow-up questions, use the conversation history.

Conversation history:
{context}

User message: {question}

Answer as the hotel chatbot:
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the Hotel Travel Assistant! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        result = chain.invoke({
            "context": context,
            "question": user_input
        })

        print(f"Bot: {result}\n")

        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
