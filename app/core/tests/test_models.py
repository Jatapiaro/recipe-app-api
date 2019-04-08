from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models
from unittest.mock import patch

def sample_user(email = "test@test.com", password="testpassword"):
    return get_user_model().objects.create_user(email, password)

class ModelTest(TestCase):

    def test_create_user_successful(self):
        """ Test creating a new user with an email is successful """
        email = "test@test.com"
        password = "password"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    
    def test_new_user_normalize(self):
        email = "test@TEST.COM"
        password = "password"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email.lower())

    
    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email = None,
                password = "123456"
            )
    

    def test_create_new_superuser(self):
        """ Test creating a new super user """
        user = get_user_model().objects.create_superuser(
            email = "test@test.com",
            password = "123456"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    
    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Vegan"
        )
        self.assertEqual(str(tag), tag.name)

    
    def test_ingredient_str(self):
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name="Cucumber"
        )
        self.assertEqual(str(ingredient), ingredient.name)

    
    def test_recipe_str(self):
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title="Steak and mushroom sauce",
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')
        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)

    