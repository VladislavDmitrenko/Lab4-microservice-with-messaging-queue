import subprocess


logging_service_ports = [8002]
for port in logging_service_ports:
    command = f"./logging-service --port={port}"
    subprocess.Popen(command, shell=True)


hazelcast_config_files = ["hazelcast_config_1.xml", "hazelcast_config_2.xml", "hazelcast_config_3.xml"]
for config_file in hazelcast_config_files:
    command = f"./hazelcast --config={config_file}"
    subprocess.Popen(command, shell=True)