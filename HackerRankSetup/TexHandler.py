import requests


class TexHandler(object):
    # api = 'http://chart.apis.google.com/chart?cht=tx&chs=24&chl=%24A_1%2C%20A_2%2C%20%5Ccdots%2C%20A_N%24'
    api = 'http://chart.apis.google.com/chart'

    def __init__(self):
        tex = '$A_1, A_2, \cdots, A_N$'
        payload = {'cht': 'tx', 'chs': 20, 'chl': tex}
        r = requests.get(self.api, params=payload)
        with open('..\\assets\\image.png', 'wb') as f:
            f.write(r.content)

        print r.url


if __name__ == "__main__":
    TexHandler()


