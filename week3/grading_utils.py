#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def model_total_params(model):
    """
    Total params for Keras model
    """
    summary = []
    model.summary(print_fn=lambda x: summary.append(x))
    for line in summary:
        m = re.match("Total params: ([\d,]+)", line)
        if m:
            return int(re.sub(",", "", m.groups()[0]))
    return 0
