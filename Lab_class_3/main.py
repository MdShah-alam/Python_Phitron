""" My Camera application

author : Shah_alam   
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QImage,QIcon
import cv2

class Window(QWidget):
    """Main app window """
    def __init__(self) -> None:
        super().__init__()
        
        #variables for app window
        self.window_width=800
        self.window_height=600
        
        #varisble for image 
        self.img_width=800
        self.img_height=600
        
        # setup the window
        self.setWindowTitle('My Camera App')
        self.setGeometry(0 , 0 , self.window_width , self.window_height)
        self.setFixedSize(self.window_width , self.window_height)
        
        
    def ui(self):
        """contains all ui things"""
        # image label
        self.image_label=QLabel(self)
        self.image_label.setGeometry(0 , 0 , self.img_width , self.img_height)
        
        self.show()
    
    def save_img(self):
        """save image from camera"""
        pass
    
    def record(self):
        """video record """
        pass
    
#run
app=QApplication(sys.argv)
win=Window()
# sys.exit(app.exec_())

