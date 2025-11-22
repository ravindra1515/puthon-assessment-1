'''7.Given list of items purchased in a file display the following: No of items purchased, No of free items, Amount to pay, Discount given, Final amount paid
Concepts: files, dictonary

Sample output for purchase-1.txt file:
No of items purchased: 5 
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405

(Test your program on below given purchase-1.txt and purchase-2.txt)'''
def process_purchase(file_name):
    try:
        with open(file_name, 'r') as file:
            items = file.readlines()
        
        item_prices = {}
        for item in items:
            name, price = item.strip().split(',')
            item_prices[name] = float(price)
        
        num_items = len(item_prices)
        num_free_items = num_items // 3  # Assuming every 3rd item is free
        amount_to_pay = sum(item_prices.values())
        discount_given = sum(sorted(item_prices.values())[:num_free_items])
        final_amount_paid = amount_to_pay - discount_given
        
        print(f"Processing {file_name}:")
        print(f"No of items purchased: {num_items}")
        print(f"No of free items: {num_free_items}")
        print(f"Amount to pay: {amount_to_pay}")
        print(f"Discount given: {discount_given}")
        print(f"Final amount paid: {final_amount_paid}\n")
    
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

process_purchase('Purchase-1.txt')
process_purchase('Purchase-2.txt')
print("PROGRAM 7 COMPLETED")