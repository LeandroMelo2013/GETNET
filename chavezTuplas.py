# Lista dentro Lista
from GETNET.funcoes import *
usuarios={}
opcao = perguntar ()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    opcao = perguntar()
    
    ("O que deseja realizar?\n" +
            "<I> - Para Inserir um usuário\n" +
            "<P> - Para Pesquisar um usuário\n" +
            "<E> - Para Excluir um usuário\n" +
            "<L> - Para Listar um usuário: ").upper()