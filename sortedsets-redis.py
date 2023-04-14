import redis
cur = redis.Redis(host='127.0.0.1', port=6379, db=0, password='')
my_data = {'first_name': 'sasuke',
           'last_name': 'uchiha', 'place': 'konoha'}

# Insert data into hash


def insert_data(table, data):
    data = str(data)
    # cur.zcount(table, '-inf', '+inf') returns the number of elements in the sorted set table with scores between -inf (negative infinity) and +inf (positive infinity), which essentially means all the elements in the set.
    score = cur.zcount(table, '-inf', '+inf')+1
    cur.zadd(table, {data: score})
    print('data inserted')


insert_data('deta', my_data)


# To delete the data


def delete_data(table, score):
    # To check whether the data with score exists or not, score score refers to the max and min scores
    if cur.zremrangebyscore(table, score, score) == 0:
        print('data does not exist')
    else:
        cur.zrem(table, score)
        print('data deleted successfuly')


delete_data('deta', 4)


# To display all the data

def display_all(table):
    print(cur.zrange(table, 0, -1))


display_all('deta')
