import smtplib
import email.message

nome_re = input('Olá, qual é seu nome?')
remetente = input('Digite seu e-mail:')
senha = input('Digite sua senha ')
destinatario = input('Para quem deseja enviar esse email?')
nome_des = input('Qual é o nome dessa pessoa?')
assunto = input('Qual é o assunto desse e-mail?')

def enviar():
    corpo = f''' 
    <p>Olá {destinatario},</p>
    <p>Estou enviando este e-mail para mostrar a minnha capacidade de automatizar tarefas.</p>
    <p>Atenciosamente,</p>
    <p> {remetente}</p>'''

    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario
    password = senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('Pronto')