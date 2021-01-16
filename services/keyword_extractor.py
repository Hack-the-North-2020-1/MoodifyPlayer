import requests
import json
from settings import IBM_NLU_API_KEY

url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/4045ca02-d14e-4fca-b476-7c80aa5a04ca/v1/analyze?version=2019-07-12"

class KeywordExtractor():

    def extract(self):
        lyrics = "Baby, can\'t you see I\'m calling?\r\nA guy like you should wear a warning\r\nIt\'s dangerous, I\'m falling\r\nThere\'s no escape, I can\'t wait\r\nI need a hit, baby, give me it\r\nYou\'re dangerous, I\'m loving it\r\nToo high, can\'t come down\r\nLosing my head, spinnin\' \'round and \'round\r\nDo you feel me now?\r\nWith a taste of your lips, I\'m on a ride\r\nYou\'re toxic, I\'m slippin\' under\r\nWith a taste of a poison paradise\r\nI\'m addicted to you\r\nDon\'t you know that you\'re toxic?\r\nAnd I love what you do\r\nDon\'t you know that you\'re toxic?\r\nIt\'s getting late to give you up\r\nI took a sip from my devil\'s cup\r\nSlowly, it\'s taking over me\r\nToo high, can\'t come down\r\nIt\'s in the air and it\'s all around\r\nCan you feel me now?\r\nWith a taste of your lips, I\'m on a ride\r\nYou\'re toxic, I\'m slippin\' under\r\nWith a taste of a poison paradise\r\nI\'m addicted to you\r\nDon\'t you know that you\'re toxic?\r\nAnd I love what you do\r\nDon\'t you know that you\'re toxic?\r\nDon\'t you know that you\'re toxic?\r\nTaste of your lips, I\'m on a ride\r\nYou\'re toxic, I\'m slippin\' under\r\nWith a taste of a poison paradise\r\nI\'m addicted to you\r\nDon\'t you know that you\'re toxic?\r\nWith a taste of your lips, I\'m on a ride\r\nYou\'re toxic, I\'m slippin\' under (toxic)\r\nWith a taste of a poison paradise\r\nI\'m addicted to you\r\nDon\'t you know that you\'re toxic?\r\nIntoxicate me now, with your lovin\' now\r\nI think I\'m ready now, I think I\'m ready now\r\nIntoxicate me now, with your lovin\' now\r\nI think I\'m ready now"
        headers = {
            'Content-Type': 'application/json',
        }

        params = (
            ('version', '2019-07-12'),
        )

        data = {"text": f"${lyrics}",
                "features": {
                       "keywords": {}
                  }
               }

        data_json = json.dumps(data)

        response = requests.post(url, headers=headers, params=params,
                                 data=data_json, auth=('apikey', IBM_NLU_API_KEY))

        print(response.json())


extractor = KeywordExtractor()

extractor.extract()
