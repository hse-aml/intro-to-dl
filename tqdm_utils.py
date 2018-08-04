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
        for i in range(steps):
            self.current_step += 1
            if self.current_step % self.print_frequency == 0:
                print("*", end='')

    def close(self):
        print("\n" + self.desc)
