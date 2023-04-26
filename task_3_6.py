class Car():
    """Модель автомобиля"""

    def __init__(self, 
                 model, 
                 year_of_release, 
                 engine_capacity, 
                 price,
                 mileage 
                 ):

        self.model = model
        self.year_of_release = year_of_release
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.num_of_wheels = 4

    def description_car(self):
        """Получение описания автомобиля"""
        description = (f'Название модели: {self.model}.\n' 
                       f'Год производства: {self.year_of_release}.\n' 
                       f'Объем двигателя: {self.engine_capacity}.\n'
                       f'Стоимость: {self.price}.\n' 
                       f'Пробег: {self.mileage}.\n' 
                       f'Кол-во колеc: {self.num_of_wheels}.\n')
        print(description)

class Truck(Car):
    """Модель грузовика"""

    def __init__(self, model, year_of_release, 
                 engine_capacity, price, mileage):
        """Инициализация атрибутов класса-родителя"""
        super().__init__(model, year_of_release, 
                         engine_capacity, price, mileage)
        self.num_of_wheels = 8
