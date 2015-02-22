import os
import unittest
import json

from mock import MagicMock, patch

import nose.tools as test
import shutil
import HackerRankSetup

from HackerRankSetup.HackerRankReadme import HackerRankReadme, TexHandler
from HackerRankSetup.TexHandler import TexHandler


class TestHackerRankReadme(unittest.TestCase):
    def setUp(self):
        self.test_url = 'https://www.hackerrank.com/' \
                        'challenges/sherlock-and-queries'
        self.test_directory = './tests/temp/'
        self.handler = HackerRankReadme(self.test_url,
                                        directory=self.test_directory)
        self.mock_get_model()
        patcher = patch('HackerRankSetup.HackerRankReadme.TexHandler')
        self.MockTex = patcher.start()
        self.addCleanup(patcher.stop)
        test_tex = self.MockTex.return_value

        with open('./tests/assets/mock_tex_response.json') as response:
            tex_api = json.load(response)
        test_tex.get.side_effect = lambda x: tex_api.get(x)
        assert HackerRankSetup.HackerRankReadme.TexHandler is self.MockTex

    def tearDown(self):
        del self.handler
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)

    def mock_get_model(self):
        self.handler.get_model = MagicMock()
        with open('./tests/assets/mock_hackerrank_response.json') as response:
            mock_response = json.load(response)['model']
        self.handler.get_model.return_value = mock_response
        assert self.handler.get_model() == mock_response


    def test_class_initializes_properly(self):
        test.assert_equals(self.handler._directory, self.test_directory)
        test.assert_equals(self.handler.url, self.test_url)
        rest_endpoint = 'https://www.hackerrank.com' \
                        '/rest/contests/master/challenges/' \
                        'sherlock-and-queries'
        test.assert_equals(self.handler.rest_endpoint, rest_endpoint)
        test.assert_equals(self.handler.readme_file_name, 'README.md')
        test.assert_is_none(self.handler._model)
        test.assert_is_none(self.handler._source)
        test.assert_is_none(self.handler._readme)
        test.assert_is_none(self.handler._source_file_name)
        test.assert_false(os.path.exists(self.test_directory))

    def test_correct_file_name_for_source(self):
        test.assert_equals(self.handler.source_file_name,
                           'sherlock-and-queries.md')

    def test_build_source(self):
        with open('./tests/assets/sherlock-and-queries.md') as source:
            print self.handler.build_source()
            test.assert_equals(self.handler.build_source(), source.read())

    def test_build_readme(self):
        with open('./tests/assets/README.md') as readme:
            # print self.handler.build_readme()
            test.assert_equals(self.handler.build_readme(), readme.read())

    def test_run(self):
        self.handler.run()
        actual_source = './tests/assets/sherlock-and-queries.md'
        actual_readme = './tests/assets/README.md'
        test_source = './tests/temp/sherlock-and-queries.md'
        test_readme = './tests/temp/README.md'

        with open(actual_source) as actual_source, open(
                test_source) as test_source:
            test.assert_equals(actual_source.read(), test_source.read())
        with open(actual_readme) as actual_readme, open(
                test_readme) as test_readme:
            test.assert_equals(actual_readme.read(), test_readme.read())


if __name__ == '__main__':
    unittest.main()
