from unittest.mock import MagicMock

from what_is_year_now import what_is_year_now


class Test_Year_Now(TestCase):
    @patch('', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)

class TestYearNow(TestCase):
    @patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

    def test_get_ads(self):
        resp = MagicMock()
        resp.
        
        exp_resp_json ={
            '$id':'1',
            'currentDateTime': '2019-03-13T19:13Z',
            'dayOfTheWeek': 'Wednesday',
            'timeZoneName': 'UTC'
        }
        with patch.object(, 'get_ads', return_value=exp_resp_json):
            avito = Avito('access_token')
            ads = avito.get_ads(exp_ads['id'])
        assert ads == exp_ads

