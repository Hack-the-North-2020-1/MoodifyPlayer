import requests


key = "74b3dd84769d49a886d087347a06933e"
api_endpoint = "https://api.bing.microsoft.com/v7.0/images/search"



class BingImageQuery():

    def __init__(self):
        self.images = []

    def query_images(self, search_query='happy'):
        params = dict(q=search_query, count=20)
        image_results = requests.get(api_endpoint, headers={"Ocp-Apim-Subscription-Key": key}, params=params)
        res = image_results.json()
        im_metadata = res.get('value')
        for item in im_metadata:
            self.images.append(item.get('contentUrl'))
        print(self.images)


bing = BingImageQuery()
bing.query_images()


