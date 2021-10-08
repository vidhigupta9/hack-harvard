import requests

auth_key = '7a38375e92034c79bbecc5766323244e'

headers = {
    "authorization": auth_key,
    "content-type": "application/json"
}

def read_file(filename):
   with open(filename, 'rb') as _file:
       while True:
           data = _file.read(5242880)
           if not data:
               break
           yield data

def trancribe_file():
	upload_response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_file('filename'))
	audio_url = upload_response.json()['upload_url']

	transcript_request = {'audio_url': audio_url}
	endpoint = "https://api.assemblyai.com/v2/transcript"
	transcript_response = requests.post(endpoint, json=transcript_request, headers=headers)
	_id = transcript_response.json()['id']

	endpoint = "https://api.assemblyai.com/v2/transcript/" + _id
	polling_response = requests.get(endpoint, headers=headers)

	if polling_response.json()['status'] != 'completed':
   		print(polling_response.json())
	else:
	   with open(_id + '.txt', 'w') as f:
	       return f.write(polling_response.json()['text'])