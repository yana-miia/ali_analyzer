from pprint import pprint
from seller import Seller

#Uncomment the following blocks to test them
if __name__ == '__main__':
    seller = Seller("Solomiia")
    print(seller)

    #print("Best Selling:")
    #for product in seller.get_best_products():
    #    print(product)
    #print("\n\n\n")

    #print("Demand:")
    #pprint(seller.find_demand())
    #print("\n\n\n")

    #print("Best Sellers:")
    #pprint(seller.get_best_sellers())
    #print("\n\n\n")

    #print("Statistic about 'phone charger':")
    #pprint(seller.get_product_statistic('phone charger'))
    #print("\n\n\n")

    #print("Analyzed:")
    #for i in seller.get_personal_recommendations([32922653638, 32954832491]):
    #    print(i)
    #print("\n\n\n")
