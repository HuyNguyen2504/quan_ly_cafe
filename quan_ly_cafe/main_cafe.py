from PyQt5 import QtCore,QtWidgets,QtGui
import sys
import Hoa_don,Man_hinh_thong_ke_ui ,man_hinh_quan_ly_hoa_don , quan_ly_ban_khach, quan_ly_san_pham 
import Goi_mon,Goi_mon_cafe,Goi_mon_kem,Goi_mon_tra_hoa_qua,Goi_mon_tra_sua
ui=''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def hdUi():
    global ui
    ui = Hoa_don.Ui_Hoa_Don()
    ui.setupUi(MainWindow)
    ui.thong_ke.clicked.connect(mhtkUi)
    ui.menu.clicked.connect(qlb)
    ui.food.clicked.connect(gm)
    ui.quan_ly_hoa_don.clicked.connect(qlhdUi)
    MainWindow.show()
def mhtkUi():
    global ui
    ui = Man_hinh_thong_ke_ui.Ui_Man_hinh_thong_ke()
    ui.setupUi(MainWindow)
    ui.hoa_don.clicked.connect(hdUi)
    ui.menu.clicked.connect(qlb)
    ui.food.clicked.connect(gm)
    ui.quan_ly_hoa_don.clicked.connect(qlhdUi)
    MainWindow.show() 
def qlhdUi():
    global ui
    ui = man_hinh_quan_ly_hoa_don.Ui_man_hinh_quan_ly_hoa_don()
    ui.setupUi(MainWindow)
    ui.thong_ke.clicked.connect(mhtkUi)
    ui.hoa_don.clicked.connect(hdUi)
    ui.food.clicked.connect(gm)
    ui.menu.clicked.connect(qlb)
    MainWindow.show()
def qlb():
    global ui
    ui = quan_ly_ban_khach.Ui_quan_ly_ban_khach()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.quan_ly_san_pham.clicked.connect(qlsp)
    ui.food.clicked.connect(gm)
    MainWindow.show()
def qlsp():
    global ui
    ui = quan_ly_san_pham.Ui_search()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.food.clicked.connect(gm)
    ui.quan_ly_ban.clicked.connect(qlb)
    MainWindow.show()
def gm():
    global ui
    ui = Goi_mon.Ui_goi_mon()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.menu.clicked.connect(qlb)
    ui.loai_cafe.clicked.connect(cf)
    ui.loai_tra_hoa_qua.clicked.connect(thq)
    ui.loai_tra_sua.clicked.connect(ts)
    ui.loai_kem.clicked.connect(ice_cream)
    MainWindow.show()
def cf():
    global ui
    ui = Goi_mon_cafe.Ui_goi_mon_cafe()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.menu.clicked.connect(qlb)
    ui.loai_tra_hoa_qua.clicked.connect(thq)
    ui.loai_tra_sua.clicked.connect(ts)
    ui.loai_kem.clicked.connect(ice_cream)
    MainWindow.show()
def ts():
    global ui
    ui = Goi_mon_tra_sua.Ui_goi_mon_tra_sua()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.menu.clicked.connect(qlb)
    ui.loai_cafe.clicked.connect(cf)
    ui.loai_tra_hoa_qua.clicked.connect(thq)
    ui.loai_kem.clicked.connect(ice_cream)
    MainWindow.show()
def thq():
    global ui
    ui = Goi_mon_tra_hoa_qua.Ui_goi_mon_tra_hoa_qua()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.menu.clicked.connect(qlb)
    ui.loai_tra_sua.clicked.connect(ts)
    ui.loai_cafe.clicked.connect(cf)
    ui.loai_kem.clicked.connect(ice_cream)
    MainWindow.show()
def ice_cream():
    global ui
    ui = Goi_mon_kem.Ui_goi_mon_kem()
    ui.setupUi(MainWindow)
    ui.check.clicked.connect(mhtkUi)
    ui.menu.clicked.connect(qlb)
    ui.loai_tra_sua.clicked.connect(ts)
    ui.loai_cafe.clicked.connect(cf)
    ui.loai_tra_hoa_qua.clicked.connect(thq)
    MainWindow.show()
#run
hdUi()
sys.exit(app.exec())
