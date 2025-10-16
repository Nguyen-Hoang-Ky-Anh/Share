from abc import ABC, abstractmethod

class Bookstore :
    def __init__(self, publication = []):
        self.__publication = publication
    
    def getPublications(self):
        return self.__publication
    
    # 4) Compute the cost of all publications in the bookstore.
    def total_cost(self) :
        return sum([pub.getPrice() for pub in self.getPublications()])
    
    # 5) Find the reference book with the chapter containing the most pages.
    def most_pages_chapter_references_book(self):
        result_book = None
        max_pages = 0
        
        for pub in self.__publication:
            if not isinstance(pub, References):
                continue
            else:
                for chapter in pub.getChapters():
                    if chapter.getNumberOfPages() > max_pages:
                        max_pages = chapter.getNumberOfPages()
                        result_book = pub
        
        return result_book
    
    # 6) Check whether a magazine is in the bookstore based on its name.
    def checkWhetherAMagazineIsInTheBookstoreBaseOnName(self, magazine_name):
        return any(
            isinstance(pub, Magazines) and pub.getName() == magazine_name
            for pub in self.getPublications()
        )
    
    # 7) Find all magazines published in a given year.    
    def findAllMagazinesPublishedInAGivenYear(self, year):
        return [pub for pub in self.getPublications() 
                if isinstance(pub, Magazines) and pub.getYearOfPublication() == year]

    
class Publication (ABC) :
    def __init__(self, title, numberOfPages, yearOfPublication, author, price):
        super().__init__()
        self._title = title
        self._numberOfPages = numberOfPages
        self._yearOfPublication = yearOfPublication
        self._author = author
        self._price = price
        
    def getTitle(self):
        return self._title
    
    def getNumberOfPages(self):
        return self._numberOfPages
    
    def getYearOfPublication(self):
        return self._yearOfPublication
    
    def getAuthor(self):
        return self._author    
        
    def getPrice(self):
        return self._price
    
    # 1) Determine the type of each publication (Magazine or Reference). (Override in subclass)
    @abstractmethod    
    def typeOfPublication(self):
        return "Unknown publication!"
    
    # 2) Whether a publication is a magazine and was published 10 years ago (from 2024).    
    @abstractmethod    
    def isAMagazine10YearsAgoFrom2024(self):
        return "This is not a magazine"
    
    # 3) Whether two publications are of the same type and by the same author.
    def sameTypeSameAuthor(self, other):
        if isinstance(other, Publication):
            return (self.typeOfPublication(), self.getAuthor()) == (other.typeOfPublication(), self.getAuthor())
        else:
            return NotImplemented
    
        
class Magazines (Publication):
    def __init__(self, title, numberOfPages, yearOfPublication, author, price, name):
        super().__init__(title, numberOfPages, yearOfPublication, author, price)
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def typeOfPublication(self):
        return "This is magazine!"
    
    def isAMagazine10YearsAgoFrom2024(self):
        if(2024 - self.getYearOfPublication() == 10):
            return "This magazine was published 10 years ago"
        elif(2024 - self.getYearOfPublication() > 10):
            return "This magazine was published more than 10 years ago"
        else:
            return "This magazine was published less than 10 years ago"

class References (Publication):
    def __init__(self, title, numberOfPages, yearOfPublication, author, price, field, chapters = []):
        super().__init__(title, numberOfPages, yearOfPublication, author, price)
        self.__field = field
        self.__chapters = chapters
    
    def getField(self):
        return self.__field
    
    def getChapters(self):
        return self.__chapters
    
    def typeOfPublication(self):
        return "This is references book!"
    
    def isAMagazine10YearsAgoFrom2024(self):
        return "This is not a magazine"


class Chapter:
    def __init__(self, title, numberOfPages):
        self.__title = title
        self.__numberOfPages = numberOfPages
        
    def getTitle(self):
        return self.__title
    
    def getNumberOfPages(self):
        return self.__numberOfPages

# -----------TEST-----------  
if __name__ == "__main__":
   if __name__ == "__main__":
    # Create chapters
    chapters1 = [Chapter("Intro to AI", 12), Chapter("Neural Networks", 45), Chapter("Deep Learning", 50)]
    chapters2 = [Chapter("Basic Math", 20), Chapter("Advanced Math", 80)]
    chapters3 = [Chapter("Biology 101", 15), Chapter("Genetics", 25)]

    # Create publications
    ref1 = References("AI Handbook", 200, 2020, "John Doe", 50, "AI", chapters1)
    ref2 = References("Math for Engineers", 300, 2018, "Jane Smith", 60, "Mathematics", chapters2)
    ref3 = References("Biology Basics", 250, 2021, "Anna White", 55, "Biology", chapters3)
    mag1 = Magazines("Tech World", 40, 2014, "John", 15, "Tech World")
    mag2 = Magazines("Science Daily", 45, 2023, "Anna White", 25, "Science Daily")

    # Create bookstore
    store = Bookstore([ref1, ref2, ref3, mag1, mag2])

    print("=== 1) Type of each publication ===")
    for p in store.getPublications():
        print(f"{p.getTitle()}: {p.typeOfPublication()}")

    print("\n=== 2) Whether a publication is a magazine and was published 10 years ago ===")
    print(f"{mag1.getName()}: {mag1.isAMagazine10YearsAgoFrom2024()}")
    print(f"{mag2.getName()}: {mag2.isAMagazine10YearsAgoFrom2024()}")
    print(f"{ref1.getTitle()}: {ref1.isAMagazine10YearsAgoFrom2024()}")

    print("\n=== 3) Whether two publications are same type and author ===")
    print(f"{ref1.getTitle()} and {ref2.getTitle()} -> {ref1.sameTypeSameAuthor(ref2)}")
    print(f"{ref1.getTitle()} and {ref1.getTitle()} -> {ref1.sameTypeSameAuthor(ref1)}")

    print("\n=== 4) Total cost of all publications ===")
    print(f"Total cost: {store.total_cost()}")

    print("\n=== 5) Reference book with the chapter containing the most pages ===")
    book = store.most_pages_chapter_references_book()
    print(f"Book: {book.getTitle()}")

    print("\n=== 6) Check whether a magazine is in the bookstore based on its name ===")
    print(f"Science Daily in store? {store.checkWhetherAMagazineIsInTheBookstoreBaseOnName('Science Daily')}")
    print(f"Tech Today in store? {store.checkWhetherAMagazineIsInTheBookstoreBaseOnName('Tech Today')}")

    print("\n=== 7) Find all magazines published in a given year ===")
    mags_2023 = store.findAllMagazinesPublishedInAGivenYear(2023)
    print(f"Magazines in 2023: {[m.getName() for m in mags_2023]}")
