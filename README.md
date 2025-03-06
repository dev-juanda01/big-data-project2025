# Ingestión de Datos de Productos de Platzi E-commerce

Este proyecto extrae datos de productos de la API de Platzi e-commerce, los almacena en una base de datos SQLite y genera archivos de muestra y auditoría.

## Instrucciones

1. Clonar el repositorio: `git clone <URL_del_repositorio>`
2. Crear un entorno virtual: `python3 -m venv venv`
3. Activar el entorno virtual:
   * Linux/macOS: `source venv/bin/activate`
   * Windows: `venv\Scripts\activate`
4. Instalar dependencias: `pip install -e .`
5. Ejecutar el script: `python src/main.py`

## Automatización con GitHub Actions

El workflow en `.github/workflows/ingestion.yml` automatiza la ejecución del script. Los artefactos generados se pueden descargar desde la ejecución del workflow.
