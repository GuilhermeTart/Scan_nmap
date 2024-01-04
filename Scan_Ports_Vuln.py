#Criar letras em ASCII https://www.ascii-art-generator.org/



import subprocess

print(r"""
   ______      _ ____                                ___                          __      
  / ____/_  __(_) / /_  ___  _________ ___  ___     /   | __  ______ ___  _______/ /_____ 
 / / __/ / / / / / __ \/ _ \/ ___/ __ `__ \/ _ \   / /| |/ / / / __ `/ / / / ___/ __/ __ \
/ /_/ / /_/ / / / / / /  __/ /  / / / / / /  __/  / ___ / /_/ / /_/ / /_/ (__  ) /_/ /_/ /
\____/\__,_/_/_/_/ /_/\___/_/  /_/ /_/ /_/\___/  /_/  |_\__,_/\__, /\__,_/____/\__/\____/ 
                                                             /____/                       
                           _   __     __     _____                
                          / | / /__  / /_   / ___/_________ _____ 
                         /  |/ / _ \/ __/   \__ \/ ___/ __ `/ __ \
                        / /|  /  __/ /_    ___/ / /__/ /_/ / / / /
                       /_/ |_/\___/\__/   /____/\___/\__,_/_/ /_/ 
""")

# Essa linha define uma função chamada scan_network que recebe três parâmetros: network (endereço da rede a ser escaneada), ports (lista de portas a serem escaneadas) e protocols (lista de protocolos a serem usados).
def scan_network(network, ports, protocols):
    # Essa linha constrói o comando do Nmap que será executado no terminal. Ele inclui a opção -p seguida da primeira porta da lista ports, bem como outras opções como -sV (detecção de versão), -sC (execução de scripts padrão)
    command = f"nmap -p{ports[0]} -sV -sC  {network}" #Armazena o comando em "command" e formata com o "f"nmap" as strings das variáveis "port" e "network" e roda o comando -sV que detecta a versão do serviço e -Sc que roda os sctrips padrão do nmap

    if len(ports) > 1: #se o número de portas for maior que 1 significa que tem mais portas para o scan
        for port in ports[1:]: #Caso tenha mais de uma porta, ele gera uma sequência de consultas em outras portas.
            command += f" & nmap -p{port} -sV -sC {network}" #Usando essas funções no for
    Vulnerabilities = input("Deseja realizar um scan de vulnerabilidades? (y/n): ")
    if Vulnerabilities.lower() =="y": #Se a resposta for "y" ele irá acrescentar  --script vuln  junto ao command.  o comando .lower() transforma qualquer input do usuário em letra minúsculas. Se for n, não irá ter nenhum impacto no código
        command += " --script vuln"


    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True) #Cria um novo processo usando a função Popen() do módulo "subprocess" ele executa o comando na variável command. Já o comando "stdout=subprocess.PIPE" ele redireciona a saída para um objeto do tipo "PIPE" O "Shell=True" indica que o comando será usado em um Shell, isso é necessário para que o Shell interprete o comando.
    output, error = process.communicate() #O método "communicate ()" é chamado no objeto "process" que retorna uma dupla saída contendo uma saída do resultado e outra do erro. A vareável "output" Irá armazenar a saída do comando a partir do objeto "PIPE" E "error" é a variável que irá armazenar os erros caso tiver.

    # Imprime o resultado do scan essa linha armazena todas as saídas do scan
    print(output.decode())

# Inputs o método slip(",") é usado para dividir uma string em substrings separando por ",'
network = input("Digite o endereço da rede a ser escaneada (exemplo: 192.168.0.0/24): ")
ports = input("Digite as portas a serem escaneadas (exemplo: 80,443,8080): ").split(",")
protocols = input("Digite os protocolos a serem usados (exemplo: tcp,udp): ").split(",")

scan_network(network, ports, protocols)
