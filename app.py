from flask import Flask, request, render_template
from expression_parser import evaluate_expression, draw_syntax_tree

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    expression = ""
    tree_path = None
    if request.method == "POST":
        expression = request.form.get("expression")
        try:
            result = evaluate_expression(expression)
            tree_path = draw_syntax_tree(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", expression=expression, result=result, tree_path=tree_path)

if __name__ == "__main__":
    app.run(debug=True)
