from pprint import pprint
from seller import Seller
from buyer import Buyer

nick = input("Hello, I'm AliAnalzer.\nTo help you,"\
                + "I need to know what is your name?\n")
print()

usertype = input("You are 'Buyer' or 'Seller'?\n")
print()
while usertype != 'Buyer' and usertype != 'Seller':
    usertype = input("Wrong type of user!\nEnter 'Seller' or 'Buyer'\n")
    print()

# Seller's author is Solomiia Dubnevych
if usertype == 'Seller':
    seller = Seller(nick)

    print("Print 'stop' to finish program.")
    print()

    categories = []
    for category in seller.main_categories:
        categories.append(category)


    while True:

        print(seller)
        print()
        command = input("Choose command: ")
        print()

        if command == "stop":
            break

        elif command == "best products":
            print(categories)
            print()
            ctgr = input("Choose category from given list:")
            pprint(seller.get_best_products(ctgr))

        elif command == "demand":
            pprint(seller.find_demand())

        elif command == "trend":
            pprint(seller.get_trend())

        elif command == "sellers":
            print(categories)
            print()
            ctgr = input("Choose category from given list: ")
            pprint(seller.get_best_sellers(ctgr))

        elif command == "statistic":
            print("Print type of product")
            print("F.e.: 'phone charger'")
            product = input("Product: ")
            pprint(seller.get_product_statistic(product))

        elif command == "recommendations":
            print("Give me a list of your products using their id.")
            print("F.e.: 32922653638, 32954832491")
            products = input("Products: ").split(", ")
            list_of_products = list(map(lambda id: int(id), products))
            print(list_of_products)
            try:
                pprint(seller.get_personal_recommendations(list_of_products))
            except ApiException as e:
                print("Some problems with server data for your input.")
                print(e)

        else:
            print("You called wrong command.")
            print()



elif usertype == 'Buyer':

    buyer = Buyer(nick)

    print("Print 'stop' to finish program.")
    print()

    categories = []
    for category in buyer.main_categories:
        categories.append(category)

    while True:
        break
