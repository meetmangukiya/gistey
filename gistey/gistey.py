import os
import sys

import requests

from .ArgumentParser import parser

# Processing
# ----------


def process_files(args):
    """
    :param args:
        The arguments parsed by argparse
    :returns:
        A dict containing file_names as keys and a
        dict containing a key `content` as the value

    Example return:
        {
            "file_name": {
                "content": {
                    # file contents
                }
            }
        }
    """
    files = [os.path.abspath(file) for file in args.files]
    file_contents = {}
    for file in files:
        try:
            f = open(file)
            file_contents[os.path.split(file)[1]] = dict(content=f.read())
            f.close()
        except FileNotFoundError:
            print('File "{}"\n\tdoes not exist'.format(file))
            should_create = input(
                'Create the gist without this file [Y/n]: ') or 'Y'
            if not should_create == 'Y':
                sys.exit("gistey: exiting ...")
    return file_contents


def create_gist(data):
    """
    :param data:
        The JSON data to be posted to the API
    :returns:
        request object of the POST request made to create the gist
    """
    end_point = 'https://api.github.com/gists'
    rq = requests.post(end_point, json=data)
    return rq


def construct_data(args):
    """
    :param args:
        The arguments parsed by argparse
    :returns:
        `data` dict to be passed to crete the POST request
    """
    data = {
        "public": not args.secret,
        "description": args.description if args.description else '',
        "files": process_files(args)
    }
    return data

# Execution
# ---------

def main():
    args = parser.parse_args()
    response = create_gist(construct_data(args))
    print("URL of the gist created: ", response.json()["html_url"])

if __name__ == "__main__":
    main()
