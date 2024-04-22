from flask import Flask, render_template, request

app = Flask(__name__)

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

filename = "messages.txt"
server = Server(filename)
passcode = "6633"
participants = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join', methods=['POST'])
def join_chat():
    name = request.form['name']
    user_passcode = request.form['passcode']
    if user_passcode == passcode:
        participants.append(name)
        messages = server.retrieve_messages()
        return render_template('chat.html', name=name, messages=messages)
    else:
        return "Incorrect passcode. Unable to join the chat room."

@app.route('/send', methods=['POST'])
def send_message():
    name = request.form['name']
    message = request.form['message']
    message_to_save = f"{name}: {message}"
    server.save_message(message_to_save)
    return message_to_save

if __name__ == '__main__':
    app.run(debug=True)
