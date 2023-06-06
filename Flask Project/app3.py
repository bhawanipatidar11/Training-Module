from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def defult():
    return "This is default"

@app.route('/home')
def home():
    return "This is Home"

@app.route('/about')
def about():
    return render_template('temp1.html')
    # return "This is About"

@app.route('/services')
def services():
    return "This is a services"


if __name__ == '__main__':
    app.run(debug = True)
