#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tqdm
import requests


def download_from_github(version, fn, target_dir):
    url = "https://github.com/hse-aml/intro-to-dl/releases/download/{0}/{1}".format(version, fn)
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length'))
    full_fn = os.path.join(target_dir, fn)
    with open(full_fn, 'wb') as f:
        bar = tqdm.tqdm_notebook(total=total_size, unit='B', unit_scale=True)
        bar.set_description(fn)
        for chunk in r.iter_content(32*1024):
            f.write(chunk)
            bar.update(len(chunk))
    if os.path.getsize(full_fn) != total_size:
        # not full download
        os.remove(full_fn)


def sequential_downloader(version, fns, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    for fn in fns:
        download_from_github(version, fn, target_dir)
