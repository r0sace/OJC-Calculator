
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox
from PyQt5.QtGui import QFont, QFontDatabase, QIntValidator, QPixmap
import sys


class OjcCalculator(QMainWindow):
    def __init__(self):
        super(OjcCalculator, self).__init__()
        self.setStyleSheet("QMainWindow {background-color: #441501}")
        self.setAutoFillBackground(True)
        self.setGeometry(1500, 500, 725, 700)
        self.setFixedHeight(700)
        self.setFixedWidth(723)
        self.setWindowTitle("Onion, Jalapeno, Cilantro Calculator")

        self.total_mild_onions = 0
        self.total_corn_onions = 0
        self.total_guac_onions = 0

        self.total_white_cilantro = 0
        self.total_brown_cilantro = 0
        self.total_mild_cilantro = 0
        self.total_corn_cilantro = 0
        self.total_guac_cilantro = 0

        self.total_mild_jalapenos = 0
        self.total_corn_jalapenos = 0
        self.total_guac_jalapenos = 0

        QFontDatabase.addApplicationFont("Gotham Bold.otf")
        QFontDatabase.addApplicationFont("Gotham Medium.otf")
        QFontDatabase.addApplicationFont("Gotham Book.otf")

        self._set_images()
        self._set_header_labels()
        self._set_ingredient_labels()
        self._set_cc_label()
        self._set_spin_boxes()
        self._onion_result_labels()
        self._jalapeno_result_labels()
        self._cilantro_result_labels()
        self._total_labels()
        self.show()

    def _get_font(self, font_name):
        db = QFontDatabase()
        if font_name == "bold":
            return db.font("Gotham", "Bold", 42)
        elif font_name == "book":
            return db.font("Gotham", "Book", 18)
        else:
            return db.font("Gotham", "Medium", 17)

    def _set_images(self):
        # insert
        logo = QPixmap('chippie.svg')
        logo_label = QtWidgets.QLabel(self)
        logo_label.setPixmap(logo)
        logo_label.adjustSize()
        logo_label.move(15, 15)

        box_pattern = QPixmap('pepper-background.png')
        img_y_axis = 193

        for i in range(5):
            box_label = QtWidgets.QLabel(self)
            box_label.setPixmap(box_pattern)
            box_label.setGeometry(206, img_y_axis, 60, 18)
            img_y_axis += 50

        total_font = self._get_font("bold")
        medium = self._get_font("medium")


        total_pattern = QPixmap('total-pattern.png')
        self.total_label = QtWidgets.QLabel(self)
        self.total_label.setPixmap(total_pattern)
        self.total_label.setGeometry(80, 515, 560, 115)
        self.total_label.setStyleSheet("border: 1px solid #AB2218;")

        total_text = QtWidgets.QLabel(self)
        total_text.setFont(medium)
        total_text.setText(("T O T A L   I N G R E D I E N T S"))
        total_text.setStyleSheet("color: white;"
                                 "background-color: transparent;"
                                 "font-size: 24pt")
        total_text.move(170, 470)
        total_text.adjustSize()

    def _set_header_labels(self):
        # set and style title label
        title_font = self._get_font("bold")

        title_label = QtWidgets.QLabel(self)
        title_label.setText("O J C   C A L C U L A T O R")
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: white")
        title_label.adjustSize()
        title_label.move(75, 57)

        body_font = self._get_font("book")

        top_headers = ["Ingredient", "Needs", "Onions", "Jalapenos", "Cilantro"]
        x_axis = 80

        for header in top_headers:
            if header == "Ingredient" or header == "Needs":
                top_header = QtWidgets.QLabel(self)
                top_header.setText(u"\u2009" + header + u"\u2009")
                top_header.setFont(body_font)
                top_header.setStyleSheet("color: white;"
                                         "background-color: #AB2218;")
                top_header.move(x_axis, 150)
                top_header.setContentsMargins(0,4,0,2)
                top_header.adjustSize()
                x_axis += 125
            elif header == "Onions":
                top_header = QtWidgets.QLabel(self)
                top_header.setText(u"\u2009" + header + u"\u2009")
                top_header.setFont(body_font)
                top_header.setStyleSheet("color: white;"
                                         "background-color: #AB2218;")
                top_header.move(350, 150)
                top_header.setContentsMargins(0, 4, 0, 2)
                top_header.adjustSize()
                x_axis = 446
            else:
                top_header = QtWidgets.QLabel(self)
                top_header.setText(u"\u2009" + header + u"\u2009")
                top_header.adjustSize()
                top_header.setFont(body_font)
                top_header.setStyleSheet("color: white;"
                                         "background-color: #AB2218;")
                top_header.move(x_axis, 150)
                top_header.setContentsMargins(0, 4, 0, 2)
                top_header.adjustSize()
                x_axis += 123

    def _set_ingredient_labels(self):
        ingredients = ["Brown Rice", "White Rice", "Mild Salsa", "Corn Salsa", "Guacamole"]
        item_font = self._get_font("medium")
        y_axis = 195

        for items in ingredients:
            label = QtWidgets.QLabel(self)
            label.setText(items)
            label.setFixedSize(100, 20)
            label.setAlignment(QtCore.Qt.AlignRight)
            label.setFont(item_font)
            label.setStyleSheet("color: white;")
            label.move(78, y_axis)
            y_axis += 50

    def _set_cc_label(self):
        cc_font = self._get_font("medium")

        copyright = QtWidgets.QLabel(self)
        copyright.setText("© 2022 Cristina Rosace")
        copyright.setFont(cc_font)
        copyright.move(298, 680)
        copyright.adjustSize()
        copyright.setStyleSheet("font-size: 10pt;"
                                "color:grey")

    def _onion_result_labels(self):
        medium = self._get_font("medium")

        self.brown_onion = QtWidgets.QLabel(self)
        self.brown_onion.setText("0.0 " + "lbs")
        self.brown_onion.setFont(medium)
        self.brown_onion.setFixedSize(68, 20)
        self.brown_onion.setAlignment(QtCore.Qt.AlignRight)
        self.brown_onion.move(344, 192)
        self.brown_onion.setStyleSheet("color: white;"
                                       "font-size: 16pt;")

        self.white_onion = QtWidgets.QLabel(self)
        self.white_onion.setText("0.0 " + "lbs")
        self.white_onion.setFont(medium)
        self.white_onion.setFixedSize(68, 20)
        self.white_onion.setAlignment(QtCore.Qt.AlignRight)
        self.white_onion.move(344, 243)
        self.white_onion.setStyleSheet("color: white;"
                                       "font-size: 16pt;")

        self.mild_onion = QtWidgets.QLabel(self)
        self.mild_onion.setText("0.0 " + "lbs")
        self.mild_onion.setFont(medium)
        self.mild_onion.setFixedSize(68, 20)
        self.mild_onion.setAlignment(QtCore.Qt.AlignRight)
        self.mild_onion.move(344, 294)
        self.mild_onion.setStyleSheet("color: white;"
                                      "font-size: 16pt;")

        self.corn_onion = QtWidgets.QLabel(self)
        self.corn_onion.setText("0.0 " + "lbs")
        self.corn_onion.setFont(medium)
        self.corn_onion.setFixedSize(68, 20)
        self.corn_onion.setAlignment(QtCore.Qt.AlignRight)
        self.corn_onion.move(344, 345)
        self.corn_onion.setStyleSheet("color: white;"
                                      "font-size: 16pt;")

        self.guac_onion = QtWidgets.QLabel(self)
        self.guac_onion.setText("0.0 " + "lbs")
        self.guac_onion.setFont(medium)
        self.guac_onion.setFixedSize(68, 20)
        self.guac_onion.setAlignment(QtCore.Qt.AlignRight)
        self.guac_onion.move(344, 396)
        self.guac_onion.setStyleSheet("color: white;"
                                      "font-size: 16pt;")

    def _jalapeno_result_labels(self):
        medium = self._get_font("medium")

        self.brown_jal = QtWidgets.QLabel(self)
        self.brown_jal.setText("0 " + "lbs")
        self.brown_jal.setFont(medium)
        self.brown_jal.setFixedSize(60, 20)
        self.brown_jal.setAlignment(QtCore.Qt.AlignRight)
        self.brown_jal.move(460, 192)
        self.brown_jal.setStyleSheet("color: white;"
                                     "font-size: 16pt;")

        self.white_jal = QtWidgets.QLabel(self)
        self.white_jal.setText("0 " + "lbs")
        self.white_jal.setFont(medium)
        self.white_jal.setFixedSize(60, 20)
        self.white_jal.setAlignment(QtCore.Qt.AlignRight)
        self.white_jal.move(460, 243)
        self.white_jal.setStyleSheet("color: white;"
                                     "font-size: 16pt;")

        self.mild_jal = QtWidgets.QLabel(self)
        self.mild_jal.setText("0 " + "lbs")
        self.mild_jal.setFont(medium)
        self.mild_jal.setFixedSize(60, 20)
        self.mild_jal.setAlignment(QtCore.Qt.AlignRight)
        self.mild_jal.move(460, 294)
        self.mild_jal.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

        self.corn_jal = QtWidgets.QLabel(self)
        self.corn_jal.setText("0 " + "lbs")
        self.corn_jal.setFont(medium)
        self.corn_jal.setFixedSize(60, 20)
        self.corn_jal.setAlignment(QtCore.Qt.AlignRight)
        self.corn_jal.move(460, 345)
        self.corn_jal.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

        self.guac_jal = QtWidgets.QLabel(self)
        self.guac_jal.setText("0 " + "lbs")
        self.guac_jal.setFont(medium)
        self.guac_jal.setFixedSize(60, 20)
        self.guac_jal.setAlignment(QtCore.Qt.AlignRight)
        self.guac_jal.move(460, 396)
        self.guac_jal.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

    def _cilantro_result_labels(self):
        medium = self._get_font("medium")

        self.brown_cil = QtWidgets.QLabel(self)
        self.brown_cil.setText("0 " + "bags")
        self.brown_cil.setFont(medium)
        self.brown_cil.setFixedSize(70, 20)
        self.brown_cil.setAlignment(QtCore.Qt.AlignRight)
        self.brown_cil.move(570, 192)
        self.brown_cil.setStyleSheet("color: white;"
                                     "font-size: 16pt;")

        self.white_cil = QtWidgets.QLabel(self)
        self.white_cil.setText("0 " + "bags")
        self.white_cil.setFont(medium)
        self.white_cil.setFixedSize(70, 20)
        self.white_cil.setAlignment(QtCore.Qt.AlignRight)
        self.white_cil.move(570, 243)
        self.white_cil.setStyleSheet("color: white;"
                                     "font-size: 16pt;")

        self.mild_cil = QtWidgets.QLabel(self)
        self.mild_cil.setText("0 " + "bags")
        self.mild_cil.setFont(medium)
        self.mild_cil.setFixedSize(70, 20)
        self.mild_cil.setAlignment(QtCore.Qt.AlignRight)
        self.mild_cil.move(570, 294)
        self.mild_cil.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

        self.corn_cil = QtWidgets.QLabel(self)
        self.corn_cil.setText("0 " + "bags")
        self.corn_cil.setFont(medium)
        self.corn_cil.setFixedSize(70, 20)
        self.corn_cil.setAlignment(QtCore.Qt.AlignRight)
        self.corn_cil.move(570, 345)
        self.corn_cil.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

        self.guac_cil = QtWidgets.QLabel(self)
        self.guac_cil.setText("0 " + "bags")
        self.guac_cil.setFont(medium)
        self.guac_cil.setFixedSize(70, 20)
        self.guac_cil.setAlignment(QtCore.Qt.AlignRight)
        self.guac_cil.move(570, 396)
        self.guac_cil.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

    def _set_spin_boxes(self):
        stylesheet = ("background: transparent;"
                      "selection-background-color: transparent;"
                      "selection-color: black;"
                      "color: black")

        self.brown_rice = QSpinBox(self)
        self.brown_rice.setStyleSheet(stylesheet)
        self.brown_rice.setAlignment(QtCore.Qt.AlignRight)
        self.brown_rice.setGeometry(206, 193, 60, 18)
        self.brown_rice.setMaximum(50)
        self.brown_rice.valueChanged.connect(lambda: self._calculate_cilantro("brown"))

        self.white_rice = QSpinBox(self)
        self.white_rice.setStyleSheet(stylesheet)
        self.white_rice.setAlignment(QtCore.Qt.AlignRight)
        self.white_rice.setGeometry(206, 243, 60, 18)
        self.white_rice.setMaximum(50)
        self.white_rice.valueChanged.connect(lambda: self._calculate_cilantro("white"))

        self.mild = QSpinBox(self)
        self.mild.setStyleSheet(stylesheet)
        self.mild.setAlignment(QtCore.Qt.AlignRight)
        self.mild.setGeometry(206, 293, 60, 18)
        self.mild.setMaximum(50)
        self.mild.valueChanged.connect(lambda: self._calculate_onions("mild"))
        self.mild.valueChanged.connect(lambda: self._calculate_cilantro("mild"))
        self.mild.valueChanged.connect(lambda: self._calculate_jalapenos("mild"))

        self.corn = QSpinBox(self)
        self.corn.setStyleSheet(stylesheet)
        self.corn.setAlignment(QtCore.Qt.AlignRight)
        self.corn.setGeometry(206, 343, 60, 18)
        self.corn.setMaximum(50)
        self.corn.valueChanged.connect(lambda: self._calculate_onions("corn"))
        self.corn.valueChanged.connect(lambda: self._calculate_jalapenos("corn"))
        self.corn.valueChanged.connect(lambda: self._calculate_cilantro("corn"))

        self.guac = QSpinBox(self)
        self.guac.setStyleSheet(stylesheet)
        self.guac.setAlignment(QtCore.Qt.AlignRight)
        self.guac.setGeometry(206, 393, 60, 18)
        self.guac.setMaximum(50)
        self.guac.valueChanged.connect(lambda: self._calculate_onions("guac"))
        self.guac.valueChanged.connect(lambda: self._calculate_jalapenos("guac"))
        self.guac.valueChanged.connect(lambda: self._calculate_cilantro("guac"))

    def _calculate_onions(self, ingredient):
        if ingredient == "mild":
            value = self.mild.value()
            cups = 2 * value
            ounces = cups * 4
            pounds = round((ounces / 16), 1)
            self.mild_onion.setText(str(pounds) + " lbs")
            self.total_mild_onions = pounds

        elif ingredient == "corn":
            cups = self.corn.value()
            ounces = cups * 4
            pounds = round((ounces / 16), 1)
            self.corn_onion.setText(str(pounds) + " lbs")
            self.total_corn_onions = pounds

        elif ingredient == "guac":
            value = self.guac.value()
            cups = 2.50 * value
            ounces = cups * 4
            pounds = round((ounces / 16), 1)
            self.guac_onion.setText(str(pounds) + " lbs")
            self.total_guac_onions = pounds

        self._calculate_total_onions()

    def _calculate_jalapenos(self, ingredient):
        if ingredient == "mild":
            value = self.mild.value()
            cups = .33 * value
            ounces = cups * 4
            pounds = round((ounces / 16), 1)
            self.mild_jal.setText(str(pounds) + " lbs")
            self.total_mild_jalapenos = pounds

        elif ingredient == "corn":
            value = self.corn.value()
            cups = .75 * value
            ounces = cups * 4
            pounds = round((ounces / 16), 1)
            self.corn_jal.setText(str(pounds) + " lbs")
            self.total_corn_jalapenos = pounds

        elif ingredient == "guac":
            cups = self.guac.value()
            ounces = cups * 4
            pounds = round((ounces / 16), 1)
            self.guac_jal.setText(str(pounds) + " lbs")
            self.total_guac_jalapenos = pounds

        self._calculate_total_jalapenos()

    def _calculate_cilantro(self, ingredient):
        if ingredient == 'brown':
            value = self.brown_rice.value()
            cups = value * 2
            total = round((cups / 12), 1)
            self.brown_cil.setText(str(total) + " bags")
            self.total_brown_cilantro = total

        elif ingredient == "white":
            value = self.white_rice.value()
            cups = value * 2
            total = round((cups / 12), 1)
            self.white_cil.setText(str(total) + " bags")
            self.total_white_cilantro = total

        elif ingredient == "mild":
            value = self.mild.value()
            cups = value * 2
            total = round((cups / 12), 1)
            self.mild_cil.setText(str(total) + " bags")
            self.total_mild_cilantro = total

        elif ingredient == "corn":
            value = self.corn.value()
            cups = value * 2
            total = round((cups / 12), 1)
            self.corn_cil.setText(str(total) + " bags")
            self.total_corn_cilantro = total

        elif ingredient == "guac":
            value = self.guac.value()
            cups = value * 2.5
            total = round((cups / 12), 1)
            self.guac_cil.setText(str(total) + " bags")
            self.total_guac_cilantro = total

        self._calculate_total_cilantro()

    def _total_labels(self):
        bold = self._get_font("bold")
        book = self._get_font("book")

        self.onion_total_header = QtWidgets.QLabel(self)
        self.onion_total_header.setFont(bold)
        self.onion_total_header.setStyleSheet("color: #AB2218;"
                                              "font-size:18pt;")
        self.onion_total_header.setAlignment(QtCore.Qt.AlignRight)
        self.onion_total_header.setText("O N I O N S")
        self.onion_total_header.adjustSize()
        self.onion_total_header.move(103, 525)

        self.jalapenos_total_header = QtWidgets.QLabel(self)
        self.jalapenos_total_header.setFont(bold)
        self.jalapenos_total_header.setStyleSheet("color: #AB2218;"
                                                  "font-size: 18pt;")
        self.jalapenos_total_header.setAlignment(QtCore.Qt.AlignRight)
        self.jalapenos_total_header.setText("J A L A P E N O S")
        self.jalapenos_total_header.adjustSize()
        self.jalapenos_total_header.move(263, 525)

        self.cilantro_total_header = QtWidgets.QLabel(self)
        self.cilantro_total_header.setFont(bold)
        self.cilantro_total_header.setStyleSheet("color: #AB2218;"
                                                 "font-size: 18pt;")
        self.cilantro_total_header.setAlignment(QtCore.Qt.AlignRight)
        self.cilantro_total_header.setText("C I L A N T R O")
        self.cilantro_total_header.adjustSize()
        self.cilantro_total_header.move(480, 525)

        self.onion_total = QtWidgets.QLabel(self)
        self.onion_total.setFont(bold)
        self.onion_total.setStyleSheet("color: black;"
                                       "font-size:50pt;")
        self.onion_total.setAlignment(QtCore.Qt.AlignCenter)
        self.onion_total.setText("0.0")
        self.onion_total.setFixedSize(115, 50)
        self.onion_total.move(100, 553)

        self.jalapenos_total = QtWidgets.QLabel(self)
        self.jalapenos_total.setFont(bold)
        self.jalapenos_total.setStyleSheet("color: black;"
                                           "font-size:50pt;")
        self.jalapenos_total.setAlignment(QtCore.Qt.AlignCenter)
        self.jalapenos_total.setFixedSize(115, 50)
        self.jalapenos_total.setText("0.0")
        self.jalapenos_total.move(285, 553)

        self.cilantro_total = QtWidgets.QLabel(self)
        self.cilantro_total.setFont(bold)
        self.cilantro_total.setStyleSheet("color: black;"
                                          "font-size:50pt;")
        self.cilantro_total.setAlignment(QtCore.Qt.AlignCenter)
        self.cilantro_total.setFixedSize(115, 50)
        self.cilantro_total.setText("0.0")
        self.cilantro_total.adjustSize()
        self.cilantro_total.move(490, 553)

        self.onion_lbs = QtWidgets.QLabel(self)
        self.onion_lbs.setFont(book)
        self.onion_lbs.setStyleSheet("color: black;"
                                     "font-size: 14pt;")
        self.onion_lbs.setText("p  o  u  n  d  s")
        self.onion_lbs.adjustSize()
        self.onion_lbs.move(110, 603)

        self.jalapeno_lbs = QtWidgets.QLabel(self)
        self.jalapeno_lbs.setFont(book)
        self.jalapeno_lbs.setStyleSheet("color: black;"
                                        "font-size: 14pt;")
        self.jalapeno_lbs.setText("p    o    u    n    d    s")
        self.jalapeno_lbs.adjustSize()
        self.jalapeno_lbs.move(280, 603)

        self.cilantro_lbs = QtWidgets.QLabel(self)
        self.cilantro_lbs.setFont(book)
        self.cilantro_lbs.setStyleSheet("color: black;"
                                        "font-size: 14pt;")
        self.cilantro_lbs.setText("b       a       g       s")
        self.cilantro_lbs.adjustSize()
        self.cilantro_lbs.move(487, 603)

    def _calculate_total_onions(self):
        total = round(self.total_mild_onions + self.total_corn_onions + self.total_guac_onions, 1)
        total = str(total)
        self.onion_total.setText(total)
        self.onion_total.adjustSize()

    def _calculate_total_jalapenos(self):
        total = round(self.total_mild_jalapenos + self.total_corn_jalapenos + self.total_guac_jalapenos, 1)
        self.jalapenos_total.setText(str(total))
        self.jalapenos_total.adjustSize()

    def _calculate_total_cilantro(self):
        total = round(self.total_brown_cilantro + self.total_white_cilantro + self.total_mild_cilantro +
                      self.total_corn_cilantro + self.total_guac_cilantro, 1)
        self.cilantro_total.setText(str(total))
        self.cilantro_total.adjustSize()

        "hi hi ii'm trying to commit this project"
def window():
    app = QApplication(sys.argv)
    win = OjcCalculator()
    win.show()
    ret = app.exec_()
    sys.exit(ret)


window()
