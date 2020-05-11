import json
import os


def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return site_root + path


def get_static_json(file):
    x = get_static_file('\\static\\json\\' + file)
    return json.load(open(x))