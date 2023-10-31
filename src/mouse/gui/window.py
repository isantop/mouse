#!/usr/bin/env python3

""" Mouse
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Mouse - The anony-mouse, privacy focused browser view.
"""

from gi.repository import Gtk

from .header import Header

class MouseWindow(Gtk.ApplicationWindow):
    def __init__(self, app_info:dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        header = Header()
        self.set_title(app_info['name'])
        self.set_default_size(1200, 800)
        self.set_titlebar(header)