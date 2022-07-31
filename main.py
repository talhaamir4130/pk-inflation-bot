import requests

print('Sending request...')

response = requests.get('https://httpbin.org/ip')

if response.status_code != 200:
    print('Error:', response.status_code)
    exit(1)

json = response.json()

print('Response:', json)

