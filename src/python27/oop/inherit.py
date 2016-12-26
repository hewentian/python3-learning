# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Eating meat...'


class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()

print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(c, Dog)
print isinstance(c, Animal)
print isinstance(b, Dog)


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())


class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'

run_twice(Tortoise())
