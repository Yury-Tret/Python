class Book:

    def __init__(self, year, name, author):
        self.year = year
        self.name = name
        self.author = author
        self.reviews = []

    def __eq__(self, other):
        if [self.year, self.name, self.author] == [other.year, other.name, other.author]:
            print(True)
        else:
            print(False)

    def add_review(self, text):
        self.reviews.append(text)

    def show_reviews(self):
        counter = 0
        for review in self.reviews:
            counter += 1
            print('{}.\n{}\n'.format(counter, review))


book1 = Book('Nineteen Eighty-Four', 1949, 'George Orwell')
book2 = Book('Nineteen Eighty-Four', 1949, 'George Orwell')
book3 = Book('Над пропастью во ржи', 1951, 'Jerome David Salinger')

book1 == book2
book1 == book3

book1.add_review('Cool!!')
book1.add_review('Not bad')
book1.show_reviews()
