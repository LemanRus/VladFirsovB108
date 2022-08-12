# Предметная область – магазин. Разработать класс Shop, описывающий работу магазина продуктов.
# Разработать класс Products, продукт описывается следующими параметрами: уникальный идентификатор,
# название продукта, стоимость, количество. Разработать класс FruitProduct на базе класс Product,
# фрукт характеризуется параметрами: страна изготовителя, срок годности.


class Product:
    def __init__(self, article: int, name: str, price: int, quantity: int):
        self.article = article
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return "Продукт: {:>4d}: {}, цена: {}, кол-во: {}".format(self.article, self.name, self.price, self.quantity)


class FruitProduct(Product):
    def __init__(self, article: int, name: str, price: int, quantity: int, origin_country: str, shelf_life: int):
        super().__init__(article, name, price, quantity)
        self.origin_country = origin_country
        self.shelf_life = shelf_life

    def __str__(self) -> str:
        return "Фрукт: {:>4d}: {}, цена: {}, кол-во: {}, " \
               "страна: {}, срок годности (дней): {:>3d}".format(self.article, self.name, self.price, self.quantity,
                                                                 self.origin_country, self.shelf_life)


class Shop:
    """
    Класс магазина.

    max_qty: максимальное количество разных товаров (т.е. различных артикулов)
    __product_list: массив продуктов (за исключением фруктов)
    __fruit_product_list: массив фкруктов
    __articles: массив артикулов товаров
    """
    def __init__(self, max_qty: int):
        self.max_qty = max_qty
        self.product_count = 0
        self.fruit_product_count = 0
        self.__product_list = []
        self.__fruit_product_list = []
        self.__articles = []

    def add_product(self, product: Product) -> None:
        if product.article in self.__articles:
            print("Товар с артикулом {} уже существует".format(product.article))
        else:
            if self.max_qty > self.product_count + self.fruit_product_count:
                self.__product_list.append(product)
                self.__articles.append(product.article)
                self.product_count += 1
            else:
                print('Невозможно добавить продукт {}. Недостаточно места.'.format(product.name))

    def add_fruit_product(self, fruit_product: FruitProduct) -> None:
        if fruit_product.article in self.__articles:
            print("Товар с артикулом {} уже существует".format(fruit_product.article))
        else:
            if self.max_qty > self.product_count + self.fruit_product_count:
                self.__fruit_product_list.append(fruit_product)
                self.__articles.append(fruit_product.article)
                self.fruit_product_count += 1
            else:
                print('Невозможно добавить фрукт {}. Недостаточно места..'.format(fruit_product.name))

    def get_product(self, article: int, qty: int) -> None:
        searched_product = None
        for product in self.__product_list:
            if product.article == article:
                searched_product = product
                break
        if searched_product:
            check_qty = searched_product.quantity - qty
            if check_qty < 0:
                print("Невозможно выдать продукт {} в количестве {}".format(searched_product.name, qty))
            elif check_qty == 0:
                print("Вот ваш продукт {}".format(searched_product.name))
                searched_product.quantity = check_qty
                self.__fruit_product_list.remove(searched_product)
                self.product_count -= 1
            else:
                print("Вот ваш продукт {}".format(searched_product.name))
                searched_product.quantity = check_qty

    def get_fruit_product(self, article: int, qty: int) -> None:
        searched_fruit_product = None
        for fruit in self.__fruit_product_list:
            if fruit.article == article:
                searched_fruit_product = fruit
                break
        if searched_fruit_product:
            check_qty = searched_fruit_product.quantity - qty
            if check_qty < 0:
                print("Невозможно выдать фрукт {} в количестве {}".format(searched_fruit_product.name, qty))
            elif check_qty == 0:
                print("Вот ваш фрукт {}".format(searched_fruit_product.name))
                searched_fruit_product.quantity = check_qty
                self.__fruit_product_list.remove(searched_fruit_product)
                self.fruit_product_count -= 1
            else:
                print("Вот ваш фрукт {}".format(searched_fruit_product.name))
                searched_fruit_product.quantity = check_qty
        else:
            print("Фрукт c артикулом {} остутствует".format(article))

    def print(self) -> None:
        print('-' * 79)
        if self.__product_list:
            print("Продукты: ")
            for product in self.__product_list:
                print(product)

        if self.__fruit_product_list:
            print("Фрукты: ")
            for fruit in self.__fruit_product_list:
                print(fruit)

        print('-' * 79)


shop = Shop(4)
product1 = Product(1, "Сыр", 150, 2)
product2 = Product(2, "Курица", 219, 10)
fruit1 = FruitProduct(3, 'Ананас', 250, 100, "Эфиопия", 30)
fruit2 = FruitProduct(4, 'Апельсин', 30, 30, "Турция", 90)
fruit3 = FruitProduct(4, 'Банан', 15, 50, "Египет", 15)

shop.add_product(product1)
shop.add_product(product2)
shop.add_fruit_product(fruit1)
shop.add_fruit_product(fruit2)
shop.add_fruit_product(fruit3)
shop.print()
shop.get_product(2, 3)
shop.get_product(2, 30)
shop.get_fruit_product(2, 10)
shop.get_fruit_product(3, 1)
shop.get_fruit_product(3, 500)
shop.get_fruit_product(3, 5)
shop.print()
shop.get_fruit_product(3, 94)
shop.add_fruit_product(fruit3)
shop.print()
