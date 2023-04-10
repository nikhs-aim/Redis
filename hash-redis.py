import datetime
import redis
import uuid
cur = redis.Redis(host='127.0.0.1', port=6379, db=0, password='')


# Insert json/dictionary in redis hashes
def insert_data(table, data):
    for key, value in data.items():
        cur.hmset(table, {key: value})
    print(cur.hgetall(table))
    print('The length ' + str(cur.hlen(table)))


data = {'id': str(uuid.uuid1()), 'first_name': 'Nikhitha', 'last_name': 'Karanth',
        'place': 'Bangalore', 'timestamp': str(datetime.datetime.now())}  # redis always updates the data in the string or byte format
insert_data('details', data)


# Update hashes
def update_hash(table, key, value):
    if cur.hexists(table, 'first_name'):
        cur.hset(table, key, value)
        print('updated')
        print(cur.hkeys(table))
        print(cur.hvals(table))
    else:
        print('data not found')


update_hash('details', 'first_name', 'Nikhs')
