from flask import Flask, render_template, request, redirect

from core.conversation import Conversation
from core.options import ConversationOptions

app = Flask(__name__)
current_conversation: Conversation

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', conversation=current_conversation)

@app.route('/options', methods=['GET', 'POST'])
def options():
    if request.method == 'POST':
        current_options.from_request(request.form)
        return redirect("/")

    return render_template('options.html', options=current_options)

@app.route('/user_input', methods=['POST'])
def user_input():
    user_input_text = request.form['user_input_text']
    current_conversation.next_step(user_input=user_input_text,options=current_options)
    return render_template('index.html', conversation=current_conversation)

if __name__ == '__main__':
    current_options = ConversationOptions()
    current_options.self_check()

    current_conversation = Conversation()
    current_conversation.start()

    app.run(debug=True)
