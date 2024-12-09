class BrowserHistory:
    def __init__(self):
        self.history = []  # Using a list as a stack

    def add_page(self, url):
        """Add a new page to the browsing history"""
        self.history.append(url)
        print(f"\nAdded page to history: {url}")

    def remove_page(self):
        """Remove and return the most recently visited page"""
        if not self.is_empty():
            removed_page = self.history.pop()
            print(f"\nRemoved page from history: {removed_page}")
            return removed_page
        else:
            print("\nHistory is empty!")
            return None

    def get_history_size(self):
        """Return the number of pages in history"""
        return len(self.history)

    def is_empty(self):
        """Check if browsing history is empty"""
        return len(self.history) == 0

    def view_current_page(self):
        """View the current page (top of stack) without removing it"""
        if not self.is_empty():
            current_page = self.history[-1]
            print(f"\nCurrent page: {current_page}")
            return current_page
        else:
            print("\nNo pages in history!")
            return None

    def view_history(self):
        """Display all pages in the browsing history"""
        if not self.is_empty():
            print("\nBrowsing History (most recent first):")
            for i, page in enumerate(reversed(self.history), 1):
                print(f"{i}. {page}")
        else:
            print("\nNo browsing history!")

# Testing the Browser History Management
if __name__ == "__main__":
    # Create an instance of BrowserHistory
    browser = BrowserHistory()

    print("=== Testing Browser History Management ===")

    # Test adding pages
    browser.add_page("www.google.com")
    browser.add_page("www.github.com")
    browser.add_page("www.stackoverflow.com")
    browser.add_page("www.python.org")

    # View current history size
    print(f"\nCurrent history size: {browser.get_history_size()} pages")

    # View all history
    browser.view_history()

    # View current page
    browser.view_current_page()

    # Remove some pages
    browser.remove_page()
    browser.remove_page()

    print(f"\nHistory size after removing pages: {browser.get_history_size()} pages")

    # View updated history
    browser.view_history()

    # Add another page
    browser.add_page("www.wikipedia.org")

    # Final history view
    browser.view_history()

    # Clear remaining history
    while not browser.is_empty():
        browser.remove_page()

    # Try to remove page when history is empty
    browser.remove_page()
