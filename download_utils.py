#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import os
import tqdm
import requests

kill_thread = threading.Event()


def download_from_github(version, fn, target_dir):
    url = "https://github.com/hse-aml/intro-to-dl/releases/download/{0}/{1}".format(version, fn)
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length'))
    full_fn = os.path.join(target_dir, fn)
    with open(full_fn, 'wb') as f:
        bar = tqdm.tqdm_notebook(total=total_size, unit='B', unit_scale=True)
        for chunk in r.iter_content(32*1024):
            f.write(chunk)
            bar.update(len(chunk))
            if kill_thread.is_set():
                # master asks to stop
                break
    if os.path.getsize(full_fn) != total_size:
        # not full download
        os.remove(full_fn)


def parallel_downloader(version, fns, target_dir):
    kill_thread.clear()
    os.system("mkdir -p {0}".format(target_dir))
    threads = []
    try:
        for fn in fns:
            t = threading.Thread(target=download_from_github, args=(version, fn, target_dir))
            t.daemon = True
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("Killed")
    finally:
        kill_thread.set()
        for t in threads:
            t.join()
    print("Done")


def sequential_downloader(version, fns, target_dir):
    kill_thread.clear()
    os.system("mkdir -p {0}".format(target_dir))
    for fn in fns:
        download_from_github(version, fn, target_dir)
