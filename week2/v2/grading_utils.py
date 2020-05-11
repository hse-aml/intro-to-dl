#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_tensors_shapes_string(tensors):
    res = []
    for t in tensors:
        res.extend([str(v) for v in t.shape])
    return " ".join(res)
