# import kivy dependencies
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# import kivy UX components
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

# import other kivy stuf
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger

# import other dependencies
import os
import tensorflow as tf
# from layers import L1Dist
import torch  # upload YOLO model and make detections
from matplotlib import pyplot as plt  # for visualising images
import numpy as np  # for array transformation
import cv2  # helps access the webcam and render feeds


class LegoApp(App):
	def build(self):
		# Main layout components
		self.img1 = Image(size_hint=(1, .8))  # 80proc height of layer img size
		self.button = Button(text="Verify", size_hint=(1, .1))  # button 10proc size
		self.verification = Label(text="Verification Uninitiated", size_hint=(1, .1))  # verified or not 10proc size

		# Add items to layout
		layout = BoxLayout(orientation='vertical')
		layout.add_widget(self.img1)
		layout.add_widget(self.button)
		layout.add_widget(self.verification)

		return layout


if __name__ == '__main__':
	LegoApp().run()
