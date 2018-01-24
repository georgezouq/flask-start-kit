import pandas as pd
import pymysql
import json


from .config import config


class DBUtil():
    @staticmethod
    def test():
        # print(Conf.SQLALCHEMY_DATABASE_URI)
        return config.SQLALCHEMY_DATABASE_URI

    # db_utils
    @staticmethod
    def get_mysql_engine(type=1):
        mysql_user = config.MYSQL_USER
        mysql_pwd = config.MYSQL_PWD
        mysql_host = config.MYSQL_HOST
        mysql_port = config.MYSQL_PORT
        mysql_db = config.MYSQL_DB

        mysql_uri = config.SQLALCHEMY_DATABASE_URI

        if type == 1:
            # pymysql
            return pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, passwd=mysql_pwd, db=mysql_db, charset='utf8')
        elif type == 2:
            # sqlalchemy
            # mysql_uri = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (
            #     mysql_user, mysql_pwd, mysql_host, mysql_port, mysql_db)
            # 将数据写入mysql的数据库，但需要先通过sqlalchemy.create_engine建立连接,且字符编码设置为utf8，否则有些latin字符不能处理
            return create_engine(mysql_uri)
        else:
            return -1

    # pymysql
    @staticmethod
    def get_mysql_conn():
        return DBUtil.get_mysql_engine(1)

    # 把DataFrame数据写入数据库
    # df DataFrame
    # tb_name 表名
    # conn sqlalchemy引擎
    @staticmethod
    def pd_to_sql(df, tb_name):
        conn = DBUtil.get_mysql_engine(2)
        return pd.io.sql.to_sql(df, tb_name, conn, if_exists='append',
                                index=False, chunksize=10000)

    @staticmethod
    def read_sql_pd(sql):
        conn = DBUtil.get_mysql_engine(1)
        return pd.read_sql(sql, conn)

    @staticmethod
    def read_sql_json_one(sql):
        df = DBUtil.read_sql_pd(sql)
        if df.empty:
            return({})
        r = df.iloc[0].to_json()
        return json.loads(r, encoding='utf8')

    @staticmethod
    def read_sql_json(sql):
        df = DBUtil.read_sql_pd(sql)
        r = df.to_json(orient='records', force_ascii=False)
        return json.loads(r, encoding='utf8')
