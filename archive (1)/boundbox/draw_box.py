import os
import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

img = None
tl_list = []
br_list = []
object_list = []

image_folder = 'images'
savedir = 'annotations'
obj = ''