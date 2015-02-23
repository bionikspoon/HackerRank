import os
import tempfile
import unittest
import json
import cPickle

import mock

import nose.tools as test
import shutil

import HackerRankSetup.HackerRankReadme as HRHR


class TestHackerRankReadme(unittest.TestCase):
    hackerrank_response = cPickle.load(
        open('./tests/resources/hackerrank_response.p', 'rb'))
    test_url = ('https://www.hackerrank.com/'
                'challenges/sherlock-and-queries')
    temp_dir = None
    tex_response = os.path.normpath('./tests/resources/mock_tex_response.json')


    @classmethod
    def setUpClass(cls):
        tempfile.tempdir = os.path.normpath('./tests/.tmp')
        cls.temp_dir = tempfile.mkdtemp()
        cls.assets = '../assets/'


    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.temp_dir):
            shutil.rmtree(cls.temp_dir)

    def setUp(self):
        self.handler = HRHR.HackerRankReadme(self.test_url,
                                             directory=self.temp_dir,
                                             assets=self.assets)
        patcher = mock.patch('HackerRankSetup.HackerRankReadme.TexHandler')
        self.MockTex = patcher.start()
        self.addCleanup(patcher.stop)

        patcher2 = mock.patch('HackerRankSetup.HackerRankReadme.requests')
        self.addCleanup(patcher2.stop)
        self.mock_requests = patcher2.start()
        self.mock_requests.get.return_value = self.hackerrank_response
        assert HRHR.requests is self.mock_requests

        test_tex = self.MockTex.return_value
        with open(self.tex_response) as response:
            tex_api = json.load(response)
        test_tex.get.side_effect = tex_api.get
        assert HRHR.TexHandler is self.MockTex

    def tearDown(self):
        del self.handler

    def test_class_initializes_properly(self):
        test.assert_equals(self.handler._directory, self.temp_dir)
        test.assert_equals(self.handler.url, self.test_url)
        rest_endpoint = ('https://www.hackerrank.com/'
                         'rest/contests/master/challenges/sherlock-and-queries')
        test.assert_equals(self.handler.rest_endpoint, rest_endpoint)
        test.assert_equals(self.handler.readme_file_name, 'README.md')
        test.assert_is_none(self.handler._model)
        test.assert_is_none(self.handler._source)
        test.assert_is_none(self.handler._readme)
        test.assert_is_none(self.handler._source_file_name)
        # test.assert_false(os.path.exists(self.temp_dir))

    def test_correct_file_name_for_source(self):
        test.assert_equals(self.handler.source_file_name,
                           'sherlock-and-queries.md')

    def test_build_source(self):
        with open('./tests/resources/sherlock-and-queries.md') as source:
            print self.handler.build_source()
            test.assert_equals(self.handler.build_source(), source.read())

    def test_build_readme(self):
        with open('./tests/resources/README.md') as readme:
            test.assert_equals(self.handler.build_readme(), readme.read())

    def test_run(self):
        self.handler.run()
        expected_source = os.path.normpath(
            './tests/resources/sherlock-and-queries.md')
        expected_readme = os.path.normpath('./tests/resources/README.md')
        test_source = os.path.join(self.temp_dir, 'sherlock-and-queries.md')
        test_readme = os.path.join(self.temp_dir, 'README.md')

        with open(expected_source) as expected_source, open(
                test_source) as test_source:
            test.assert_equals(expected_source.read(), test_source.read())
        with open(expected_readme) as expected_readme, open(
                test_readme) as test_readme:
            test.assert_equals(expected_readme.read(), test_readme.read())


if __name__ == '__main__':
    unittest.main()
