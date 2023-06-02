import pymysql
import pymysql.cursors
from .. import conf
from .logger import logger


class HandleMysql:
    def __init__(self):
        self.db = pymysql.Connect(host=conf.mysql["host"],
                                  user=conf.mysql["user"],
                                  password=conf.mysql["password"],
                                  database=conf.mysql["database"],
                                  charset="utf8",
                                  cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def get_data(self,sql,d_type=None,args=None):
        """查询数据库返回数据
        """
        try:
            self.cursor.execute(sql,args=args)
            self.db.commit()
            if d_type == "all":
                return self.cursor.fetchall()
            if isinstance(d_type,int):
                return self.cursor.fetchmany(d_type)
            else:
                return self.cursor.fetchone()
        except Exception as e:
            logger.error("数据库连接失败！！！%s"%e)

    def update_data(self,sql,args=None):
        """更改数据库数据
        """
        self.cursor.execute(sql,args=args)
        self.db.commit()

    def delete_data(self,sql,args=None):
        """删除数据库数据
        """
        pass

if __name__ == '__main__':
    do_mysql = HandleMysql()
    sql1 = 'SELECT * FROM t_user_order_service.order_base WHERE order_id="%s"' %12183933850
    sql2 = 'SELECT id FROM t_order_config_service.config_server_category where cn_name="灯具"'
    sql3 = 'SELECT parent_id,goods_id FROM t_order_config_service.goods where goods_name = "立柱式台灯"'
    r = do_mysql.get_data(sql1)
    print(r)