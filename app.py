from flask import Flask, render_template, request
from agents.communication_agent import CommunicationAgent

app = Flask(__name__)
agent = CommunicationAgent()

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        destination = request.form["destination"]
        days = int(request.form["days"])
        budget = int(request.form["budget"])

        result = agent.run(destination, days, budget)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)