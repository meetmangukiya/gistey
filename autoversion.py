import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument('--type', '-t',
                    action='store',
                    required=True, 
                    choices=['dev', 'release'])

# TODO: Implement auto stable_version release
args = parser.parse_args()

now = time.gmtime()
dev_string = 'dev' + str(now.tm_year) + str(now.tm_month) + str(now.tm_day) + str(now.tm_hour) + str(now.tm_minute)

with open("stable_version.txt") as version:
    stable_version = version.read().rstrip()
    if args.type != 'release':
        dev_version = stable_version + dev_string
    with open("tmp_version.txt", 'w') as tmp:
        tmp.write(dev_version)
