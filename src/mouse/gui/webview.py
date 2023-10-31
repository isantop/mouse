#!/usr/bin/env python3

""" Mouse
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Mouse - The anony-mouse, privacy focused browser view.
"""

from gi.repository import WebKit

class WebView(WebKit.WebView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def load(self, uri:str):
        print(f'Loading {uri}')
        # self.request = WebKit.URIRequest.new(uri)

        if not '://' in uri:
            uri = f'https://{uri}'
        self.load_uri(uri)
        