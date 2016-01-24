from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template("index.html")

@app.route('/about/')
def about():
	return render_template ("about.html")

@app.route('/blog/')
def blogt():
	return render_template ("blog.html")

@app.route("/blog/<int:post_id>")
def search(post_id):
    return 'Post %d'  % post_id

if __name__ == "__main__":
	app.run()
