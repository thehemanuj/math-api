from flask import Flask, jsonify
import random
import mathgenerator  # Import the library that generates math problems

app = Flask(__name__)

# Get all available math problem functions from mathgenerator
available_problems = [
    func for func_name, func in vars(mathgenerator).items()
    if callable(func) and func_name != "main"
]

@app.route('/generate_problem', methods=['GET'])
def generate_problem():
    # Randomly select a problem generator from all domains
    math_function = random.choice(available_problems)
    problem, solution = math_function()  # Generate the problem and solution
    
    # Return the generated problem and solution as JSON
    return jsonify({
        "problem": problem,
        "solution": solution
    })

if __name__ == '__main__':
    app.run(debug=True)
