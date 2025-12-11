from sqlalchemy import String,Integer,Column, DateTime, ForeignKey
from .database import base
from datetime import datetime

class User(base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    email=Column(String,unique=True)
    password=Column(String)
    elo=Column(Integer,default=1000)



class Debate(base):
    __tablename__="debate"

    id=Column(Integer ,primary_key=True,index=True)
    topic=Column(String ,nullable=False)
    user_id_a =Column(Integer,ForeignKey("users.id"))
    user_id_b =Column(Integer,ForeignKey("users.id"))
    winner_id =Column(Integer,ForeignKey("users.id"),nullable=True )

    created_at = Column(DateTime, default=datetime.utcnow)
    