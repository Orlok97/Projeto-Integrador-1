from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    telefone=db.Column(db.Integer)
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
    @staticmethod
    def create(bairro,rua,area,desc,user_id):
       
        coleta=Coleta(bairro=bairro,rua=rua,area=area,desc=desc,user_id=user_id)
        db.session.add(coleta)
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(f"erro ao criar : {e}")
            db.session.rollback() 
            return False
    @staticmethod
    def delete(id):
        coleta=Coleta().query.filter_by(id=id).first()
        coleta_id=coleta.id
        db.session.delete(coleta_id)
        db.session.commit()
        return True
    
class Arquivos(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    coleta_id=db.Column(db.Integer,db.ForeignKey('coleta.id'),nullable=False)

class Auth:
    def login(self,e,senha):
        usuario=Usuario.query.filter_by(email=e).first()
        if usuario.senha == senha:
            return True
        
