from flask import Flask, request, jsonify
from chatbot import chatbot

app = Flask(__name__)

@app.route("/chat")
def chat():

    query = request.args.get("q")

    answer = chatbot(query)

    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
