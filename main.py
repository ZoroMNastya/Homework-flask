import json

from flask import Flask, jsonify

from model.post import Post

twits = []

app = Flask(__name__)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return {'body': obj.body, 'author': obj.author}
        else:
            return super().default(obj)


app.json_encoder = CustomJSONEncoder


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


@app.route('/post', methods=['POST'])
def create_post():
    """(body="Hello, world", author="@aqaguy")
    """
    post = Post()
    twits.append(post)
    return jsonify({'status': 'success'})


@app.route('/post', methods=['GET'])
def read_posts():
    return jsonify({'twits': twits})


if __name__ == '__main__':
    app.run(debug=True)
