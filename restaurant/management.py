from audioop import add
from restaurant.menu import AVAILABLE_MENU
# from restaurant.screen import add_item_screen

# print(AVAILABLE_MENU)

def get_item(item_id):
	print(item_id)
	item_int = int(item_id)
	if(len(AVAILABLE_MENU)>0):
		# print (AVAILABLE_MENU[1]['id'])
		# print (AVAILABLE_MENU[1]['id'])
		items = [item for item in AVAILABLE_MENU if item['id']==item_int]
		if items:
			# print(items[0])
			return items[0]
# print(get_item(1))


def add_item_to_tab (table_tab,item_id,amount):
	item = get_item(item_id)
	amount_int = int(amount)
	# print(item)
	if item:
		table_tab.append({'id':item_id,'name':item['name'],'price':item['price'],'amount':amount_int})
	return table_tab

# print(add_item_to_tab([],1,3))

def calculate_tab(table_tab):
	total=0
	for product in table_tab:
		total+=product['price']
	return total
print(calculate_tab(AVAILABLE_MENU))