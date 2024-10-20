from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("data/dictionary.csv")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def dictionary(word: str):
    result = {"definition": None, "word": word}
    definition = df[df["word"] == word]["definition"].squeeze()
    if type(definition) == str and len(definition) > 0:
        result["definition"] = definition
    return result


if __name__ == '__main__':
    app.run(debug=True, port=8000)
