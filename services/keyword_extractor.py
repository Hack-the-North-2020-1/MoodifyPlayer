import requests
import json
from settings import IBM_NLU_API_KEY

url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/4045ca02-d14e-4fca-b476-7c80aa5a04ca/v1/analyze?version=2019-07-12"

class KeywordExtractor():

    def extract(self, lyrics):

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
        response_obj = response.json()
        list_of_keywords = []
        print(response_obj)
        for i in range(5):
            list_of_keywords.append(response_obj.get("keywords")[i].get("text"))

        print(list_of_keywords)
        return list_of_keywords


# extractor = KeywordExtractor()
#
# extractor.extract()
