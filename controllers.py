from flask import render_template, request, url_for
from flask import redirect , session, flash
from models import *

class LoginController:
    def index(self):
        if request.method=='POST':
            email=request.form.get('email')
            senha=request.form.get('senha')
            if email == '' or senha == '':
                flash('os campos devem ser preenchidos!')
            else:
                if self.auth(email,senha):
                    session['email']=email
                    return redirect(url_for('home'))
                else:
                    flash('email ou senha incorretos')
        return render_template('login.html')
    def auth(self,email,senha):
        try:
            if Auth().login(email,senha):
                return True
        except Exception as e:
            print('error >> ',e)

class CadastroController:
    def index(self):
        if request.method=='POST':
            nome=request.form.get('nome')
            email=request.form.get('email')
            telefone=request.form.get('telefone')
            senha=request.form.get('senha')
            if nome == '' or email == '' or telefone == '' or senha == '':
                flash('os campos nao podem ficar vazio!','amber accent-2')
            else:
                if Usuario().isTaken(email):
                    flash('esse endereço de email ja foi cadastrado!','amber accent-2')
                else:
                    try:
                        if Usuario().create(nome,email,telefone,senha):
                            flash('usuario cadastrado com sucesso!','green lighten-1')
                        else:
                            flash('erro ao cadastrar!','red lighten-2')
                    except Exception as err:
                        return str(err)
        return render_template('cadastro.html')
            
class HomeController:
    def index(self):
        if not 'email' in session:
            return redirect(url_for('index'))
        else:
            if request.method == 'POST':
                user=Usuario().auth(session['email'])
                user_id=user.id
                bairro=request.form.get('bairro')
                rua=request.form.get('rua')
                area=request.form.get('area')
                desc=request.form.get('desc')
                if area=='' or bairro=='' or rua=='':
                    flash('os campos nao podem ficar vazio','amber accent-2')
                else:
                    try:
                        if Coleta().create(bairro,rua,area,desc,user_id):
                            flash('coleta solicitada com sucesso!','green lighten-1')
                        else:
                            flash('erro ao solicitar o serviço','red lighten-2')
                    except Exception as e:
                        return str(e)
            user=Usuario().auth(session['email'])
            user_id=user.id
            coletas=Coleta().query.filter_by(user_id=user_id)
            return render_template('home.html',user=user,coletas=coletas)
    
         
    def logout(self):
        session.pop('email',None)
        return redirect(url_for('index'))