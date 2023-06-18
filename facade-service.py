from flask import Flask, request
from hazelcast import HazelcastClient

app = Flask(__name__)
client = HazelcastClient()

queue = client.get_queue("messages_queue")

@app.route('/', methods=['POST'])
def publish_message():
    message = request.data.decode("utf-8")
    queue.put(message)
    return "Message published to the queue"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)