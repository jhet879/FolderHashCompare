from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QDesktopWidget
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import qdarktheme
import compare
import sys

class MainWindow(QWidget):

    PATH1_INVALID = 'Path 1: INVALID PATH'
    PATH2_INVALID = 'Path 2: INVALID PATH'
    FONT = QFont('Courier New')

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        browse_btn1 = QPushButton('Folder 1', self)
        browse_btn1.clicked.connect(lambda: self.showFolderDialog(1))
        browse_btn1.setFont(self.FONT)
        vbox.addWidget(browse_btn1)
        self.path1_lbl = QLabel(self.PATH1_INVALID, self)
        self.directory1 = ""
        self.path1_lbl.setFont(self.FONT)
        self.path1_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.path1_lbl)

        browse_btn2 = QPushButton('Folder 1', self)
        browse_btn2.clicked.connect(lambda: self.showFolderDialog(2))
        browse_btn2.setFont(self.FONT)
        vbox.addWidget(browse_btn2)
        self.path2_lbl = QLabel(self.PATH2_INVALID, self)
        self.directory2 = ""
        self.path2_lbl.setFont(self.FONT)
        self.path2_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.path2_lbl)

        self.check_btn = QPushButton('CHECK', self)
        self.check_btn.setEnabled(False)
        self.check_btn.clicked.connect(lambda: self.handle_compare())
        self.check_btn.setFont(self.FONT)
        vbox.addWidget(self.check_btn)

        self.HASH1_lbl = QLabel('HASH 1:', self)
        self.HASH1_lbl.setFont(self.FONT)
        self.HASH1_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.HASH1_lbl)
        self.HASH2_lbl = QLabel('HASH 2:', self)
        self.HASH2_lbl.setFont(self.FONT)
        self.HASH2_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.HASH2_lbl)
        self.status_lbl = QLabel('STATUS: ', self)
        self.status_lbl.setFont(self.FONT)
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.status_lbl)

        self.setLayout(vbox)
        self.setWindowTitle('FHC')
        self.setWindowIcon(QIcon('icon.png'))

        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - 700) // 2
        y = (screen.height() - 300) // 2
        self.setGeometry(x, y, 700, 300)
        self.show()

    def showFolderDialog(self, btn_number):
        options = QFileDialog.Options()
        options |= QFileDialog.Option.ShowDirsOnly
        # add directory= parameter so that we can return to the previous DIR when opening a folder again
        directory = QFileDialog.getExistingDirectory(self, "Select Directory", options=options)
        if btn_number == 1:
            if directory:
                self.path1_lbl.setText('Path 1: ' + directory)
                self.directory1 = directory
            else:
                self.path1_lbl.setText(self.PATH1_INVALID)
        elif btn_number == 2:
            if directory:
                self.path2_lbl.setText('Path 2: ' + directory)
                self.directory2 = directory
            else:
                self.path2_lbl.setText(self.PATH2_INVALID)
        self.updateLabel()

    def updateLabel(self):
        if ((self.path1_lbl.text() != self.PATH1_INVALID) and (self.path2_lbl.text() != self.PATH2_INVALID)):
            self.check_btn.setEnabled(True)
        else:
            self.check_btn.setEnabled(False)

    def handle_compare(self):
        hash1, hash2, result = compare.compare_folders(self.directory1, self.directory2)
        # MOVE THJIS TO THE COMPARE.PY FILE
        hash1 = hash1[39:((hash1.find(' ', 39)) - 1)]
        hash2 = hash2[39:((hash2.find(' ', 39)) - 1)]
        self.HASH1_lbl.setText('HASH 1: ' + str(hash1))
        self.HASH2_lbl.setText('HASH 2: ' + str(hash2))
        self.status_lbl.setText('STATUS: ' + str(result))
        self.check_btn.setEnabled(False)
        self.raise_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    ex = MainWindow()
    sys.exit(app.exec_())
