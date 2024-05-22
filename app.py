from flask import Flask
from flask_mail import Mail, Message
from flask import redirect, url_for, render_template, request ,jsonify
from controllers import *
from models import db, Coleta

UPLOAD_FOLDER = '/upload/coleta'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__,template_folder='views',static_folder='static')
app.secret_key='123456789'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/PI'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'prefeiturasv2024@gmail.com'
app.config['MAIL_PASSWORD'] = 'bpkd xxmm nqqw vbgq '
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

db.init_app(app)
mail = Mail(app)

with app.app_context():
    db.create_all()
 
@app.route('/',methods=['GET','POST'])
def index():
    return LoginController().index()


@app.route('/admin-login',methods=['GET','POST'])
def admin():
    return AdminController().index()

@app.route('/admin/home',methods=['GET','POST'])
def admin_home():
    return AdminController().home()

@app.route('/admin/logout',methods=['GET'])
def admin_logout():
    return AdminController().logout()


@app.route('/usuarios',methods=['GET'])
def users():
    return AdminController().getUsuarios()

@app.route('/coletas',methods=['GET','POST'])
def coleta():
    return AdminController().getSolicitacoes()
    
@app.route('/cadastro',methods=['GET','POST'])
def cadastro():
    return CadastroController().index()

@app.route('/home',methods=['GET','POST'])
def home():
    return HomeController().index()
@app.route('/minha-conta',methods=['GET','POST'])
def conta():
    return render_template('conta.html')
  
@app.route('/logout')   
def logout():
    return HomeController().logout()

@app.route('/enviar-email/<int:id>')
def email(id):
    try:
        usuario=Usuario().auth(session['email'])
        coleta=Coleta().query.filter_by(id=id).first()
        foto=Arquivos()
        foto_nome=foto.query.filter_by(coleta_id=id).first()
        msg = Message("Coleta Solicitada",
                  sender='noreply@gmail.com',
                  recipients=["prefeiturasv2024@gmail.com"])
        
        msg.html=render_template('email.html',coleta=coleta,usuario=usuario,foto=foto,foto_nome=foto_nome)
        mail.send(msg)
        coleta.status='confirmado'
        db.session.commit()
        flash('solicitação confirmada com sucesso!','green lighten-1')
        return redirect((url_for('home')))

    except Exception as e:
        return str(e)
@app.route('/delete/<int:id>')
def delete(id):
    try:
        Coleta.delete(id)
        flash('solicitação cancelada','green lighten-1')
        return redirect(url_for('home'))
    except Exception as e:
        return str(e)

@app.route('/update/<int:id>',methods=['POST'])
def update(id):
    if request.method=='POST':
        bairro=request.form.get('bairro')
        rua=request.form.get('rua')
        area=request.form.get('area')
        desc=request.form.get('desc')
        try:
            files = request.files.getlist('file2')
            for f in files:
                if f.filename != '':
                    f.save('static/upload/coleta/'+f.filename)
                arquivo=Arquivos.query.filter_by(coleta_id=id).first()
                if arquivo:
                    if f.filename != '':
                        Arquivos.update(id,f.filename)
                    elif f.filename == '':
                        Arquivos.update(id,arquivo.filename)
                else:
                    Arquivos.create(id,f.filename)
                Coleta.update(id,bairro,rua,area,desc)
            flash('Dados Alterados','green lighten-1')
            return redirect(url_for('home'))
        except Exception as e:
            return str(e)
        
if __name__ == '__main__':
    app.run(debug=True)