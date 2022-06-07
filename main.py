# Você não precisará mexer neste arquivo
from restaurant.screen import initial_screen
from restaurant.management import get_item

# AVAILABLE_MENU=[
#   {'id': 1, 'name': 'ADICIONAL FRANGO 50G', 'price': 4.0},
#   {'id': 2, 'name': 'burguer', 'price': 35.0}
#   ]

def main():
	# print(get_item(2))
	initial_screen()


if __name__ == '__main__':
	main()