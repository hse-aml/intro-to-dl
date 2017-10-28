#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
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


def link_all_files_from_dir(src_dir, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)
    for fn in os.listdir(src_dir):
        src_file = os.path.join(src_dir, fn)
        dst_file = os.path.join(dst_dir, fn)
        if os.name == "nt":
            shutil.copyfile(src_file, dst_file)
        else:
            if not os.path.exists(dst_file):
                os.symlink(os.path.abspath(src_file), dst_file)


def link_all_keras_resources():
    link_all_files_from_dir("../readonly/keras/datasets/", os.path.expanduser("~/.keras/datasets"))
    link_all_files_from_dir("../readonly/keras/models/", os.path.expanduser("~/.keras/models"))


def link_week_3_resources():
    link_all_files_from_dir("../readonly/week3/", ".")


def link_week_4_resources():
    link_all_files_from_dir("../readonly/week4/", ".")


def link_week_6_resources():
    link_all_files_from_dir("../readonly/week6/", ".")
