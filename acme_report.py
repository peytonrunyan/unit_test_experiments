from acme import Product
import random

def generate_products(number_of_products=30):
    products = {}
    for i in range(number_of_products):
        adj_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        noun_list = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
        adj = random.choice(adj_list)
        noun = random.choice(noun_list)

        name = '{} {}'.format(adj, noun)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        products[i] = Product(name,price,weight,flammability)
    return products

def inventory_report(x):
    name_list = []
    price_list = []
    weight_list = []
    flammability_list = []

    for i in range(len(x)):
        name_list.append(x[i].name)
        price_list.append(x[i].price)
        weight_list.append(x[i].weight)
        flammability_list.append(x[i].flammability)
    
    unique_names = set(name_list)
    
    def average(y):
        return sum(y)/len(y)
    
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ', len(unique_names))
    print('Average price: ', average(price_list))
    print('Average weight: ', average(weight_list))
    print('Average flammability: ', average(flammability_list))

if __name__ == '__main__':
    inventory_report(generate_products())
