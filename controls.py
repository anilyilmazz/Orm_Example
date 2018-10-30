import flask
import json
from db_model import User,Session
import api_tools
app = flask.Flask(__name__)


@app.route("/")
def index():
    session = Session()
    all_users = session.query(User).all()
    session.close()
    return flask.render_template("index.html" , users = all_users)

@app.route("/register/",methods=['GET'])
def register():
    return flask.render_template("register.html")

@app.route("/register/",methods=['POST'])
def create_user():
    session = Session()
    new_user = User()
    new_user.fullname = flask.request.form["fullname"]
    new_user.name = flask.request.form["name"]
    new_user.password = flask.request.form["password"]
    session.add(new_user)
    session.commit()
    session.close()

    return flask.render_template("register.html",name = "completed")

@app.route("/login",methods=['GET'])
def login():
    return flask.render_template("login.html")

@app.route("/login",methods=['POST'])
def login_auth():

    username = flask.request.form["username"]
    password = flask.request.form["password"]
    session = Session()
    users = session.query(User).filter(User.name == username).first()
    if users is None:
        log = "kullanıcı bulunamadı"
    else :
        if users.password == password:
            log ="Giriş Yaptınız"
        else :
            log = "Kullanıcı Adı ve ya Şifre Yanlış"
    session.close()
    return flask.render_template("login.html",log=log)



@app.route("/users",methods = ['GET','POST'])
def users_json():
    if flask.request.args.get('api_key')=='123':
        session = Session()
        all_users = session.query(User).all()
        session.close()
        liste = []
        for i in all_users:
                liste.append({
                'id' : i.id,
                'isim' : i.name,
                'FullName': i.fullname,
                'Password' : api_tools.md5_converter(i.password)
            })
        return flask.jsonify(liste)
    else:
        return flask.abort(404)


if __name__ == '__main__':
    app.run(debug=True)
