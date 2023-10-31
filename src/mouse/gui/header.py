#!/usr/bin/env python3

""" Mouse
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Mouse - The anony-mouse, privacy focused browser view.
"""

from gi.repository import Gtk

class Header(Gtk.HeaderBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nav_button_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
        Gtk.StyleContext.add_class(self.nav_button_box.get_style_context(), "linked")
        self.pack_start(self.nav_button_box)

        self.back_button = Gtk.Button.new_from_icon_name('go-previous-symbolic')
        self.nav_button_box.append(self.back_button)

        self.forward_button = Gtk.Button.new_from_icon_name('go-next-symbolic')
        self.nav_button_box.append(self.forward_button)