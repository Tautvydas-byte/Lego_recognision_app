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
		self.web_cam = Image(size_hint=(1, .8))  # 80proc height of layer img size
		self.button = Button(text="Verify", size_hint=(1, .1))  # button 10proc size
		self.verification = Label(text="Verification Uninitiated", size_hint=(1, .1))  # verified or not 10proc size

		# Add items to layout
		layout = BoxLayout(orientation='vertical')
		layout.add_widget(self.web_cam)
		layout.add_widget(self.button)
		layout.add_widget(self.verification)

		# Setup video capture device
		self.capture = cv2.VideoCapture(0)  # reikia pasizaist kuris skaicius jog pasiektu tinkama webcam
		Clock.schedule_interval(self.update, 1.0/33.0)#Update function running to interval of time

		return layout

	# Run continuously to get webcam feed
	def update(self, *args):
		# Read frame from opencv
		ret, frame = self.capture.read()  # reading a frame
		frame = frame[120:120 + 320, 200: 200 + 320,:]  # cutting down to 120 width and 250 height

		# Flip horizontal and convert raw OpenCV2 image array to texture for rendering. Then setting our image equal to that texture
		buf = cv2.flip(frame, 0).tostring()#flip image to horizontal and convert to string
		img_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')#allow convert image to texture kivy documentation
		img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')#taking image converting to texture and render to app
		self.web_cam.texture = img_texture#setting web_cam image texture to image texture


if __name__ == '__main__':
	LegoApp().run()
