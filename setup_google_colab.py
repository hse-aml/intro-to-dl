#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def download_github_code(path):
    filename = path.rsplit("/")[-1]
    os.system("wget https://raw.githubusercontent.com/hse-aml/intro-to-dl/master/{} -O {}".format(path, filename))


def setup_common():
    os.system("pip install tqdm")
    os.system("pip install --upgrade Keras==2.0.6")  # latest version breaks callbacks
    download_github_code("keras_utils.py")
    download_github_code("grading.py")
    download_github_code("download_utils.py")
    download_github_code("tqdm_utils.py")


def setup_week1():
    setup_common()
    download_github_code("week1/target.npy")
    download_github_code("week1/train.npy")


def setup_week2():
    setup_common()
    download_github_code("week2/matplotlib_utils.py")
    download_github_code("week2/preprocessed_mnist.py")
    download_github_code("week2/submit.py")
    download_github_code("week2/util.py")
    download_github_code("week2/validation_predictons.txt")
    setup_keras()


def setup_week2_v2():
    setup_common()
    download_github_code("week2/v2/grading_utils.py")
    download_github_code("week2/v2/matplotlib_utils.py")
    download_github_code("week2/v2/preprocessed_mnist.py")
    setup_keras()


def setup_week3():
    setup_common()
    download_github_code("week3/grading_utils.py")
    import download_utils
    download_utils.download_week_3_resources("../readonly/week3")
    setup_keras()


def setup_week4():
    setup_common()
    download_github_code("week4/lfw_dataset.py")
    download_github_code("week4/submit.py")
    download_github_code("week4/submit_honor.py")
    import download_utils
    download_utils.download_week_4_resources("../readonly/week4")


def setup_week5():
    setup_common()
    download_github_code("week5/data_copyright")
    download_github_code("week5/mtg_card_names.txt")
    download_github_code("week5/names")
    download_github_code("week5/submit.py")


def setup_week6():
    setup_common()
    download_github_code("week6/grading_utils.py")
    download_github_code("week6/utils.py")
    import download_utils
    download_utils.download_week_6_resources("../readonly/week6")
    setup_keras()


def setup_keras():
    import download_utils
    download_utils.download_all_keras_resources("../readonly/keras/models", "../readonly/keras/datasets")
