import scrapy
import json
from urllib.parse import urlencode
import scrapy


class MonsterSpider(scrapy.Spider):
    name = "monster"

    def get_indeed_search_url(self, keyword, location, offset=0):
        ''' Create the target url for monser search '''
        parameters = {"q": keyword, "l": location, "fromage": 14, "filter": 0, "start": offset}
        return "https://www.de.indeed.com/jobs?" + urlencode(parameters)
