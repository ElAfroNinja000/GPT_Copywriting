from flask import Flask, render_template, request
from gpt_copywriting_generator import GPTCopywritingGenerator

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    article = ""
    return render_template('index.html', article=article)


@app.route('/generate_article', methods=['POST'])
def generate_article():
    query       = request.form["query"]
    words_count = int(request.form["words_count"])
    options = {
        "examples":       (request.form.get("with_examples")       == "on"),
        "bullet points":  (request.form.get("with_bullet_points")  == "on"),
        "call to action": (request.form.get("with_call_to_action") == "on")
    }
    article = GPTCopywritingGenerator().send_request(query, words_count, options)
    return render_template('index.html', article=article)
