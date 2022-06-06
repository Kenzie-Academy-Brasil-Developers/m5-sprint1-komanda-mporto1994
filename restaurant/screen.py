from restaurant.management import add_item_to_tab, get_item

TABLE_TAB=[]

def initial_screen ():
    while(True):
        print("1. Adicionar item a comanda")
        print("2. Fechar comanda")
        option = input("O que deseja fazer: ")

        if option=="1":
            add_item_screen()
        elif option=="2":
            check_out_screen()
        else:
            print("Digite uma opção válida")

def add_item_screen():
    id = input("Digite o id do item: ")
    item = get_item(id)
    item_name = item['name']
    if(item):
        qtd = input("Digite a quantidade desejada: ")
    else:
        print(f'{id} não é um id de item válido')
        add_item_screen()
        
    add_item_to_tab(TABLE_TAB, item, qtd)
    print('{qtd} {item_name} adicionado(s) a comanda!')

def check_out_screen():
    
    print ("""Item {NUMERO_DO_ITEM}: {QUANTIDADE} {NOME} - R${SUB_TOTAL}
        --------------------------------------------------
        Total: R${TOTAL}

        Digite F para finalizar o sistema
        """)