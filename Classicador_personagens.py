"""

🧠 Atividade Prática – Classificador de Personagens + Escolha de Ação | Dia 04/02

🎯 Objetivo da Atividade:
 
Fixar os conceitos de estruturas condicionais em Python (if/elif/else e match case) através de uma situação simulada de escolha e ação dentro de 
um jogo.
 
📋 Descrição da Tarefa:
 
Você está criando um pequeno sistema de um jogo de aventura onde o jogador será classificado por sua experiência e, com base em sua escolha, executará uma ação dentro do jogo.
 
🔧 O que seu programa deve fazer:
 
1.Pedir ao jogador quantos pontos de experiência ele tem (XP):
 
Menos de 100 → "Iniciante"
 
Entre 100 e 500 → "Intermediário"
 
Mais de 500 → "Veterano"
 
Use if/elif/else para essa classificação.
 
2. Depois, o programa deve perguntar qual ação o jogador deseja executar (usar match case):
 
"A" → Atacar
 
"D" → Defender
 
"F" → Fugir
 
Qualquer outra tecla → "Ação inválida"
 
Mostre uma mensagem apropriada para cada ação, como:
 
"Você avançou para o ataque!"
 
"Você levantou o escudo!"
 
"Você fugiu da batalha!"
 
📝 Regras de Entrega:
Crie seu código em um arquivo .py
Faça testes com diferentes níveis de XP e ações
Envie o código por GitHub ou por sua plataforma de aulas

"""

nivel = int(input("quantos pontos de Experiencia voce tem "))


if nivel < 99:
    print("Voce é Iniciante!")
elif nivel < 499:
    print("Você é Intermediario!")
else:
    print("Você é Veterano!")

acao = input(" Qual ação voce vai realizar: (D = DEFENDER, A = Atacar, F = Fugir)")
match acao:
    case "A" | "a":
        print(" Você utilizou um Ataque")
    case "D" | "d":
        print("Você utilizou a defesa")
    case "F" |"f":
        print("Você fugiu da batalha!")
    case _:
        print("Opção Invalida")