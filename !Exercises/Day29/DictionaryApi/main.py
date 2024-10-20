from flask import Flask, render_template
import requests as rq

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def dictionary(word: str):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    result = {"definition": None, "word": word}
    response = rq.get(url)
    if response.status_code != 200:
        return result
    content = response.json()
    definitions = content[0]["meanings"][0]["definitions"]
    whole_def = ""
    for index, definition in enumerate(definitions):
        whole_def += f"{(index + 1)}. {definition['definition']}\n "
    result["definition"] = whole_def
    return result


if __name__ == '__main__':
    app.run(debug=True, port=8000)
