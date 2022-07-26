from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder


import pyfiledb


Window.size = (700, 250)


Builder.load_string("""
<Main>:
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    entry_hashs_input: entry_hashs_input
    entry_path_label: entry_path_label
    entry_status_label: entry_status_label
    search_hashs_input: search_hashs_input
    reslut_box: reslut_box

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
            ScrollView:
                size_hint_x: 3
                BoxLayout:
                    id: reslut_box
                    orientation: "vertical"
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


class Main(TabbedPanel):
    entry_hashs_input = None
    entry_path_label = None
    entry_status_label = None
    reslut_box = None

    def entry_file(self):
        entry_data.hashs = self.entry_hashs_input.text
        self.entry_status_label.text = f"{entry_data.file_path}\n{entry_data.hashs}\nを追加"
        filedb = pyfiledb.pyfiledb()
        filedb.append(entry_data.file_path, entry_data.hashs)
        filedb.close()

    def search_file(self):
        def _on_press(instance):
            Clipboard.copy(instance.text)
        self.reslut_box.clear_widgets()
        search_data.reslut = []  # reset
        search_data.hashs = self.search_hashs_input.text
        filedb = pyfiledb.pyfiledb()
        try:
            search_data.reslut.append(filedb.search(search_data.hashs))
            if search_data.reslut != [{}]:
                _ = BoxLayout()
                _.add_widget(
                    Label(text="クリックでPathコピー", font_name="ipaexg00401/ipaexg.ttf", size_hint_x=3.5))
                _.add_widget(
                    Label(text="ハッシュ", font_name="ipaexg00401/ipaexg.ttf"))
                self.reslut_box.add_widget(_)
                for datum in search_data.reslut:
                    for key, value in datum.items():
                        _ = BoxLayout()
                        _.add_widget(
                            Button(
                                text=f"{key}",
                                font_name="ipaexg00401/ipaexg.ttf",
                                font_size=11,
                                on_press=_on_press,
                                size_hint_x=3.5))
                        _.add_widget(
                            Label(
                                text=f"{value}",
                                font_name="ipaexg00401/ipaexg.ttf"))
                        self.reslut_box.add_widget(_)
            else:
                self.reslut_box.add_widget(
                    Label(
                        text="ハッシュ検索 結果なし",
                        font_name="ipaexg00401/ipaexg.ttf"))
        except ValueError:
            self.reslut_box.add_widget(
                Label(
                    text="ハッシュが#〇〇〇になってないです",
                    font_name="ipaexg00401/ipaexg.ttf"))


class MainApp(App):
    def build(self):
        self.main = Main()
        Window.bind(on_dropfile=self._on_dropped_file)
        return self.main

    def _on_dropped_file(self, window, file_path):
        entry_data.file_path = file_path.decode('utf-8')
        self.main.ids.entry_path_label.text = entry_data.file_path


if __name__ == '__main__':
    MainApp().run()
