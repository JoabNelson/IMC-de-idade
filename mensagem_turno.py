"""
Você foi contrato para criar um menu interativo de mensagens de cumprimento.
 
- Se o usuário entrar com a letra M ou palavra Manhã, deve mostrar a mensagem "Bom dia e o nome da pessoa!"
- Se o usuário entrar com a letra T ou palavra Tarde, deve mostrar a mensagem "Boa tarde e o nome da pessoa!"
- Se o usuãrio entrar com a letra N ou palavra Noite, deve mostrar a mensagem "Boa noite eo nome da pessoa!"
"""
"""
 Entrada de dados

 usuario = Nome da Pessoa
 periodo = periodo que a pessoa esta (Mnhã, Tarde ou Noite)
"""

usuario = input ("Digite o seu nome: ")
turno = input ("Qual o seu Turno: ")

match turno:
    case "M" |"m" | "Manhã" | "Manha":
        print("Bom Dia, seu ", usuario)
    case "T" | "t" | "Tarde":
        print("Boa Tarde, seu ", usuario)
    case "N" | "n" | "Noite":
        print("Boa Noite, seu ", usuario)