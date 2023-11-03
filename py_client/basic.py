import requests

# endpoint = "https://www.httpbin.org/status/200/"
# endpoint = "https://www.httpbin.org/anything"
endpoint = "localhost:8000/"
get_response = requests.get(endpoint)
print(get_response.text)