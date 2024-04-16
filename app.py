from flask import Flask
from flask_mail import Mail, Message
from flask import redirect, url_for, render_template
from controllers import *
from models import db, Coleta


app = Flask(__name__,template_folder='views',static_folder='static')
app.secret_key='123456789'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/PI'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'ec456cb0a7ba69'
app.config['MAIL_PASSWORD'] = '8c680bc93c2edb'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db.init_app(app)
mail = Mail(app)

with app.app_context():
    db.create_all()
 
@app.route('/',methods=['GET','POST'])
def index():
    return LoginController().index()

@app.route('/cadastro',methods=['GET','POST'])
def cadastro():
    return CadastroController().index()

@app.route('/home',methods=['GET','POST'])
def home():
    return HomeController().index()
  
@app.route('/logout')   
def logout():
    return HomeController().logout()

@app.route('/enviar-email/<int:id>')
def email(id):
    try:
        usuario=Usuario().auth(session['email'])
        coleta=Coleta().query.filter_by(id=id).first()
        msg = Message("Coleta Solicitada",
                  sender="from@gmail.com",
                  recipients=["test@example.com"])
        
        msg.html=render_template('email.html',coleta=coleta,usuario=usuario)
        mail.send(msg)
        coleta.status='confirmado'
        db.session.commit()
        flash('solicitação confirmada com sucesso!','green lighten-1')
        return redirect((url_for('home')))

    except Exception as e:
        return str(e)
@app.route('/delete/<int:id>')
def delete(id):
    return HomeController().delete(id)
if __name__ == '__main__':
    app.run(debug=True)