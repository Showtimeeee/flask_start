from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Seva')


if __name__ == "__main__":
    app.run(debug=1, port=8000)

