from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.tab import MDTabsBase

Window.size = (400, 700)

KV = '''
<StarButton@MDIconButton>
    icon: "star"
    on_release: self.icon = "star-outline" if self.icon == "star" else "star"

Screen:
    MDBoxLayout:
        orientation:"vertical"
        MDToolbar:
            title: "Movies Base"
            icon: "git"
            height:100
            left_action_items: [["menu", lambda x: x]]
            mode: "free-end"
        
        MDTabs:
            id:tabs
            on_tab_switch: app.on_tab_switch(*args)
            Tab:
                text:"All"
                id:allTab
                
                MDBoxLayout:
                    orientation:"vertical"
                    MDTextField:
                        hint_text: "Search movie"
                        size_hint:(.9,None)
                        pos_hint:{'center_x':.5, 'center_y':0.5}
                        mode: "rectangle"
                        
                    ScrollView:
                        MDList:
                            padding:10
                            spacing:10
                            id:scrollList
                            
            Tab:
                text:"New"
                id:newTab
                MDBoxLayout:
                    orientation:"vertical"
                    ScrollView:
                        MDList:
                            id:newList


<MoviesListCard>:
    orientation: "vertical"
    size_hint: 0.9, None
    size: "430dp", "180dp"
    border_radius: 10
    radius: [15]
    height: box_top.height + box_bottom.height
    # focus_behavior: True
    # ripple_behavior: True

    MDBoxLayout:
        id: box_top
        spacing: "20dp"
        adaptive_height: True

        FitImage:
            source: "img_5.jpg"
            size_hint: .3, None
            height: text_box.height
            border_radius: 20
            radius: [15]

        MDGridLayout:
            cols:2
            id: text_box
            orientation: "vertical"
            adaptive_height: True
            spacing: "10dp"
            padding: 0, "10dp", "10dp", "10dp"

            MDLabel:
                id:text1
                text: "Ride the Lightning"
                theme_text_color: "Primary"
                font_style: "H5"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]

            MDRectangleFlatButton:
                text: "Open"
                
            MDLabel:
                text: "July 27, 1984"
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: "Primary"
            
    MDSeparator:

    MDBoxLayout:
        id: box_bottom
        adaptive_height: True
        padding: "10dp", 0, 0, 0

        MDLabel:
            text: "Your Rating"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_y": .5}
            theme_text_color: "Primary"

        StarButton:
        StarButton:
        StarButton:
        StarButton:
'''
class Tab(FloatLayout, MDTabsBase):
    pass

class NewMoviesDetected(ScrollView):
    pass

class MoviesListCard(MDCard):
    pass

class MainApp(MDApp):


    List = []

    def __init__(self, **kwargs):
        super( ).__init__( **kwargs )


    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_start(self):
        if self.List.__len__() is 0:
            pass
        for i in range(5): self.root.ids.scrollList.add_widget( MoviesListCard() )

        for k in range(5): self.root.ids.newList.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        print(tab_text)

MainApp().run()