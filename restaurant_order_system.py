from collections import deque
from datetime import datetime

class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Order #{self.order_id} - Customer: {self.customer_name}, Items: {self.items}"

class RestaurantOrderSystem:
    def __init__(self):
        self.order_queue = deque()
        self.current_order_id = 1

    def add_order(self, customer_name, items):
        """Add a new order to the queue"""
        new_order = Order(self.current_order_id, customer_name, items)
        self.order_queue.append(new_order)
        print(f"\nNew order added: {new_order}")
        self.current_order_id += 1

    def complete_order(self):
        """Remove and return the next order to be completed"""
        if not self.is_empty():
            completed_order = self.order_queue.popleft()
            print(f"\nCompleted order: {completed_order}")
            return completed_order
        else:
            print("\nNo orders to complete!")
            return None

    def view_next_order(self):
        """View the next order in the queue without removing it"""
        if not self.is_empty():
            next_order = self.order_queue[0]
            print(f"\nNext order to process: {next_order}")
            return next_order
        else:
            print("\nNo orders in queue!")
            return None

    def is_empty(self):
        """Check if the order queue is empty"""
        return len(self.order_queue) == 0

    def queue_size(self):
        """Return the number of orders in the queue"""
        return len(self.order_queue)

# Testing the Restaurant Order System
if __name__ == "__main__":
    # Create an instance of the RestaurantOrderSystem
    restaurant = RestaurantOrderSystem()

    # Add some test orders
    print("=== Testing Restaurant Order System ===")
    restaurant.add_order("John Doe", ["Burger", "Fries", "Coke"])
    restaurant.add_order("Jane Smith", ["Pizza", "Salad", "Water"])
    restaurant.add_order("Bob Johnson", ["Pasta", "Garlic Bread", "Wine"])

    print(f"\nCurrent queue size: {restaurant.queue_size()}")

    # View next order
    restaurant.view_next_order()

    # Complete some orders
    restaurant.complete_order()
    restaurant.complete_order()

    print(f"\nRemaining orders in queue: {restaurant.queue_size()}")

    # Add another order
    restaurant.add_order("Alice Brown", ["Steak", "Mashed Potatoes", "Beer"])

    # Complete remaining orders
    while not restaurant.is_empty():
        restaurant.complete_order()

    # Try to complete order when queue is empty
    restaurant.complete_order()
