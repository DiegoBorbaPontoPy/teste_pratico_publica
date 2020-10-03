from flask import Flask, render_template, request, redirect, session, flash, url_for
#render template: passando o nome do modelo e a variáveis ele vai renderizar o template
#request: faz as requisições da nosa aplicação
#redirect: redireciona pra outras páginas
#session: armazena informações do usuário
#flash:mensagem de alerta exibida na tela
#url_for: vai para aonde o redirect indica

app = Flask(__name__)
app.secret_key = 'flask'
#chave secreta da sessão
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#Configuração de cache

#Função que processa as estatísticas da temporada a partir do placar
#Parâmetros: Placar do jogo atual, e estatisticas do placar anterior
def adicionar_jogo(placar:int,lista:list):
    numero = lista[0]+1
    
    #Definindo se o maximo foi batido com um if simples usando a lista
    if placar < lista[2]:
        minimo = placar
        minimo_batido = lista[4]+1
    else:
        minimo = lista[2]
        minimo_batido = lista[4]
    
    #Definindo se o mínimo foi batido com mais um if utilizando a lista
    if placar > lista[3]:
        maximo = placar
        maximo_batido = lista[5]+1
    else:
        maximo = lista[3]
        maximo_batido = lista[5]

    return [numero,placar,minimo,maximo,minimo_batido,maximo_batido]

#Lista dos placares e estatísticas  
lista = [
    [1,12,12,12,0,0],
    [2,24,12,24,0,1],
    [3,10,10,24,1,1],
    [4,24,10,24,1,1]
        ]

#configuração da rota index.
@app.route('/')
def index():
    return render_template('lista.html', titulo='Lista de Jogos', lista=lista)
    #renderizando o template lista e as variáveis desejadas. 

#configuração da rota novo
@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')
        #renderiza o template novo
    
#configuração da rpta criar que usa o método post para enviar dados do novo placar
@app.route('/criar', methods=['POST',])
def criar():
    x = request. form['nome']
    x = int(x)
    lista.append(adicionar_jogo(x,lista[len(lista)-1]))
    return redirect(url_for('index'))
#já inclui o novo placar na lista da tela inicial

#"Roda" o web-app
app.run(debug=True)
