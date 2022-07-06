
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QDesktopWidget
from PyQt5.QtGui import QFontDatabase, QPixmap
import sys


class OjcUi(QMainWindow):
    """OJC Calculator's View (GUI)."""

    def __init__(self):
        super().__init__()
        """Initializes the GUI."""
        self.setWindowTitle("Onion, Jalapeno, Cilantro Calculator")
        self.setStyleSheet("QMainWindow {background-color: #441501}")
        self.setFixedSize(725, 700)

        QFontDatabase.addApplicationFont("Fonts/Gotham Bold.otf")
        QFontDatabase.addApplicationFont("Fonts/Gotham Medium.otf")
        QFontDatabase.addApplicationFont("Fonts/Gotham Book.otf")

        self._center_on_screen()
        self._set_images()
        self._create_header_labels()
        self._create_prep_item_labels()
        self._create_copyright_label()
        self._create_spin_boxes()
        self._create_onion_result_labels()
        self._create_cilantro_result_labels()
        self._create_jalapenos_result_labels()
        self._create_total_labels()

    def _center_on_screen(self):
        """Calculates the center of the user's screen and center positions the window."""
        resolution = QDesktopWidget().screenGeometry()
        self.move(round((resolution.width() / 2) - (self.frameSize().width() / 2)),
                  round((resolution.height() / 2) - (self.frameSize().height() / 2)))

    def _get_font(self, font):
        """Returns a requested font."""
        db = QFontDatabase()

        if font == "bold":
            return db.font("Gotham", "Bold", 42)
        elif font == "book":
            return db.font("Gotham", "Book", 18)
        else:
            return db.font("Gotham", "Medium", 17)

    def _set_images(self):
        """Displays the spinbox background image and total box background image."""
        box_pattern = QPixmap('spin-box-background.png')
        img_y_axis = 193

        # display each spinbox background
        for i in range(5):
            box_label = QtWidgets.QLabel(self)
            box_label.setPixmap(box_pattern)
            box_label.setGeometry(206, img_y_axis, 60, 18)
            img_y_axis += 50

        # display total box background
        total_pattern = QPixmap('pattern.svg')
        self.total_label = QtWidgets.QLabel(self)
        self.total_label.setPixmap(total_pattern)
        self.total_label.setGeometry(80, 515, 560, 115)
        self.total_label.setStyleSheet("border: 1px solid #AB2218;")


    def _create_header_labels(self):
        """Creates, styles, and places all header text including the title and total."""
        # get fonts needed for each header
        title_font = self._get_font("bold")
        body_font = self._get_font("book")
        medium = self._get_font("medium")

        # create, style, and place the title
        title_label = QtWidgets.QLabel(self)
        title_label.setText("O J C   C A L C U L A T O R")
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: white")
        title_label.adjustSize()
        title_label.move(75, 57)

        top_headers = ["Prep Item", "Needs", "Onions", "Jalapenos", "Cilantro"]
        x_axis = 84

        # create, style, and place the calculator headers
        for header in top_headers:
            if header == "Prep Item" or header == "Needs":
                top_header = QtWidgets.QLabel(self)
                top_header.setText(u"\u2009" + header + u"\u2009")
                top_header.setFont(body_font)
                top_header.setStyleSheet("color: white;"
                                         "background-color: #AB2218;")
                top_header.move(x_axis, 150)
                top_header.setContentsMargins(0, 4, 0, 2)
                top_header.adjustSize()
                x_axis += 121
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

        # create, style, and place total box header
        total_text = QtWidgets.QLabel(self)
        total_text.setFont(medium)
        total_text.setText(("T O T A L   I N G R E D I E N T S"))
        total_text.setStyleSheet("color: white;"
                                 "background-color: transparent;"
                                 "font-size: 24pt")
        total_text.move(170, 470)
        total_text.adjustSize()

    def _create_prep_item_labels(self):
        """Creates, styles, and places the prep item labels."""
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

    def _create_copyright_label(self):
        """Creates, styles, and places the copyright symbol and my name. """
        cc_font = self._get_font("medium")

        copyright = QtWidgets.QLabel(self)
        copyright.setText("© 2022 Cristina Rosace")
        copyright.setFont(cc_font)
        copyright.move(298, 680)
        copyright.adjustSize()
        copyright.setStyleSheet("font-size: 10pt;"
                                "color:grey")

    def _create_spin_boxes(self):
        """
        Creates, styles, and places the calculator spin boxes.
        Allows users to input prep item needs up to 50.
        """

        stylesheet = ("background: transparent;"
                      "selection-background-color: transparent;"
                      "selection-color: black;"
                      "color: black")

        # brown rice spin box
        self.brown_rice = QSpinBox(self)
        self.brown_rice.setStyleSheet(stylesheet)
        self.brown_rice.setAlignment(QtCore.Qt.AlignRight)
        self.brown_rice.setGeometry(206, 193, 60, 18)
        self.brown_rice.setMaximum(50)

        # white rice spin box
        self.white_rice = QSpinBox(self)
        self.white_rice.setStyleSheet(stylesheet)
        self.white_rice.setAlignment(QtCore.Qt.AlignRight)
        self.white_rice.setGeometry(206, 243, 60, 18)
        self.white_rice.setMaximum(50)

        # mild spin box
        self.mild = QSpinBox(self)
        self.mild.setStyleSheet(stylesheet)
        self.mild.setAlignment(QtCore.Qt.AlignRight)
        self.mild.setGeometry(206, 293, 60, 18)
        self.mild.setMaximum(50)

        # corn spin box
        self.corn = QSpinBox(self)
        self.corn.setStyleSheet(stylesheet)
        self.corn.setAlignment(QtCore.Qt.AlignRight)
        self.corn.setGeometry(206, 343, 60, 18)
        self.corn.setMaximum(50)

        # guac spin box
        self.guac = QSpinBox(self)
        self.guac.setStyleSheet(stylesheet)
        self.guac.setAlignment(QtCore.Qt.AlignRight)
        self.guac.setGeometry(206, 393, 60, 18)
        self.guac.setMaximum(50)

    def _create_onion_result_labels(self):
        """Creates, styles, and places onion result labels for needs of each prep item."""

        medium = self._get_font("medium")

        # brown rice onion results, don't change
        self.brown_onion = QtWidgets.QLabel(self)
        # initialize to 0 lbs
        self.brown_onion.setText("0.0 " + "lbs")
        self.brown_onion.setFont(medium)
        self.brown_onion.setFixedSize(68, 20)
        self.brown_onion.setAlignment(QtCore.Qt.AlignRight)
        self.brown_onion.move(344, 192)
        self.brown_onion.setStyleSheet("color: white;"
                                       "font-size: 16pt;")

        # white rice onion results, don't change
        self.white_onion = QtWidgets.QLabel(self)
        # initialize to 0 lbs
        self.white_onion.setText("0.0 " + "lbs")
        self.white_onion.setFont(medium)
        self.white_onion.setFixedSize(68, 20)
        self.white_onion.setAlignment(QtCore.Qt.AlignRight)
        self.white_onion.move(344, 243)
        self.white_onion.setStyleSheet("color: white;"
                                       "font-size: 16pt;")

        # mild salsa onion results
        self.mild_onion = QtWidgets.QLabel(self)
        # initialize to 0 lbs
        self.mild_onion.setText("0.0 " + "lbs")
        self.mild_onion.setFont(medium)
        self.mild_onion.setFixedSize(68, 20)
        self.mild_onion.setAlignment(QtCore.Qt.AlignRight)
        self.mild_onion.move(344, 294)
        self.mild_onion.setStyleSheet("color: white;"
                                      "font-size: 16pt;")
        # corn salsa onion results
        self.corn_onion = QtWidgets.QLabel(self)
        # initialize to 0 lbs
        self.corn_onion.setText("0.0 " + "lbs")
        self.corn_onion.setFont(medium)
        self.corn_onion.setFixedSize(68, 20)
        self.corn_onion.setAlignment(QtCore.Qt.AlignRight)
        self.corn_onion.move(344, 345)
        self.corn_onion.setStyleSheet("color: white;"
                                      "font-size: 16pt;")

        # guacamole onion results
        self.guac_onion = QtWidgets.QLabel(self)
        # initialize to 0 lbs
        self.guac_onion.setText("0.0 " + "lbs")
        self.guac_onion.setFont(medium)
        self.guac_onion.setFixedSize(68, 20)
        self.guac_onion.setAlignment(QtCore.Qt.AlignRight)
        self.guac_onion.move(344, 396)
        self.guac_onion.setStyleSheet("color: white;"
                                      "font-size: 16pt;")

    def _create_jalapenos_result_labels(self):
        """Creates, styles, and places jalapenos result labels for needs of each prep item."""
        medium = self._get_font("medium")

        # brown rice jalapeno results, don't change
        self.brown_jal = QtWidgets.QLabel(self)
        # initialize to 0 lbs
        self.brown_jal.setText("0.0 " + "lbs")
        self.brown_jal.setFont(medium)
        self.brown_jal.setFixedSize(60, 20)
        self.brown_jal.setAlignment(QtCore.Qt.AlignRight)
        self.brown_jal.move(460, 192)
        self.brown_jal.setStyleSheet("color: white;"
                                     "font-size: 16pt;")

        # white rice jalapeno results, don't change
        self.white_jal = QtWidgets.QLabel(self)
        # initialize to 0 lbs
        self.white_jal.setText("0.0 " + "lbs")
        self.white_jal.setFont(medium)
        self.white_jal.setFixedSize(60, 20)
        self.white_jal.setAlignment(QtCore.Qt.AlignRight)
        self.white_jal.move(460, 243)
        self.white_jal.setStyleSheet("color: white;"
                                     "font-size: 16pt;")

        # mild salsa jalapenos results
        self.mild_jal = QtWidgets.QLabel(self)
        # initialize to 0 lbs
        self.mild_jal.setText("0.0 " + "lbs")
        self.mild_jal.setFont(medium)
        self.mild_jal.setFixedSize(60, 20)
        self.mild_jal.setAlignment(QtCore.Qt.AlignRight)
        self.mild_jal.move(460, 294)
        self.mild_jal.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

        # corn salsa jalapeno results
        self.corn_jal = QtWidgets.QLabel(self)
        # initialize to 0 lbs
        self.corn_jal.setText("0.0 " + "lbs")
        self.corn_jal.setFont(medium)
        self.corn_jal.setFixedSize(60, 20)
        self.corn_jal.setAlignment(QtCore.Qt.AlignRight)
        self.corn_jal.move(460, 345)
        self.corn_jal.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

        # guacamole jalapeno results
        self.guac_jal = QtWidgets.QLabel(self)
        # initialize to 0 lbs
        self.guac_jal.setText("0.0 " + "lbs")
        self.guac_jal.setFont(medium)
        self.guac_jal.setFixedSize(60, 20)
        self.guac_jal.setAlignment(QtCore.Qt.AlignRight)
        self.guac_jal.move(460, 396)
        self.guac_jal.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

    def _create_cilantro_result_labels(self):
        """
        Creates, styles, and places cilantro result labels for needs of each prep item..
        """
        medium = self._get_font("medium")

        # brown rice cilantro results
        self.brown_cilantro = QtWidgets.QLabel(self)
        # initialize to 0 bags
        self.brown_cilantro.setText("0.0 " + "bags")
        self.brown_cilantro.setFont(medium)
        self.brown_cilantro.setFixedSize(70, 20)
        self.brown_cilantro.setAlignment(QtCore.Qt.AlignRight)
        self.brown_cilantro.move(570, 192)
        self.brown_cilantro.setStyleSheet("color: white;"
                                     "font-size: 16pt;")

        # white rice cilantro results
        self.white_cilantro = QtWidgets.QLabel(self)
        # initialize to 0 bags
        self.white_cilantro.setText("0.0 " + "bags")
        self.white_cilantro.setFont(medium)
        self.white_cilantro.setFixedSize(70, 20)
        self.white_cilantro.setAlignment(QtCore.Qt.AlignRight)
        self.white_cilantro.move(570, 243)
        self.white_cilantro.setStyleSheet("color: white;"
                                     "font-size: 16pt;")

        # mild salsa cilantro results
        self.mild_cilantro = QtWidgets.QLabel(self)
        # initialize to 0 bags
        self.mild_cilantro.setText("0.0 " + "bags")
        self.mild_cilantro.setFont(medium)
        self.mild_cilantro.setFixedSize(70, 20)
        self.mild_cilantro.setAlignment(QtCore.Qt.AlignRight)
        self.mild_cilantro.move(570, 294)
        self.mild_cilantro.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

        # corn salsa cilantro results
        self.corn_cilantro = QtWidgets.QLabel(self)
        # initialize to 0 bags
        self.corn_cilantro.setText("0.0 " + "bags")
        self.corn_cilantro.setFont(medium)
        self.corn_cilantro.setFixedSize(70, 20)
        self.corn_cilantro.setAlignment(QtCore.Qt.AlignRight)
        self.corn_cilantro.move(570, 345)
        self.corn_cilantro.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

        # guacamole cilantro results
        self.guac_cilantro = QtWidgets.QLabel(self)
        # initialize to 0 bags
        self.guac_cilantro.setText("0.0 " + "bags")
        self.guac_cilantro.setFont(medium)
        self.guac_cilantro.setFixedSize(70, 20)
        self.guac_cilantro.setAlignment(QtCore.Qt.AlignRight)
        self.guac_cilantro.move(570, 396)
        self.guac_cilantro.setStyleSheet("color: white;"
                                    "font-size: 16pt;")

    def _create_total_labels(self):
        """Creates, styles, and places the labels inside of the total box."""
        bold = self._get_font("bold")
        book = self._get_font("book")

        # onions total header
        onion_total_header = QtWidgets.QLabel(self)
        onion_total_header.setFont(bold)
        onion_total_header.setStyleSheet("color: #AB2218;"
                                              "font-size:18pt;")
        onion_total_header.setAlignment(QtCore.Qt.AlignRight)
        onion_total_header.setText("O N I O N S")
        onion_total_header.adjustSize()
        onion_total_header.move(103, 525)

        # jalapenos total header
        jalapenos_total_header = QtWidgets.QLabel(self)
        jalapenos_total_header.setFont(bold)
        jalapenos_total_header.setStyleSheet("color: #AB2218;"
                                                  "font-size: 18pt;")
        jalapenos_total_header.setAlignment(QtCore.Qt.AlignRight)
        jalapenos_total_header.setText("J A L A P E N O S")
        jalapenos_total_header.adjustSize()
        jalapenos_total_header.move(263, 525)

        # cilantro total header
        cilantro_total_header = QtWidgets.QLabel(self)
        cilantro_total_header.setFont(bold)
        cilantro_total_header.setStyleSheet("color: #AB2218;"
                                                 "font-size: 18pt;")
        cilantro_total_header.setAlignment(QtCore.Qt.AlignRight)
        cilantro_total_header.setText("C I L A N T R O")
        cilantro_total_header.adjustSize()
        cilantro_total_header.move(480, 525)

        # onion total, updates with spin box changes
        self.onion_total = QtWidgets.QLabel(self)
        self.onion_total.setFont(bold)
        self.onion_total.setStyleSheet("color: black;"
                                       "font-size:50pt;")
        self.onion_total.setAlignment(QtCore.Qt.AlignCenter)
        self.onion_total.setText("0.0")
        self.onion_total.setFixedSize(115, 50)
        self.onion_total.move(100, 553)

        # jalapenos total, updates with spin box changes
        self.jalapenos_total = QtWidgets.QLabel(self)
        self.jalapenos_total.setFont(bold)
        self.jalapenos_total.setStyleSheet("color: black;"
                                           "font-size:50pt;")
        self.jalapenos_total.setAlignment(QtCore.Qt.AlignCenter)
        self.jalapenos_total.setFixedSize(115, 50)
        self.jalapenos_total.setText("0.0")
        self.jalapenos_total.move(285, 553)

        # cilantro total, updates with spin box changes
        self.cilantro_total = QtWidgets.QLabel(self)
        self.cilantro_total.setFont(bold)
        self.cilantro_total.setStyleSheet("color: black;"
                                          "font-size:50pt;")
        self.cilantro_total.setAlignment(QtCore.Qt.AlignCenter)
        self.cilantro_total.setFixedSize(115, 50)
        self.cilantro_total.setText("0.0")
        self.cilantro_total.adjustSize()
        self.cilantro_total.move(490, 553)

        # onion lbs label
        onion_lbs = QtWidgets.QLabel(self)
        onion_lbs.setFont(book)
        onion_lbs.setStyleSheet("color: black;"
                                     "font-size: 14pt;")
        onion_lbs.setText("p  o  u  n  d  s")
        onion_lbs.adjustSize()
        onion_lbs.move(110, 603)

        # jalapeno lbs label
        jalapeno_lbs = QtWidgets.QLabel(self)
        jalapeno_lbs.setFont(book)
        jalapeno_lbs.setStyleSheet("color: black;"
                                        "font-size: 14pt;")
        jalapeno_lbs.setText("p    o    u    n    d    s")
        jalapeno_lbs.adjustSize()
        jalapeno_lbs.move(280, 603)

        # cilantro lbs label
        cilantro_lbs = QtWidgets.QLabel(self)
        cilantro_lbs.setFont(book)
        cilantro_lbs.setStyleSheet("color: black;"
                                        "font-size: 14pt;")
        cilantro_lbs.setText("b       a       g       s")
        cilantro_lbs.adjustSize()
        cilantro_lbs.move(487, 603)


