#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 访问数据库->使用SQLAlchemy(orm框架 处理表与对象之间的关系)
# 用法示例：

from sqlalchemy import Column, String,Integer,Float,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
class User(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20))
    password = Column(String(30))
    email = Column(String(40),unique=True)
    score = Column(Integer())

# 初始化数据库连接(echo=True打印操作信息):
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test',echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session=DBSession()
#查询数据
user=session.query(User).filter(User.id=='1').one()
#添加数据
u1=User(name='jack',password='dadd123',email='jack@email.com',score=32)
session.add(u1);
u2=User(name='rose',password='srt2123',email='rose@email.com',score=55)
session.add(u2)
u3=User(name='tom',password='t2hkj3',email='tom@email.com',score=11)
session.add(u3)
session.commit()
#删除用户
u=session.query(User).filter(User.id=='2').one()
session.delete(u)
session.commit()
#修改数据：获取一条数据对象，修改属性并提交即可
user=session.query(User).filter(User.id=='2').one()
user.score=99
session.commit();
session.close();