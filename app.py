from flask import Flask, Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bp = Blueprint('app', __name__)

user= 'nosjncww'
password= 'p8UBg9V0sxMKGWym1UAf03sHreI1SXUy'
host= 'tuffi.db.elephantsql.com'
database= 'nosjncww'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Jogos(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  plataforma = db.Column(db.String(60), nullable = False)
  titulo = db.Column(db.String(60), nullable = False)
  genero = db.Column(db.String(60), nullable = False)
  img = db.Column(db.String(120), nullable = False)

  def __init__(self, titulo, plataforma, genero, img):
    self.titulo = titulo
    self.plataforma = plataforma
    self.genero = genero
    self.img = img

  @staticmethod 
  def todos_playstation():
    # SELECT * from filmes order by id asc;
    #return Jogos.query.order_by(Jogos.id.asc()).all()
    return Jogos.query.where(Jogos.plataforma == "playstation") # vai selecionar somete da plataforma playstation

  @staticmethod 
  def todos_xbox():
    # SELECT * from filmes order by id asc;
    #return Jogos.query.order_by(Jogos.id.asc()).all()
    return Jogos.query.where(Jogos.plataforma == "xbox") # vai selecionar somete da plataforma playstation

  @staticmethod 
  def todos_switch():
    # SELECT * from filmes order by id asc;
    #return Jogos.query.order_by(Jogos.id.asc()).all()
    return Jogos.query.where(Jogos.plataforma == "switch") # vai selecionar somete da plataforma playstation






# essa é nossa rota home 
@bp.route('/')
def home():
    return render_template("index.html")


# quando entrar na rota do play ele chamar a função
@bp.route('/playstation')
def jogos_playstation():
  jogos = Jogos.todos_playstation() # aqui ela vai armazenar o retorno do metodo todos_playstationl que está dentro da class Jogos

  return render_template('todosJogos.html', listaJogos=jogos); # além de renderizar a o html especifico, ele tbm cria uma variavel para ser usadada no html(uma lista com os dados em questão)


# rota do xbox
@bp.route('/xbox')
def jogos_xbox():
  jogos = Jogos.todos_xbox() # aqui ela vai armazenar o retorno do metodo todos_xbox que está dentro da class Jogos

  return render_template('todosJogos.html', listaJogos=jogos); # além de renderizar a o html especifico, ele tbm cria uma variavel para ser usadada no html(uma lista com os dados em questão)


# roto do switch
@bp.route('/switch')
def jogos_switch():
  jogos = Jogos.todos_switch() # aqui ela vai armazenar o retorno do metodo todos_switch que está dentro da class Jogos

  return render_template('todosJogos.html', listaJogos=jogos); # além de renderizar a o html especifico, ele tbm cria uma variavel para ser usadada no html(uma lista com os dados em questão)








app.register_blueprint(bp)


if __name__ == "__main__":
    app.run(debug=True)