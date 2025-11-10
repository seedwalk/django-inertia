# Django + Inertia.js - Heroes Demo

Un proyecto de demostración para probar la integración de **Django** con **Inertia.js** y **React**. Esta aplicación muestra un catálogo de héroes y villanos de cómics con sus poderes, afiliaciones y relaciones.

> Desarrollado por [@seedwalk](https://github.com/seedwalk)

## 🦸 Sobre el Proyecto

Esta es una aplicación full-stack que demuestra cómo usar Inertia.js como puente entre Django (backend) y React (frontend), eliminando la necesidad de crear una API REST tradicional. 

### Características

- ✨ Stack moderno: Django 5.1 + Inertia.js + React 18 + Vite
- 🎨 UI con Tailwind CSS v4 y componentes de Radix UI
- 🐳 Desarrollo con Docker Compose
- 🗃️ PostgreSQL como base de datos
- 🦸 Modelos complejos con relaciones many-to-many
- 🎭 Seed de datos con héroes y villanos de Marvel y DC

## 🛠️ Tecnologías

### Backend
- **Django 5.1** - Framework web
- **inertia-django** - Adaptador de Inertia.js para Django
- **django-vite** - Integración con Vite
- **PostgreSQL** - Base de datos
- **uv** - Gestor de paquetes Python moderno

### Frontend
- **React 18** - Librería UI
- **Inertia.js** - Cliente para comunicación con Django
- **Vite 6** - Build tool y dev server
- **Tailwind CSS 4** - Framework CSS
- **Radix UI** - Componentes headless
- **Lucide React** - Iconos

## 🚀 Inicio Rápido

### Prerrequisitos

- Docker y Docker Compose instalados
- Nada más! Docker maneja todo lo demás

### 1. Clonar el repositorio

```bash
git clone https://github.com/seedwalk/django-inertia.git
cd django-inertia
```

### 2. Crear archivo de entorno

Crea un archivo `.env` en la raíz del proyecto:

```bash
# Django
SECRET_KEY=tu-secret-key-super-segura
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://postgres:postgres@db:5432/django-inertia

# Vite
DJANGO_VITE_DEV_SERVER_HOST=localhost
DJANGO_VITE_DEV_SERVER_PORT=5173
```

### 3. Levantar los servicios con Docker

```bash
docker compose up -d
```

Esto iniciará tres servicios:
- **web**: Django corriendo en `http://localhost:8000`
- **vite**: Vite dev server en `http://localhost:5173`
- **db**: PostgreSQL en el puerto 5432

### 4. Verificar que los contenedores estén corriendo

```bash
docker ps
```

Deberías ver algo como:

```
CONTAINER ID   IMAGE                    STATUS         PORTS                    NAMES
abc123def456   django-inertia-web       Up 2 minutes   0.0.0.0:8000->8000/tcp  django-inertia-web-1
def456ghi789   django-inertia-vite      Up 2 minutes   0.0.0.0:5173->5173/tcp  django-inertia-vite-1
ghi789jkl012   postgres:17-alpine       Up 2 minutes   0.0.0.0:5432->5432/tcp  django-inertia-db-1
```

### 5. Correr las migraciones

Una vez que los contenedores estén corriendo, ejecuta las migraciones dentro del contenedor de Django:

```bash
# Opción 1: Usando el nombre exacto del contenedor (reemplaza con el nombre que ves en docker ps)
docker exec -it django-inertia-web-1 uv run python manage.py migrate

# Opción 2: Si el nombre es diferente, usa este patrón
docker exec -it <nombre-del-contenedor-web> uv run python manage.py migrate
```

### 6. Poblar la base de datos con héroes

Ejecuta el comando de seed para crear héroes, villanos, poderes y afiliaciones:

```bash
docker exec -it django-inertia-web-1 uv run python manage.py seed_heroes
```

Este comando creará:
- 🦸 ~40 héroes (Spider-Man, Iron Man, Batman, Superman, etc.)
- 🦹 ~30 villanos (Joker, Thanos, Lex Luthor, etc.)
- ⚡ ~20 poderes diferentes
- 🛡️ Afiliaciones (Avengers, Justice League, X-Men, etc.)
- 🔗 Relaciones entre aliados y enemigos

### 7. Actualizar imágenes de héroes (Recomendado)

Ejecuta este comando para actualizar las imágenes con URLs de alta calidad:

```bash
docker exec -it django-inertia-web-1 uv run python manage.py update_hero_images
```

Este comando:
- 🖼️ Actualiza las imágenes usando la SuperHero API (CDN confiable)
- ✨ Imágenes de alta calidad para ~70+ personajes
- 🚀 Se ejecuta en segundos
- ℹ️ Muestra qué personajes fueron actualizados

### 8. Acceder a la aplicación

Abre tu navegador y ve a:

```
http://localhost:8000
```

¡Listo! Deberías ver el catálogo de héroes.

## 📝 Comandos Útiles

### Ver logs de los contenedores

```bash
# Todos los servicios
docker compose logs -f

# Solo Django
docker compose logs -f web

# Solo Vite
docker compose logs -f vite
```

### Acceder a la shell de Django

```bash
docker exec -it django-inertia-web-1 uv run python manage.py shell
```

### Crear un superusuario para el admin de Django

```bash
docker exec -it django-inertia-web-1 uv run python manage.py createsuperuser
```

Luego accede al admin en: `http://localhost:8000/admin`

### Detener los servicios

```bash
docker compose down
```

### Detener y eliminar volúmenes (limpia la BD)

```bash
docker compose down -v
```

### Reconstruir las imágenes

Si cambias las dependencias (package.json o pyproject.toml):

```bash
docker compose up -d --build
```

### Comandos de gestión de datos

```bash
# Poblar la base de datos con héroes
docker exec -it django-inertia-web-1 uv run python manage.py seed_heroes

# Actualizar imágenes de héroes (después del seed)
docker exec -it django-inertia-web-1 uv run python manage.py update_hero_images

# Limpiar y volver a poblar
docker compose down -v  # Elimina la BD
docker compose up -d    # Levanta los servicios
docker exec -it django-inertia-web-1 uv run python manage.py migrate
docker exec -it django-inertia-web-1 uv run python manage.py seed_heroes
docker exec -it django-inertia-web-1 uv run python manage.py update_hero_images
```

### Ejecutar comandos de Django

```bash
# Patrón general
docker exec -it django-inertia-web-1 uv run python manage.py <comando>

# Ejemplos:
docker exec -it django-inertia-web-1 uv run python manage.py makemigrations
docker exec -it django-inertia-web-1 uv run python manage.py showmigrations
```

### Ejecutar comandos de npm/node

```bash
# Instalar una dependencia
docker exec -it django-inertia-vite-1 npm install <paquete>

# Build de producción
docker exec -it django-inertia-vite-1 npm run build
```

## 📁 Estructura del Proyecto

```
django-inertia/
├── django-inertia/          # Configuración principal de Django
│   ├── settings.py          # Configuración
│   ├── urls.py              # URLs principales
│   ├── middleware.py        # Middleware custom
│   └── views.py             # Vistas de Inertia
├── heroes/                  # App de héroes
│   ├── models.py            # Modelos (Character, Power, Affiliation)
│   ├── views.py             # Vistas
│   ├── urls.py              # URLs
│   └── management/
│       └── commands/
│           └── seed_heroes.py  # Comando para poblar DB
├── frontend/                # Frontend con React
│   ├── js/
│   │   ├── main.jsx         # Punto de entrada
│   │   ├── components/      # Componentes React
│   │   │   ├── Layout.jsx
│   │   │   └── ui/          # Componentes UI (shadcn/ui)
│   │   └── pages/           # Páginas de Inertia
│   │       ├── Index.jsx    # Listado de héroes
│   │       └── Heroes/
│   │           └── Detail.jsx  # Detalle de héroe
│   └── css/                 # Estilos
│       ├── main.css
│       └── tailwind.css
├── templates/
│   └── base.html            # Template base para Inertia
├── docker-compose.yaml      # Configuración de Docker
├── dev.Dockerfile           # Dockerfile para Django
├── vite.Dockerfile          # Dockerfile para Vite
├── vite.config.js           # Configuración de Vite
├── package.json             # Dependencias de Node
└── pyproject.toml           # Dependencias de Python
```

## 🎨 Modelos de Datos

### Character (Personaje)
Modelo principal que representa héroes y villanos con:
- Información básica (nombre, nombre real, alias)
- Tipo (héroe, villano, antihéroe, neutral)
- Universo (Marvel, DC, Image, Dark Horse, etc.)
- Características (género, especie, ocupación)
- Estado y nivel de poder
- Relaciones many-to-many con poderes, afiliaciones, aliados y enemigos
- Imágenes y colores para la UI
- Biografía e historia de origen

### Power (Poder)
Habilidades y poderes especiales:
- Super fuerza, vuelo, velocidad, telepatía, etc.

### Affiliation (Afiliación)
Equipos y organizaciones:
- Avengers, Justice League, X-Men, etc.
- Tipo (equipo, organización, gobierno, criminal)

## 🎛️ Panel de Administración de Django

Django incluye un **panel de administración** integrado que te permite gestionar todos los registros desde una interfaz web sin tocar código.

### Acceder al Admin

1. **Crear un superusuario** (solo la primera vez):

```bash
docker exec -it django-inertia-web-1 uv run python manage.py createsuperuser
```

Ingresa:
- Username (ej: `admin`)
- Email (puede ser ficticio)
- Password (mínimo 8 caracteres)

2. **Acceder al panel**:

Abre tu navegador en: `http://localhost:8000/admin`

### ¿Qué puedes hacer en el Admin?

El panel ya está configurado con todas las funcionalidades para gestionar tus héroes:

#### 📋 Characters (Personajes)
- ✏️ Ver, crear, editar y eliminar personajes
- 🔍 Búsqueda rápida por nombre, nombre real o alias
- 🎯 Filtros por tipo, universo, estado y género
- 🔗 Seleccionar poderes, afiliaciones, aliados y enemigos con widgets visuales
- 📝 Campos organizados en secciones lógicas (Información básica, Características, Poderes, Relaciones, etc.)

#### ⚡ Powers (Poderes)
- Gestionar todos los poderes y habilidades
- Ver qué personajes tienen cada poder

#### 🛡️ Affiliations (Afiliaciones)
- Administrar equipos y organizaciones
- Filtrar por universo (Marvel, DC) y tipo
- Ver todos los miembros de cada afiliación

### Ejemplo de flujo

1. Accede a `/admin` con tu superusuario
2. Click en "Characters" → selecciona un héroe (ej: Spider-Man)
3. Modifica cualquier campo: poderes, nivel de poder, biografía, imágenes, etc.
4. Guarda los cambios
5. Los cambios se reflejan inmediatamente en tu aplicación

**Perfecto para**: ajustar datos, corregir errores, agregar nuevos personajes, sin necesidad de escribir código.

## 🔧 Desarrollo sin Docker

Si prefieres correr la app sin Docker:

### Backend

```bash
# Instalar uv (si no lo tienes)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependencias
uv sync

# Correr migraciones
uv run python manage.py migrate

# Seed
uv run python manage.py seed_heroes

# Correr servidor
uv run python manage.py runserver
```

### Frontend

```bash
# Instalar dependencias
npm install

# Correr dev server
npm run dev
```

## 🤝 Contribuciones

Este es un proyecto de demostración, pero si encuentras bugs o mejoras, siéntete libre de abrir un issue o PR.

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

Desarrollado por [@seedwalk](https://github.com/seedwalk)

