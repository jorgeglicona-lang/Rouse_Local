# NEXT_STEPS (Semana 2 - Memoria y Persistencia)

1. Diseñar el esquema de la base de datos en SQLite (tablas `conversations` y `messages`).
2. Configurar la conexión a la base de datos en `app/data/`.
3. Modificar `/chat` para que reciba un `session_id` y guarde el historial del usuario.
4. Lograr que `llm_service.py` recupere los últimos N mensajes de la base de datos antes de enviar el prompt a Ollama.
5. Preparar una interfaz web mínima tipo chat (HTML/JS) para dejar de usar Swagger UI.