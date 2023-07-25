# coding:utf-8
"""
QGraphicsScene的子类
"""
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QBrush, QColor


class VisualTestScene(QGraphicsScene):

    def __int__(self, parent=None):
        super().__init__(parent)

        self.setBackgroundBrush(QBrush(QColor(0, 0, 0, 255)))
