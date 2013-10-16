from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/site<num>')
def site(num):
    # Works for /site01, /site02, /site03, etc.
    return redirect(url_for('templates', site{0}.html.format(num))

@app.route('/site01')
def index():
    return redirect(url_for('templates', filename='site01.html'))



# Include a module runner to allow local testing
if __name__ == '__main__':
    app.run(debug=True)  # Set to false for production