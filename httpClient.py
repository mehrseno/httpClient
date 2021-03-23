import argparse
import requests
import validators
import sys
import warnings
from requests.exceptions import Timeout
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
parser.add_argument(
    "--timeout",
    type = float
)

parser.add_argument("--json")
parser.add_argument("--file")

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

print(url, method, headers, queries, data, json, file)


def urlCheck(url):
    valid = validators.url(url)
    if valid == True:
        print("Url is valid")
    else:
        print("Invalid url\n", "terminated!")
        sys.exit()


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


def query(queries):
    queries_dic = {}
    for i in queries:
        list = i.split("&")
        for j in range(len(list)):
            key_value = list[j].split("=")
            key = key_value[0].lower()
            value = key_value[1]
            print(queries_dic)
            if key in queries_dic.keys():
                warning = str(key) + " is already exists"
                warnings.warn(warning)
                queries_dic[key] = value
            else:
                queries_dic[key] = value
    print(queries_dic)
    return queries_dic


def request(m, u, h, q, d, j, t):
    try:
        return requests.request(m, u, headers=h, params=q, data=d, json=j, timeout=t)
    except Timeout:
        print('The request timed out')
        sys.exit()


def dataFunction(headers_dic):
    if "content-type" not in headers_dic.keys() or headers_dic is None:
        headers_dic["content-type"] = "application/x-www-form-urlencoded"
    return headers_dic


def jsonFunction(headers_dic):
    if "content-type" not in headers_dic.keys() or headers_dic is None:
        headers_dic["content-type"] = "application/json"
    return headers_dic


urlCheck(url)
if headers is not None:
    headers_dic = header(headers)
else:
    headers_dic = None

if queries is not None:
    queries_dic = query(queries)
else:
    queries_dic = None

if data is not None and json is not None:
    print("please enter data or json, not both of them")
    sys.exit()
else:
    if data:
        headers_dic = dataFunction(headers_dic)
    elif json:
        headers_dic = jsonFunction(headers_dic)
    response = request(method, url, headers_dic, queries_dic, data, json, timeout)

print(response)