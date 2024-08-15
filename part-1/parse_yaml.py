import yaml

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

if __name__ == '__main__':
    data = read_yaml('sample_config.yaml')
    print(data)