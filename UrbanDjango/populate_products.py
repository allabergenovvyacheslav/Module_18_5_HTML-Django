from example1.models import Product, Category

def populate_data():
    phones_category = Category.objects.get_or_create(name='Телефоны')[0]
    laptops_category = Category.objects.get_or_create(name='Ноутбуки')[0]

    Product.objects.create(
        name='iPhone15',
        descriptions='Смартфоны Aple',
        price=120000,
        category=phones_category
    )

    Product.objects.create(
        name='Mac Book Pro',
        descriptions='Компьютеры Aple',
        price=250000,
        category=laptops_category
    )

    print('Данные успешно добавлены')