import subprocess






#Essa linha define uma função chamada scan_network que recebe três parâmetros: network (endereço da rede a ser escaneada), ports (lista de portas a serem escaneadas) e protocols (lista de protocolos a serem usados).
def scan_network(network, ports, protocols):

    # Essa linha define uma função chamada scan_network que recebe três parâmetros: network (endereço da rede a ser escaneada), ports (lista de portas a serem escaneadas) e protocols (lista de protocolos a serem usados).
    protocols_string = ",".join(protocols)

#Essa linha converte a lista protocols em uma string, unindo os elementos com uma vírgula. Isso é feito usando o método join().
    command = f"nmap -p{ports[0]} -sV -sC -Pn {network}"

    # Essa linha constrói o comando do Nmap que será executado no terminal. Ele inclui a opção -p seguida da primeira porta da lista ports, bem como outras opções como -sV (detecção de versão), -sC (execução de scripts padrão) e -Pn (ignorar a descoberta de hosts).
    if len(ports) > 1:
        for port in ports[1:]:
            command += f" & nmap -p{port} -sV -sC -Pn {network}"
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            output, error = process.communicate()

    # Imprime o resultado do scan
            print(output.decode())

# Exemplo de uso
network = input("Digite o endereço da rede a ser escaneada (exemplo: 192.168.0.0/24): ")
ports = input("Digite as portas a serem escaneadas (exemplo: 80,443,8080): ").split(",")
protocols = input("Digite os protocolos a serem usados (exemplo: tcp,udp): ").split(",")

scan_network(network, ports, protocols)
