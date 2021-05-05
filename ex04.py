cars=100
space_in_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car
average_passengers_per_car=passengers/cars_driven
x=1
y=1
z=1

print('In stock', cars, 'cars')
print("And only", drivers, 'drivers came to work')
print('It turns out that', cars_not_driven, 'cars are empty')
print('We can carry today', carpool_capacity, 'persons')
print('Today we need to transport', passengers, 'persons')
print("Each car will have approximately", average_passengers_per_car, 'persons')
print('Sum x,y,z =', x+y+z)
