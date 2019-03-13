from unittest.mock import MagicMock, patch

from what_is_year_now import what_is_year_now


class TestYearNow(TestCase):

    def test_get_ads(self):
        resp = MagicMock()
        resp.
        exp_resp_json ={
            '$id':'1',
            'currentDateTime': '2019-03-13T19:13Z',
            'dayOfTheWeek': 'Wednesday',
            'timeZoneName': 'UTC'
        }
        with patch.object(, '', return_value=exp_resp_json):
            avito = Avito('access_token')
            ads = avito.get_ads(exp_ads['id'])
        assert ads == exp_ads

