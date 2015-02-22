import os
import requests
import hashlib


class TexHandler(object):
    api = 'http://chart.apis.google.com/chart'

    def __init__(self, _directory='..\\assets\\'):
        if not os.path.exists(_directory):
            os.makedirs(_directory)
        self.directory = _directory

    def get(self, tex):
        payload = {'cht': 'tx', 'chs': 20, 'chl': tex}
        hash_id = hashlib.md5(tex).hexdigest()
        file_name = '{}{}.{}'.format(self.directory, hash_id, 'png')
        r = requests.get(self.api, params=payload)
        with open(file_name, 'wb') as f:
            f.write(r.content)
        return '{}.{}'.format(hash_id, 'png')


if __name__ == "__main__":
    from Tkinter import Tk

    r = Tk()
    r.withdraw()
    directory = '..\\assets\\'
    # equation = r.selection_get(selection="CLIPBOARD")
    equation = '$A_1, A_2, \cdots, A_N$'
    chart = TexHandler(directory)
    image = chart.get(equation)
    raw_content = 'https://raw.githubusercontent.com/' \
                  'bionikspoon/HackerRank/master/assets/'
    md_link = '![{}]({})'.format(equation, raw_content + image)
    r.clipboard_clear()
    r.clipboard_append(md_link)
    print md_link
    r.destroy()


