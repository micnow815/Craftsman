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
        
