#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from packaging import version


def fetch_tags(repo, filter=None):
    url = 'https://hub.docker.com/v2/repositories/%s/tags/?ordering=-last_updated&page_size=100&page=1' % repo
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
    return sorted(tags, key=lambda x: version.Version(x))


def main():
    this_repo_tags = fetch_tags(
        'leoppro/docker-caddy-webdav', lambda tag: re.match(r'^\d+\.\d+\.\d+$', tag))
    first_this_repo_tags = '0.0.0'
    if len(this_repo_tags) > 0:
        first_this_repo_tags = this_repo_tags[0]
    caddy_tags = fetch_tags(
        'library/caddy', lambda tag: re.match(r'^\d+\.\d+\.\d+$', tag) and version.Version(tag) >= version.Version(first_this_repo_tags))
    need_push_tags = list(set(caddy_tags).difference(set(this_repo_tags)))
    need_push_tags = sorted(need_push_tags, key=lambda x: version.Version(x))
    if len(need_push_tags) == 0:
        print('push_tag=')
        return
    print('push_tag=%s' % need_push_tags[0])


if __name__ == '__main__':
    main()
