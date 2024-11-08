# app.py
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Route for the main page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the name submitted by the user
        name = request.form.get("name")
        # Render the page with the personalized greeting
        return render_template("index.html", name=name)
    # Render the page without a name (initial load)
    return render_template("index.html", name=None)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
