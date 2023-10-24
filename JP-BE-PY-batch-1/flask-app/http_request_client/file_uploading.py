import requests

url = 'http://localhost:3000/input/post/form-data/upload-files'
fp = '/Users/danish/Desktop/000.json'

files = {'my_json_file': open(fp, 'rb')}
payload = {'file_id': '1234'}

response = requests.post(url, files=files, data=payload, verify=False)

print(response)