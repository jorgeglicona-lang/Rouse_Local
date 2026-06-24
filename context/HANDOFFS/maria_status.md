# HANDOFF - Estado actual de Rouse Local

## Resumen
Rouse Local ya tiene backend funcional con FastAPI, conexión real a Ollama, personalidad desacoplada y persistencia mínima de conversaciones con SQLite.

## Estado actual confirmado
- Proyecto: Rouse Local
- Asistente: Rouse
- Backend: FastAPI
- Entorno virtual configurado
- Repositorio Git inicializado
- Endpoint `/health` funcionando
- Endpoint `/chat` funcionando
- Ollama instalado y probado

## Modelos actuales
- `dolphin-llama3:8b` → general principal
- `llama3:8b` → general alternativo / fallback manual
- `qwen2.5-coder:7b` → coding principal

---

# Estado funcional actual

## 1. Chat con modelos locales
El endpoint `/chat` ya se comunica con Ollama y responde correctamente.

## 2. Persistencia mínima con SQLite
Ya existe `app/db/` con:
- `database.py`
- `models.py`
- `crud.py`

### Base física
`data/db/rouse.db`

### Tablas ya existentes
- conversations
- messages

### CRUD ya disponible
- `get_or_create_conversation(db, session_id)`
- `add_message(db, conversation_id, role, content)`
- `get_last_messages(db, conversation_id, limit=10)`

### 3. Historial corto persistente

`/chat` ya:

- recibe session_id
- crea o recupera conversación
- guarda mensaje del usuario
- recupera últimos N mensajes
- consulta al modelo con contexto
- guarda la respuesta de Rouse

## 4. Personalidad desacoplada

Ya existen:

- `app/prompts/system_prompt.txt`
- `app/prompts/persona.json`
- `app/services/persona_loader.py`

La ruta `/chat` ya usa el loader de personalidad en lugar de un prompt hardcodeado.

## Tarea siguiente para María
### Objetivo

Implementar la interfaz web mínima tipo chat para dejar de depender de Swagger y empezar a conversar con Rouse desde una página local.

### Entregable esperado

Una interfaz simple servida por FastAPI, con:

1. caja de texto para mensaje
2. input o selector de `session_id`
3. selector de modo:
    - general
    - coding
    - complemento
4. botón de enviar
5. área donde se muestren mensajes del usuario y respuestas de Rouse

### Alcance recomendado

**Backend**
- servir archivos estáticos o una plantilla HTML simple
- exponer una ruta tipo `/ui` o `/chat-ui`

**Frontend mínimo**
- `chat.html`
- opcionalmente `chat.js` y `chat.css`
- `fetch()` al endpoint `/chat`

### Flujo esperado

La interfaz debe mandar algo como:

```JSON
 {
  "message": "Hola Rouse",
  "session_id": "test-session-1",
  "mode": "general"
}
```
### Importante

Todavía NO implementar en este bloque:

- memoria larga
- tabla `memories`
- embeddings
- RAG
- auth
- interfaz bonita/final

Solo una UI mínima funcional para usar el sistema real sin Swagger.