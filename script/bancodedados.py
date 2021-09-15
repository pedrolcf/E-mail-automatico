import mysql.connector 
usuario = input('Usuário do MySQL:')
senha = input('Senha MySQL:')
con = mysql.connector.connect(host = 'localhost' , database = 'cadastro' , user = usuario , password  = senha)
#isso serve para conectar com o mysql

if con.is_connected():
    db_info = con.get_server_info()
    print(f'está conectado ao Servidor MySQL versão {db_info}')
#isso serve para mostrar informações no mysql
