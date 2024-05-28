import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.set('foo', 'bar')
# True
r.set('arafat', 'dfkjasldkfj')
print(r.get('arafat'))
print(r.get('foo'))