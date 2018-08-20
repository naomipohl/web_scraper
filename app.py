from flask import Flask, render_template, request
import urllib.request

app = Flask(__name__)

def get_html(input_url):
	with urllib.request.urlopen(input_url) as url:
		s = url.read(300)
	return s

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():

	print("I got clicked!")
	input_url = str(request.form['text'])
	html = get_html(input_url)
	print(html)

	output = '''Here's the HTML: {}'''.format(html)

	return render_template('result.html',output=html)

if __name__ == '__main__':
	app.run(debug=True)