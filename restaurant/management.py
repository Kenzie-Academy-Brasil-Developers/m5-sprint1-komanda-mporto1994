from audioop import add
from restaurant.menu import AVAILABLE_MENU

def get_item(item_id):
	print(item_id)
	item_int = int(item_id)
	if(len(AVAILABLE_MENU)>0):
		items = [item for item in AVAILABLE_MENU if item['id']==item_int]
		if items:
			return items[0]


def add_item_to_tab (table_tab,item_id,amount):
	item = get_item(item_id)
	amount_int = int(amount)
	if item:
		table_tab.append({'id':item_id,'name':item['name'],'price':item['price'],'amount':amount_int})
	return table_tab

def calculate_tab(table_tab):
	total=0
	for product in table_tab:
		total+=product['price']
	return total
print(calculate_tab(AVAILABLE_MENU))