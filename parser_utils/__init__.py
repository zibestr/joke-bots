import requests
from bs4 import BeautifulSoup
from time import sleep


class WebHTMLParser:
    def __init__(self, url):
        self.response = None
        self.soup = None
        self.url = url

    def _find_element(self, tag, html_class):
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

        element = self.soup.find(tag, class_=html_class)

        sleep(0.5)
        return element


class BaneksParser(WebHTMLParser):
    def __init__(self):
        super().__init__('https://baneks.site/random')

    def find_joke(self):
        joke = str(self._find_element('div',
                                      'block-content '
                                      'mdl-card__supporting-text '
                                      'mdl-color--grey-300 '
                                      'mdl-color-text--grey-900').find('p')).replace('<p>', '').replace('</p>', '')
        joke = joke.replace('<br/>', '\n')

        return joke
