import multiprocessing as mp

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

import pyfiledb


Window.size = (700, 250)


Builder.load_string("""
#:import Clipboard kivy.core.clipboard.Clipboard

<Test>:
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    entry_hashs_input: entry_hashs_input
    entry_path_label: entry_path_label
    entry_status_label: entry_status_label
    search_hashs_input: search_hashs_input
    search_status_label: search_status_label

    TabbedPanelItem:
        text: 'Entry'
        BoxLayout:
            orientation: 'vertical'
            TextInput:
                id: entry_hashs_input
                text: 'ハッシュを「#xxxx#yyyy」のように入力'
                font_name: 'ipaexg00401/ipaexg.ttf'
                size_hint_y: 1
            Label:
                id: entry_path_label
                text: 'ファイルをドラッグ＆ドロップ'
                font_name: 'ipaexg00401/ipaexg.ttf'
                font_size: 13
                size_hint_y: 1
            Label:
                id: entry_status_label
                text: ''
                font_name: 'ipaexg00401/ipaexg.ttf'
                font_size: 14
                size_hint_y: 3
            Button:
                text: 'Entry'
                on_release: root.entry_file()
                size_hint_y: 1

    TabbedPanelItem:
        text: 'Search'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                TextInput:
                    id: search_hashs_input
                    text: 'ハッシュを「#xxxx#yyyy」のように入力'
                    font_name: 'ipaexg00401/ipaexg.ttf'
                Button:
                    text: 'Search'
                    on_release: root.search_file()
            BoxLayout:
                orientation: 'vertical'
                size_hint_x: 3
                Button:
                    text: 'Copy'
                    on_release: Clipboard.copy(search_status_label.text)
                Label:
                    text: '検索結果'
                    id: search_status_label
                    text_size: root.width * 2 / 3, None
                    font_name: 'ipaexg00401/ipaexg.ttf'
                    size_hint_y: 5
""")


class EntryData:
    def __init__(self) -> None:
        self.file_path = ''
        self.hashs = ''


class SearchData:
    def __init__(self) -> None:
        self.hashs = ''
        self.reslut = []


entry_data = EntryData()
search_data = SearchData()


class Test(TabbedPanel):
    entry_hashs_input = None
    entry_path_label = None
    entry_status_label = None
    search_hashs_input = None
    search_status_label = None

    def entry_file(self):
        entry_data.hashs = self.entry_hashs_input.text
        self.entry_status_label.text = f"{entry_data.file_path}\n{entry_data.hashs}\nを追加"
        filedb = pyfiledb.pyfiledb()
        filedb.append(entry_data.file_path, entry_data.hashs)
        filedb.close()

    def search_file(self):
        search_data.reslut = []  # reset
        search_data.hashs = self.search_hashs_input.text
        filedb = pyfiledb.pyfiledb()
        search_data.reslut.append(filedb.search(search_data.hashs))
        if len(search_data.reslut) != 0:
            tmp_text = []
            for i, datum in enumerate(search_data.reslut):
                for key, value in datum.items():
                    tmp_text.append(f"-[{i}]-\npath: {key}\nhash: {value}")
            self.search_status_label.text = '\n'.join(tmp_text)


class TabbedPanelApp(App):
    def build(self):
        self.test = Test()
        Window.bind(on_dropfile=self._on_dropped_file)
        return self.test

    def _on_dropped_file(self, window, file_path):
        entry_data.file_path = file_path.decode('utf-8')
        self.test.ids.entry_path_label.text = entry_data.file_path


TabbedPanelApp().run()
