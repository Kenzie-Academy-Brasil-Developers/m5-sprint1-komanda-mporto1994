import os
from restaurant.management import add_item_to_tab, get_item

TABLE_TAB=[]

def initial_screen ():
    os.system("clear")
    while(True):
        print("1. Adicionar item a comanda")
        print("2. Fechar comanda")
        option = input("O que deseja fazer: ")

        if option=="1":
            os.system("clear")
            add_item_screen()
        elif option=="2":
            os.system("clear")
            is_out = check_out_screen()
            if(is_out):break
        else:
            print("Digite uma opção válida")

def add_item_screen():
    os.system("clear")
    id = input("Digite o id do item: ")
    item = get_item(id)
    
    if(item):
        qtd = input("Digite a quantidade desejada: ")
    else:
        print(f'{id} não é um id de item válido')
        add_item_screen()

    item_name = item['name']    
    add_item_to_tab(TABLE_TAB, id, qtd)
    print('{qtd} {item_name} adicionado(s) a comanda!')

def check_out_screen():
    total = 0
    for product in TABLE_TAB:
        sub_total = product["amount"]*product["price"]
        amt = product["amount"]
        nm = product["name"]
        print(f"Item {TABLE_TAB.index(product)+1}: {amt} {nm} - R${sub_total}")
        total += sub_total
    
    print (f"""--------------------------------------------------
        Total: R${total}

        
        """)
    while(True):
        out = input("Digite F para finalizar o sistema")
        print(out)
        if(out == "F"):
            return True
