from django.shortcuts import render
from inertia import inertia
from .models import Character, Power, Affiliation


@inertia('Index')
def heroes_index(request):
    """Vista principal de héroes"""
    characters = Character.objects.filter(character_type='HERO').select_related().prefetch_related('powers', 'affiliations')
    
    return {
        'heroes': [
            {
                'id': char.id,
                'name': char.name,
                'realName': char.real_name,
                'universe': char.get_universe_display(),
                'profileImage': char.profile_image,
                'powerLevel': char.power_level,
                'powers': [power.name for power in char.powers.all()],
            }
            for char in characters
        ]
    }


@inertia('Heroes/Detail')
def hero_detail(request, pk):
    """Vista de detalle de un héroe/villano"""
    character = Character.objects.prefetch_related(
        'powers', 'affiliations', 'allies', 'enemies'
    ).get(pk=pk)
    
    return {
        'character': {
            'id': character.id,
            'name': character.name,
            'realName': character.real_name,
            'alias': character.alias,
            'type': character.get_character_type_display(),
            'universe': character.get_universe_display(),
            'gender': character.get_gender_display(),
            'species': character.species,
            'occupation': character.occupation,
            'status': character.get_status_display(),
            'powerLevel': character.power_level,
            'profileImage': character.profile_image,
            'backgroundImage': character.background_image,
            'primaryColor': character.primary_color,
            'secondaryColor': character.secondary_color,
            'biography': character.biography,
            'backgroundStory': character.background_story,
            'notableQuotes': character.notable_quotes,
            'firstAppearance': character.first_appearance,
            'createdBy': character.created_by,
            'baseOfOperations': character.base_of_operations,
            'powers': [
                {'id': power.id, 'name': power.name, 'description': power.description}
                for power in character.powers.all()
            ],
            'affiliations': [
                {'id': aff.id, 'name': aff.name, 'type': aff.get_type_display()}
                for aff in character.affiliations.all()
            ],
            'allies': [
                {'id': ally.id, 'name': ally.name, 'profileImage': ally.profile_image}
                for ally in character.allies.all()
            ],
            'enemies': [
                {'id': enemy.id, 'name': enemy.name, 'profileImage': enemy.profile_image}
                for enemy in character.enemies.all()
            ],
        }
    }

