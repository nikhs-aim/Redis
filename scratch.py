import redis

cur = redis.Redis(host='127.0.0.1', port=6379, db=0,
                  password='')  # There are 16 DB's, using db0


# List insert from head
def inser_from_head(key, data):
    cur.lpush(key, data)
    print("Data inserted")


inser_from_head('food', 'idli')


# List insert from tail
def insert_from_head(key, data):
    cur.rpush(key, data)
    print("Data inserted")


# To insert multiple keys
def multiple_keys(key, data):
    for i in data:
        cur.lpush(key, i)
    print('data inserted')


value = ['paneer', 'ButterNaan']
multiple_keys('food', value)


# Display list data
def display_all(key):
    print(cur.lrange(key, 0, -1))


display_all('food')


# To find the length of a key
def length_of_key(key):
    print(cur.llen(key))


length_of_key('food')


#  To get the index number
def index_key(key, num):
    print(cur.lindex(key, num))


index_key('food', 1)


# To delete data from the top
def delete_from_top(key):
    cur.lpop(key)
    print('data deleted from the top')


delete_from_top('food')


# To delete data from the bottom
def delete_from_bottom(key):
    cur.rpop(key)
    print('data deleted from the bottom')


delete_from_bottom('food')
