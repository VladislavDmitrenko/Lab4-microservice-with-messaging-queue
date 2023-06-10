import subprocess


messages_service_ports = [9000]
for port in messages_service_ports:
    command = f"./messages-service --port={port}"
    subprocess.Popen(command, shell=True)