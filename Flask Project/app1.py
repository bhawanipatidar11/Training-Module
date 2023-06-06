from flask import Flask , render_template

app = Flask(__name__)   #initaliation

@app.route('/')         # url declare
def hello_world():
    return 'Hello world'


@app.route('/services')
def services():
    return render_template('flas1.html')
    # return 'this is service page'

@app.route('/contact')
def contact():
    return render_template('flas.html')
    

@app.route('/about')
def about():
    return 'this is About page'

if __name__ == '__main__':
    app.run(debug = True)