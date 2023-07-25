# coding:utf-8
"""
QGraphicsView的子类，是Scene的container
"""
from PySide6.QtWidgets import QGraphicsView


class VisualTestView(QGraphicsView):

    def __int__(self, scene, parent=None):
        super().__init__(parent)

        self._scene = scene
        self.setScene(self._scene)
