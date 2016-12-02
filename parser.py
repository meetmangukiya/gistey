import argparse

parser = argparse.ArgumentParser(description="Create github gists from cmdline",
                                 prog="gist")

parser.add_argument('-s', '--secret',
                    default=False,
                    help="To create a secret gist",
                    action='store_true')

parser.add_argument('-f','--files',
                    nargs='+',
                    help="Files to be uploaded in the gist",
                    action='store')

parser.add_argument('-D', '--no-description',
                    default=False,
                    help='Create the file gists without any description',
                    action='store_true')
