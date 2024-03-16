from flask import Flask, request, jsonify
import openai_prompt

app = Flask(__name__)

@app.route("/get_response")
def get_response():
    prompt = request.args.get('prompt')
    if prompt:
        chat = openai_prompt.load_model()
        answer = openai_prompt.gen_qa(chat, prompt)
        return jsonify(answer), 200

    else:
        return "Include Prompt in Query", 400


if __name__ == "__main__":
    app.run(debug=True)