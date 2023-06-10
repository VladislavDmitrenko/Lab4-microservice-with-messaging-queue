from hazelcast import HazelcastClient

# Подключение к кластеру Hazelcast
client = HazelcastClient()

# Получение распределенной очереди
message_queue = client.get_queue("messageQueue")

# Получение сообщений из очереди
message1 = message_queue.take()
message2 = message_queue.take()
message3 = message_queue.take()

print(message1)
print(message2)
print(message3)

# Закрытие подключения к кластеру Hazelcast
client.shutdown()