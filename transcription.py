import requests
import speech_recognition as sr
import wave

auth_key = '7a38375e92034c79bbecc5766323244e'

headers = {
    "authorization": auth_key,
    "content-type": "application/json"
}

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		with open('speech.wav','wb') as f:
			f.write(audio.get_wav_data())
		obj = wave.open('speech.wav','r')
		return obj

def read_file(filename):
   with open(filename, 'rb') as _file:
       while True:
           data = _file.read(5242880)
           if not data:
               break
           yield data

def trancribe_file():
	upload_response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=get_audio())
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