import openai
from flask import Flask, render_template, request
import config

app = Flask(__name__)
app.config.from_object(config.config['development'])

@app.route('/')
def chat():
    return render_template('chat.html')

@app.route('/send', methods=['POST'])
def send():
    # Get the input text from the form
    input_text = request.form['input_text']

    # Use OpenAI's API to generate a response
    openai.api_key = config.OPENAI_API_KEY
    response = openai.Completion.create(engine="text-davinci-003", prompt=input_text, max_tokens=1024, temperature=0.5)
    response_text = response['choices'][0]['text']

    # Render the chat template with the input text and response text
    return render_template('chat.html', input_text=input_text, response_text=response_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)

