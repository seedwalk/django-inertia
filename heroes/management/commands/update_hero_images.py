from django.core.management.base import BaseCommand
from heroes.models import Character
import urllib.request
import json


class Command(BaseCommand):
    help = 'Actualiza las imágenes de los héroes usando la SuperHero API'

    def handle(self, *args, **kwargs):
        # Mapeo de nombres de personajes a sus IDs en la SuperHero API
        # https://www.superheroapi.com/
        hero_image_mapping = {
            # Marvel Heroes
            'Spider-Man': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/620-spider-man.jpg',
            'Iron Man': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/346-iron-man.jpg',
            'Captain America': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/149-captain-america.jpg',
            'Thor': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/659-thor.jpg',
            'Hulk': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/332-hulk.jpg',
            'Black Widow': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/107-black-widow.jpg',
            'Wolverine': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/717-wolverine.jpg',
            'Deadpool': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/213-deadpool.jpg',
            'Doctor Strange': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/226-doctor-strange.jpg',
            'Black Panther': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/106-black-panther.jpg',
            'Scarlet Witch': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/586-scarlet-witch.jpg',
            'Vision': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/684-vision.jpg',
            'Hawkeye': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/313-hawkeye.jpg',
            'Ant-Man': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/39-ant-man.jpg',
            'Wasp': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/694-wasp.jpg',
            'Captain Marvel': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/157-captain-marvel.jpg',
            'Daredevil': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/201-daredevil.jpg',
            'Luke Cage': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/413-luke-cage.jpg',
            'Jessica Jones': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/358-jessica-jones.jpg',
            'Punisher': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/544-punisher.jpg',
            
            # DC Heroes
            'Batman': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/70-batman.jpg',
            'Superman': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/644-superman.jpg',
            'Wonder Woman': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/720-wonder-woman.jpg',
            'Flash': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/263-flash.jpg',
            'Aquaman': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/45-aquaman.jpg',
            'Green Lantern': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/299-green-lantern.jpg',
            'Cyborg': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/196-cyborg.jpg',
            'Shazam': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/589-shazam.jpg',
            'Green Arrow': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/297-green-arrow.jpg',
            'Supergirl': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/643-supergirl.jpg',
            'Nightwing': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/476-nightwing.jpg',
            'Robin': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/562-robin.jpg',
            'Batgirl': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/63-batgirl.jpg',
            'Starfire': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/625-starfire.jpg',
            'Raven': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/555-raven.jpg',
            'Beast Boy': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/74-beast-boy.jpg',
            'Zatanna': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/735-zatanna.jpg',
            'Constantine': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/182-constantine.jpg',
            'Martian Manhunter': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/418-martian-manhunter.jpg',
            'Hawkgirl': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/317-hawkgirl.jpg',
            
            # Marvel Villains
            'Thanos': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/655-thanos.jpg',
            'Loki': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/405-loki.jpg',
            'Magneto': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/415-magneto.jpg',
            'Doctor Doom': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/224-doctor-doom.jpg',
            'Green Goblin': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/299-green-goblin.jpg',
            'Venom': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/687-venom.jpg',
            'Red Skull': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/557-red-skull.jpg',
            'Ultron': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/676-ultron.jpg',
            'Hela': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/321-hela.jpg',
            'Killmonger': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/370-killmonger.jpg',
            'Mysterio': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/463-mysterio.jpg',
            'Kingpin': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/371-kingpin.jpg',
            'Carnage': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/154-carnage.jpg',
            'Apocalypse': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/42-apocalypse.jpg',
            'Galactus': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/275-galactus.jpg',
            
            # DC Villains
            'Joker': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/370-joker.jpg',
            'Lex Luthor': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/405-lex-luthor.jpg',
            'Harley Quinn': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/309-harley-quinn.jpg',
            'Darkseid': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/203-darkseid.jpg',
            'Deathstroke': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/212-deathstroke.jpg',
            'Bane': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/58-bane.jpg',
            'Poison Ivy': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/527-poison-ivy.jpg',
            'Catwoman': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/162-catwoman.jpg',
            'Riddler': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/559-riddler.jpg',
            'Penguin': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/508-penguin.jpg',
            'Two-Face': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/674-two-face.jpg',
            'Ra\'s Al Ghul': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/549-ras-al-ghul.jpg',
            'Black Manta': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/101-black-manta.jpg',
            'Sinestro': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/605-sinestro.jpg',
            'Reverse Flash': 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/558-reverse-flash.jpg',
        }
        
        updated_count = 0
        not_found_count = 0
        
        for character_name, image_url in hero_image_mapping.items():
            try:
                character = Character.objects.get(name=character_name)
                character.profile_image = image_url
                character.save()
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Actualizado: {character_name}')
                )
            except Character.DoesNotExist:
                not_found_count += 1
                self.stdout.write(
                    self.style.WARNING(f'✗ No encontrado: {character_name}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'✗ Error con {character_name}: {str(e)}')
                )
        
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(f'=== Resumen ==='))
        self.stdout.write(self.style.SUCCESS(f'Actualizados: {updated_count}'))
        self.stdout.write(self.style.WARNING(f'No encontrados: {not_found_count}'))
        self.stdout.write('')
        self.stdout.write(
            self.style.SUCCESS('¡Imágenes actualizadas exitosamente!')
        )

