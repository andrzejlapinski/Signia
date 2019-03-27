# coding: utf8
from backend import test, fetchdata


class TestFetchData(test.TestCase):

    def test_get(self):
        obj = fetchdata.FetchData.get()
        self.assertTrue(obj.success == True)
        self.assertTrue(type(obj.data) == fetchdata.FetchDataTestProperty)
        self.assertTrue(obj.data.test == 123)

    def test_get_no_data(self):
        self.assertRaises(fetchdata.KeyNotFound,
                          lambda: fetchdata.FetchData.get(url="http://www.mocky.io/v2/5c97db042f00006c009f2ebe"))

    def test_get_no_test_key(self):
        self.assertRaises(fetchdata.KeyNotFound,
                          lambda: fetchdata.FetchData.get(url="http://www.mocky.io/v2/5c97e5702f00002a009f2ec2"))

    def test_get_wrong_status(self):
        self.assertRaises(fetchdata.UrlNotFound,
                          lambda: fetchdata.FetchData.get(url="http://www.mocky.io/v2/5c9a968f3500006200d0c6f2"))

    def test_get_no_success_key(self):
        self.assertRaises(fetchdata.KeyNotFound,
                          lambda: fetchdata.FetchData.get(url="http://www.mocky.io/v2/5c9a97da3500004c00d0c6f5"))


class TestFetchDataApi(test.TestCase):
    def test_login(self):
        self.api_mock.post("/api/user.create", dict(email="test@gmail.com", password="test"))

        resp = self.api_mock.post("/api/fetchdata.get")
        self.assertEqual(resp.get("error"), None)
