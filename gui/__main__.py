from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.toast import toast

from .parameter import DEFAULT_PATH


KV = '''
<Widget>:
    font_name: 'ipaexg00401/ipaexg.ttf'

MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "PyFileDB"

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)

<EntryTab>
    MDLabel:
        id: label
        text: "Tab 0"
        halign: "center"

    MDRaisedButton:
        text: "push"
        pos_hint: {'center_x': 0.5,'center_y': 0.2}

<SearchTab>
    MDLabel:
        id: label
        text: "Tab 0"
        halign: "center"

    MDTextField:
        hint_text: "No helper text"
        pos_hint: {'center_x': 0.5,'center_y': 0.3}
'''


class EntryTab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    pass


class SearchTab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    pass


class EntryData:
    def __init__(self) -> None:
        self.path: str = ''
        self.hashs: str = ''


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entrydata = EntryData()
        self.screen = Builder.load_string(KV)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            # preview=True,
        )

    def build(self, ):
        Window.bind(on_dropfile=self._on_file_drop)
        self.theme_cls.primary_palette = "Green"
        return self.screen

    def file_manager_open(self):
        self.file_manager.show(DEFAULT_PATH)
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        self.manager_open = False

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def on_start(self):
        self.root.ids.tabs.add_widget(EntryTab(title="Entry"))
        self.root.ids.tabs.add_widget(SearchTab(title="Search"))

    def on_tab_switch(self, instance_tabs, instance_tab,
                      instance_tab_label, tab_text):

        instance_tab.ids.label.text = self.entrydata.hashs

    def _on_file_drop(self, window, file_path):
        self.entrydata.hashs = file_path.decode('utf-8')


MainApp().run()
