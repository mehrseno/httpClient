import argparse
import requests
import validators
import sys


parser = argparse.ArgumentParser(description="httpClient:)")
parser.add_argument(
    "URL",
    nargs=1
)

parser.add_argument(
    "-M",
    "--method",
    choices=["GET", "POST", "PATCH", "PUT", "DELETE"],
    default="GET"
)


parser.add_argument(
    "-H",
    "--headers",
    # handle multiple headers
    action="append"
)

parser.add_argument(
    "-Q",
    "--queries",
    action="append"
)

parser.add_argument(
    "-D",
    "--data"
)

parser.add_argument("--json")
parser.add_argument("--file")
parser.add_argument("--timeout")

try:
    args = parser.parse_args()
except Exception as Argument:
    print(type(Argument))
    sys.exit()

url = args.URL[0]
method = args.method
headers = args.headers
queries = args.queries
data = args.data
json = args.json
file = args.file
timeout = args.timeout
# print(url, method, headers, queries, data, json, file
#       )


def urlCheck(url):
    valid = validators.url(url)
    if valid == True:
        print("Url is valid")
    else:
        print("Invalid url\n", "terminated!")
        sys.exit()


