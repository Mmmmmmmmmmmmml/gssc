import threading

class Server:
    def __init__(self, filename):
        self.filename = filename

    def save_message(self, message):
        with open(self.filename, 'a') as file:
            file.write(message + '\n')

    def retrieve_messages(self):
        with open(self.filename, 'r') as file:
            messages = file.readlines()
            return messages

import threading

class Server:
    def __init__(self, filename):
        self.filename = filename

    def save_message(self, message):
        with open(self.filename, 'a') as file:
            file.write(message + '\n')

    def retrieve_messages(self):
        with open(self.filename, 'r') as file:
            messages = file.readlines()
            return messages

class ChatRoom:
    def __init__(self, passcode, server):
        self.passcode = passcode
        self.participants = []
        self.server = server

    def join_chat(self):
        name = input("Enter your name: ")
        user_passcode = input("Enter the passcode to join the chat room: ")
        if user_passcode == self.passcode:
            self.participants.append(name)
            print(f"{name} joined the chat room.")
            messages = self.server.retrieve_messages()
            for message in messages:
                print(message, end='')
        else:
            print("Incorrect passcode. Unable to join the chat room.")

    def send_message(self):
        name = input("Enter your name: ")
        if name in self.participants:
            message = input("Type your message (or `exit` to leave): ")
            if message.lower() == 'exit':
                return
            message_to_save = f"{name}: {message}"
            self.server.save_message(message_to_save)
            print(message_to_save)
        else:
            print("You are not authorized to send messages.")

    def run_chat(self):
        while True:
            self.join_chat()
            while True:
                self.send_message()

filename = "messages.txt"
server = Server(filename)
passcode = "6633"
chat_room = ChatRoom(passcode, server)

# Running the chat room
chat_room.run_chat()

filename = "messages.txt"
server = Server(filename)
passcode = "6633"
chat_room = ChatRoom(passcode, server)

# Running the chat room
chat_room.run_chat()
