import xlrd
import xlwt
import csv
import pandas as pd
import os
from .HandleMysql import HandleMysql

class HandleExcel:
    def __init__(self):
        curPath = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        self.filePath = curPath + '/data/phone.csv'

    def get_data(self,filePath=None):
        """
        读取csv文件
        :param filePath:
        :return:
        """
        data = []
        if filePath is None:
            with open(self.filePath,'r') as f:
                reader = csv.reader(f)
                reader.__next__()
                for row in reader:
                    for i in row:
                        data.append(i)
        else:
            with open(filePath,'r') as f:
                reader = csv.reader(f)
                reader.__next__()
                for row in reader:
                    for i in row:
                        data.append(i)
        return data


    def write_phone(self,phone):
        """
        给csv写入数据,入参为列表，数据为字典，例：[{'phone': '13861328159'}]
        """
        with open(self.filePath,'w',newline="") as f:
            fieldnames = ["phone"]
            f_writer = csv.DictWriter(f,fieldnames=fieldnames)
            f_writer.writeheader()
            f_writer.writerows(phone)


    # def write_data(self,file,column_name,orderId):
    #     with open(file,'w',newline="") as f:
    #         f_writer = csv.writer(f)
    #         f_writer.writerow(column_name)
    #         f_writer.writerows(orderId)




if __name__ == '__main__':
    h = HandleExcel()
    # m = HandleMysql()
    # order_no = "P5176871240"
    # sql2 = 'SELECT t1.phone from t_master_order_service.order_push t2 JOIN t_master_information_service.master_info t1 WHERE t1.master_id = t2.master_id AND t2.order_id IN ( SELECT order_id FROM t_master_order_service.order_base WHERE order_no = "%s" AND t1.master_source = "apps" );' %order_no
    # phone = m.get_data(sql2,50)
    # h.write_data(phone)

    # phone = [[12184402080], [12184400683]]
    # path = "D:\wsf\github\wsfAutoTest\data\orderId.csv"
    # h.write_data2(path,['1645645465','19468456456'])

    # h.write_data(path,["orderId"],phone)

    # h.write_data('17688968877')

    p = h.get_data("D:\wsf\github\wsfAutoTest\data\orderId.csv")
    print(p)




   

