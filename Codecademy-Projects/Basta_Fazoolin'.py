class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
        return "{name} menu available from {start} until {end}".format(name=self.name, start=self.start_time, end=self.end_time)
  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
    return total_price
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}     
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
brunch = Menu("Brunch", brunch_items, "11:00am", "4:00pm")
early_bird = Menu("Early Bird", early_bird_items, "3:00pm", "6:00pm")
dinner = Menu("Dinner", dinner_items, "5:00pm", "11:00pm")
kids = Menu("Kids", kids_items, "11:00am", "9:00pm")

order = ['pancakes', 'home fries', 'coffee']
total_price = brunch.calculate_bill(order)
print("Total price for the order:", total_price)