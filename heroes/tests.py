from django.test import TestCase
from .models import Character, Power, Affiliation


class PowerModelTest(TestCase):
    def test_create_power(self):
        power = Power.objects.create(
            name="Super Fuerza",
            description="Fuerza sobrehumana"
        )
        self.assertEqual(str(power), "Super Fuerza")


class CharacterModelTest(TestCase):
    def test_create_character(self):
        character = Character.objects.create(
            name="Spider-Man",
            real_name="Peter Parker",
            character_type="HERO",
            universe="MARVEL"
        )
        self.assertEqual(str(character), "Spider-Man (Héroe)")
        self.assertTrue(character.is_hero)
        self.assertFalse(character.is_villain)

