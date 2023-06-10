from hazelcast import HazelcastClient

# Подключение к кластеру Hazelcast
client = HazelcastClient()

# Получение распределенной очереди
message_queue = client.get_queue("messageQueue")

# Отправка сообщений в очередь
message_queue.put("msg1")
message_queue.put("msg2")
message_queue.put("msg3")

# Закрытие подключения к кластеру Hazelcast
client.shutdown()