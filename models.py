from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Usuario(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    telefone=db.Column(db.String(120),nullable=False)
    senha=db.Column(db.String(120),nullable=False)

    @staticmethod
    def create(nome,email,telefone,senha):
        usuario=Usuario(nome=nome,email=email,telefone=telefone,senha=senha)
        db.session.add(usuario)
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(f"erro ao criar : {e}")
            db.session.rollback()
            return False
    @staticmethod
    def isTaken(email):
        usuario=Usuario.query.filter_by(email=email).first()
        if usuario:
            return True
    @staticmethod
    def auth(email):
        usuario=Usuario.query.filter_by(email=email).first()
        if usuario:
            return usuario

class Coleta(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    bairro=db.Column(db.String(120),nullable=False)
    rua=db.Column(db.String(120),nullable=False)
    area=db.Column(db.String(120),nullable=False)
    desc=db.Column(db.String(120),nullable=True)
    status=db.Column(db.String(120),default='pendente')
    user_id=db.Column(db.Integer,db.ForeignKey('usuario.id'),nullable=False)
    arquivos=db.relationship('Arquivos',backref='parent',cascade='all,delete-orphan')
    data=db.Column(db.Date)
    hora=db.Column(db.Time)
    
    @staticmethod
    def create(bairro,rua,area,desc,user_id):
        data_atual=datetime.now()
        data_formatada=data_atual.strftime('%Y/%m/%d')
        hora_formatada=data_atual.strftime('%H:%M:%S')
        coleta=Coleta(bairro=bairro,rua=rua,area=area,desc=desc,user_id=user_id,data=data_formatada,hora=hora_formatada)
        db.session.add(coleta)
        try:
            db.session.commit()
            return coleta
        except Exception as e:
            print(f"erro ao criar : {e}")
            db.session.rollback() 
            return False

    @staticmethod
    def update(id,bairro,rua,area,desc):
        coleta=Coleta.query.get(id)
        if coleta:
            coleta.bairro=bairro
            coleta.rua=rua
            coleta.area=area
            coleta.desc=desc
            db.session.commit()
            print('dados alterados')
            
    @staticmethod
    def delete(id):
        coleta=Coleta.query.get(id)
        db.session.delete(coleta)
        db.session.commit()
        return 'ok'
    
class Arquivos(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    coleta_id=db.Column(db.Integer,db.ForeignKey('coleta.id'),nullable=False)
    filename=db.Column(db.String(120),nullable=False)

    @staticmethod
    def create(id,filename):
        arquivo=Arquivos(coleta_id=id,filename=filename)
        db.session.add(arquivo)
        try:
            db.session.commit()
            return arquivo
        except Exception as e:
            print(f"erro ao criar : {e}")
            db.session.rollback() 
            return False
            
    @staticmethod
    def update(id,filename):
        arquivo=Arquivos.query.filter_by(coleta_id=id).first()
        if arquivo:
            arquivo.filename=filename
            db.session.commit()
            print('nome do arquivo alterado')
        else:
            print('erro ao mudar o arquivo')


class Auth:
    def login(self,e,senha):
        usuario=Usuario.query.filter_by(email=e).first()
        if usuario.senha == senha:
            return True
        
