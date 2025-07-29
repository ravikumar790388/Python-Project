# Simple Chatbot using NLTK

import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (run once)
nltk.download('punkt')

# Define pairs: pattern-response pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created for your internship task!"]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thanks for asking!", "I'm fine! How can I help you?"]
    ],
    [
        r"go to hell",
        ["You can't talk me like that...."]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No worries!", "Don't mention it."]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Great! How can I assist you?"]
    ],
    [
        r"(.*) age?",
        ["I'm a bot, I don't have an age!"]
    ],
    [
        r"(.*) created you?",
        ["I was created by a Ravi for a CodTech internship task."]
    ],
    [
        r"quit",
        ["Bye! Have a great day!", "Goodbye!"]
    ],
    [
        r"quit",
        ["Bye! Have a great day!", "Goodbye!"]
    ],
]

# Create Chatbot
def codtech_chatbot():
    print("Hi! I'm your internship chatbot. Type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Run the chatbot
codtech_chatbot()