class OjcCalcModel:
    """
    OJC Calculator's model.
    Calculates onions, jalapenos, and cilantro for each prep ingredient.
    Calculates the total of onions, jalapenos, and cilantro total.
    """

    def __init__(self, view):
        """
        Model initializer, connects to the view GUI.
        """

        super().__init__()
        self._view = view

        # initialize total onions to 0 for each prep item
        self._total_mild_onions = 0
        self._total_corn_onions = 0
        self._total_guac_onions = 0

        # initialize total jalapenos to 0 for each prep item
        self._total_mild_jalapenos = 0
        self._total_corn_jalapenos = 0
        self._total_guac_jalapenos = 0

        # initialize total cilantro to 0 for each prep item
        self._total_brown_cilantro = 0
        self._total_white_cilantro = 0
        self._total_mild_cilantro = 0
        self._total_corn_cilantro = 0
        self._total_guac_cilantro = 0

    def _calculate_onions(self, prep_item):
        """
        Calculates and displays the amount of onions needed for the prep item based off of the recipe card.
        Calculation details: On average, 4oz of onions per cup.

        :param prep_item: prep item with a spin box increase or decrease
        :returns: updated amount of onions needed for the prep item
        """

        # calculate and display mild onion needs, per tray
        if prep_item == "mild":
            value = self._view.mild.value()
            cups = 2 * value
            ounces = cups * 4
            # round to nearest tenth
            pounds = round((ounces / 16), 1)
            self._view.mild_onion.setText(str(pounds) + " lbs")
            # update total mild onions
            self._total_mild_onions = pounds

        # calculate and display corn onion needs, per 6th pan
        elif prep_item == "corn":
            cups = self._view.corn.value()
            ounces = cups * 4
            # round to nearest tenth
            pounds = round((ounces / 16), 1)
            self._view.corn_onion.setText(str(pounds) + " lbs")
            # update total corn onions
            self._total_corn_onions = pounds

        # calculate and displaay guac onion needs, per case
        elif prep_item == "guac":
            value = self._view.guac.value()
            cups = 2.50 * value
            ounces = cups * 4
            # round to nearest tenth
            pounds = round((ounces / 16), 1)
            self._view.guac_onion.setText(str(pounds) + " lbs")
            # update total guac onions
            self._total_guac_onions = pounds

        # update onion total based off of new prep item onion calculation
        self._calculate_total_onions()

    def _calculate_jalapenos(self, prep_item):
        """
        Calculates and displays the amount of jalapenos needed for the prep item based off of the recipe card.
        Calculation details: On average, 4oz of jalapenos per cup.

        :param prep_item: prep item with a spin box increase or decrease
        :return: updated amount of jalapenos needed for the prep item
        """

        # calculate and display mild jalapeno needs, per tray
        if prep_item == "mild":
            value = self._view.mild.value()
            cups = .33 * value
            ounces = cups * 4
            # round to nearest tenth
            pounds = round((ounces / 16), 1)
            self._view.mild_jal.setText(str(pounds) + " lbs")
            # update total mild jalapenos
            self._total_mild_jalapenos = pounds

        # calculate and display corn jalapeno needs, per 6th pan
        elif prep_item == "corn":
            value = self._view.corn.value()
            cups = .75 * value
            ounces = cups * 4
            # round to nearest tenth
            pounds = round((ounces / 16), 1)
            self._view.corn_jal.setText(str(pounds) + " lbs")
            # update total corn jalapenos
            self._total_corn_jalapenos = pounds

        # calculate and display guac jalapeno needs, per case
        elif prep_item == "guac":
            cups = self._view.guac.value()
            ounces = cups * 4
            # round to nearest tenth
            pounds = round((ounces / 16), 1)
            self._view.guac_jal.setText(str(pounds) + " lbs")
            # update total guac jalapenos
            self._total_guac_jalapenos = pounds

        # update jalapeno total based off of new prep item jalapeno calculation
        self._calculate_total_jalapenos()

    def _calculate_cilantro(self, ingredient):
        """
        Calculates and displays the amount of cilantro needed for the prep item based off of the recipe card.
        Calculation details: On average, 12 cups of cilantro per bag.

        :param ingredient: prep item with a spin box increase or decrease
        :return: updated amount of cilantro needed for the prep item
        """

        # calculate and display brown rice cilantro needs, per deep
        if ingredient == 'brown':
            value = self._view.brown_rice.value()
            cups = value * 2
            # round to nearest tenth
            total = round((cups / 12), 1)
            self._view.brown_cilantro.setText(str(total) + " bags")
            # update total brown rice cilantro
            self._total_brown_cilantro = total

        # calculate and display white rice cilantro needs, per deep
        elif ingredient == "white":
            value = self._view.white_rice.value()
            cups = value * 2
            # round to nearest tenth
            total = round((cups / 12), 1)
            self._view.white_cilantro.setText(str(total) + " bags")
            # update total white rice cilantro
            self._total_white_cilantro = total

        # calculate and display mild cilantro needs, per tray
        elif ingredient == "mild":
            value = self._view.mild.value()
            cups = value * 2
            # round to nearest tenth
            total = round((cups / 12), 1)
            self._view.mild_cilantro.setText(str(total) + " bags")
            # update total mild cilantro
            self._total_mild_cilantro = total

        # calculate and display corn cilantro needs, per 6th pan
        elif ingredient == "corn":
            value = self._view.corn.value()
            cups = value * 2
            # round to nearest tenth
            total = round((cups / 12), 1)
            self._view.corn_cilantro.setText(str(total) + " bags")
            # update total corn cilantro
            self._total_corn_cilantro = total

        # calculate and display guac cilantro needs, per case
        elif ingredient == "guac":
            value = self._view.guac.value()
            cups = value * 2.5
            # round to nearest tenth
            total = round((cups / 12), 1)
            self._view.guac_cilantro.setText(str(total) + " bags")
            self._total_guac_cilantro = total

        # update cilantro total based off of new prep item cilantro calculation
        self._calculate_total_cilantro()

    def _calculate_total_onions(self):
        """Calculates and displays the total amount of onions needed."""
        # add all onion totals up, round to the nearest tenth, update label
        total = round(self._total_mild_onions + self._total_corn_onions + self._total_guac_onions, 1)
        total = str(total)
        self._view.onion_total.setText(total)
        self._view.onion_total.adjustSize()

    def _calculate_total_jalapenos(self):
        """Calculates and displays the total amount of jalapenos needed."""
        # add all jalapeno totals up, round to the nearest tenth, update label
        total = round(self._total_mild_jalapenos + self._total_corn_jalapenos + self._total_guac_jalapenos, 1)
        self._view.jalapenos_total.setText(str(total))
        self._view.jalapenos_total.adjustSize()

    def _calculate_total_cilantro(self):
        """Calculates and displays the total amount of cilantro needed."""
        # add all cilantro totals up, round to the nearest tenth, update label
        total = round(self._total_brown_cilantro + self._total_white_cilantro + self._total_mild_cilantro +
                      self._total_corn_cilantro + self._total_guac_cilantro, 1)
        self._view.cilantro_total.setText(str(total))
        self._view.cilantro_total.adjustSize()


