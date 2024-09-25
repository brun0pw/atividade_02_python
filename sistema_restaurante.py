"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Bruno Henrique Alves Santos
2 - 
"""


import os

# Limpa o terminal.
os.system("cls || clear") 


#criando uma lista que tenha código, nome do prato e valor
Cardapio = [{"Código do prato": 1, "Nome": "Feijoada", "Valor": 60.0} ,
         {"Código do prato": 2, "Nome": "Buchada", "Valor": 50.0} ,
         {"Código do prato": 3, "Nome": "Mocofato", "Valor": 45.0},
        {"Código do prato": 4, "Nome": "Dobradinha", "Valor": 40.0},
         {"Código do prato": 5, "Nome": "Panelada", "Valor": 35.0}, 
          {"Código do prato": 6, "Nome": "Baião de dois", "Valor": 30.0}, 
           {"Código do prato": 7, "Nome": "Caldo de sururu", "Valor": 25.0} 
     ] 
lista_de_pedidos = []
#perguntando ao user se ele vai querer ver o cardapio
vercadapio = int(input("""
===BEM-VINDO AO RESTAURANTE DE COMIDAS TIPICAS===
             DESEJA VER O CARDAPIO ? 
                 1 - SIM
                 2 - NÃO
"""))
os.system("cls || clear")
#caso sim ele mostra o cardapio com um for
if vercadapio == 1:
    for menu in Cardapio:
      print(f"|código do prato: {menu["Código do prato"]} | Nome: {menu["Nome"]} | Valor: {menu["Valor"]}|")
#caso não ele para o programa
else:
    print("===FIM===")
#escolhendo o pedido e fazendo a pergunta se o user vai continuar
while True:
   contador_de_pedidos = 0
   escolha = int(input("Digite o código do seu pedido: \nCaso não deseje pedir nada digite 0\n"))
   if escolha < 0 or escolha > 7:
      print("Código inválido")
   else:  
     match escolha:
      case 1:
         lista_de_pedidos.append(0)
         contador_de_pedidos += 1
         print(f"Codigo escolhido: {Cardapio[0]["Código do prato"]} | Nome:{Cardapio[0]["Nome"]} | Valor: {Cardapio[0]["Valor"]}")
      case 2:
         lista_de_pedidos.append(1)
         contador_de_pedidos += 1
         print(f"Codigo escolhido: {Cardapio[1]["Código do prato"]} | Nome:{Cardapio[1]["Nome"]} | Valor: {Cardapio[1]["Valor"]}")
      case 3:
         lista_de_pedidos.append(2)
         contador_de_pedidos += 1
         print(f"Codigo escolhido: {Cardapio[2]["Código do prato"]} | Nome:{Cardapio[2]["Nome"]} | Valor: {Cardapio[2]["Valor"]}")
      case 4:
         lista_de_pedidos.append(3)
         contador_de_pedidos += 1
         print(f"Codigo escolhido: {Cardapio[3]["Código do prato"]} | Nome:{Cardapio[3]["Nome"]} | Valor: {Cardapio[3]["Valor"]}")
      case 5:
         lista_de_pedidos.append(4)
         contador_de_pedidos += 1
         print(f"Codigo escolhido: {Cardapio[4]["Código do prato"]} | Nome:{Cardapio[4]["Nome"]} | Valor: {Cardapio[4]["Valor"]}")
      case 6:
         lista_de_pedidos.append(5)
         contador_de_pedidos += 1
         print(f"Codigo escolhido: {Cardapio[5]["Código do prato"]} | Nome:{Cardapio[5]["Nome"]} | Valor: {Cardapio[5]["Valor"]}")
      case 7:
        lista_de_pedidos.append(6)
        contador_de_pedidos += 1
        print(f"Codigo escolhido: {Cardapio[6]["Código do prato"]} | Nome:{Cardapio[6]["Nome"]} | Valor: {Cardapio[6]["Valor"]}")
      case 0:
        print("===FIM===")
        break
    #aqui usa o contador criado dento do while para ver se o cliente vai querer algo mais
   if contador_de_pedidos >= 1:
        resposta_do_user =input("Deseja pedir mais alguma coisa ?\nResponda apenas com um caracter ").upper()
        if resposta_do_user == "S":
           print("Como desejar\n")
           os.system("cls || clear")
        else: 
           break
print(lista_de_pedidos)

