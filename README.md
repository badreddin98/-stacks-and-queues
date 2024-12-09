# Stacks and Queues Assignment

This repository contains implementations of two data structure applications:
1. Restaurant Order Management System (using Queue)
2. Browser History Management (using Stack)

## Restaurant Order Management System

The restaurant order management system uses a queue data structure to process orders in a FIFO (First-In-First-Out) manner. This ensures that orders are processed in the order they are received.

### Features:
- Add new orders to the queue
- Complete orders (remove from queue)
- View next order in queue
- Check queue size
- Check if queue is empty

### Usage:
```python
python restaurant_order_system.py
```

## Browser History Management

The browser history management system uses a stack data structure to keep track of visited pages. This allows for efficient management of browsing history with last-in-first-out (LIFO) behavior.

### Features:
- Add new pages to history
- Remove most recent page
- View current page
- Check history size
- Check if history is empty
- View complete browsing history

### Usage:
```python
python browser_history.py
```

## Requirements
- Python 3.x
- No additional packages required

## Testing
Both systems include test cases that demonstrate their functionality. Running each file directly will execute these test cases.
