hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price
print(total_price)

average_price = total_price / len(prices)
print("Average Haircut Price: ", average_price)

new_prices = [ap - 5 for ap in prices]
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: ", total_revenue) 
  
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)


cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)

test_array = [i for i in range(len(hairstyles))]
print(test_array)

test_array_minus_one = [i for i in range(len(hairstyles)-1)]
print(test_array_minus_one)

print(len(new_prices))

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)

cuts_under_30 = [hairstyles[i - 1] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)

grouped_topics = [["Algorithms", "Data Structures", "AI"], ["Linear Regression", "SQL"]]
for sublist in grouped_topics:
  print(sublist)
  for sublist_element in sublist: 
    print(sublist_element)  

desired_list = [-1, 0, 1, 2, 3]
[i-1 for i in range(5)]
print(desired_list)

fruits = ["orange", "apple", "banana"]
for fruit in fruits:
  fruit += 's'
print(fruit)

number = 4
for i in range(3):
  number = number + 1
  print(number)

secret_keys = [["Amy", "Amy123"], ["Zara", "abcde"], ["Donald", "321"]]

for pair in secret_keys:
  for item in pair:
    print(item)