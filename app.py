from flask import Flask, Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bp = Blueprint('app', __name__)

user= 'fnmuduqr'
password= 'nNTHlOm-oPbeZKy71sw0mS2Sj_suCD52'
host= 'tuffi.db.elephantsql.com'
database= 'fnmuduqr'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Jogos(db.Model):
  jogo_id = db.Column(db.Integer, primary_key = True)
  plataforma = db.Column(db.String(255), nullable = False)
  nome_jogo = db.Column(db.String(255), nullable = False)
  genero = db.Column(db.String(255), nullable = False)
  imagem_url = db.Column(db.String(255), nullable = False)

  def __init__(self, nome_jogo, plataforma, genero, imagem_url):
    self.nome_jogo = nome_jogo
    self.plataforma = plataforma
    self.genero = genero
    self.imagem_url = imagem_url

  @staticmethod 
  def todos_playstation():
    # SELECT * from filmes order by id asc;
    #return Jogos.query.order_by(Jogos.id.asc()).all()
    #return Jogos.query.where(Jogos.plataforma == "Playstation")
    return Jogos.query.where(Jogos.plataforma.in_(["Playstation",''])) # vai selecionar somete da plataforma playstation

  @staticmethod 
  def todos_xbox():
    # SELECT * from filmes order by id asc;
    #return Jogos.query.order_by(Jogos.id.asc()).all()
    return Jogos.query.where(Jogos.plataforma.in_(['', 'Xbox'])) # vai selecionar somete da plataforma playstation

  @staticmethod 
  def todos_switch():
    # SELECT * from filmes order by id asc;
    #return Jogos.query.order_by(Jogos.id.asc()).all()
    return Jogos.query.where(Jogos.plataforma.in_(['', 'Nintendo Switch'])) # vai selecionar somete da plataforma playstation


  @staticmethod
  def read_single(jogo_id):
    # SELECT * from filmes where id = <id_de_um_filme>;
    return Jogos.query.get(jogo_id)
  

  # insere jogo
  def save(self):
    db.session.add(self) # estamos adicionandno as informações passadas no fomr (nome, url) para o banco de dados(utilizando sessão)
    db.session.commit()

  def update(self, new_data):
    self.nome_jogo = new_data.nome_jogo
    self.plataforma = new_data.plataforma
    self.genero = new_data.genero
    self.imagem_url = new_data.imagem_url
    self.save()

  def delete(self):
    db.session.delete(self) # estamos removendo as infomações de um jogo do banco de dados
    db.session.commit()

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

@bp.route('/devs')
def devs():
  return render_template("devs.html")

# rota de update
@bp.route('/updateJogo/<jogo_id>', methods=('GET', 'POST'))
def update(jogo_id):
  sucesso = None
  jogo = Jogos.read_single(jogo_id) # aqui n pode ser um, tem q arrumar alguma forma para o usuario conseguir selecionar o jogo q ele quer editar

  if request.method == 'POST':
    form = request.form
    new_data = Jogos(form['nome_jogo'], form['plataforma'], form['genero'], form['imagem_url'])
    
    jogo.update(new_data)

    sucesso = True
  return render_template('updateJogo.html', jogo = jogo, sucesso = sucesso ) 

#rota do delete (deletar)

@bp.route('/deleteJogo/<jogo_id>') # rota que realiza de fato a deleção do jogo selecionado e mostra o html de sucesso
def delete_confirmed(jogo_id):

  jogo = Jogos.read_single(jogo_id)

  if jogo:
    jogo.delete()
  
  return render_template('index.html')

@bp.route('/create', methods=('GET', 'POST'))
def create():
    id_atribuido = None
#Como o método utilizado no formulário é POST, pegamos os valores dos campos
    if request.method == 'POST':
        form = request.form
        jogo = Jogos(form['nome_jogo'], form['plataforma'], form['genero'], form['imagem_url'])

        jogo.save()

        #id_atribuido = jogo.id
    return render_template('create.html')




@bp.route('/desenvolvedores')
def dev():
  return render_template('devs.html')




app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)