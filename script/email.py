import smtplib
import email.message

nome_re = input('Olá, qual é seu nome?')
remetente = input('Digite seu e-mail:')
senha = input('Digite sua senha ')
destinatario = input('Para quem deseja enviar esse email?')
nome_des = input('Qual é o nome dessa pessoa?')

def enviar():
    corpo = f'''
    <p>Olá {nome_des},  </p>
    <p>Estou enviando este e-mail para mostrar a minnha capacidade de </p>
    <p></p>
    <p></p>
    '''
