from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/site<num>')
def site(num):
    # Works for /site01, /site02, /site03, etc.
    return render_template('site{0}.html'.format(num))

@app.route('/test')
def test():
	return render_template('tournament.html')

@app.route('/login')
def test():
	return render_template('login.html')


# Include a module runner to allow local testing
if __name__ == '__main__':
    app.run(debug=True)  # Set to false for production