from flask import Flask
from flask import redirect
from flask import jsonify
from flask import request
import redis
import uuid
import datetime

app = Flask(__name__)

cur = redis.Redis(host='127.0.0.1', port='6379', db=0, password='')


@app.route('/write', methods=['POST'])   # End point
def write():
    # First convert string into json
    name = request.get_json()['name']
    email = request.get_json()['email']
    id = uuid.uuid1()
    date = datetime.datetime.now()
    # Check current score, if it is 'x' add one to it. It gets the count of the previous key and then gets the present score
    score = cur.zcount("data", '-inf', '+inf')+1

    # Insert the data. Create a json datatype into string datatype
    data = str({'id': score, 'uuid': id, 'name': name,
               'email': email, 'created_date': date})
    cur.zadd("data", {data: score})
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port='5000')
