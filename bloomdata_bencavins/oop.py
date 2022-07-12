class Animal:
    sound = '???'

    def __init__(self, name, age):  # constructor
        print('constuctor called')
        self.name = name
        self.age = age

    def say_hi(self):
        print(f'{self.name} says "{self.sound}!"')


class Dog(Animal):
    sound = 'bark'

    def __init__(self, name, age, breed='lab'):
        super().__init__(name, age)
        self.breed = breed


class Cat(Animal):
    sound = 'meow'


class Horse(Animal):
    sound = 'neigh'

    def ride(person):
        pass


if __name__ == '__main__':
    dog1 = Dog('fido', 3, 'yorkie')
    dog2 = Dog('rex', 5)
    cat1 = Cat('salem', 10)

    print(dog1.breed, dog2.breed)
