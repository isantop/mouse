#!/usr/bin/env python3

""" Mouse
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Mouse - The anony-mouse, privacy focused browser view.
"""

import gi

gi.require_versions({
    'Gtk': '4.0',
    'Gio': '2.0',
})

from .gui.window import MouseWindow
from gi.repository import Gtk, Gio

VERSION = '0.0.1'

def make_window(app, data=None):
    # window = MouseWindow.new(app)
    window = Gtk.ApplicationWindow.new(app)
    window.present()

def run_mouse():
    app = Gtk.Application.new(
        'ro.santopiet.mouse', 
        Gio.ApplicationFlags.DEFAULT_FLAGS
    )

    app.connect('activate', make_window)

    app.run(None)
