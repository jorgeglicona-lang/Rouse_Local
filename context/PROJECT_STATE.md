# PROJECT_STATE

## Nombre del proyecto
Rouse Local

## Objetivo
Construir un asistente personal local con personalidad, memoria persistente, ayuda técnica para programación y acceso móvil posterior.

## Estado actual
- Estructura base del proyecto creada.
- Entorno Python configurado.
- Repositorio Git inicializado.
- FastAPI funcionando localmente.
- Endpoint `/health` funcionando.
- Ollama instalado y validado.
- Modelos locales disponibles:
  - `dolphin-llama3:8b`
  - `llama3:8b`
  - `qwen2.5-coder:7b`
- Endpoint `/chat` funcionando con Ollama.
- Rouse ya responde desde el backend.

## Semana 2 - estado actual
### Personalidad
- Existe `system_prompt.txt`.
- Existe `persona.json`.
- Existe `persona_loader.py`.
- La personalidad ya está conectada al flujo de `/chat`.
- El prompt del sistema ya no está hardcodeado en la ruta.

### Persistencia
- SQLite ya está integrado como base inicial.
- La base física existe en:
  - `data/db/rouse.db`
- Existen tablas:
  - `conversations`
  - `messages`
- Ya hay CRUD base para:
  - crear/recuperar conversación por `session_id`
  - guardar mensajes
  - recuperar últimos N mensajes

### Chat persistente
- `/chat` ya acepta `session_id`
- guarda mensajes del usuario y del asistente
- recupera historial corto por conversación
- permite modo general y modo coding

## Stack base
- Windows 11
- Python 3.11
- FastAPI
- Ollama
- SQLite

## Próximo objetivo
Semana 2 siguiente fase:
1. interfaz web mínima tipo chat
2. memoria simple persistente (`memories`)