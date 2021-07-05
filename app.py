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


  @staticmethod
  def read_single(jogo_id):
    # SELECT * from filmes where id = <id_de_um_filme>;
    return Jogos.query.get(jogo_id)
  

  # insere jogo
  def save(self):
    db.session.add(self) # estamos adicionandno as informações passadas no fomr (nome, url) para o banco de dados(utilizando sessão)
    db.session.commit()

  def update(self, new_data):
    self.titulo = new_data.titulo
    self.plataforma = new_data.plataforma
    self.genero = new_data.genero
    self.img = new_data.img
    self.save()


  



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




# rota de update
@bp.route('/updateJogo', methods=('GET', 'POST'))
def update():
  sucesso = None
  jogo = Jogos.read_single(1) # aqui n pode ser um, tem q arrumar alguma forma para o usuario conseguir selecionar o jogo q ele quer editar

  if request.method == 'POST':
    form = request.form
    new_data = Jogos(form['titulo'], form['plataforma'], form['genero'], form['img'])
    
    jogo.update(new_data)

    sucesso = True

  return render_template('updateJogo.html', jogo = jogo, sucesso = sucesso ) 

    









app.register_blueprint(bp)


if __name__ == "__main__":
    app.run(debug=True)