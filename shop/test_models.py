from django.test import TestCase
from PCShop.models import Product, Category

class ModelsTest(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_product_category_setup(self):
        product = Product(
            name = 'test',
            ser = 'test',
            category = Category(name = 'test'),
            price = 99
        )

        product.category.save()
        product.save()

        self.product_test = Product.objects.order_by('-id').first()

        self.assertIsNotNone(self.product_test.category)