#-*-coding:utf-8-*-

import pymysql

class MysqlUtils:

    @classmethod
    def initDB(self):
        # 打开数据库连接
        global db;
        db = pymysql.connect(host="123.207.227.103", port=3306, user="root", passwd="Mysql_123456", db="crawler");

    @classmethod
    def inserUrl(self,url,width,height):
        # 使用cursor()方法获取操作游标
        cursor = db.cursor();
        # SQL 插入语句
        sql = "INSERT INTO jiandan_url(url,width,height, create_time) VALUES ('"+url+"',"+str(width)+" ,"+str(height)+", NOW())";
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()

    @classmethod
    def isExsitByUrl(self,url):
        cursor = db.cursor();
        sql = "select count(*) from jiandan_url where url='"+url+"' ";
        cursor.execute(sql);
        result = cursor.fetchone()[0];
        if result >= 1:
            return True;
        else:
            return False;


    @classmethod
    def closeDB(self):
        # 关闭数据库连接
        db.close()


if __name__ == '__main__':
    MysqlUtils.initDB();
    url= "https://ws3.sinaimg.cn/large/006wUWIjgy1ftalns5zjhg30aq07o1ky.gif";
    print(MysqlUtils.isExsitByUrl(url));

    MysqlUtils.closeDB();
