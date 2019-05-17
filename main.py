from pprint import pprint
from seller import Seller
from buyer import Buyer

nick = input("Hello! I'm AliAnalyzer.\nTo help you, "\
                + "I need to know what is your name?\n")
print()

usertype = input("Are you Buyer(enter 1) or Seller(enter 2)?\n")
print()
while usertype != '1' and usertype != '2':
    usertype = input("Wrong type of user!\nEnter '1' or '2'\n")
    print()

# Seller's author is Solomiia Dubnevych
if usertype == '2':
    seller = Seller(nick)

    print("Print 'stop' to finish program.")
    print()

    categories = []
    for category in seller.main_categories:
        categories.append(category)


    while True:

        print(seller)
        print()
        command = input("Choose command №: ")

        if command == "stop":
            break

        elif command == "1":
            print("(best products)", "\n")
            print("Categories:\n")
            for category in categories:
                print(category)
            print('\n')
            ctgr = input("Choose category from given list:")
            for prod in seller.get_best_products(ctgr):
                print(prod)

        elif command == "2":
            print("(demand)", "\n")
            pprint(seller.find_demand())

        elif command == "3":
            print("(trend)", "\n")
            pprint(seller.get_trend())

        elif command == "4":
            print("(sellers)", "\n")
            print("Categories:\n")
            for category in categories:
                print(category)
            print('\n')
            ctgr = input("Choose category from given list: ")
            pprint(seller.get_best_sellers(ctgr))

        elif command == "5":
            print("(statistic)", "\n")
            print("Print type of product")
            print("F.e.: 'phone charger'")
            product = input("Product: ")
            pprint(seller.get_product_statistic(product))

        elif command == "6":
            print("(recommendations)", "\n")
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

# Buyer's author is Yana Kryshchuk
elif usertype == '1':

    buyer = Buyer(nick)

    print("Print 'stop' to finish program.")
    print()

    categories = []
    for category in buyer.main_categories:
        categories.append(category)

    while True:
        print(buyer, '\n')
        command = input('Choose command №: ')

        if command == 'stop':
            break
        # needs to be finished
        elif command == '1':
            print("(best products)", "\n")
            print("Categories:\n")
            for category in categories:
                print(category)
            print('\n')
            ctgr = input("Choose category from given list:\n")
            print("Best products in category ", ctgr, ":")
            for product in buyer.get_best_products(ctgr):
                print(product)

        elif command == '2':
            print("(best sellers)", "\n")
            print("Categories:\n")
            for category in categories:
                print(category)
            print('\n')
            ctgr = input("Choose category from given list:\n")
            print("Best sellers in category ", ctgr, ":")
            for seller in buyer.get_best_sellers(ctgr):
                print(seller)

        elif command == '3':
            print("(worst sellers)", "\n")
            print("Categories:\n")
            for category in categories:
                print(category)
            print('\n')
            ctgr = input("Choose category from given list:\n")
            print("Worst sellers in category ", ctgr, ":")
            for seller in buyer.get_worst_sellers(ctgr):
                print(seller)

        elif command == '4':
            print("(best shipping)", "\n")
            print("Print type of product")
            print("F.e.: 'phone charger'")
            product = input("Product: ")
            print("Best shipping options:")
            for ship in buyer.find_best_shipping(product):
                print(ship)

        elif command == '5':
            print("(alternative)", "\n")
            print("Give me your product ID")
            print("F.e.: '32922653638'")
            product_id = input("Product ID:\n")
            print("Alternatives for the product:")
            for alt in buyer.get_alternative(product_id):
                print(alt)
