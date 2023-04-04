# 有不足之处在于只能实现一次检测，检测成功后需要关闭客户端和服务器端重新运行，才能开始新一轮的检测
from PyQt5 import QtCore, QtWidgets
import sys
from functools import partial
import numpy as np
import pymysql
import os
import time
import sys
import socket
import zmail


from window import Ui_MainWindow as main_ui 

class mainui(QtWidgets.QMainWindow, main_ui):
    def __init__(self):
        super(mainui, self).__init__()
        self.setupUi(self)

# 连接数据库
# db=pymysql.connect(host="localhost",user="root",password="411818hitwh",charset="utf8mb4") #这就是mysql和python的连接语言


# 点击“查询”按钮触发该函数
def show(ui,photo_id):
    # 清空
    ui.listWidget.clear()
    ui.listWidget_2.clear()
    ui.listWidget_3.clear()
    ui.listWidget_4.clear()
    db=pymysql.connect(host="localhost",user="root",password="411818hitwh",charset="utf8mb4") #这就是mysql和python的连接语言
    # 转换一步
    a=str(photo_id)
    print(a)

    sql1="""
    USE embedding;
    """

    sql2="""
    select name
    from infor
    where photo=%s;
    """

    sql3="""
    select gender
    from infor
    where photo=%s;
    """

    sql4="""
    select age
    from infor
    where photo=%s;
    """

    cursor=db.cursor()
    db.ping(reconnect=True)
    cursor.execute(sql1)
    
    cursor.execute(sql2,[a])
    all_db=cursor.fetchall()#输出所有内容
    if(all_db):
        for i in all_db:
            #print(i)
            ui.listWidget.addItem(str(i).replace("(","").replace(",","").replace(")","").replace("'",""))
    
    cursor.execute(sql3,[a])
    all_db=cursor.fetchall()#输出所有内容
    if(all_db):
        for i in all_db:
            #print(i)
            ui.listWidget_2.addItem(str(i).replace("(","").replace(",","").replace(")","").replace("'",""))
    
    cursor.execute(sql4,[a])
    all_db=cursor.fetchall()#输出所有内容
    if(all_db):
        for i in all_db:
            #print(i)
            ui.listWidget_3.addItem(str(i).replace("(","").replace(",","").replace(")","").replace("'",""))

    db.commit()
    cursor.close()
    print("hello")
    db.close()




if __name__ == '__main__':    
    app = QtWidgets.QApplication(sys.argv)
    a = mainui()
    a.show()
    
    server=zmail.server('miner_song_kall@163.com','HRYDRGKQUWYXREJE')
    latest_mail=server.get_latest()
    zmail.show(latest_mail)
    print(latest_mail.get('Content_text'))
    temp=str(latest_mail.get('Content_text')).replace("['","").replace("']","")
    print(temp)

    # #创建套接字
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # #绑定ip，port
    # sock.bind((HOST, PORT)) #绑定端口，告诉别人，这个端口我使用了，其他人别用了
    # # 启动被动连接
    # #多少个客户端可以连接
    # sock.listen(5)  #监听这个端口，可连接最多5个设备  
    # #使用socket创建的套接字默认的属性是主动的
    # #使用listen将其变为被动的，这样就可以接收别人的链接了
    # # 创建接收
    # # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
    # buf=''
    # while True:  #死循环，服务器端一直提供服务。
    #     print("sssssssssssssssssssssssssssssssssssssssssss")
    #     connection,address = sock.accept() #接收客户端的连接请求
    #     print(address)
    #     try:
    #         connection.settimeout(10)  #设置10s时限
    #         buf = connection.recv(1024)#接收数据实例化
    #         print("接收的数据：",buf.decode("utf-8"))
    #         buf=buf.decode("utf-8")
    #         if buf:  #接收成功
    #             connection.send(b'welcome to server!')  #发送消息，b表示bytes类型
    #             print('Connection success!')
    #             # 连接成功，退出
    #             break
    #         else:  #接收失败
    #             connection.send(b'Please go out!')
    #     except socket.timeout:  #超时
    #         print('time out!')
    #     connection.close()  #关闭连接
    

    a.listWidget_4.addItem(str(temp))
    a.pushButton.clicked.connect(partial(show,a,str(temp)))  

    sys.exit(app.exec_())