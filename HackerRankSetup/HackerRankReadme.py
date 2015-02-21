import os
# import urllib2
# import requests
import json
import re


class HackerRankReadme(object):
    rest_base = 'https://www.hackerrank.com' \
                '/rest/contests/master/challenges/'
    hackerrank_logo = 'https://www.hackerrank.com/' \
                      'assets/brand/typemark_60x200.png'

    def __init__(self, url, directory='../temp/', readme_file='README.md'):
        self._directory = None
        self.directory = directory

        self.url = url
        self.rest_endpoint = self.get_rest_endpoint(url)
        self.readme_file = readme_file
        with open('tests/mock_response.json') as response:
            self.model = json.load(response)['model']

        self.source = self.build_source()
        self.readme = self.build_readme()

        self.source_file = self.get_source_file_name()


    def run(self):
        with open(self.directory + self.source_file, 'w') as f:
            f.write(self.source)
        with open(self.directory + self.readme_file, 'w') as f:
            f.write(self.readme)

    def get_source_file_name(self):
        return '{}.md'.format(self.model['slug'])

    def build_readme(self):
        readme = self.source.replace('**', '###')
        return readme

    def build_source(self):
        logo = '![{}]({})'.format('HackerRank', self.hackerrank_logo)
        name = '#{}#'.format(self.model['name'].strip())
        url_crumb = '{} \ {} \ {} \ {}'.format('HackerRank',
                                               self.model['track'][
                                                   'track_name'],
                                               self.model['track']['name'],
                                               self.model['name'])
        link = '[{}]({})'.format(url_crumb, self.url)
        preview = '\n{}'.format(self.model['preview'])
        body = '\n##{}##\n\n{}'.format('Problem Statement', self.model['body'])

        source = '\n'.join([logo, name, link, preview, body])
        source = re.sub(r' +$', '', source, flags=re.M)
        source = source.replace('**\n', '**\n\n')
        return source

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, value):
        if not os.path.exists(value):
            os.makedirs(value)
        self._directory = value

    def get_rest_endpoint(self, from_url):
        url_slug = re.search(r'/([a-z1-9-]+)/?$', from_url).group(1)
        return self.rest_base + url_slug


if __name__ == "__main__":
    _url = 'https://www.hackerrank.com/challenges/sherlock-and-queries'
    HackerRankReadme(_url).run()