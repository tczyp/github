# coding:utf-8

# 实现利用部件管理器来定义空间
import os
import sys
# 导入Qt的所有模块
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import matplotlib

matplotlib.use("Qt4Agg")
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


# from configobj import ConfigObj
# import pyHook
# import pythoncom



# reload(sys)
# sys.setdefaultencoding('utf-8')



# 做两个模板 ？
########################################################################
class FourCanvas(FigureCanvas):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent=None):
        """Constructor"""
        self.fig = Figure()
        self.ax0 = self.fig.add_subplot(111)
        # self.ax1= self.fig.add_subplot(222)
        # self.ax2 = self.fig.add_subplot(223)
        # self.ax3 = self.fig.add_subplot(224)

        self.myCanvas()
        FigureCanvas.__init__(self, self.fig)
        # self.canvas = FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.parent = parent
        # self.toolbar =NavigationToolbar(FigureCanvas ,self)

        # FigureCanvas.setSizePolicy(self,
        # QSizePolicy.Expanding,
        # QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    # ----------------------------------------------------------------------
    def clab(self):
        """测试成功 这里是清楚关系 """
        self.fig.clf(False)

    # ----------------------------------------------------------------------
    def generate_fig(self):
        """"""
        self.ax0 = self.fig.add_subplot(221)
        self.ax1 = self.fig.add_subplot(222)
        self.ax2 = self.fig.add_subplot(223)
        # self.ax3 = self.fig.add_subplot(224)

        # self.myCanvas()
        # FigureCanvas.__init__(self, self.fig)
        ##self.canvas = FigureCanvas.__init__(self, fig)
        # self.setParent(self.parent)

        ##FigureCanvas.setSizePolicy(self,
        ##QSizePolicy.Expanding,
        ##QSizePolicy.Expanding)
        # FigureCanvas.updateGeometry(self)
        ##self.fig.draw()

    # ----------------------------------------------------------------------
    def generate_figone(self):
        """"""
        self.ax0 = self.fig.add_subplot(111)

    # ----------------------------------------------------------------------
    def myCanvas():
        """  这里 ax 是描述4个周的表头"""
        pass


########################################################################
class setForCanvas(FourCanvas):
    """ 继承实现绘制功能"""

    # ----------------------------------------------------------------------
    def __init__(self, parent=None):
        """"""
        super(setForCanvas, self).__init__(parent)

    # ----------------------------------------------------------------------
    def myCanvas(self):
        """"""
        # t = np.arange(0.0, 3.0, 0.01)
        # s =  np.arange(0.0, 3.0, 0.01)
        # self.ax0.stackplot (t,s,color ="#ff654a" ,alpha= .4 )
        # td = u"熊熊"
        # self.ax0.set_title (td)
        # self.ax1.stackplot (t,s,color ="#ff654a" ,alpha= .4 )
        # self.ax2.stackplot (t,s,color ="#ff654a" ,alpha= .4 )
        # self.ax3.stackplot (t,s,color ="#ff654a" ,alpha= .4 )
        pass

    def cavas_h_dp(self, t, s, c):
        """ t s  都是链表的链表 这样就可以表现多个情况 """
        ci = len(t)
        if c == None:
            for each in range(ci):
                self.ax0.plot(t[each], s[each], linewidth=2)
                # self.ax0.hold()
        else:
            for each in range(ci):
                self.ax0.plot(t[each], s[each], linewidth=2, color=c[each])
                # self.ax0.hold()

    # ----------------------------------------------------------------------
    def cavas_dp(self, scene_name):
        """这里实现低配绘制显示"""
        pass


