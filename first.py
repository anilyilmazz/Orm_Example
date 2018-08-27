from model import User,Session

session = Session()

#INSERT
deneme = User()
deneme.fullname = "deneme-full"
deneme.name = "deneme-name"
deneme.password = "deneme-password"
session.add(deneme)
session.commit()

#WHERE
users = session.query(User).filter(User.id==2).first()
users.name = "degistirdim"

#DELETE
users = session.query(User).filter(User.id == 2).first()
session.delete(users)
session.commit()


#SELECT
print(session.query(User).all())


session.close()