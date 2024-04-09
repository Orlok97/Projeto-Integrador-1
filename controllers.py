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
                    if(self.create(nome,email,telefone,senha)):
                        flash('usuario cadastrado com sucesso!','green lighten-1')
                    else:
                        flash('erro ao cadastrar!','red lighten-2')
        return render_template('cadastro.html')
    def create(self,nome,email,telefone,senha):
        try:
            Usuario().create(nome,email,telefone,senha)
            print('usuario cadastrado com sucesso!')
            return True
        except Exception as e:
            print('um erro ocorreu: ',e)
            
class HomeController:
    def index(self):
        if not 'email' in session:
            return redirect(url_for('index'))
        else:
            if request.method == 'POST':
                cidade=request.form.get('cidade')
                bairro=request.form.get('bairro')
                rua=request.form.get('rua')
                desc=request.form.get('desc')
                user=Usuario().auth(session['email'])
                if cidade=='' or bairro=='' or rua=='':
                    flash('os campos nao podem ficar vazio','amber accent-2')
                else:
                    if self.create(cidade,bairro,rua,desc,user.id):
                        flash('coleta solicitada com sucesso!','green lighten-1')
                    else:
                        flash('erro ao solicitar o serviço','red lighten-2')
            user=Usuario().auth(session['email'])
            user_id=user.id
            coletas=Coleta().query.filter_by(user_id=user_id)
            return render_template('home.html',user=user,coletas=coletas)
    def create(self,cidade,bairro,rua,desc,user_id):
        try:
            Coleta().create(cidade,bairro,rua,desc,user_id)
            print('solicitaçao feita com sucesso!')
            return True
        except Exception as e:
            print('erro: ',e)

    def logout(self):
        session.pop('email',None)
        return redirect(url_for('index'))
        
class ColetaController:
    def index(self,id):
        coleta=Coleta().query.filter_by(id=id).first()
        return render_template('coletas.html',id=id,coleta=coleta)
    
         