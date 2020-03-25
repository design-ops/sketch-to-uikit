import json
import pathlib


def read_template(path):
    with open(path) as template_file:
        template_src = template_file.read()
    template_file.close()
    return template_src


def read_json(path):
    with open(path) as json_file:
        json_obj = json.load(json_file)
        json_file.close()
    return json_obj


def write_json(path, output_json):
    with open(path, 'w+') as f:
        f.write(json.dumps(output_json))
    f.close()


def write_file(path, file):
    with open(path, 'w+') as f:
        f.write(file)
    f.close()


def create_dir(path):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)


def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item


def empty_str(default: str, value: str, prefix: str = "", suffix: str = "_"):
    return default if value is None else prefix + str(value) + suffix
