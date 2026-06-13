from flask import Flask, jsonify, request
from calculator import add, subtract, multiply, divide, power, average

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    op = data.get("op")
    args = data.get("args", [])
    ops = {
        "add": lambda: add(*args),
        "subtract": lambda: subtract(*args),
        "multiply": lambda: multiply(*args),
        "divide": lambda: divide(*args),
        "power": lambda: power(*args),
        "average": lambda: average(args),
    }
    if op not in ops:
        return jsonify({"error": f"Unknown operation: {op}"}), 400
    try:
        return jsonify({"result": ops[op]()})
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 422


if __name__ == "__main__":
    app.run(debug=True, port=5000)
