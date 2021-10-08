from django.test import TestCase
from app.models import Location, Category, Image

# Create your tests here.

# location model tests
class LocationTestCase(TestCase):

    def setUp(self):
        """
        Create a location for testing
        """
        Location.objects.create(name="Test Location")

    def test_location_name(self):
        """
        Test that the location name is correct
        """
        location = Location.objects.get(name="Test Location")
        self.assertEqual(location.name, "Test Location")

    def test_location_str(self):
        """
        Test that the location string representation is correct
        """
        location = Location.objects.get(name="Test Location")
        self.assertEqual(str(location), "Test Location")


# category models test
class CategoryTestCase(TestCase):

    def setUp(self):
        """
        Create a category for testing
        """
        Category.objects.create(name="Test Category")

    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_category_str(self):
        """
        Test that the category string representation is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(str(category), "Test Category")


# image model tests
class ImageTestCase(TestCase):

    def setUp(self):
        """
        Create a image for testing
        """
        Image.objects.create(
            name="Test Image",
            description="Test Description",
            location=Location.objects.create(name="Test Location"),
            category=Category.objects.create(name="Test Category"),
            image="http://test.com/test.jpg",
            created_at=None
        )

    def test_image_name(self):
        """
        Test that the image name is correct
        """
        image = Image.objects.get(name="Test Image")
        self.assertEqual(image.name, "Test Image")

    def test_image_description(self):
        """
        Test that the image description is correct
        """
        image = Image.objects.get(name="Test Image")
        self.assertEqual(image.description, "Test Description")

    def test_image_location(self):
        """
        Test that the image location is correct
        """
        image = Image.objects.get(name="Test Image")
        self.assertEqual(image.location.name, "Test Location")

    def test_image_category(self):
        """
        Test that the image category is correct
        """
        image = Image.objects.get(name="Test Image")
        self.assertEqual(image.category.name, "Test Category")

    def test_image_image(self):
        """
        Test that the image image is correct
        """
        image = Image.objects.get(name="Test Image")
        self.assertEqual(image.image, "http://test.com/test.jpg")


    def test_image_str(self):
        """
        Test that the image string representation is correct
        """
        image = Image.objects.get(name="Test Image")
        self