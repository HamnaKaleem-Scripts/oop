# main.py
from dog import Dog
from cat import Cat

def main():
    dog1 = Dog("Buddy", 4, "Golden Retriever")
    cat1 = Cat("Whiskers", 2, "White")

    print(dog1.info())
    print(dog1.speak())

    print(cat1.info())
    print(cat1.speak())

if __name__ == "__main__":
    main()
