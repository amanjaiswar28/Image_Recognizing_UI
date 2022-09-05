from kivy.app import App
from kivy.uix.button import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import *
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import random
from kivy.uix.popup import Popup



class MyLayout(GridLayout):
    url_ans_dict = {
        "https://nationaltoday.com/wp-content/uploads/2021/11/pangolin-day.jpg": [
            "Pengolin", "Ant eater"],
        "https://images.unsplash.com/photo-1566034356854-23137d8128de?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YW50ZWxvcGV8ZW58MHx8MHx8&w=1000&q=80": [
            "Antelope", "Black buck"],
        "https://www.wwf.org.uk/sites/default/files/styles/social_share_image/public/2019-04/Jaguar%20in%20a%20tree%2C%20Brazil%20%C2%A9%20Y.-J.%20Rey-Millet%20%20WWF%20_2.jpg?itok=63SNvaO0": [
            "Jaguar", "Leopard"]
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.load_new_image(url=list(self.url_ans_dict.keys())[0])

    def ans_correct_callback(self, url, instance):
        print(f"This button was called -- {instance.text}")
        if self.url_ans_dict.get(url)[0] == instance.text:
            print("Correct Answer")
            correct = True
        else:
            print("Wrong Answer")
            correct = False
        self.show_popup(correct)
        self.clear_widgets()

        rand_int = random.randint(1, len(list(self.url_ans_dict.keys()))-1)
        self.load_new_image(list(self.url_ans_dict.keys())[rand_int])
    
    
    
    def show_popup(self, correct):
        layout = GridLayout(cols=1, padding=10)
        label = Label(text="Correct") if correct else Label(text="Wrong Answer")
        layout.add_widget(label)
        popup = Popup(title="", content=layout, size_hint=(None, None), size=(200, 200), auto_dismiss=True)
        popup.open()




    def load_new_image(self, url):
        self.ans_button = self.url_ans_dict.get(url)
        self.add_widget(AsyncImage(source=url))
        self.bottom_layout = FloatLayout(size=(600, 600))
        self.ans_1 = Button(text=self.ans_button[0],
                            background_color=(0.1, 0.5, 0.3, 1),
                            size_hint=(0.2, 0.2),
                            pos_hint={'x': 0.3, 'y': 0.5})
        buttoncallback = lambda *args: self.ans_correct_callback(url, *args)
        self.ans_1.bind(on_press=buttoncallback)
        self.bottom_layout.add_widget(self.ans_1)
        self.ans_2 = Button(text=self.ans_button[1],
                            background_color=(0.1, 0.5, 0.3, 1),
                            size_hint=(0.2, 0.2),
                            pos_hint={'x': 0.5, 'y': 0.5})
        self.ans_2.bind(on_press=buttoncallback)
        self.bottom_layout.add_widget(self.ans_2)
        self.add_widget(self.bottom_layout)


class MykivyApp(App):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()


if __name__ == '__main__':
    MykivyApp().run()