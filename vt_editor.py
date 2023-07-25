# coding:utf-8
"""
编辑器主体
"""
import sys

from PySide6.QtWidgets import QWidget, QBoxLayout
from vt_view import VisualTestView
from vt_scene import VisualTestScene


class VisualTestEditor(QWidget):
    def __int__(self, parent=None):
        super().__init__(parent)
        self.setup_editor()

    def setup_editor(self):
        # 窗口位置及大小
        self.setGeometry(400, 400, 1000, 720)
        self.setWindowTitle('Visual Test')
        self.layout = QBoxLayout(QBoxLayout.Direction.LeftToRight, self)
        self.layout.setContentsMargins(10, 10, 10, 10)

        # 初始化scene
        self.scene = VisualTestScene()
        self.view = VisualTestView(self.scene, self)
        self.layout.addWidget(self.view)

        # 显示窗口
        self.show()
