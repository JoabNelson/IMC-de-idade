'''🧠 Atividade: Central de Atendimento Interativa | Dia 03/02
 
🎯 Objetivo:
Utilizar a estrutura match case para simular um menu de atendimento onde o usuário escolhe uma opção e o sistema retorna uma mensagem correspondente.
 
 
📋 Enunciado:
 
Você foi contratado para criar um menu interativo de atendimento para uma empresa fictícia. O sistema deve exibir as opções abaixo e, de acordo com o número digitado, apresentar uma resposta:
 
Opções do menu:
[1] Falar com atendente
[2] Segunda via de boleto
[3] Cancelar serviço
[4] Informações sobre planos
[5] Sair
 
✅ O que o programa deve fazer:
Mostrar o menu acima.
Receber a opção digitada pelo usuário.
Utilizar match case para responder com base na opção.
Exibir uma mensagem apropriada para cada caso.
Caso digite algo inválido, exibir: "Opção inválida, tente novamente!"
✅ Critérios para o desafio estar completo:
Testar diferentes entradas para verificar todas as respostas.
Enviar o link do repositório com o Código

\n = pular uma linha LMEBRESSE DISSO'''

print('''
Opções do menu:
[1] Falar com atendente
[2] Segunda via de boleto
[3] Cancelar serviço
[4] Informações sobre planos
[5] Sair'''
      )
# Entrada de dados (Opção desejada)
opcao_usuario = input("Entre com a opção desejada: ")

match opcao_usuario: 
    case "1":
        print("==== Iremos colcoar você com um atendente")
    case "2":
        print("==== Iremos encaminhar para voce a segunda via do boleto")
    case "3":
        print("==== Vamos cancelar o seu serviço")
    case "4":
        print("==== Vamos informar nossos planos")
    case"5":
        print("==== Sair")
    case _:
        print("Opção invalida #ERROR404")