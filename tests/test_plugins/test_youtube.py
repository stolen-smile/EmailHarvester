import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add the root directory of your project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from plugins.youtube import Plugin, search

class TestYoutubePlugin(unittest.TestCase):
    def setUp(self):
        self.app_mock = MagicMock()
        self.config = {'useragent':'test-agent', 'proxy': None}
        self.plugin = Plugin(self.app_mock, self.config)

    def test_plugin_init(self):
        self.app_mock.register_plugin.assert_called_once_with('youtube', {'search': search})
    
    @patch('plugins.youtube.app_emailharvester')
    def test_search(self, mock_app_emailharvester):
        all_emails = []

        mock_app_emailharvester.init = MagicMock()
        mock_app_emailharvester.process = MagicMock()
        mock_app_emailharvester.get_emails = MagicMock(side_effect=[
            ['22@email.com', 'john.doe@email.com'],
            [],
            ['2212@email.com'],
            [],
            []
        ])

        domain = "email.com"
        limit = 10
        result = search(domain,limit)

        expected_calls = [
            unittest.mock.call("http://search.yahoo.com/search?p=site%3Ayoutube.com+%40{word}&n=100&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vd=all&vst=0&vf=all&vm=p&fl=0&fr=yfp-t-152&xargs=0&pstart=1&b={counter}", domain, limit, 1, 100, 'Yahoo + Youtube'),
            unittest.mock.call("http://www.bing.com/search?q=site%3Ayoutube.com+%40{word}&count=50&first={counter}", domain, limit, 0, 50, 'Bing + Youtube'),
            unittest.mock.call('https://www.google.com/search?num=100&start={counter}&hl=en&q=site%3Ayoutube.com+"%40{word}"', domain, limit, 0, 100, 'Google + Youtube'),
            unittest.mock.call('http://www.baidu.com/search/s?wd=site%3Ayoutube.com+"%40{word}"&pn={counter}', domain, limit, 0, 10, 'Baidu + Youtube'),
            unittest.mock.call("http://www.exalead.com/search/web/results/?q=site%3Ayoutube.com+%40{word}&elements_per_page=10&start_index={counter}", domain, limit, 0, 50, 'Exalead + Youtube')
        ]

        mock_app_emailharvester.init_search.assert_has_calls(expected_calls)

        self.assertEqual(result, ['22@email.com', 'john.doe@email.com', '2212@email.com'])
        

if __name__ == '__main__':
    unittest.main()