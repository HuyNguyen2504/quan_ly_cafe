# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Goi_mon_cafe.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_goi_mon_cafe(object):
    def setupUi(self, goi_mon_cafe):
        goi_mon_cafe.setObjectName("goi_mon_cafe")
        goi_mon_cafe.resize(1031, 811)
        self.centralwidget = QtWidgets.QWidget(goi_mon_cafe)
        self.centralwidget.setObjectName("centralwidget")
        self.thong_ke_gr = QtWidgets.QGroupBox(self.centralwidget)
        self.thong_ke_gr.setGeometry(QtCore.QRect(0, 0, 1031, 811))
        self.thong_ke_gr.setStyleSheet("background-color: rgb(0, 0, 212);")
        self.thong_ke_gr.setTitle("")
        self.thong_ke_gr.setObjectName("thong_ke_gr")
        self.check = QtWidgets.QPushButton(self.thong_ke_gr)
        self.check.setGeometry(QtCore.QRect(30, 360, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check.setFont(font)
        self.check.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.check.setObjectName("check")
        self.exit = QtWidgets.QPushButton(self.thong_ke_gr)
        self.exit.setGeometry(QtCore.QRect(30, 700, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exit.setObjectName("exit")
        self.main = QtWidgets.QPushButton(self.thong_ke_gr)
        self.main.setGeometry(QtCore.QRect(30, 120, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main.setFont(font)
        self.main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main.setObjectName("main")
        self.account = QtWidgets.QPushButton(self.thong_ke_gr)
        self.account.setGeometry(QtCore.QRect(30, 580, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.account.setFont(font)
        self.account.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.account.setObjectName("account")
        self.food = QtWidgets.QPushButton(self.thong_ke_gr)
        self.food.setGeometry(QtCore.QRect(30, 470, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.food.setFont(font)
        self.food.setStyleSheet("\n"
"background-color: rgb(85, 255, 255);")
        self.food.setObjectName("food")
        self.menu = QtWidgets.QPushButton(self.thong_ke_gr)
        self.menu.setGeometry(QtCore.QRect(30, 230, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menu.setObjectName("menu")
        self.label_7 = QtWidgets.QLabel(self.thong_ke_gr)
        self.label_7.setGeometry(QtCore.QRect(870, 140, 41, 51))
        self.label_7.setStyleSheet("border-image: url(:/picture/395070080_1102509174491433_4288964831604057301_n.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.thong_ke_gr)
        self.label_8.setGeometry(QtCore.QRect(870, 220, 51, 51))
        self.label_8.setStyleSheet("border-image: url(:/picture/386430766_2761601370663967_2700256571421014709_n.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(self.thong_ke_gr)
        self.groupBox.setGeometry(QtCore.QRect(220, 0, 811, 811))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.loai_cafe = QtWidgets.QPushButton(self.groupBox)
        self.loai_cafe.setGeometry(QtCore.QRect(630, 0, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loai_cafe.setFont(font)
        self.loai_cafe.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.loai_cafe.setObjectName("loai_cafe")
        self.loai_tra_sua = QtWidgets.QPushButton(self.groupBox)
        self.loai_tra_sua.setGeometry(QtCore.QRect(630, 90, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loai_tra_sua.setFont(font)
        self.loai_tra_sua.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);")
        self.loai_tra_sua.setObjectName("loai_tra_sua")
        self.loai_tra_hoa_qua = QtWidgets.QPushButton(self.groupBox)
        self.loai_tra_hoa_qua.setGeometry(QtCore.QRect(630, 180, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loai_tra_hoa_qua.setFont(font)
        self.loai_tra_hoa_qua.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);")
        self.loai_tra_hoa_qua.setObjectName("loai_tra_hoa_qua")
        self.loai_kem = QtWidgets.QPushButton(self.groupBox)
        self.loai_kem.setGeometry(QtCore.QRect(630, 270, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loai_kem.setFont(font)
        self.loai_kem.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);")
        self.loai_kem.setObjectName("loai_kem")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(260, 0, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(0, 20, 351, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(340, 0, 20, 801))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(620, 0, 20, 801))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.ten_mon = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon.setGeometry(QtCore.QRect(0, 30, 261, 51))
        self.ten_mon.setObjectName("ten_mon")
        self.ten_mon_2 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_2.setGeometry(QtCore.QRect(0, 80, 261, 51))
        self.ten_mon_2.setObjectName("ten_mon_2")
        self.ten_mon_4 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_4.setGeometry(QtCore.QRect(0, 180, 261, 51))
        self.ten_mon_4.setObjectName("ten_mon_4")
        self.ten_mon_3 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_3.setGeometry(QtCore.QRect(0, 130, 261, 51))
        self.ten_mon_3.setObjectName("ten_mon_3")
        self.ten_mon_6 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_6.setGeometry(QtCore.QRect(0, 280, 261, 51))
        self.ten_mon_6.setObjectName("ten_mon_6")
        self.ten_mon_7 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_7.setGeometry(QtCore.QRect(0, 330, 261, 51))
        self.ten_mon_7.setObjectName("ten_mon_7")
        self.ten_mon_5 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_5.setGeometry(QtCore.QRect(0, 230, 261, 51))
        self.ten_mon_5.setObjectName("ten_mon_5")
        self.ten_mon_8 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_8.setGeometry(QtCore.QRect(0, 380, 261, 51))
        self.ten_mon_8.setObjectName("ten_mon_8")
        self.ten_mon_12 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_12.setGeometry(QtCore.QRect(0, 580, 261, 51))
        self.ten_mon_12.setObjectName("ten_mon_12")
        self.ten_mon_11 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_11.setGeometry(QtCore.QRect(0, 530, 261, 51))
        self.ten_mon_11.setObjectName("ten_mon_11")
        self.ten_mon_10 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_10.setGeometry(QtCore.QRect(0, 480, 261, 51))
        self.ten_mon_10.setObjectName("ten_mon_10")
        self.ten_mon_9 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_9.setGeometry(QtCore.QRect(0, 430, 261, 51))
        self.ten_mon_9.setObjectName("ten_mon_9")
        self.ten_mon_13 = QtWidgets.QLineEdit(self.groupBox)
        self.ten_mon_13.setGeometry(QtCore.QRect(0, 630, 261, 51))
        self.ten_mon_13.setObjectName("ten_mon_13")
        self.so_luong = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong.setGeometry(QtCore.QRect(260, 30, 81, 51))
        self.so_luong.setObjectName("so_luong")
        self.so_luong_2 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_2.setGeometry(QtCore.QRect(260, 80, 81, 51))
        self.so_luong_2.setObjectName("so_luong_2")
        self.so_luong_3 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_3.setGeometry(QtCore.QRect(260, 130, 81, 51))
        self.so_luong_3.setObjectName("so_luong_3")
        self.so_luong_4 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_4.setGeometry(QtCore.QRect(260, 180, 81, 51))
        self.so_luong_4.setObjectName("so_luong_4")
        self.so_luong_5 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_5.setGeometry(QtCore.QRect(260, 230, 81, 51))
        self.so_luong_5.setObjectName("so_luong_5")
        self.so_luong_6 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_6.setGeometry(QtCore.QRect(260, 280, 81, 51))
        self.so_luong_6.setObjectName("so_luong_6")
        self.so_luong_7 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_7.setGeometry(QtCore.QRect(260, 330, 81, 51))
        self.so_luong_7.setObjectName("so_luong_7")
        self.so_luong_8 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_8.setGeometry(QtCore.QRect(260, 380, 81, 51))
        self.so_luong_8.setObjectName("so_luong_8")
        self.so_luong_9 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_9.setGeometry(QtCore.QRect(260, 430, 81, 51))
        self.so_luong_9.setObjectName("so_luong_9")
        self.so_luong_10 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_10.setGeometry(QtCore.QRect(260, 480, 81, 51))
        self.so_luong_10.setObjectName("so_luong_10")
        self.so_luong_11 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_11.setGeometry(QtCore.QRect(260, 530, 81, 51))
        self.so_luong_11.setObjectName("so_luong_11")
        self.so_luong_12 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_12.setGeometry(QtCore.QRect(260, 580, 81, 51))
        self.so_luong_12.setObjectName("so_luong_12")
        self.so_luong_13 = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_13.setGeometry(QtCore.QRect(260, 630, 81, 51))
        self.so_luong_13.setObjectName("so_luong_13")
        self.line_7 = QtWidgets.QFrame(self.groupBox)
        self.line_7.setGeometry(QtCore.QRect(0, 720, 351, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 740, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sum_tien = QtWidgets.QLineEdit(self.groupBox)
        self.sum_tien.setGeometry(QtCore.QRect(62, 731, 201, 71))
        self.sum_tien.setObjectName("sum_tien")
        self.so_luong_sum = QtWidgets.QLineEdit(self.groupBox)
        self.so_luong_sum.setGeometry(QtCore.QRect(260, 730, 81, 71))
        self.so_luong_sum.setObjectName("so_luong_sum")
        self.cafe_sua = QtWidgets.QPushButton(self.groupBox)
        self.cafe_sua.setGeometry(QtCore.QRect(350, 0, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cafe_sua.setFont(font)
        self.cafe_sua.setObjectName("cafe_sua")
        self.cafe_nau_da = QtWidgets.QPushButton(self.groupBox)
        self.cafe_nau_da.setGeometry(QtCore.QRect(490, 0, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cafe_nau_da.setFont(font)
        self.cafe_nau_da.setObjectName("cafe_nau_da")
        self.bac_xiu = QtWidgets.QPushButton(self.groupBox)
        self.bac_xiu.setGeometry(QtCore.QRect(350, 130, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bac_xiu.setFont(font)
        self.bac_xiu.setObjectName("bac_xiu")
        self.cafe_den = QtWidgets.QPushButton(self.groupBox)
        self.cafe_den.setGeometry(QtCore.QRect(490, 130, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cafe_den.setFont(font)
        self.cafe_den.setObjectName("cafe_den")
        self.line_3.raise_()
        self.loai_cafe.raise_()
        self.loai_tra_sua.raise_()
        self.loai_tra_hoa_qua.raise_()
        self.loai_kem.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.line_2.raise_()
        self.line.raise_()
        self.ten_mon.raise_()
        self.ten_mon_2.raise_()
        self.ten_mon_4.raise_()
        self.ten_mon_3.raise_()
        self.ten_mon_6.raise_()
        self.ten_mon_7.raise_()
        self.ten_mon_5.raise_()
        self.ten_mon_8.raise_()
        self.ten_mon_12.raise_()
        self.ten_mon_11.raise_()
        self.ten_mon_10.raise_()
        self.ten_mon_9.raise_()
        self.ten_mon_13.raise_()
        self.so_luong.raise_()
        self.so_luong_2.raise_()
        self.so_luong_3.raise_()
        self.so_luong_4.raise_()
        self.so_luong_5.raise_()
        self.so_luong_6.raise_()
        self.so_luong_7.raise_()
        self.so_luong_8.raise_()
        self.so_luong_9.raise_()
        self.so_luong_10.raise_()
        self.so_luong_11.raise_()
        self.so_luong_12.raise_()
        self.so_luong_13.raise_()
        self.line_7.raise_()
        self.label.raise_()
        self.sum_tien.raise_()
        self.so_luong_sum.raise_()
        self.cafe_sua.raise_()
        self.cafe_nau_da.raise_()
        self.bac_xiu.raise_()
        self.cafe_den.raise_()
        goi_mon_cafe.setCentralWidget(self.centralwidget)

        self.retranslateUi(goi_mon_cafe)
        QtCore.QMetaObject.connectSlotsByName(goi_mon_cafe)

    def retranslateUi(self, goi_mon_cafe):
        _translate = QtCore.QCoreApplication.translate
        goi_mon_cafe.setWindowTitle(_translate("goi_mon_cafe", "MainWindow"))
        self.check.setText(_translate("goi_mon_cafe", "Hóa Đơn"))
        self.exit.setText(_translate("goi_mon_cafe", "Đăng Xuất"))
        self.main.setText(_translate("goi_mon_cafe", "Trang chủ"))
        self.account.setText(_translate("goi_mon_cafe", "Tài Khoản"))
        self.food.setText(_translate("goi_mon_cafe", "Gọi Món"))
        self.menu.setText(_translate("goi_mon_cafe", "MENU"))
        self.loai_cafe.setText(_translate("goi_mon_cafe", "Cafe"))
        self.loai_tra_sua.setText(_translate("goi_mon_cafe", "Trà Sữa"))
        self.loai_tra_hoa_qua.setText(_translate("goi_mon_cafe", "Trà Hoa Quả"))
        self.loai_kem.setText(_translate("goi_mon_cafe", "Kem"))
        self.label_3.setText(_translate("goi_mon_cafe", "Tên món"))
        self.label_4.setText(_translate("goi_mon_cafe", "Số Lượng"))
        self.label.setText(_translate("goi_mon_cafe", "Tổng : "))
        self.cafe_sua.setText(_translate("goi_mon_cafe", "Cafe Sữa\n"
"\n"
"40.000"))
        self.cafe_nau_da.setText(_translate("goi_mon_cafe", "Cafe Nâu Đá\n"
"\n"
"35.000"))
        self.bac_xiu.setText(_translate("goi_mon_cafe", "Bạc Xỉu\n"
"\n"
"35.000"))
        self.cafe_den.setText(_translate("goi_mon_cafe", "Cafe Đen\n"
"\n"
"45.000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    goi_mon_cafe = QtWidgets.QMainWindow()
    ui = Ui_goi_mon_cafe()
    ui.setupUi(goi_mon_cafe)
    goi_mon_cafe.show()
    sys.exit(app.exec_())
