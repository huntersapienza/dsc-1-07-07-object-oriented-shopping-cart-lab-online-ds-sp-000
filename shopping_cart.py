class ShoppingCart:
    
    def __init__(self, employee_discount=None):
        self._total = 0
        self._items = []
        self._employee_discount = employee_discount
    
    def set_total(self, total):
        self._total = total
    def get_total(self):
        return self._total
    total = property(get_total, set_total)
    
    def set_item(self, item):
        self.items.append[item]
    def get_items(self):
        return self._items
    item = property(get_items, set_item)
    
    def set_employee_discount(self, employee_discount):
        self._employee_discount = employee_discount
    def get_employee_discount(self):
        return self._employee_discount
    employee_discount = property(get_employee_discount, set_employee_discount)
    
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self._items.append({"name": name, "price": price})
        self._total += price*quantity
        return self._total
    
    def mean_item_price(self):
        item_count = len(self._items)
        mean = self._total/item_count
        return mean
    
    def median_item_price(self):
        prices = [self.get_attr(item, "price") for item in self._items]
        prices.sort()
        return self.find_median(prices)
    
    def find_median(self, list_of_prices):
        length = len(list_of_prices)
        if (length%2 == 0):
            mid_one = int(length/2)
            mid_two = mid_one - 1
            median = (list_of_prices[mid_one] + list_of_prices[mid_two])/2
            return median
        mid = int(length/2)
        return list_of_prices[mid]
    
    def get_attr(self, item, attr):
        return item[attr]
    
    def apply_discount(self):
        if self._employee_discount:
            discount = self._employee_discount/100
            discount_total = self._total*(1-discount)
            return discount_total
        else:
            return "Sorry, there is no discount to apply to your cart :("
        
    def item_names(self):
        item_names = []
        for item in self._items:
            item_names.append(item["name"])
        return item_names
    
    def void_last_item(self):
        if self._items:
            self._total-= self._items[-1]["price"]
            self._items.pop()
        else:
            return "There are no items in your cart."
    
