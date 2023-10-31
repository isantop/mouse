#!/usr/bin/env python3

""" Mouse
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Mouse - The anony-mouse, privacy focused browser view.
"""

import subprocess

from gi.repository import Gtk, WebKit

from .header import Header
from .webview import WebView

class MouseWindow(Gtk.ApplicationWindow):
    def __init__(self, app_info:dict, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.webview = WebKit.WebView()
        self.webview.set_hexpand(True)
        self.webview.set_vexpand(True)
        self.webview.show()

        header = Header(self.webview)
        self.set_title(app_info['name'])
        self.set_default_size(1200, 800)
        self.set_titlebar(header)


        header.firefox_button.connect('clicked', self.open_in_firefox)
        
        self.web_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        self.set_child(self.web_box)
        self.web_box.append(self.webview)

    def open_in_firefox(self, button, data=None):
        """This is placeholder, but gets the basic idea fully functional"""
        uri = self.webview.props.uri
        subprocess.run(['firefox', '--new-tab', uri])
        self.destroy()
    
    def _test_load_uri(self, button, data=None):
        print('clicked')
        self.webview.load_uri('https://santopiet.ro')
        # self.webview.load_plain_text('Hello World!')
