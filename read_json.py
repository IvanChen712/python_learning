from urllib import request
import json


def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
        pobj = json.loads(data.decode('utf-8'))

    return pobj


URL = 'https://yesno.wtf/api'
url_data = fetch_data(URL)
print(url_data)
assert url_data['answer'] == 'yes' and not url_data['forced']
print('ok')
