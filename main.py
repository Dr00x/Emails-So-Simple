import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, init

init(autoreset=True)

print(Fore.BLUE+"Utilize apenas gmail, este programa não é credenciado\n logo, para que ele possa acessar a conta é nescessario estar com\n a opção 'Acesso menos seguro ativada', aconselho utilisar uma conta de testes,\n Não me responsabilizo por nenhuma alteração feita no programa para cometer fraudes.\n")

port = "587"
hostGm = "smtp.gmail.com"

login = str(input('\nDigite o email de onde será enviado \n>:'))
senha = str(input('\nDigite a senha do email\n>:'))


server = smtplib.SMTP(hostGm, port)

server.ehlo()
server.starttls()
try:
    server.login(login,senha)
except:
    print(Fore.RED + "Login ou senha incorretor ou a opção indicada a cima não esta ativada, reinicie o programa")
    quit()


corpo = str(input("\nCorpo do email\n>:"))
msgEmail = MIMEMultipart()

msgEmail['From'] = login
msgEmail['To'] = str(input('\nDestinatário do email\n>:'))
msgEmail['Subject'] = str(input('\nAssunto do email\n>:'))
msgEmail.attach(MIMEText(corpo, 'plain'))

server.sendmail(msgEmail['From'],msgEmail['To'], msgEmail.as_string())
server.quit()   

#dr00x_
