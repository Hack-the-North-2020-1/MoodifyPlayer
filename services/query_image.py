import requests
from settings import AZURE_IMAGE_API_KEY

key = AZURE_IMAGE_API_KEY
api_endpoint = "https://api.bing.microsoft.com/v7.0/images/search"


class BingImageQuery():

    def __init__(self):
        self.images = []

    def query_images(self, search_query='happy', count=5):
        self.images.clear()
        params = dict(q=search_query, count=count)
        image_results = requests.get(api_endpoint, headers={"Ocp-Apim-Subscription-Key": key}, params=params)
        res = image_results.json()
        im_metadata = res.get('value')
        for item in im_metadata:
            self.images.append(item.get('contentUrl'))
        print(self.images)

        return self.images


# bing = BingImageQuery()
# bing.query_images()


