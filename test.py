#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Python imports
import sys

# Gtk imports
import gi
gi.require_versions({
    'Gtk': '4.0',
    'WebKit': '6.0',
})
from gi.repository import Gtk, Gdk, WebKit


class BrowserTab(Gtk.Box):
    def __init__(self, *args, **kwargs):
        super(BrowserTab, self).__init__(*args, **kwargs)
        self.set_orientation(Gtk.Orientation.VERTICAL)

        go_button = Gtk.Button.new_with_label("go to...")
        go_button.connect("clicked", self._load_url)
        self.url_bar = Gtk.Entry()
        self.url_bar.connect("activate", self._load_url)
        self.webview = WebKit.WebView()
        for i in [self, self.webview]:
            i.set_hexpand(True)
            i.set_vexpand(True)
        # self.show()

        self.go_back = Gtk.Button.new_with_label("Back")
        self.go_back.connect("clicked", lambda x: self.webview.go_back())
        self.go_forward = Gtk.Button.new_with_label("Forward")
        self.go_forward.connect("clicked", lambda x: self.webview.go_forward())

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_child(self.webview)

        find_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
        close_button = Gtk.Button.new_with_label("Close")
        close_button.connect("clicked", lambda x: find_box.hide())
        self.find_entry = Gtk.Entry()
        self.find_entry.connect("activate",
                            lambda x: self.webview.search_text(
                                self.find_entry.get_text(),
                                    False, True, True))
        prev_button = Gtk.Button.new_with_label("Previous")
        next_button = Gtk.Button.new_with_label("Next")
        prev_button.connect("clicked",
                            lambda x: self.webview.search_text(
                                self.find_entry.get_text(),
                                    False, False, True))
        next_button.connect("clicked",
                            lambda x: self.webview.search_text(
                                self.find_entry.get_text(),
                                    False, True, True))
        find_box.append(close_button)
        find_box.append(self.find_entry)
        find_box.append(prev_button)
        find_box.append(next_button)
        self.find_box = find_box

        url_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
        url_box.append(self.go_back)
        url_box.append(self.go_forward)
        url_box.append(self.url_bar)
        url_box.append(go_button)

        self.append(url_box)
        self.append(scrolled_window)
        self.append(find_box)

        # url_box.show_all()
        # scrolled_window.show_all()

    def _load_url(self, widget):
        url = self.url_bar.get_text()
        if not "://" in url:
            url = "http://" + url
        self.webview.load_uri(url)


class Browser(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super(Browser, self).__init__(*args, **kwargs)

        # create notebook and tabs
        # self.notebook = Gtk.Notebook()
        # self.notebook.set_scrollable(True)

        # basic stuff
        self.tabs = []
        self.set_size_request(400, 400)

        # create a first, empty browser tab
        # self.tabs.append((self._create_tab(), Gtk.Label.new("New Tab")))
        # self.notebook.append_page(*self.tabs[0])
        # self.set_child(self.notebook)

        # connect signals
        # self.connect("destroy", Gtk.main_quit)
        # self.connect("key-press-event", self._key_pressed)
        # self.notebook.connect("switch-page", self._tab_changed)

        # self.notebook.show()
        self.set_child(self._create_tab())

    def _tab_changed(self, notebook, current_page, index):
        if not index:
            return
        title = self.tabs[index][0].webview.get_title()
        if title:
            self.set_title(title)

    def _title_changed(self, webview, frame, title):
        current_page = self.notebook.get_current_page()

        counter = 0
        for tab, label in self.tabs:
            if tab.webview is webview:
                label.set_text(title)
                if counter == current_page:
                    self._tab_changed(None, None, counter)
                break
            counter += 1

    def _create_tab(self):
        tab = BrowserTab()
        # tab.webview.connect("title-changed", self._title_changed)
        return tab

    def _reload_tab(self):
        self.tabs[self.notebook.get_current_page()][0].webview.reload()

    def _close_current_tab(self):
        if self.notebook.get_n_pages() == 1:
            return
        page = self.notebook.get_current_page()
        current_tab = self.tabs.pop(page)
        self.notebook.remove(current_tab[0])

    def _open_new_tab(self):
        current_page = self.notebook.get_current_page()
        page_tuple = (self._create_tab(), Gtk.Label.new("New Tab"))
        self.tabs.insert(current_page + 1, page_tuple)
        self.notebook.insert_page(page_tuple[0], page_tuple[1],
            current_page + 1)
        self.notebook.set_current_page(current_page + 1)

    def _focus_url_bar(self):
        current_page = self.notebook.get_current_page()
        self.tabs[current_page][0].url_bar.grab_focus()

    def _raise_find_dialog(self):
        current_page = self.notebook.get_current_page()
        self.tabs[current_page][0].find_box.show_all()
        self.tabs[current_page][0].find_entry.grab_focus()

    def _key_pressed(self, widget, event):
        modifiers = Gtk.accelerator_get_default_mod_mask()
        mapping = {Gdk.KEY_r: self._reload_tab,
                   Gdk.KEY_w: self._close_current_tab,
                   Gdk.KEY_t: self._open_new_tab,
                   Gdk.KEY_l: self._focus_url_bar,
                   Gdk.KEY_f: self._raise_find_dialog,
                #    Gdk.KEY_q: Gtk.main_quit}
        }

        if event.state & modifiers == Gdk.ModifierType.CONTROL_MASK \
          and event.keyval in mapping:
            mapping[event.keyval]()


def on_activate(app):
    win = Browser(application=app)
    win.present()

app = Gtk.Application()
app.connect('activate', on_activate)

app.run(None)