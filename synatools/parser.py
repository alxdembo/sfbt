import json
import os


# post pull and pre commit


def parse_sql():
    if __name__ == '__main__':
        directory = './sqlscript/'
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                print(os.path.join(directory, filename))
                with open(os.path.join(directory, filename)) as f:
                    contents = json.loads(f.read())
                    with open('./parsed_scripts/' + filename.replace('.json', '.sql'), 'w') as nf:
                        nf.write(contents['properties']['content']['query'])


def test():
    print('yolo')