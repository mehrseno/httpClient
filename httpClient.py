import argparse
import requests
import validators
import sys
import warnings
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
except:
    print("Argument Is Invalid")
    sys.exit()

url = args.URL[0]
method = args.method
headers = args.headers
queries = args.queries
data = args.data
json = args.json
file = args.file
timeout = args.timeout
#       )


def urlCheck(url):
    valid = validators.url(url)
    if valid == True:
        print("Url is valid")
    else:
        print("Invalid url\n", "terminated!")
        sys.exit()


print(url, method, headers, queries, data, json, file)


def header(headers):
    header_dic = {}
    for i in headers:
        list = i.split(",")
        for j in range(len(list)):
            key_value = list[j].split(":")
            key = key_value[0].lower()
            value = key_value[1]
            print(header_dic)
            if key in header_dic.keys():
                warning = str(key) + " is already exists"
                warnings.warn(warning)
                header_dic[key] = value
            else:
                header_dic[key] = value
    print(header_dic)
    return header_dic
