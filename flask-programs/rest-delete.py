from flask import Flask
from flask import request
from flask import jsonify
import redis

app = Flask(__name__)


cur = redis.Redis(host='127.0.0.1', port='6379', db=0, password='')


@app.route('/read', methods=['GET'])
def read():
    all_data = cur.zrange("data", 0, -1, withscores=True)
    serialized_data = []
    for data in all_data:
        # data[0].decode() is used to convert the bytes object to a string so that it can be serialized to JSON. data[1] is already an integer, so it can be included as is in the tuple that is appended to serialized_data.
        serialized_data.append((data[0].decode(), data[1]))
    return jsonify(serialized_data)


@app.route('/delete/<int:score>', methods=['DELETE'])
def delete(score):
    if cur.zremrangebyscore("data", score, score) == 0:
        return jsonify({"error": "data not found in the key"})
    else:
        cur.zremrangebyscore("data", score, score)
        return read()


if __name__ == '__main__':
    app.run(debug=True, port='5000')
