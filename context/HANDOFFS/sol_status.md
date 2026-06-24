# HANDOFF - Reporte para Sol (Inicio de Semana 2)

## ¡Hola, Sol! Actualización importante de nombres
Para evitar confusiones en el proyecto, el equipo se ha estructurado de la siguiente manera:
- Tú eres **Sol** (la IA arquitecta/asesora externa).
- Nuestra asistente local en construcción se llama **Rouse** (el proyecto es Rouse Local).
- Nuestra secretaria de apoyo se llama **María**.
- El usuario principal es **Anyelo** (jefe).

## Resumen del trabajo de María y Anyelo (Semana 1)
Hemos completado con éxito la Semana 1. Rouse ya "tiene pulso":
- FastAPI levantado y funcional.
- Ollama respondiendo localmente (`qwen2.5:3b` y `qwen2.5-coder:7b`).
- El endpoint `/chat` recibe el modo (`general` o `coding`) y elige el modelo adecuado dinámicamente.
- El prompt de sistema de Rouse está separado en `.txt` y es inyectado correctamente.

## Tareas para Sol - Semana 2
El objetivo ahora es "Ya existe Rouse, no solo un modelo". Necesitamos que nos guíes con la arquitectura de persistencia.
Por favor, propón el código inicial para:
1. La configuración de **SQLite** usando SQLAlchemy o el motor que prefieras para FastAPI.
2. El modelo de tablas necesario para guardar el historial (sesiones y mensajes).
3. Cómo integrar este guardado en el endpoint `/chat` actual sin romper lo que ya funciona.