#!/usr/bin/env python3

""" Mouse
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Mouse - The anony-mouse, privacy focused browser view.
"""

from gi.repository import Gtk

class URLBar(Gtk.Entry):
    def __init__(self, webview, header, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.webview = webview
        self.set_icon_from_icon_name(
            Gtk.EntryIconPosition.SECONDARY,
            'go-last-symbolic'
        )
        self.header = header
        self.set_icon_sensitive(Gtk.EntryIconPosition.SECONDARY, True)
        self.connect('activate', self.load_uri)
        self.connect('icon-release', self.icon_clicked)
        self.webview.connect('resource-load-started', self.set_uri_match)
        self.webview.connect('load-changed', self.update_progress)
        for i in ['notify::uri', 'notify::estimated-load-progress', 'notify::is-loading']:
            self.webview.connect(i, self.update_progress)

        self.set_hexpand(True)
    
    def update_progress(self, webview, data=None):
        progress = self.webview.get_estimated_load_progress()
        print(f'Loading progress: {progress}')
        self.set_progress_fraction(progress)
        if self.get_progress_fraction() == 1.0:
            self.set_progress_fraction(0.0)
        self.sync_ui()
    
    def sync_ui(self):
        self.header.back_button.set_sensitive(
            self.webview.can_go_back()
        )
        self.header.forward_button.set_sensitive(
            self.webview.can_go_forward()
        )

    def set_uri_match(self, web_view, resource, request):
        self.set_text(self.webview.props.uri)
    
    def icon_clicked(self, entry, pos, data=None):
        if pos == Gtk.EntryIconPosition.SECONDARY:
            self.load_uri(entry)

    def load_uri(self, widget, data=None):
        uri:str = self.get_text()
        search_term:str = ''
        if not '://' in uri:
            if not '.' in uri:
                search_term_lst = uri.split()
                search_term = '+'.join(search_term_lst)
                uri = f'https://duckduckgo.com/?t=h_&q={search_term}&ia=mouse-browser'
            else:
                uri = f'https://{uri}'
        
        self.webview.load_uri(uri)
