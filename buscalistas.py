# Multipla Lista
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
 equipamentos.append(input("Equipamento: "))
 valores.append(float(input("Valor: ")))
 seriais.append(int(input("Número Serial: ")))
 departamentos.append(input("Departamento: "))
 resposta = input("Digite \"S\" para continuar: ").upper()
 
busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
    if indice in range(0,len(equipamentos)):
        print("Valor........: ", valores[indice])
        print("Serial.......: ", seriais[indice])