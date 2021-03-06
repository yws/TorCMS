# -*- coding: utf-8 -*-

'''
Generating sitemap.
'''
import os
from torcms.model.post_model import MPost
from torcms.model.wiki_model import MWiki
from config import router_post, SITE_CFG

sitemap_file = 'sitemap.txt'


def gen_post_map():
    mpost = MPost()
    with open(sitemap_file, 'a') as fo:
        for kind_key in router_post:
            recent_posts = mpost.query_all(kind=kind_key)
            for recent_post in recent_posts:
                url = os.path.join(SITE_CFG['site_url'],
                                   router_post[recent_post.kind],
                                   recent_post.uid)
                fo.write('{url}\n'.format(url=url))


def gen_wiki_map():
    mwiki = MWiki()

    # wiki
    wiki_recs = mwiki.query_all(limit=10000, kind='1')

    with open(sitemap_file, 'a') as fo:
        for rec in wiki_recs:
            url = os.path.join(SITE_CFG['site_url'], 'wiki', rec.title)
            fo.write('{url}\n'.format(url=url))

    ## page.
    page_recs = mwiki.query_all(limit=10000, kind='2')

    with open(sitemap_file, 'a') as fo:
        for rec in page_recs:
            url = os.path.join(SITE_CFG['site_url'], 'page', rec.uid)

            fo.write('{url}\n'.format(url=url))


def run_sitemap(*args):
    if os.path.exists(sitemap_file):
        os.remove(sitemap_file)

    gen_wiki_map()
    gen_post_map()
