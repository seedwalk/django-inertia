from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Power(models.Model):
    """Modelo para los poderes/habilidades"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del poder")
    description = models.TextField(blank=True, verbose_name="Descripción")
    
    class Meta:
        verbose_name = "Poder"
        verbose_name_plural = "Poderes"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Affiliation(models.Model):
    """Modelo para organizaciones/equipos"""
    UNIVERSE_CHOICES = [
        ('MARVEL', 'Marvel'),
        ('DC', 'DC Comics'),
        ('OTHER', 'Otro'),
    ]
    
    TYPE_CHOICES = [
        ('TEAM', 'Equipo'),
        ('ORGANIZATION', 'Organización'),
        ('GOVERNMENT', 'Gobierno'),
        ('CRIMINAL', 'Criminal'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción")
    universe = models.CharField(max_length=20, choices=UNIVERSE_CHOICES, verbose_name="Universo")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Tipo")
    
    class Meta:
        verbose_name = "Afiliación"
        verbose_name_plural = "Afiliaciones"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Character(models.Model):
    """Modelo principal para héroes y villanos"""
    
    # Choices para los diferentes campos
    CHARACTER_TYPE_CHOICES = [
        ('HERO', 'Héroe'),
        ('VILLAIN', 'Villano'),
        ('ANTIHERO', 'Antihéroe'),
        ('NEUTRAL', 'Neutral'),
    ]
    
    UNIVERSE_CHOICES = [
        ('MARVEL', 'Marvel'),
        ('DC', 'DC Comics'),
        ('IMAGE', 'Image Comics'),
        ('DARK_HORSE', 'Dark Horse'),
        ('OTHER', 'Otro'),
    ]
    
    STATUS_CHOICES = [
        ('ALIVE', 'Vivo'),
        ('DECEASED', 'Fallecido'),
        ('UNKNOWN', 'Desconocido'),
        ('RETIRED', 'Retirado'),
    ]
    
    GENDER_CHOICES = [
        ('MALE', 'Masculino'),
        ('FEMALE', 'Femenino'),
        ('OTHER', 'Otro'),
        ('UNKNOWN', 'Desconocido'),
    ]
    
    # Información básica
    name = models.CharField(max_length=200, verbose_name="Nombre del personaje")
    real_name = models.CharField(max_length=200, blank=True, verbose_name="Nombre real/Alter ego")
    alias = models.CharField(max_length=500, blank=True, verbose_name="Alias/Otros nombres")
    
    # Tipo y universo
    character_type = models.CharField(
        max_length=20, 
        choices=CHARACTER_TYPE_CHOICES,
        default='HERO',
        verbose_name="Tipo de personaje"
    )
    universe = models.CharField(
        max_length=20,
        choices=UNIVERSE_CHOICES,
        default='MARVEL',
        verbose_name="Universo"
    )
    
    # Características físicas y personales
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='UNKNOWN',
        verbose_name="Género"
    )
    species = models.CharField(max_length=100, default="Humano", verbose_name="Especie")
    occupation = models.CharField(max_length=200, blank=True, verbose_name="Ocupación")
    
    # Estado y nivel
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ALIVE',
        verbose_name="Estado"
    )
    power_level = models.IntegerField(
        default=50,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name="Nivel de poder (1-100)"
    )
    
    # Poderes y habilidades (relación many-to-many)
    powers = models.ManyToManyField(
        Power,
        blank=True,
        related_name='characters',
        verbose_name="Poderes"
    )
    
    # Afiliaciones (equipos, organizaciones)
    affiliations = models.ManyToManyField(
        Affiliation,
        blank=True,
        related_name='members',
        verbose_name="Afiliaciones"
    )
    
    # Relaciones con otros personajes
    allies = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='allied_with',
        verbose_name="Aliados"
    )
    enemies = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='enemy_of',
        verbose_name="Enemigos"
    )
    
    # Imágenes y apariencia
    profile_image = models.URLField(
        blank=True,
        verbose_name="URL de imagen de perfil"
    )
    background_image = models.URLField(
        blank=True,
        verbose_name="URL de imagen de fondo"
    )
    primary_color = models.CharField(
        max_length=7,
        default='#000000',
        verbose_name="Color primario (hex)"
    )
    secondary_color = models.CharField(
        max_length=7,
        default='#FFFFFF',
        verbose_name="Color secundario (hex)"
    )
    
    # Descripción y biografía
    biography = models.TextField(
        blank=True,
        verbose_name="Biografía"
    )
    background_story = models.TextField(
        blank=True,
        verbose_name="Historia de origen"
    )
    notable_quotes = models.TextField(
        blank=True,
        verbose_name="Frases célebres"
    )
    
    # Información adicional
    first_appearance = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Primera aparición"
    )
    created_by = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Creado por"
    )
    base_of_operations = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Base de operaciones"
    )
    
    # Metadatos
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    
    class Meta:
        verbose_name = "Personaje"
        verbose_name_plural = "Personajes"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['character_type', 'universe']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.get_character_type_display()})"
    
    def get_all_enemies(self):
        """Obtiene todos los enemigos del personaje"""
        return self.enemies.all()
    
    def get_all_allies(self):
        """Obtiene todos los aliados del personaje"""
        return self.allies.all()
    
    def get_power_names(self):
        """Obtiene una lista de nombres de poderes"""
        return list(self.powers.values_list('name', flat=True))
    
    @property
    def is_hero(self):
        return self.character_type == 'HERO'
    
    @property
    def is_villain(self):
        return self.character_type == 'VILLAIN'

