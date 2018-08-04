#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function


class SimpleTqdm():
    def __init__(self, total):
        self.total = total
        self.current_step = 0
        self.print_frequency = self.total // 50

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
