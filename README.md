# 🚨 BrutalDB - Ranking de Entretenimiento

<p align="center">
  <img src="https://img.icons8.com/color/200/000000/imdb.png" alt="BrutalDB Logo" width="200"/>
</p>

---

## 📱 Descripción

BrutalDB es un sistema web tipo **IMDb** desarrollado con **Django + PostgreSQL + Docker** y frontend **100% Bootstrap 5 (sin CSS personalizado)**. Incluye rankings de:

- 🎬 Top Películas
- 📺 Top Series
- 🎥 Top Documentales
- 🎵 Top Canciones

> El sistema está pensado para funcionar como una base sólida de producción: completamente responsive, con administración de contenido, búsqueda global y despliegue dockerizado.

---

## ✨ Características

### Funcionalidades Implementadas ✅

- ✅ Home con secciones top por categoría
- ✅ Catálogo de películas, series y documentales
- ✅ Ranking de canciones
- ✅ Página de detalle por título
- ✅ Búsqueda global (títulos + canciones)
- ✅ Panel administrativo Django (`/admin`)
- ✅ Base de datos PostgreSQL en Docker
- ✅ Seed automático con datos demo
- ✅ Diseño responsive con Bootstrap 5 puro
- ✅ Preparado para despliegue con Gunicorn

### Próximamente 🔄

- 🔐 Sistema de autenticación de usuarios
- ⭐ Favoritos y watchlist personal
- 🗳️ Rating por usuarios
- 🎞️ Paginación y filtros avanzados
- 🌐 API REST con Django REST Framework

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Versión |
|------------|------------|---------|
| Backend | Django | 5.1.6 |
| Lenguaje | Python | 3.12 |
| Base de Datos | PostgreSQL | 16 |
| Frontend UI | Bootstrap | 5.3.3 |
| Servidor WSGI | Gunicorn | 23.0.0 |
| Contenedores | Docker + Compose | Latest |

---

## 📁 Estructura del Proyecto

```
__Automatizador-de-zoom/
├── brutaldb/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── catalog/
│   ├── management/commands/seed_demo.py
│   ├── migrations/0001_initial.py
│   ├── templates/catalog/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── media_list.html
│   │   ├── songs_list.html
│   │   ├── title_detail.html
│   │   └── search.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── .dockerignore
└── README.md
```

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Clonar el Repositorio
```bash
git clone <TU_REPO_URL>
cd __Automatizador-de-zoom
```

### 2. Ejecutar con Docker (Recomendado)
```bash
# Construir y levantar servicios
docker compose up --build
```

Aplicación:
- http://localhost:8000

Admin:
- http://localhost:8000/admin

> Nota: el contenedor ejecuta migraciones, carga datos demo y colecta estáticos automáticamente.

### 3. Ejecutar en Local (sin Docker)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

---

## 📊 Modelo de Datos

### Tabla `Title`

```txt
campo       | descripción                           | tipo
------------|---------------------------------------|---------
name        | Nombre del título                     | string
media_type  | movie / series / documentary          | string
year        | Año de lanzamiento                    | integer
duration    | Duración o temporadas                 | string
score       | Puntuación tipo IMDb                  | decimal
synopsis    | Sinopsis                              | text
poster_url  | URL del poster                        | string
trailer_url | URL del trailer                       | string
cast        | Relación N:N con personas             | relation
```

### Tabla `Song`

```txt
campo       | descripción                           | tipo
------------|---------------------------------------|---------
title       | Nombre de la canción                  | string
artist      | Artista                               | string
year        | Año                                   | integer
album       | Álbum                                 | string
score       | Puntuación                            | decimal
cover_url   | URL de portada                        | string
description | Descripción                           | text
```

---

## 🎯 Endpoints Principales

- `/` → Home con rankings top
- `/top/peliculas/` → Top películas
- `/top/series/` → Top series
- `/top/documentales/` → Top documentales
- `/top/canciones/` → Top canciones
- `/titulo/<id>/` → Detalle de título
- `/buscar/?q=texto` → Búsqueda global
- `/admin/` → Administración

---

## 📦 Crear ZIP del proyecto

Para generar el comprimido descargable:

```bash
cd ..
zip -r brutaldb_imdb_system.zip __Automatizador-de-zoom
```

Esto genera el archivo:
- `brutaldb_imdb_system.zip`

---

## 👨‍💻 Desarrollado por Isaac Esteban Haro Torres

**Ingeniero en Sistemas · Full Stack Developer · Automatización · Data**

### 📞 Contacto

- 📧 **Email:** zackharo1@gmail.com
- 📱 **WhatsApp:** [+593 988055517](https://wa.me/593988055517)
- 💻 **GitHub:** [ieharo1](https://github.com/ieharo1)
- 🌐 **Portafolio:** [ieharo1.github.io](https://ieharo1.github.io/portafolio-isaac.haro/)

---

## 📄 Licencia

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.

---

⭐ Si te gustó el proyecto, ¡dame una estrella en GitHub!
