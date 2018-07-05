from lesson_6.homework_6.homework_1 import Car


class ShowRoom:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.cars = []

    def add_car(self, Car):
        self.cars.append(Car)

    def show_all(self):
        counter = 0
        for car in self.cars:
            counter += 1
            print('{}\n-----------\n{}\n'.format(counter, car))

    def sell_car(self, Car):
        for car in self.cars:
            if car == Car:
                self.cars.remove(car)
                print('Car has been sold!')
                return
        print('No such car!')


car1 = Car('Audi', 'Red', '1999', '$12000')
car2 = Car('BMW', 'Black', '2009', '$18000')
car3 = Car('VW', 'Green', '2005', '$8000')

showroom = ShowRoom('Borshagovska 17', 'Volkswagen showroom')

showroom.add_car(car1)
showroom.add_car(car2)

showroom.show_all()

# showroom.sell_car(car1)
showroom.sell_car(car3)
showroom.sell_car(car2)
# showroom.sell_car(car3)

showroom.show_all()

showroom.sell_car(car2)
