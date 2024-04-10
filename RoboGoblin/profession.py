class Pattern:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

class Category:
    def __init__(self, name):
        self.name = name
        self.patterns = []

    def add_pattern(self, pattern):
        self.patterns.append(Pattern(pattern))

class Profession:
    def __init__ (self, name):
        self.name = name
        self.categories = {}
        self.active_category = None
    
    def return_name(self):
        return self.name

    def add_category(self, category_name):
        category = Category(category_name)
        self.categories[category_name] = category
        self.active_category = category

    def add_pattern(self, pattern_name):
        self.active_category.add_pattern(pattern_name)

    def print_category(self, category_name):
        items = []
        category = self.categories.get(category_name)
        for pattern in category.patterns:
            items.append(pattern.name)

        return items
        
    def get_all_categories(self):
        items = []
        for category_name, category in self.categories.items():
            items.append(category_name)

        return items
    
    def patterns_in_category(self, category_name):
        """Returns the number of patterns in a specified category."""
        category = self.categories.get(category_name)
        if category is not None:
            return len(category.patterns)
        else:
            print(f"No category found with the name '{category_name}'.")
            return 0
