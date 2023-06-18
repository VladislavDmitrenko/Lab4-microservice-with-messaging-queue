from hazelcast import HazelcastClient

client = HazelcastClient(cluster_name="my-cluster", cluster_members=["127.0.0.1:5701", "127.0.0.1:5702"])

queue = client.get_queue("messages_queue")

while True:
    message = queue.take().result()
    print("Logging message:", message)