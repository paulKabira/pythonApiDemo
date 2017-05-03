from django.db import models

# Create your models here.
class SearchApi(object):
    """docstring for SearchApi."""
    def __init__(self):
        super(SearchApi, self).__init__()

    def getResults( self, of='Google', q='' ):
        reqParam = {
            'q':q
        }

        if 'Google' == of:
            reqParam.update({
                'cx' : '016825447971944065611:3in-xyqlnfq',
                'key': 'AIzaSyC4IwU6NFM4FIMa0y1lIIIwrlNW90yxSZc',
                'num': '1'
            })
            url = 'https://www.googleapis.com/customsearch/v1'
        if 'Duck' == of:
            reqParam.update({
                'format': 'json'
            })
            url = 'http://api.duckduckgo.com/'

        res = requests.get( url, json = reqParam, timeout = 1 )
