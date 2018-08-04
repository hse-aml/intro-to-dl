#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def download_github_code(path):
    filename = path.rsplit("/")[-1]
    os.system("wget https://raw.githubusercontent.com/hse-aml/intro-to-dl/master/{} -O {}".format(path, filename))


def setup_common():
    os.system("pip install tqdm")
    os.system("pip install --upgrade Keras=2.0.6")  # latest version breaks callbacks
    download_github_code("keras_utils.py")
    download_github_code("grading.py")
    download_github_code("download_utils.py")


def setup_week2_v2():
    setup_common()
    download_github_code("week2/v2/grading_utils.py")
    download_github_code("week2/v2/matplotlib_utils.py")
    download_github_code("week2/v2/preprocessed_mnist.py")
