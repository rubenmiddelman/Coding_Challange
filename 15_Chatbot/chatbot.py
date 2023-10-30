"""
 # @ Author: Ruben Middelman
 # @ Create Time: 2023-10-30 13:13:56
 # @ Modified by: Ruben Middelman
 # @ Modified time: 2023-10-30 13:34:14
 # @ Description:
 Small chatbot program learning to use chatterbot
 """

from chatterbot import ChatBot

chatbot = ChatBot("Chatpot")

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
