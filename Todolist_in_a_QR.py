import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import qrcode
import tkinter
from tkinter import filedialog
import os
from PIL import Image
import time




class mygridlayout(GridLayout):
    def __init__(self, **kwargs):
        super(mygridlayout, self).__init__(**kwargs)
        # columns
        self.cols = 1
        # Box Size widget
        self.add_widget(Label(text="what box size you want:"))
        # Box Size input
        self.Box_Size = TextInput(multiline=False)
        self.add_widget(self.Box_Size)
        # Border_Size widget
        self.add_widget(Label(text="what border size do you want:"))
        # Border_Size input
        self.Border_Size = TextInput(multiline=False)
        self.add_widget(self.Border_Size)
        # qrcode content widget
        self.add_widget(Label(text="what u will do today inshallah and include in this qrcode:"))
        # qrcode content input
        self.QRcode_Content = TextInput(multiline=True)
        self.add_widget(self.QRcode_Content)
        # qrcode foreground widget
        self.add_widget(Label(text="what qrcode foreground color do u want(if no special preference type black):"))
        # qrcode foreground input
        self.foreground = TextInput(multiline=False)
        self.add_widget(self.foreground)
        # qrcode background widget
        self.add_widget(Label(text="what qrcode background color do u want(if no special preference type white):"))
        # qrcode background input
        self.background = TextInput(multiline=False)
        self.add_widget(self.background)
        # create widget
        self.createQR = Button(text="create your todolist and include it in the qrcode", font_size=32)
        self.createQR.bind(on_press=self.press1)
        self.add_widget(self.createQR)

    def press1(self, instance):
        Box_Size = self.Box_Size.text
        Border_Size = self.Border_Size.text
        QRcode_Content = self.QRcode_Content.text
        foreground = self.foreground.text
        background = self.background.text
        tkinter.Tk().withdraw()
        # print(sqrt((float(term_point1) - float(init_point1)) ** 2 + (float(term_point2) - float(init_point2)) ** 2))
        currdir = os.getcwd()
        my_formats = [('Text File Document', '*.txt')]
        tempdir = filedialog.asksaveasfilename(parent=None, title="save As", filetypes=my_formats)
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=Box_Size,
                           border= Border_Size
                           )
        }')

        img_additional_data = qr.make_image(
            fill_color=foreground,
            back_color=background
        )

        img_additional_data.save(tempdir + ".png")

        image_path = tempdir + ".png"
        img_popup = Image.open(image_path)
        img_popup.show()

        self.add_widget(Label(text="You chose %s" % tempdir + ".png"))
        self.Box_Size.text = ""
        self.Border_Size.text = ""
        self.QRcode_Content.text = ""
        self.background.text = ""
        self.foreground.text = ""















class TodolistCreator(App):
    def build(self):
        return mygridlayout()


if __name__ == '__main__':
    TodolistCreator().run()











