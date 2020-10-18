# -*- coding: utf-8 -*-
# モジュールインポート
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# flaks-loginのライブラリ追加
from flask_login import LoginManager, login_required

app = Flask(__name__)
# ここから /// データベースの設定
app.secret_key = "dwd3893hrf03h48-0f7y8h3f4fgh8vbkdier4u58fkdu"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qa-site.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ここまで /// データベースの設定

# sqlalchemyを通してflaskからdbアクセスをするための入り口
db = SQLAlchemy(app)

# flask-loginに関する設定
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


# これを上に書くと未定義のままdbがいったりきたりするので上に書いてはいけない
from app.user_config import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
 
# authに関するルーティングを追加
from app.auth_view.auth import auth
 
# authに関するルートをflaskアプリであるappに追加
app.register_blueprint(auth)
 
 

@app.route('/')
@login_required
def index():
  return render_template('index.html')

@app.route('/post')
def post():
  return render_template('post.html')

@app.route('/a')
def a():
  return render_template('a.html')


@app.route('/article')
def article():
  lista = {"title":"あああ","author":"aaaaa","time":1602509578,"blocks":[{"type":"code","data":{"text":"<p>dsadasasddasas</p>"}},{"type":"text","data":{"text":" # ewewqqwe \n"}},{"type":"text","data":{"text":" ## ewewqqwe \n"}},{"type":"text","data":{"text":" ### ewewqqwe \n"}},{"type":"text","data":{"text":" #### ewewqqwe \n"}},{"type":"text","data":{"text":" ##### ewewqqwe \n"}},{"type":"text","data":{"text":" ###### ewewqqwe \n"}},{"type":"code","data":{"text":"<p>dsadasasddasas</p>"}},{"type":"code","data":{"text":"<p>dsadasasddasas</p>"}},{"type":"code","data":{"text":"<p>dsadasasddasas</p>"}},{"type":"code","data":{"text":"<p>dsadasasddasas</p>"}},{"type":"code","data":{"text":"<p>dsadasasddasas</p>"}},{"type":"code","data":{"text":"<p>dsadasasddasas</p>"}}],"tag":"aaa"}
  num_range = len(lista["blocks"])
  return render_template('article.html',lista = lista, num_range = num_range)