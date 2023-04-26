class Car():
    """Модель автомобиля"""

    def __init__(self, 
                 model, 
                 year_of_release, 
                 engine_capacity, 
                 price,
                 mileage 
                 ):
        """
            self.model: название модели
            self.year_of_release: год выпуска
            self.engine_capacity: объем двигателя
            self.price: стоимость
            self.mileage: пробег
            self.num_of_wheels: количество колес. По умолчанию 4 
        """
        self.model = model
        self.year_of_release = year_of_release
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.num_of_wheels = 4

    def description_car(self):
        """Получение описания человека"""
        description = (f'{self.model} {self.year_of_release} {self.engine_capacity} {self.price} {self.mileage} {self.num_of_wheels}')
        print(description)


class Truck():
    """Модель грузовика"""

    def __init__(self, model, year_of_release, 
                 engine_capacity, price, mileage):
        """Инициализация атрибутов класса-родителя"""
        super().__init__(model, year_of_release, 
                         engine_capacity, price, mileage)

