from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body>
    <h2>Enter a number to get its multiplication table</h2>
    <form method="POST">
        <input type="number" name="number" required>
        <button type="submit">Get Table</button>
    </form>

    {% if number is not none %}
        <h3>Multiplication Table for {{ number }}:</h3>
        <ul>
            {% for row in table %}
                <li>{{ row }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    table = []
    number = None
    if request.method == "POST":
        try:
            number = int(request.form["number"])
            table = [f"{number} x {i} = {number*i}" for i in range(1, 11)]
        except ValueError:
            table = ["Please enter a valid number."]
    return render_template_string(HTML_TEMPLATE, table=table, number=number)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
