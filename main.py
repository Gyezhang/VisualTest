# coding:utf-8
"""
Visual Test的入口
"""
import sys
from PySide6.QtWidgets import QApplication
from vt_editor import VisualTestEditor

if __name__ == '__main__':
    app = QApplication([])
    window = VisualTestEditor()
    window.setup_editor()
    sys.exit(app.exec())


