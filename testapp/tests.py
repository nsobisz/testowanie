from django.test import TestCase
from django.urls import reverse
from testapp.models import Book, Motor
from datetime import datetime, timedelta


# Create your tests here.
class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(title="Test Book", author="Author Name", borrow_count=101,
                            published_date=datetime.now().date() - timedelta(days=30))
        Book.objects.create(title="Another Test Book", author="Author Author", borrow_count=50,
                            published_date=datetime.now().date() - timedelta(days=800))

    def test_is_popular(self):
        popular_book = Book.objects.get(title="Test Book")
        not_popular_book = Book.objects.get(title="Another Test Book")
        self.assertTrue(popular_book.is_popular())
        self.assertFalse(not_popular_book.is_popular())


    def test_book_creation(self):
        book = Book.objects.get(title="Test Book")

        self.assertEqual(book.author, "Author Name")
        self.assertEqual(book.borrow_count, 101)

    def test_genre(self):
        book = Book.objects.get(title="Test Book")
        book.genre = "Fantasy"
        book.save()
        self.assertEqual(book.genre, "Fantasy")


    def test_string_represantation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.string_representation(), "Test Book by Author Name")


    def test_get_absolute_url(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.get_absolute_url(), reverse('book-detail', kwargs={
            'pk': book.pk}))

    def test_available_default(self):
         book = Book.objects.get(title="Test Book")
         self.assertTrue(book.available)

    def test_reserve_method(self):
        book = Book.objects.get(title="Test Book")
        book.reserve()
        self.assertFalse(book.available)

    def test_is_new_release(self):
        new_release_book = Book.objects.get(title="Test Book")
        self.assertTrue(new_release_book.is_new_release())

class MotorModelTest(TestCase):
    def setUp(self):
        Motor.objects.create(nameMotor="Test Motor", content="test", price=3000,
                            year=2024)
        Motor.objects.create(nameMotor="Another Test Motor", content="test test", price=30000,
                            year=2000)



    def test_motor_creation(self):
        motor = Motor.objects.get(nameMotor="Test Motor")
        self.assertEqual(motor.content, "test")
        self.assertEqual(motor.price, 3000)

    def test_is_cheap(self):
        cheap_motor = Motor.objects.get(nameMotor="Test Motor")
        not_cheap_motor = Motor.objects.get(nameMotor="Another Test Motor")
        self.assertTrue(cheap_motor.is_cheap())
        self.assertFalse(not_cheap_motor.is_cheap())

    def test_is_old(self):
        old_motor = Motor.objects.get(nameMotor="Another Test Motor")
        not_old_motor = Motor.objects.get(nameMotor="Test Motor")
        self.assertTrue( old_motor.is_old())
        self.assertFalse(not_old_motor.is_old())

    def test_string_representation(self):
        motor = Motor.objects.get(nameMotor="Test Motor")
        self.assertEqual(motor.string_representation(), "Test Motor for 3000")

    def test_buy(self):
        motor = Motor.objects.get(nameMotor="Test Motor")
        motor.buy()
        self.assertFalse(motor.for_sale)

    def test_default_color(self):
        motor = Motor.objects.get(nameMotor="Test Motor")
        self.assertEqual(motor.color, "white")

    def test_change_color(self):
        motor = Motor.objects.get(nameMotor="Test Motor")
        motor.change_color("blue")
        self.assertEqual(motor.color, "blue")

    def test_add_promotion(self):
        motor = Motor.objects.get(nameMotor="Test Motor")
        motor.add_promotion(10)
        self.assertEqual(motor.price, 2700)
