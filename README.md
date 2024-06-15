# Network Reset Script
>Este script em Python redefine as configurações de rede e reinicia o computador. Ele requer privilégios de administrador para ser executado.

## Funcionalidades
O script executa as seguintes operações de redefinição de rede:


### Redefinição das configurações de IP:
````
subprocess.run(["netsh", "int", "ip", "reset"], shell=True
````

### Redefinição das configurações de TCP:
````
subprocess.run(["netsh", "int", "tcp", "reset"], shell=True)
````

### Redefinição das configurações do Winsock:
````
subprocess.run(["netsh", "winsock", "reset"], shell=True)
````

### Limpeza do cache DNS:
````
subprocess.run(["ipconfig", "/flushdns"], shell=True)
````
### Registro do DNS
````
subprocess.run(["ipconfig", "/registerdns"], shell=True)
````

### Liberação do endereço IP
````
subprocess.run(["ipconfig", "/release"], shell=True)
````
### Renovação do endereço IP:
````
subprocess.run(["ipconfig", "/renew"], shell=True)
````
>Após realizar todas essas operações, o script reinicia o computador para aplicar as alterações.

## Executar o Script

### Abra o Prompt de Comando ou o PowerShell e execute o seguinte comando:
````
python Madame_Web.py
````
## Contribuições
### Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

