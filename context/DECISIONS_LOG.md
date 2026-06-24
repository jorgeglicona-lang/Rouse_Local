# DECISIONS_LOG

## Decisiones iniciales
- El asistente se llamará Rouse.
- El proyecto local se llama Rouse Local.
- El sistema correrá localmente en Windows 11.
- El backend se implementará en Python con FastAPI.
- La memoria inicial se manejará con SQLite + archivos estructurados.
- La voz no forma parte del primer MVP.
- El acceso móvil se añadirá después de estabilizar el núcleo.
- El repositorio Git ya fue inicializado.
- La primera prueba del servidor FastAPI fue exitosa.
- Ollama quedó instalado como runtime local.

## Modelos elegidos
Se ajustó la selección de modelos para equilibrar:
- coherencia conversacional
- rendimiento
- utilidad real para programación

### Modelos actuales
- `dolphin-llama3:8b` → modelo general / conversación principal
- `llama3:8b` → modelo general alternativo / comparación / fallback manual
- `qwen2.5-coder:7b` → modelo principal de programación

## Arquitectura ya implementada
### Chat
- `/chat` ya está conectado a Ollama.
- `/chat` ya soporta `session_id`.
- `/chat` ya puede recuperar historial corto persistente.

### Persistencia
- Se creó `app/db/`
- Se agregó:
  - `database.py`
  - `models.py`
  - `crud.py`

### Base de datos
- La base física se llama `rouse.db`
- Ubicación:
  - `data/db/rouse.db`

### Tablas actuales
- `conversations`
- `messages`

### Personalidad
- Se decidió desacoplar la personalidad del endpoint.
- La personalidad de Rouse se compone de:
  - `app/prompts/system_prompt.txt`
  - `app/prompts/persona.json`
- Se agregó:
  - `app/services/persona_loader.py`

## Estado funcional actual
Rouse ya no es solo un wrapper de Ollama:
- tiene prompt desacoplado
- tiene personalidad cargada desde archivos
- tiene historial corto persistente por conversación