from django.shortcuts import render
from django.core.paginator import Paginator
from inertia import inertia
from .models import Character, Power, Affiliation


@inertia('Index')
def heroes_index(request):
    """Vista principal de héroes"""
    # Obtener parámetros de query
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 12)  # 12 héroes por página
    universe = request.GET.get('universe', '')
    
    # Query base
    characters = Character.objects.filter(character_type='HERO').select_related().prefetch_related('powers', 'affiliations')
    
    # Filtro por universo si se especifica
    if universe:
        characters = characters.filter(universe=universe)
    
    # Ordenar por nombre
    characters = characters.order_by('name')
    
    # Paginación
    paginator = Paginator(characters, per_page)
    page_obj = paginator.get_page(page)
    
    return {
        'heroes': [
            {
                'id': char.id,
                'name': char.name,
                'realName': char.real_name,
                'universe': char.get_universe_display(),
                'universeCode': char.universe,
                'profileImage': char.profile_image,
                'powerLevel': char.power_level,
                'powers': [power.name for power in char.powers.all()],
            }
            for char in page_obj
        ],
        'pagination': {
            'total': paginator.count,
            'perPage': per_page,
            'currentPage': page_obj.number,
            'lastPage': paginator.num_pages,
            'hasNextPage': page_obj.has_next(),
            'hasPreviousPage': page_obj.has_previous(),
        },
        'filters': {
            'universe': universe,
        }
    }


@inertia('Villains')
def villains_index(request):
    """Vista principal de villanos"""
    # Obtener parámetros de query
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 12)  # 12 villanos por página
    universe = request.GET.get('universe', '')
    
    # Query base
    characters = Character.objects.filter(character_type='VILLAIN').select_related().prefetch_related('powers', 'affiliations')
    
    # Filtro por universo si se especifica
    if universe:
        characters = characters.filter(universe=universe)
    
    # Ordenar por nombre
    characters = characters.order_by('name')
    
    # Paginación
    paginator = Paginator(characters, per_page)
    page_obj = paginator.get_page(page)
    
    return {
        'villains': [
            {
                'id': char.id,
                'name': char.name,
                'realName': char.real_name,
                'universe': char.get_universe_display(),
                'universeCode': char.universe,
                'profileImage': char.profile_image,
                'powerLevel': char.power_level,
                'powers': [power.name for power in char.powers.all()],
            }
            for char in page_obj
        ],
        'pagination': {
            'total': paginator.count,
            'perPage': per_page,
            'currentPage': page_obj.number,
            'lastPage': paginator.num_pages,
            'hasNextPage': page_obj.has_next(),
            'hasPreviousPage': page_obj.has_previous(),
        },
        'filters': {
            'universe': universe,
        }
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

