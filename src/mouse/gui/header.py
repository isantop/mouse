#!/usr/bin/env python3

""" Mouse
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Mouse - The anony-mouse, privacy focused browser view.
"""

from gi.repository import Gtk

from .urlbar import URLBar

class Header(Gtk.HeaderBar):
    def __init__(self, webview, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.webview = webview

        self.nav_button_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
        Gtk.StyleContext.add_class(self.nav_button_box.get_style_context(), "linked")
        self.pack_start(self.nav_button_box)

        self.back_button = Gtk.Button.new_from_icon_name('go-previous-symbolic')
        self.back_button.connect('clicked', lambda x: self.webview.go_back())
        self.nav_button_box.append(self.back_button)

        self.forward_button = Gtk.Button.new_from_icon_name('go-next-symbolic')
        self.forward_button.connect('clicked', lambda x: self.webview.go_forward())
        self.nav_button_box.append(self.forward_button)

        self.refresh_button = Gtk.Button.new_from_icon_name('view-refresh-symbolic')
        self.refresh_button.connect('clicked', lambda x: self.webview.reload())
        self.pack_start(self.refresh_button)

        self.firefox_button = Gtk.Button.new_from_icon_name('firefox')
        self.pack_end(self.firefox_button)

        self.url_bar = URLBar(self.webview)
        self.set_title_widget(self.url_bar)

    
