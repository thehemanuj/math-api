from flask import Flask, jsonify
from mathgenerator import mathgen
import random  # Import random to pick a random topic ID

app = Flask(__name__)

@app.route("/generate-question", methods=["GET"])
def generate_question():
    # Generate a random topic ID within the range of available topics
    total_topics = len(mathgen.getGenList())  # Get the total number of available topics
    random_id = random.randint(0, total_topics - 1)  # Pick a random ID from the range

    question, answer = mathgen.genById(random_id)  # Generate question using the random ID
    return jsonify({"topic_id": random_id, "question": question, "answer": answer})

if __name__ == "__main__":
    app.run()
