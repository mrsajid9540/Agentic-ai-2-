from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"  # <-- Yahan apna API key daalein

@app.route('/respond', methods=['POST'])
def respond():
    data = request.get_json()
    user_message = data.get('message')

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful and smart assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
