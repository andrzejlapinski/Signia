from protorpc import remote, messages, message_types

from backend import api, fetchdata
from backend.oauth2 import oauth2


class GetResponseTest(messages.Message):
    test = messages.IntegerField(1)


class GetResponse(messages.Message):
    success = messages.BooleanField(1)
    data = messages.MessageField(GetResponseTest, 2)


@api.endpoint(path="fetchdata", title="FetchData API")
class FetchData(remote.Service):
    @oauth2.required()
    @remote.method(message_types.VoidMessage, GetResponse)
    def get(self, request):
        fetched_data = fetchdata.FetchData.get()
        fetched_data_test = GetResponseTest(
            test=fetched_data.data.test
        )
        return GetResponse(
            success=fetched_data.success,
            data=fetched_data_test
        )
