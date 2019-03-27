# coding: utf8
from google.appengine.ext import ndb

from backend import error
# from ssl import _create_unverified_context
# from urllib import urlopen
# from json import loads as json_loads
import requests


class UrlNotFound(error.Error):
    pass


class KeyNotFound(error.Error):
    pass


class FetchDataTestProperty(ndb.Model):
    test = ndb.IntegerProperty(indexed=False)


class FetchData(ndb.Model):
    data = ndb.StructuredProperty(FetchDataTestProperty)
    success = ndb.BooleanProperty(indexed=False)

    @classmethod
    def get(cls, url="https://www.mocky.io/v2/5c76b900320000b31cf46398"):
        resp = requests.get(url=url.replace("https://", "http://"), verify=False)
        data = resp.json()
        if resp.status_code != 200:
            raise UrlNotFound("There is a problem with obtaining data.")
        if 'data' not in data.keys():
            raise KeyNotFound('Can\'t find key \'data\' in response')
        if 'success' not in data.keys():
            raise KeyNotFound('Can\'t find key \'success\' in response')
        if 'test' not in data['data'].keys():
            raise KeyNotFound('Can\'t find key \'test\' in response')
        entity = cls(
            success=data['success'],
            data=FetchDataTestProperty(test=data['data']['test'])
        )

        return entity

        # to avoid ssl certificates error
        # unverified_context = _create_unverified_context()
        # api_data = urlopen(url, context=unverified_context)
        # if api_data.getcode() != 200:
        #     raise UrlNotFound('''There is a problem with obtaining data.
        #     \nStatus code:{}
        #     \nReturned message:{}'''.format(api_data.getcode(), api_data.read()))
        # data_dict = json_loads(api_data.read())
        # if 'data' not in data_dict.keys():
        #     raise KeyNotFound('Can\'t find key \'data\' in response')
        # if 'success' not in data_dict.keys():
        #     raise KeyNotFound('Can\'t find key \'success\' in response')
        # if 'test' not in data_dict['data'].keys():
        #     raise KeyNotFound('Can\'t find key \'test\' in response')
        # entity = cls(
        #     success=data_dict['success'],
        #     data=FetchDataTestProperty(test=data_dict['data']['test'])
        # )
        #
        # return entity

    @property
    def id(self):
        return self.key.urlsafe()

    def __hash__(self):
        return hash((self.__class__.__name__, self.id))
