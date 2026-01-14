from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis using the hostname 'redis' defined in docker-compose
redis_host = os.environ.get('REDIS_HOST', 'redis')
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def index():
    try:
        # Simple flow: Increment a counter in Redis
        count = r.incr('hits')
        return f'Hello Container World! This page has been viewed {count} times.\n'
    except redis.exceptions.ConnectionError as e:
        return f'Error connecting to Redis: {str(e)}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)