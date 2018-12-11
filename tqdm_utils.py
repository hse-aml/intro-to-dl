#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import tqdm
tqdm.monitor_interval = 0  # workaround for https://github.com/tqdm/tqdm/issues/481


class SimpleTqdm():
    def __init__(self, iterable=None, total=None, **kwargs):
        self.iterable = list(iterable) if iterable is not None else None
        self.total = len(self.iterable) if self.iterable is not None else total
        assert self.iterable is not None or self.total is not None
        self.current_step = 0
        self.print_frequency = max(self.total // 50, 1)
        self.desc = ""

    def set_description_str(self, desc):
        self.desc = desc

    def set_description(self, desc):
        self.desc = desc

    def update(self, steps):
        last_print_step = (self.current_step // self.print_frequency) * self.print_frequency
        i = 1
        while last_print_step + i * self.print_frequency <= self.current_step + steps:
            print("*", end='')
            i += 1
        self.current_step += steps

    def close(self):
        print("\n" + self.desc)

    def __iter__(self):
        assert self.iterable is not None
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.total:
            element = self.iterable[self.index]
            self.update(1)
            self.index += 1
            return element
        else:
            self.close()
            raise StopIteration


def use_simple_tqdm():
    try:
        import google.colab
        import os
        return not bool(int(os.environ.get("EXPERIMENTAL_TQDM", "0")))
    except ImportError:
        return False


def tqdm_notebook_failsafe(*args, **kwargs):
    if use_simple_tqdm():
        # tqdm is broken on Google Colab
        return SimpleTqdm(*args, **kwargs)
    else:
        return tqdm.tqdm_notebook(*args, **kwargs)
