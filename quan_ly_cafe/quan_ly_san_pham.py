# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quan_ly_san_pham.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_search(object):
    def setupUi(self, search):
        search.setObjectName("search")
        search.resize(1031, 811)
        self.centralwidget = QtWidgets.QWidget(search)
        self.centralwidget.setObjectName("centralwidget")
        self.thong_ke_gr = QtWidgets.QGroupBox(self.centralwidget)
        self.thong_ke_gr.setGeometry(QtCore.QRect(0, 0, 1031, 811))
        self.thong_ke_gr.setStyleSheet("background-color: rgb(0, 0, 206);")
        self.thong_ke_gr.setTitle("")
        self.thong_ke_gr.setObjectName("thong_ke_gr")
        self.check = QtWidgets.QPushButton(self.thong_ke_gr)
        self.check.setGeometry(QtCore.QRect(30, 360, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check.setFont(font)
        self.check.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.check.setObjectName("check")
        self.exit = QtWidgets.QPushButton(self.thong_ke_gr)
        self.exit.setGeometry(QtCore.QRect(30, 700, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: rgb(255, 0, 0);")
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
        self.back = QtWidgets.QPushButton(self.thong_ke_gr)
        self.back.setGeometry(QtCore.QRect(900, 747, 93, 41))
        self.back.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.back.setObjectName("back")
        self.quan_ly_san_pham = QtWidgets.QPushButton(self.thong_ke_gr)
        self.quan_ly_san_pham.setGeometry(QtCore.QRect(470, 30, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quan_ly_san_pham.setFont(font)
        self.quan_ly_san_pham.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"")
        self.quan_ly_san_pham.setObjectName("quan_ly_san_pham")
        self.food = QtWidgets.QPushButton(self.thong_ke_gr)
        self.food.setGeometry(QtCore.QRect(30, 470, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.food.setFont(font)
        self.food.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.food.setObjectName("food")
        self.quan_ly_ban = QtWidgets.QPushButton(self.thong_ke_gr)
        self.quan_ly_ban.setGeometry(QtCore.QRect(220, 30, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quan_ly_ban.setFont(font)
        self.quan_ly_ban.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quan_ly_ban.setObjectName("quan_ly_ban")
        self.menu = QtWidgets.QPushButton(self.thong_ke_gr)
        self.menu.setGeometry(QtCore.QRect(30, 230, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.menu.setObjectName("menu")
        self.groupBox = QtWidgets.QGroupBox(self.thong_ke_gr)
        self.groupBox.setGeometry(QtCore.QRect(220, 120, 771, 371))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ma_sp = QtWidgets.QLineEdit(self.groupBox)
        self.ma_sp.setGeometry(QtCore.QRect(70, 41, 113, 31))
        self.ma_sp.setObjectName("ma_sp")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 100, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ten_sp = QtWidgets.QLineEdit(self.groupBox)
        self.ten_sp.setGeometry(QtCore.QRect(70, 91, 113, 31))
        self.ten_sp.setObjectName("ten_sp")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.don_gia = QtWidgets.QLineEdit(self.groupBox)
        self.don_gia.setGeometry(QtCore.QRect(70, 151, 113, 31))
        self.don_gia.setObjectName("don_gia")
        self.add_san_pham = QtWidgets.QPushButton(self.groupBox)
        self.add_san_pham.setGeometry(QtCore.QRect(460, 40, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_san_pham.setFont(font)
        self.add_san_pham.setObjectName("add_san_pham")
        self.fix_sam_pham = QtWidgets.QPushButton(self.groupBox)
        self.fix_sam_pham.setGeometry(QtCore.QRect(600, 40, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fix_sam_pham.setFont(font)
        self.fix_sam_pham.setObjectName("fix_sam_pham")
        self.xoa_san_pham = QtWidgets.QPushButton(self.groupBox)
        self.xoa_san_pham.setGeometry(QtCore.QRect(460, 120, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.xoa_san_pham.setFont(font)
        self.xoa_san_pham.setObjectName("xoa_san_pham")
        self.lam_moi = QtWidgets.QPushButton(self.groupBox)
        self.lam_moi.setGeometry(QtCore.QRect(600, 120, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lam_moi.setFont(font)
        self.lam_moi.setObjectName("lam_moi")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(600, 210, 101, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(460, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tim_kiem = QtWidgets.QLineEdit(self.groupBox)
        self.tim_kiem.setGeometry(QtCore.QRect(460, 290, 181, 31))
        self.tim_kiem.setObjectName("tim_kiem")
        self.searching = QtWidgets.QPushButton(self.groupBox)
        self.searching.setGeometry(QtCore.QRect(640, 290, 31, 31))
        self.searching.setStyleSheet("border-image: url(:/picture/398288296_664763935842542_91204699368765392_n.png);")
        self.searching.setText("")
        self.searching.setObjectName("searching")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(460, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(370, 0, 16, 371))
        self.label_9.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(390, 0, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.groupBox_2 = QtWidgets.QGroupBox(self.thong_ke_gr)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 530, 771, 201))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(340, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(620, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.ma_sp1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ma_sp1.setGeometry(QtCore.QRect(0, 80, 241, 31))
        self.ma_sp1.setObjectName("ma_sp1")
        self.ten_sp1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ten_sp1.setGeometry(QtCore.QRect(240, 80, 281, 31))
        self.ten_sp1.setObjectName("ten_sp1")
        self.don_gia1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.don_gia1.setGeometry(QtCore.QRect(520, 80, 251, 31))
        self.don_gia1.setObjectName("don_gia1")
        self.ma_sp2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ma_sp2.setGeometry(QtCore.QRect(0, 110, 241, 31))
        self.ma_sp2.setObjectName("ma_sp2")
        self.ten_sp2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ten_sp2.setGeometry(QtCore.QRect(240, 110, 281, 31))
        self.ten_sp2.setObjectName("ten_sp2")
        self.don_gia2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.don_gia2.setGeometry(QtCore.QRect(520, 110, 251, 31))
        self.don_gia2.setObjectName("don_gia2")
        self.don_gia3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.don_gia3.setGeometry(QtCore.QRect(520, 140, 251, 31))
        self.don_gia3.setObjectName("don_gia3")
        self.ma_sp3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ma_sp3.setGeometry(QtCore.QRect(0, 140, 241, 31))
        self.ma_sp3.setObjectName("ma_sp3")
        self.ten_sp3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ten_sp3.setGeometry(QtCore.QRect(240, 140, 281, 31))
        self.ten_sp3.setObjectName("ten_sp3")
        self.don_gia4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.don_gia4.setGeometry(QtCore.QRect(520, 170, 251, 31))
        self.don_gia4.setObjectName("don_gia4")
        self.ma_sp4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ma_sp4.setGeometry(QtCore.QRect(0, 170, 241, 31))
        self.ma_sp4.setObjectName("ma_sp4")
        self.ten_sp4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.ten_sp4.setGeometry(QtCore.QRect(240, 170, 281, 31))
        self.ten_sp4.setObjectName("ten_sp4")
        search.setCentralWidget(self.centralwidget)

        self.retranslateUi(search)
        QtCore.QMetaObject.connectSlotsByName(search)

    def retranslateUi(self, search):
        _translate = QtCore.QCoreApplication.translate
        search.setWindowTitle(_translate("search", "Quản Lý Sản Phẩm"))
        self.check.setText(_translate("search", "Hóa Đơn"))
        self.exit.setText(_translate("search", "Đăng Xuất"))
        self.main.setText(_translate("search", "Trang chủ"))
        self.account.setText(_translate("search", "Tài Khoản"))
        self.back.setText(_translate("search", "Trở về"))
        self.quan_ly_san_pham.setText(_translate("search", "Quản Lý Sản Phẩm"))
        self.food.setText(_translate("search", "Gọi Món"))
        self.quan_ly_ban.setText(_translate("search", "Quản Lý Bàn"))
        self.menu.setText(_translate("search", "MENU"))
        self.groupBox.setTitle(_translate("search", "Bảng Thông Tin Sản Phẩm"))
        self.label.setText(_translate("search", "mã sp"))
        self.label_2.setText(_translate("search", "  tên sp"))
        self.label_3.setText(_translate("search", "Đơn giá"))
        self.add_san_pham.setText(_translate("search", "Thêm"))
        self.fix_sam_pham.setText(_translate("search", "Sửa"))
        self.xoa_san_pham.setText(_translate("search", "Xóa"))
        self.lam_moi.setText(_translate("search", "Làm Mới"))
        self.comboBox.setItemText(0, _translate("search", "0k-30k"))
        self.comboBox.setItemText(1, _translate("search", "30k-50k"))
        self.comboBox.setItemText(2, _translate("search", "50k-100k"))
        self.comboBox.setItemText(3, _translate("search", ">100k"))
        self.label_4.setText(_translate("search", "Khoảng giá"))
        self.label_5.setText(_translate("search", "TÌm Kiếm"))
        self.label_10.setText(_translate("search", "Chỉnh Sửa Sản Phẩm"))
        self.groupBox_2.setTitle(_translate("search", "Thông Tin"))
        self.label_6.setText(_translate("search", "mã sp"))
        self.label_7.setText(_translate("search", "tên sp"))
        self.label_8.setText(_translate("search", "Đơn giá"))
import  add_image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    search = QtWidgets.QMainWindow()
    ui = Ui_search()
    ui.setupUi(search)
    search.show()
    sys.exit(app.exec_())
