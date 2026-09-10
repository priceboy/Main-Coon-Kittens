from django.core.management.base import BaseCommand
from kittens.models import Breed, Kitten

class Command(BaseCommand):
    help = "Create presentation-ready sample kitten listings."

    def handle(self, *args, **options):
        breed, _ = Breed.objects.get_or_create(name="Maine Coon")
        samples = [
            ("Maple", "F", 13, "A sunny, affectionate girl who loves a lap and a feather wand.", True),
            ("Atlas", "M", 14, "A confident explorer with a soft purr and an even softer heart.", True),
            ("Clover", "F", 12, "Sweet-natured and playful, with a calm, observant little personality.", True),
            ("Milo", "M", 13, "A gentle companion who greets every new day with curiosity.", False),
            ("Poppy", "F", 12, "A bright, social girl who is always ready for a game.", False),
            ("Theo", "M", 14, "Easygoing, cuddly, and growing into his magnificent Maine Coon paws.", True),
        ]
        for name, gender, age, description, featured in samples:
            Kitten.objects.update_or_create(slug=name.lower(), defaults={
                "name": name, "breed": breed, "gender": gender, "age_weeks": age,
                "price": 1800, "status": "available", "description": description,
                "vaccinated": True, "dewormed": True, "is_featured": featured,
            })
        self.stdout.write(self.style.SUCCESS("Demo kittens are ready."))
