from flask import Flask
from flask import jsonify
from flask import request
from mock_transmission_server import response


app = Flask(__name__)


@app.route("/transmission/rpc", methods=['POST'])
def main():
    req = request.get_json(force=True)
    if 'tag' in req:
        print('request had tag', req['tag'])
        response.TAG = req['tag']
    return jsonify(
        arguments=response.ARGUMENTS,
        result=response.RESULT,
        tag=response.TAG,
    )


if __name__ == "__main__":
    app.run(port=5001)
