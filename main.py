# from models.product import Product
from utils import PrintTable
from models.user import User 
import sys


while True:
    PrintTable()
    check = input(" > ")
    if check == "1" :
        pass
    elif check == "2" :
        User.create_user()
    elif check == "3" :
        sys.exit(1)
    else:
        sys.exit(0)










# for product in Product.load_products():
#     print(product.name, product.price)

