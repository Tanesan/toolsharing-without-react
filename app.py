from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
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
  lista = {"title":"あああ","author":"aaaaa","time":1602509578,"blocks":[{"type":"code","data":{"text":"<p>dsadasasddasas</p>"}},{"type":"text","data":{"text":" # ewewqqwe \n"}},{"type":"text","data":{"text":" ## ewewqqwe \n"}},{"type":"text","data":{"text":" ### ewewqqwe \n"}},{"type":"text","data":{"text":" #### ewewqqwe \n"}},{"type":"text","data":{"text":" ##### ewewqqwe \n"}},{"type":"text","data":{"text":" ###### ewewqqwe \n"}},{"type":"code","data":{"text":"<p>dsadasasddasas</p>"}}],"tag":"aaa"}
  num_range = len(lista["blocks"])
  return render_template('article.html',lista = lista, num_range = num_range)

if __name__ == '__main__':
  app.run(debug=True)