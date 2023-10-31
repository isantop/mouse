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
    'WebKit': '6.0',
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
        self.connect('open', self.on_open)

    def on_activate(self, app):
        self.win = MouseWindow(APP_INFO, application=app)
        self.win.present()
    
    def on_open(self, app:Adw.Application, files:list, hint:str, data=None):
        new_win = MouseWindow(APP_INFO, application=app)
        uri = files[0].get_uri()
        new_win.webview.load_uri(uri)
        new_win.present()
    
def run_mouse():
    app = MouseApp(application_id="ro.santopiet.Mouse", flags=Gio.ApplicationFlags.HANDLES_OPEN)
    app.run(sys.argv)