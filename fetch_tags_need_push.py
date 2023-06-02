#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests


def fetch_tags(filter=None):
    url = 'https://hub.docker.com/v2/repositories/library/caddy/tags/?ordering=-last_updated&page_size=100&page=1'
    tags = []
    while url != None:
        req = requests.get(url)
        resp = req.json()
        url = resp['next']
        results = resp['results']
        for result in results:
            if result['tag_status'] != 'active':
                continue
            if filter(result['name']):
                tags.append(result['name'])
    return tags


def main():
    tags = fetch_tags(lambda tag: re.match(r'^\d+\.\d+\.\d+$', tag))
    for tag in tags:
        print(tag, end=',')


if __name__ == '__main__':
    main()
