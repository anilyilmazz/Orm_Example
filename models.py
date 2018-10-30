from db_model import User,Session

class UserInfo:
    def __init__(self,name,fullname,password):
        self.name = name
        self.fullname = fullname
        self.password = password
        session = Session()
