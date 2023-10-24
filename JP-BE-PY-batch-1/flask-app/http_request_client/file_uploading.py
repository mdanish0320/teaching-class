import requests

url = 'http://localhost:3000/input/post/form-data/upload-file'
fp = '/Users/danish/Desktop/000.json'
files = {'my_json_file': open(fp, 'rb')}

# url = 'http://localhost:3000/input/post/form-data/upload-multiple-files'
# fp = '/Users/danish/Desktop/000.json'
# files = [('my_json_file', ('foo.json', open(fp, 'rb'))), ('my_json_file', ('bar.json', open(fp, 'rb')))]


payload = {'file_id': '1234'}

response = requests.post(url, files=files, data=payload, verify=False)

print(response)