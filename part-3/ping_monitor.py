import yaml
import pingparsing
import json
import time

def read_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            print("YAML file loaded successfully")
            return data
    except FileNotFoundError:
        print(f"Not able to find file {file_path}")
    except yaml.YAMLError as err:
        if hasattr(err, 'problem_mark'):
            mark = err.problem_mark
            print(f"Invalid YAML syntax at position: ({mark.line}:{mark.column})")
        else:
            print(f"An unknown YAML parsing error has occurred: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    return None

def ping_server(target):
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()

    transmitter.destination = target
    transmitter.count = 4

    result = transmitter.ping()
    statistics = ping_parser.parse(result).as_dict()
    return statistics

def display_statistics(stats):
    print(json.dumps(stats, indent=4))

if __name__ == '__main__':
    data = read_yaml('servers.yaml')
    servers = data['servers']
    interval = data['intervals']
    while True:
        for server in servers:
            stats = ping_server(server)
            display_statistics(stats)
            time.sleep(interval)