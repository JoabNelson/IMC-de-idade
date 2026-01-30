'''
Dona Maria precisa de um algoritimo que faça a seguinte decisoes

1 se a idade for menor que 12 , deve mostrar a mensagem "CRIANÇA"
2 se a idade for menor que 18, deve mostrar a mensagem "ADOLESCENTE"
3 se a idade for menor que 60, deve mostrar a mensagem "ADULTO"
Se a idade não for nenhuma dessas condiçoes, deve mostrar "IDOSO"

'''
#Entrada de Informações
idade = 65

if idade < 12:
    print("CRIANÇA")
elif idade < 18:
    print("ADOLESCENTE")
elif idade < 60:
    print("ADULTO")
else:
    print("IDOSO")