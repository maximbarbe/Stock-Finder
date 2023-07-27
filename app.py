from PySide6.QtCore import (QRect, Qt, QVariantAnimation, QAbstractAnimation)
from PySide6.QtGui import QPixmap, QFont, QCursor
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QWidget)
import sys
import os
import functools

# Node for the carousel
class ListNode:
    def __init__(self, url, next = None):
        self.url = url
        self.next = next


# Carousel for the images based on a linked list.
class Carousel:

    def __init__(self, images):
        self.head = None
        self.images = images
        self.generate_carousel(self.images)

    def generate_carousel(self, images):
        for image in images:
            if self.head == None:
                self.head = ListNode(url = image)
                temp = self.head
            else:
                temp.next = ListNode(url = image)
                temp = temp.next

    

# PyQT6 main window settings.
class MainWindow(QMainWindow):
    def __init__(self, tickers: list):
        super().__init__()
        self.tickers = Carousel(tickers)
        self.current_node = self.tickers.head
        if not self.objectName():
            self.setObjectName("MainWindow")
        self.setWindowTitle("Stock tinder")
        self.setFixedSize(1080, 1080)
        self.setStyleSheet("background-color: '#212121'")
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(1080, 1080)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("""
            QWidget {
                background-color: #212121;
            }
            QPushButton {
                font-family: Montserrat, sans-serif;
                color: white;
                font-size: 20;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton#upvote {
                background-color: #28a745;
            }  
            QPushButton#downvote {
                background-color: #dc3545;
            }      

        """)
        self.stock_image = QLabel(self.centralwidget)
        self.stock_image.setObjectName("stock_image")
        self.stock_image.setGeometry(QRect(308, 170, 461, 231))
        self.stock_image.setPixmap(QPixmap(f"./stock/{self.tickers.head.url}.jpg"))

        self.upvote = QPushButton(self.centralwidget)
        self.upvote.setObjectName("upvote")
        self.upvote.setGeometry(QRect(70, 580, 291, 141))
        font = QFont()
        font.setFamilies(["Montserrat"])
        font.setPointSize(20)
        font.setBold(True)
        self.upvote.setFont(font)
        self.upvote.setText("Upvote")
        
        self.downvote = QPushButton(self.centralwidget)
        self.downvote.setObjectName("downvote")
        self.downvote.setFont(font)
        self.downvote.setGeometry(QRect(720, 580, 291, 141))
        self.downvote.setText("Downvote")

        self.setCentralWidget(self.centralwidget)
        self.upvote.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.downvote.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.upvote.clicked.connect(self.update_pixmap)
        self.downvote.clicked.connect(self.downvote_clicked)

    # Deletes the picture when downvote button clicked and changes picture.
    def downvote_clicked(self):
        try:
            os.remove(f"./stock/{self.current_node.url}.jpg")
        except FileNotFoundError:
            return
        self.update_pixmap()

    # Changes the picture when a button is clicked
    def update_pixmap(self):
        if not self.current_node.next:
            return
        else:
            self.stock_image.setPixmap(QPixmap(f"./stock/{self.current_node.next.url}.jpg"))
            self.current_node = self.current_node.next
class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

