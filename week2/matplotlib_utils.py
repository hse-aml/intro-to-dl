#!/usr/bin/env python
# -*- coding: utf-8 -*-
from IPython.display import clear_output, display_html, HTML
import contextlib
import time
import io
import urllib
import base64


class SimpleMovieWriter(object):
    """
    Usage example:
        anim = animation.FuncAnimation(...)
        anim.save(None, writer=SimpleMovieWriter(sleep=0.01))
    """
    def __init__(self, sleep=0.1):
        self.sleep = sleep

    def setup(self, fig):
        self.fig = fig

    def grab_frame(self, **kwargs):
        img_data = io.BytesIO()
        self.fig.savefig(img_data, format='jpeg')
        img_data.seek(0)
        uri = 'data:image/jpeg;base64,' + urllib.request.quote(base64.b64encode(img_data.getbuffer()))
        img_data.close()
        clear_output(wait=True)
        display_html(HTML('<img src="' + uri + '">'))
        time.sleep(self.sleep)

    @contextlib.contextmanager
    def saving(self, fig, *args, **kwargs):
        self.setup(fig)
        try:
            yield self
        finally:
            pass
