# HANDOFF - Estado actual de Rouse Local

## Resumen
Rouse Local ya tiene backend funcional con FastAPI, conexión real a Ollama y la base inicial de persistencia con SQLite.

## Estado actual confirmado
- Proyecto: Rouse Local
- Asistente: Rouse
- Backend: FastAPI
- Entorno virtual configurado
- Repositorio Git inicializado
- Endpoint `/health` funcionando
- Endpoint `/chat` funcionando
- Ollama instalado y probado

## Modelos instalados
- `qwen2.5:3b`
- `qwen2.5-coder:7b`
- `llama3:8b`

---

# Semana 2 - progreso actual

## Ya implementado
### Persistencia base con SQLite
Se agregó `app/db/` con:

- `database.py`
- `models.py`
- `crud.py`

### Base de datos física
La base ya no es temporal.  
Existe archivo físico en:

data/db/rouse.db

## Tareas de María - Día 3
### Objetivo general
Convertir el chat actual en una primera versión de Rouse con identidad base y selección de modelo más limpia.

### Tarea 1 — Prompt base de Rouse
Crear un prompt de sistema para Rouse en `app/prompts/`, por ejemplo:
- `app/prompts/system_prompt.txt`

Debe definir:
- rol de Rouse como asistente técnico personal
- tono claro, crítico y útil
- capacidad de alternar entre conversación casual y ayuda de programación
- prioridad por precisión y estructura
- evitar respuestas excesivamente complacientes

### Tarea 2 — Refactor de `llm_service.py`
Modificar el servicio para que:
- cargue un prompt de sistema desde archivo
- envíe `system + user` al modelo
- acepte el nombre del modelo como parámetro
- deje lista la estructura para luego añadir memoria

### Tarea 3 — Configuración central de modelos
Usar `app/config.py` para definir al menos:
- modelo general por defecto: `qwen2.5:3b`
- modelo coding por defecto: `qwen2.5-coder:7b`

Opcional:
- un helper para resolver modo `"general"` o `"coding"` a nombre de modelo

### Tarea 4 — Mejorar contrato de `/chat`
Ajustar el request para que acepte algo como:
- `message`
- `model` opcional
- o `mode` con valores tipo `"general"` / `"coding"`

La idea es que si no se manda `model`, el sistema pueda usar el modelo según el modo.

### Tarea 5 — No tocar todavía memoria persistente
No implementar aún SQLite/RAG/memoria larga.
Solo dejar la arquitectura lista para que la siguiente fase agregue memoria sin romper `/chat`.

## Resultado esperado al terminar Día 3
- Rouse responde usando un prompt de sistema real
- existe distinción entre modo general y modo coding
- la selección de modelo está centralizada
- `/chat` queda más limpio y preparado para la fase de memoria