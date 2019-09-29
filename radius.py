#!/usr/bin/env python3
import urllib
import json

import requests


class Search:
    def __init__(self):
        self.api = "https://scicat.esss.se/api/v3/Datasets?filter="
        self.token = "&access_token=" + \
            "uqhj8qvLnH5oJfFH5mvE6xfUlP5vssDeCyP6g1a2g65CJHP7Do9QtMzIxeDMVXqb"

    def search(self):
        query = {"where": {"and": [{'scientificMetadata.chopper_4_radius.value': {
            "gt": 1}}, {"creationLocation": 'V20'}]}}
        # pid = "20.500.12269/0a269002-83e2-4f18-bb98-36c01836d66a"
        # query = {"where":{"pid":pid}}
        print(json.dumps(query,separators=(',', ':')))
        encode_query = urllib.parse.quote_plus(json.dumps(query,separators=(',', ':')))
        url = self.api + encode_query + self.token

        print(url)
        response = requests.get(url)
        array = response.json()
        result = array[0]
        print(result)


def main():
    search = Search()
    search.search()


if __name__ == "__main__":
    main()
