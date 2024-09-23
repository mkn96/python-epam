class Pagination:
    def __init__(self, text, symbols_per_page):
        self.text = text
        self.symbols_per_page = symbols_per_page
        self.page_count = (len(text) + symbols_per_page - 1) // symbols_per_page
        self.item_count = len(text)

    def count_items_on_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        start = page_number * self.symbols_per_page
        end = min((page_number + 1) * self.symbols_per_page, len(self.text))
        return end - start

    def find_page(self, query):
        if query not in self.text:
            raise Exception(f"'{query}' is missing on the pages")
        pages = []
        start_index = 0
        while True:
            found_index = self.text.find(query, start_index)
            if found_index == -1:
                break
            page_number = found_index // self.symbols_per_page
            pages.append(page_number)
            start_index = found_index + 1
        return pages

    def display_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        start = page_number * self.symbols_per_page
        end = min((page_number + 1) * self.symbols_per_page, len(self.text))
        return self.text[start:end]
