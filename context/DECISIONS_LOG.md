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
- Se instalaron estos modelos:
  - `qwen2.5:3b` para pruebas rápidas/general
  - `qwen2.5-coder:7b` como candidato principal para programación
  - `llama3:8b` disponible como referencia generalista
- El endpoint `/chat` ya se comunica con Ollama.

## Nomenclatura del Equipo (Actualización)
- **El Usuario / Líder del proyecto:** Anyelo (Jefe).
- **Asistente Técnica Local (El Proyecto):** Rouse (anteriormente referida como Sol en el roadmap original).
- **Asistente IA externa (ChatGPT):** Sol (anteriormente referida como Wilson).
- **Secretaria Virtual de apoyo:** María.

## Cierre de Semana 1
- Se completó la fase "Tiene pulso".
- El endpoint `/chat` funciona perfectamente con resolutor de modelos (`qwen2.5-coder:7b` y `qwen2.5:3b`).
- El prompt de sistema se desacopló exitosamente en `app/prompts/system_prompt.txt`.