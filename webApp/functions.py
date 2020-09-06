import json
import os


def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return site_root + path


def get_static_json(file):
    x = get_static_file('\\json\\' + file)
    return json.load(open(x))


def build_terminal(path):
    data = get_static_json("terminal.json")

    message = ""
    for i, string in enumerate(data['content']):

        if i != 0:
            string = "<span class='caret'>" + data['caret'] + "</span>" + string + "<br/> ^100"
        else:
            string = string + "<br/>"

        message = message + string

    lines = ""
    with open(path + "/terminal_template.js", "r") as fp:
        lines = fp.read()
        fp.close()

    lines = lines.replace("<content>", message)
    lines = lines.replace("<cursor>", data['cursor'])

    with open(path + "/terminal.js", "w") as fp:
        fp.seek(0)
        fp.write(lines)
        fp.close()