########################################################################
class Data_S(QWidget):
    """ 继承窗口类实现基本按钮设定
        关于这部分
    """

    # printf =None
    # ----------------------------------------------------------------------
    def __init__(self, parent=None):
        """Constructor"""

        super(Data_S, self).__init__(parent)
        # self.setGeometry(300, 300 , 1080 , 640 )

        self.setWindowTitle(u"shader数据工具---裴永超-- 实现输出 gl_x  gl_y gl_c 链表嵌套链表1.3= ")
        ic = QIcon("data\\ico.bmp")
        # print ic
        self.setWindowIcon(ic)
        # 通过点击选择项 修改数值 1 2 3 来进行表格tab 枚举处理
        self.INDEX_RADIOBUTTON = 0

        self.dits = {"f1": 16777264, "f2": 16777265, "f3": 16777266, "f4": 16777267, "f5": 16777268, "f6": 16777269,
                     "f7": 16777270, "f8": 16777271, "f9": 16777272, "f10": 16777273, "f11": 16777274, "f12": 16777275}
        # self.get_hook ()
        # hm = pyHook.HookManager()
        # hm.KeyDown= self.get_hook
        # hm.HookMouse()
        # hm.HookKeyboard()
        # print self.dits.keys()
        self.setup_ui()

        ##----------------------------------------------------------------------
        # def get_hook (self,event):
        # """"""
        ##self.btn_draw()
        # print "sdfsdf"

    # ----------------------------------------------------------------------
    def cout(self, *con):
        """"""
        conn = ""
        for cc in con:
            conn += unicode(cc)
            conn += " "
        conn += "\n"
        # self.editboxprint.setText("")
        self.editboxprint.insertPlainText(conn)

    # ----------------------------------------------------------------------
    def cl(self):
        """"""
        self.editboxprint.setText("")

    # ----------------------------------------------------------------------
    def setup_ui(self):
        """"""
        #
        # hbox = QVBoxLayout(self)
        self.frame_list = QFrame(self)
        # self.frame_list.setLineWidth (3)
        self.frame_list.setFrameShape(QFrame.StyledPanel)

        # conxt = "import numpy as np #np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)#c= np.arange(2,90 ,0.5)"
        # conxt +="\n"
        # conxt+= "t=[2,4]"
        # conxt+="\n"
        # conxt+="s=[3,5]"

        self.cint = '''import numpy as np
from numpy import *
cout=self.cout
#np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#c= np.arange(2,90 ,0.5)
# map  zip [] filter lambda reduce
'''

        conxt = ''' # sin cos 数据函数使用了unmpy库函数可以直接使用 增加cout 输出debug
def zz (y):
    """"""
    global cout
    if y <0 :
        y=0
    elif y>1:
        y=1
    cout(u"测试过程")
    return y

one= np.linspace(0,1,12)
a= np.linspace(0,1,12)
aa= []
yy=[]
for each in one :
    #for a in ay :
    s=3*a**2 - 2*a**3
    y=a*each

    c= map(zz, y )
    #print c
    cout(y)
    aa.append(one )
    yy.append(c*s )
gl_c=['#333333']*12
gl_x=aa
gl_y=yy
#self.cl()
'''
        self.editbox = QTextEdit(self.frame_list)
        self.editboxprint = QTextEdit(self.frame_list)
        self.editbox.insertPlainText((conxt).decode("utf-8"))
        self.but = QPushButton(u"绘制函数", self.frame_list)
        self.but_open = QPushButton(u"打开算法", self.frame_list)
        self.but_save = QPushButton(u"保存算法", self.frame_list)
        self.check_c = QCheckBox(u"是否绘制图形", self.frame_list)
        self.check_c.setCheckState(Qt.Checked)
        # self.but_cif = QLineEdit(u"t" ,self.frame_list)
        self.but_cif = QComboBox(self.frame_list)
        self.but_cif.addItems(self.dits.keys())

        h = QHBoxLayout()
        h.addWidget(self.but_cif)
        h.addWidget(self.but_open)
        h.addWidget(self.but_save)
        h.addWidget(self.but)
        h.addWidget(self.check_c)
        hh = QHBoxLayout()
        hh.addWidget(self.editboxprint)

        selffrmeV = QVBoxLayout(self.frame_list)
        selffrmeV.addWidget(self.editbox, 190)
        # selffrmeV.addWidget(self.editbox,190)
        selffrmeV.addLayout(h)
        selffrmeV.addLayout(hh, 0)

        self.but.clicked.connect(self.btn_draw)
        self.but_open.clicked.connect(self.get_show_dialog)
        self.but_save.clicked.connect(self.set_show_dia)
        self.editbox.cursorPositionChanged.connect(self.get_cursor)

        self.frame_print = QFrame(self)
        # self.frame_print.setLineWidth (3)
        self.frame_print.setFrameShape(QFrame.StyledPanel)

        self.sc = setForCanvas(self.frame_print)
        self.toolbar = NavigationToolbar(self.sc, self.frame_print)
        # self.toolbar.hide()
        l = QVBoxLayout(self.frame_print)
        l.addWidget(self.toolbar)
        l.addWidget(self.sc)

        # self.frame_print.setLayout(l)


        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.frame_list)
        self.hbox.addWidget(self.frame_print)

        self.setLayout(self.hbox)
        self.resize(1330, 730)

    # ----------------------------------------------------------------------
    def get_cursor(self):
        """通过光标获取位置"""
        # print "22"

        tc = self.editbox.textCursor()
        playout = tc.block().layout()
        n = tc.position() - tc.block().position()
        ntestline = playout.lineForTextPosition(n).lineNumber() + tc.block().firstLineNumber();
        # print ntestline
        # print tc
        self.setWindowTitle(u"shader数据工具---裴永超-- 实现输出 gl_x  gl_y gl_c 链表嵌套链表1.3= " + unicode(ntestline))

    # ----------------------------------------------------------------------
    def get_show_dialog(self):
        """"""
        tempath = sys.argv[0]
        fi = os.path.dirname(tempath) + "\\pbdata"
        filename = QFileDialog.getOpenFileName(self, "openfile", fi, "pb(*.pb)")
        filename = unicode(filename)
        if os.path.isfile(filename):
            fname = open(filename)
            t = fname.read()
            fname.close()
            # print t
            self.editbox.setText("")
            self.editbox.insertPlainText((t).decode("utf-8"))

    # ----------------------------------------------------------------------
    def set_show_dia(self):
        """"""
        tempath = sys.argv[0]
        fi = os.path.dirname(tempath) + "\\pbdata"
        filename = QFileDialog.getSaveFileName(self, "save file", fi, "pb(*.pb)")
        # print
        filename = unicode(filename)
        dirnamec = os.path.dirname(((filename)))
        if os.path.isdir(dirnamec):
            fname = open(filename, "w")
            con = self.editbox.toPlainText()
            # print con
            fname.writelines((unicode(con)).encode("utf-8"))
            fname.close()

    def keyPressEvent(self, event):
        """"""
        tem = self.but_cif.currentText()
        # print tem
        value = self.dits[str(tem)]

        if event.key() == value:
            # print (QtCore.Qt.Key_F12)
            self.btn_draw()

    # ----------------------------------------------------------------------
    def btn_draw(self):
        """ 尝试解析字符串进调用"""
        try:
            cin = self.cint
            ui = self.editbox.toPlainText()
            exe_str = unicode(cin + ui)
            print 'cin', cin
            print 'exe_str', exe_str
            # self.set_plot()
            # self.clearp()
            # self.sc.generate_figone()
            exec (exe_str)
            if self.check_c.checkState() == Qt.Checked:
                self.set_plot(gl_x, gl_y, gl_c)
                print str(self.combox.currentText()).strip()
                self.sc.draw()
                # print ui
        except Exception, ex:
            # self.mbox(str(ex) )
            titi = unicode(ex)
            # self.mbox(titi )
            self.editboxprint.setText("")
            self.editboxprint.insertPlainText(titi)

            # ----------------------------------------------------------------------

    def set_plot(self, t, s, c):
        """ 设置绘制的框架"""
        # self.sc.generate_fig()
        self.clearp()
        self.sc.generate_figone()

        self.sc.cavas_h_dp(t, s, c)
        # print str(self.combox.currentText()).strip()
        self.sc.draw()

    # ----------------------------------------------------------------------
    def open_pb(self):
        """ 用来打开我保存顺风，默认算法都是在软件工程中"""

        # print sys.argv[0]

    # ----------------------------------------------------------------------
    def clearp(self):
        """ 测试 这里是实现绘制 我哟的窗口关系"""
        self.sc.clab()
        self.sc.draw()

    # ----------------------------------------------------------------------
    def mbox(self, text):
        """ 这里是书写一个 纹理对话框"""
        self.meg = QMessageBox(self.frame_list)
        self.meg.setWindowTitle(u"对话框")
        self.meg.setText(text)
        self.meg.setIcon(QMessageBox.Information)
        self.meg.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    op = Data_S()

    # 下面测试ok 搞定 搞定
    # one = op.gettextdata()
    # new = read_obj.Get_xml_object("", read_obj.ONE)
    # outfilepath = "cc.xls"
    # new.data_write(outfilepath, read_obj.ONE , one )
    # op.config_gettextdata()
    op.show()
    sys.exit(app.exec_())








