#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_tensor_shape(t):
    return [d.value for d in t.shape]


def get_tensors_shapes_string(tensors):
    res = []
    for t in tensors:
        res.extend([str(v) for v in get_tensor_shape(t)])
    return " ".join(res)
