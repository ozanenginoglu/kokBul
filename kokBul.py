import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import numpy as np
import pyqtgraph as pg


class FindRoots(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        loadUi('window.ui', self)
        pg.setConfigOptions(antialias=True)
        self.graphicsView.showGrid(x=True, y=True, alpha=0.3)
        self.pushButton.clicked.connect(self.solve)
        self.show()

    def solve(self):
        if self.var_a.text() == '':
            self.var_a.setText('0')
        if self.var_b.text() == '':
            self.var_b.setText('0')
        if self.var_c.text() == '':
            self.var_c.setText('0')

        try:
            a = float(self.var_a.text())
            b = float(self.var_b.text())
            c = float(self.var_c.text())

            roots = np.roots([a, b, c])
            self.root1_label.setText(str(roots[0]))
            self.root2_label.setText(str(roots[1]))

            x = np.linspace(-5, 5, 100)
            self.graphicsView.plot(x, a*x**2+b*x+c)

        except ZeroDivisionError:
            print('Division by zero!')
        except ValueError:
            self.var_a.setText('0')
            self.var_b.setText('0')
            self.var_c.setText('0')
            print('Syntax error!')
        except IndexError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = FindRoots()
    sys.exit(app.exec_())
