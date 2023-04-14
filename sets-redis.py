import redis
cur = redis.Redis(host='127.0.0.1', port=6379, db=0, password='')

#  Insert bulk data through list in redis


def insert_data(table, data):
    for data in data:
        cur.sadd(table, data)
        print(cur.smembers(table))


my_data = ['nikhitha', 'karanth', 'bts', 'anime']
insert_data('details', my_data)


# Edit a particular data in redis


def updated_data(table, old, new):
    if cur.sismember(table, old):
        cur.srem(table, old)   # Deletes the old data
        cur.sadd(table, new)   # Add the new data
        print('data inserted')
    else:
        print('no data inserted before')


updated_data('details', 'nikhitha', 'nikhs')
