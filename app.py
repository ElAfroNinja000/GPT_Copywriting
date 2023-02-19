from flask import Flask, render_template, request
from gpt_copywriting_generator import GPTCopywritingGenerator

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/generate_article', methods=['POST'])
def generate_article():
    query           = request.form["query"]
    words_count     = int(request.form["words_count"])
    responses_count = int(request.form["responses_count"])
    options = {
        "examples":       (request.form.get("with_examples")       == "on"),
        "bullet points":  (request.form.get("with_bullet_points")  == "on"),
        "call to action": (request.form.get("with_call_to_action") == "on")
    }

    articles = GPTCopywritingGenerator(responses_count).send_request(query, words_count, options)
    return render_template('index.html', articles=articles)
