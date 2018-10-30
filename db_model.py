from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
Base = declarative_base()

class User(Base):
     __tablename__ = 'users'

     id = Column("id",Integer, primary_key=True)
     name = Column("name",String)
     fullname = Column("fullname",String)
     password = Column("password",String)

     def __repr__(self):
        return "User(id='%s',name='%s', fullname='%s', password='%s')" % (
                             self.id,self.name, self.fullname, self.password)



engine = create_engine('sqlite:///test.db', echo=True )
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


