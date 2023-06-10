import requests

base_url = "http://127.0.0.1:8000"

for i in range(1, 11):
    message = f"msg{i}"
    url = f"{base_url}/messages"
    data = {"message": message}

    response = requests.post(url, json=data)
    if response.status_code == 201:
        print(f"Сообщение {message} успешно отправлено")
    else:
        print(f"Ошибка при отправке сообщения {message}. Код статуса: {response.status_code}")