import os
import sys

from parser import parser

args = parser.parse_args()

def process_files():
    files = [os.path.abspath(file) for file in args.files]
    file_contents = {}
    for file in files:
        try:
            f = open(file)
            file_contents[os.path.split(file)[1]] = f.read()
            f.close()
        except FileNotFoundError:
            print('File "{}"\n\tdoes not exist'.format(file))
            should_create = input('Create the gist without this file [Y/n]: ') or 'Y'
            if not should_create == 'Y':
                sys.exit("gist: exiting ...")
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