class OjcCalcCtrl(OjcCalcModel):
    """OJC Calculator's Controller. Connects the spin box changes to the model for updates."""
    def __init__(self, view):
        """Controller initializer, connects to the view GUI."""
        super().__init__(view)
        self._view = view
        self._connect_signals()

    def _connect_signals(self):
        """Connects the spin box value changes to proper calculation functiosn in the model."""
        # calculate onions when spin box is changed
        self._view.mild.valueChanged.connect(lambda: self._calculate_onions("mild"))
        self._view.corn.valueChanged.connect(lambda: self._calculate_onions("corn"))
        self._view.guac.valueChanged.connect(lambda: self._calculate_onions("guac"))

        # calculate jalapenos when spin box is changed
        self._view.mild.valueChanged.connect(lambda: self._calculate_jalapenos("mild"))
        self._view.corn.valueChanged.connect(lambda: self._calculate_jalapenos("corn"))
        self._view.guac.valueChanged.connect(lambda: self._calculate_jalapenos("guac"))

        # calculate cilantro when spin box is changed
        self._view.brown_rice.valueChanged.connect(lambda: self._calculate_cilantro("brown"))
        self._view.white_rice.valueChanged.connect(lambda: self._calculate_cilantro("white"))
        self._view.mild.valueChanged.connect(lambda: self._calculate_cilantro("mild"))
        self._view.corn.valueChanged.connect(lambda: self._calculate_cilantro("corn"))
        self._view.guac.valueChanged.connect(lambda: self._calculate_cilantro("guac"))


def main():
    ojcCalc = QApplication(sys.argv)
    view = OjcUi()
    view.show()
    OjcCalcCtrl(view=view)
    sys.exit(ojcCalc.exec_())


if __name__ == '__main__':
    main()
