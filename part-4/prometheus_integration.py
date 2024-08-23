import yaml
import pingparsing
import json
import time
from prometheus_client import start_http_server, Gauge, Counter

metrics = dict()

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

def set_metrics(stats, server):
    domain = server.split('.')[0]
    print(domain)
    gauge_metrics = ['rtt_avg', 'rtt_min', 'rtt_max', 'packet_loss_count']
    counter_metrics = ['packet_transmit']
    description = dict(rtt_avg='average round trip time',
                       rtt_min='minimum round trip time',
                       rtt_max='maximum round trip time',
                       packet_loss_count='number of packages lost',
                       packet_transmit='number of packets transmitted')
    for metric in gauge_metrics:
        if metric not in metrics:
            metrics[metric] = Gauge(metric, description[metric], labelnames=['server'])
        val = stats.get(metric)
        metrics[metric].labels(domain).set(val)
    for metric in counter_metrics:
        if metric not in metrics:
            metrics[metric] = Counter(metric, description[metric], labelnames=['server'])
        val = stats.get(metric)
        metrics[metric].labels(domain).inc(val)


if __name__ == '__main__':
    start_http_server(8000)
    data = read_yaml('servers.yaml')
    servers = data['servers']
    interval = data['intervals']
    while True:
        for server in servers:
            stats = ping_server(server)
            set_metrics(stats, server)
            time.sleep(interval)
