import requests

def compare_websites(urls):
    responses = [requests.get(url).text for url in urls]
    if len(set(responses)) == 1:
        print("The webservers have the same HTML output.")
    else:
        print("The webservers do not have the same output.")

compare_websites(['http://0.0.0.0:8000/', 'http://0.0.0.0:5000/', 'http://0.0.0.0:7000'])


def header(urls):
    for url in urls:
        response = requests.get(url)
        print(response.headers)

header(['http://0.0.0.0:8000/', 'http://0.0.0.0:5000/', 'http://0.0.0.0:7000'])
