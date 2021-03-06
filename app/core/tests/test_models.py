from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email="test@test.com", password="testpassword"):
    """Create sample user for testing"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test to create new user"""
        email = 'test@test.test'
        password = 'test123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test to normalized new user email"""
        email = 'test@TEST.TEST'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invaild_email(self):
        """Test to rasie error on invail new user email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_superuser_creation(self):
        """Test to create new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test.test.test',
            password='test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test tag string"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='TestTag'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test ingredient string"""
        ingredient = models.Ingredient(
            user=sample_user(),
            name="Test Ingredient"
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test recipe string"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Test Recipe',
            duration=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)
