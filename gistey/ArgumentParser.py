import argparse

parser = argparse.ArgumentParser(description="Create github gists "
                                             "from cmdline", prog="gistey")

parser.add_argument('-s', '--secret',
                    default=False,
                    help="To create a secret gist",
                    action='store_true')

parser.add_argument('-f', '--files',
                    required=True,
                    nargs='+',
                    help="Files to be uploaded in the gist",
                    action='store')

parser.add_argument('-d', '--description',
                    help='Description for the gist',
                    action='store')
