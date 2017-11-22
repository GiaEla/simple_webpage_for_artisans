# load confgi for env
import os

from ruamel import yaml


def load_config(path):
    environment = os.environ.get('DJANGO_ENV_NAME')

    with open(os.path.join(path, "{0}.yml".format(environment))) as stream:
        try:
            config = yaml.load(stream=stream, Loader=yaml.Loader)
            return config
        except yaml.YAMLError as exc:
            print(exc)
            raise
