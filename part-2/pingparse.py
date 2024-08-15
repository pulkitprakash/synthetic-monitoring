import pingparsing
import json

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

def main():
    target = input("Enter the server address to ping ")
    try:
        stats = ping_server(target)
        display_statistics(stats)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()