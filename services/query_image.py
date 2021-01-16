import requests


key = "74b3dd84769d49a886d087347a06933e"
api_endpoint = "https://api.bing.microsoft.com/v7.0/images/search"
search_term = 'happy'


class BingImageQuery():

    def query_images(self, search_query):

        params = dict(q=search_term, count=20)
        image_results = requests.get(api_endpoint, headers={"Ocp-Apim-Subscription-Key": key}, params=params)
        res = image_results.json()
        print(res.get('value'))


bing = BingImageQuery()
bing.query_images('happy')


