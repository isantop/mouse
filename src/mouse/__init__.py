#!/usr/bin/env python3

""" Mouse
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Mouse - The anony-mouse, privacy focused browser view.
"""

import gi, sys

gi.require_versions({
    'Gtk': '4.0',
    'Gio': '2.0',
    'Adw': '1',
})

from .gui.window import MouseWindow
from gi.repository import Gtk, Gio, Adw

from .gui.window import MouseWindow

VERSION = '0.0.1'

APP_INFO:dict = {
    'name': 'Mouse Browser',
    'version': VERSION,
}

class MouseApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MouseWindow(APP_INFO, application=app)
        self.win.present()
    
def run_mouse():
    app = MouseApp(application_id="ro.santopiet.Mouse")
    app.run(sys.argv)