def highest_sales(transactions):
#Step 1 - Extracting prices and IDs into lists; all_product_price and all_product_id.
    all_product_id = [each_transaction[1] for each_transaction in transactions]
    all_product_price = [each_transaction[2] for each_transaction in transactions]

#Step 2 - Counting the number of times an ID's price appeared and storing it in a list called "count_price"
    count_price = [all_product_price.count(i) for i in all_product_price]

#Step 3 - Storing all sales in a list called "sales_total"
    sales_total = [count_price[i] * all_product_price[i] for i in range(0,len(all_product_price)-1)]

#Step 4 - Finding the maximum sale and the index of that sale in list "sales_total"
    max_sales = max(sales_total)
    index_max = sales_total.index(max_sales)

#Step 5 - Finding the ID of the product with the maximum sale
    highest_id = all_product_id[index_max]
    print(f"The product with the highest number of sales is product {highest_id}.")


transactions = [(1, 101, 15.0),(2, 102, 20.0),(3, 101, 15.0),(4, 103, 10.0),(5, 102, 20.0),(6, 101, 15.0), (7, 103, 10.0),
                (8, 102, 20.0),(9, 103, 10.0)]

highest_sales(transactions)