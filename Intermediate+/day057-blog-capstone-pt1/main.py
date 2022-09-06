from flask import Flask, render_template
import requests as req

app = Flask(__name__)
post_data_url = "https://api.npoint.io/c790b4d5cab58020d391"
res = req.get(post_data_url)
res.raise_for_status()
entries = res.json()


@app.route('/')
def home():
    return render_template("index.html", entries=entries)


@app.route('/blog/<entry_id>')
def get_post(entry_id):
    for entry in entries:
        if entry['id'] == int(entry_id):
            return render_template("post.html", title=entry['title'], subtitle=entry['subtitle'], body=entry['body'])
    raise IndexError(f"No entry found with id {entry_id}")


if __name__ == "__main__":
    app.run(debug=True)
