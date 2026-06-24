# ROADMAP - 12 semanas

## Semana 1: "Tiene pulso"
### **Objetivo:** Obtener el primer mensaje real con modelo local y backend mínimo.

#### *Entregables:*
- Instalar Python, Ollama, Git, VS Code
- Crear repo del proyecto
- Levantar un script o FastAPI mínimo
- Hacer una llamada al modelo local
- Responder desde terminal o una página mínima
- Definir estructura inicial de carpetas

#### *Resultado:*

Tú escribes "hola" y Rouse responde desde tu sistema, no desde una web ajena.
Tiempo estimado: 1 a 3 días

## Semana 2: "Ya existe Rouse, no solo un modelo"
### **Objetivo:** Meter personalidad base y persistencia mínima.

#### *Entregables:*
- Persona.json / system_prompt.md
- Loader de personalidad
- SQLite inicial
- Tabla de conversaciones
- Tabla de memoria simple
- Guardar y cargar historial corto
- Interfaz web mínima tipo chat

#### *Resultado:*

Ya no hablas con "el modelo"; hablas con una primera versión de Rouse.


## Semana 3: "Memoria básica útil"
### **Objetivo:** Que recuerde hechos importantes y contexto personal simple.

### *Entregables:*
- Esquema de memoria:
        * Perfil del usuario
        * Recuerdos persistentes
        * Notas de sesión
        * Reglas para guardar memoria
        * Endpoint para consultar/guardar memoria
        * Inyección de memoria relevante al prompt

### *Resultado:*

Rouse ya puede recordar cosas tuyas de forma controlada.


## Semana 4: "Modo técnico"
### **Objetivo:** Separar conversación casual de ayuda técnica.

### *Entregables:*
- Sistema de modos:
        * Casual
        * Coding
        * Planning
        * Prompts por modo
        * Selector de modo en backend/UI
        * Reglas de respuesta por modo

### *Resultado:*

Ya no responde igual si estás filosofando que si estás depurando Java.


## Semana 5: "Lee tus carpetas"
### **Objetivo:** Darle acceso seguro a una zona de archivos.

### *Entregables:*
- Carpeta raíz Documents/IA/
        * Funciones seguras:
                * Listar archivos
                * Leer archivo
                * Leer árbol de proyecto
                * Whitelist de rutas
        * Primeras pruebas con un proyecto tuyo real

### *Resultado:*

Rouse puede revisar material real, no solo inventar desde el vacío.


## Semana 6: "Contexto de proyecto"
### **Objetivo:** Que entienda qué proyecto estás tocando y pueda ayudarte con más precisión.

### *Entregables:*
- Entidad project
- Metadata por proyecto
- Conversación asociada a proyecto
- Comando para fijar proyecto activo
- Resumen de proyecto / notas de proyecto

### *Resultado:*

Puedes decir "vamos con el proyecto X" y no empezar desde cero cada vez.


## Semana 7: "RAG básico"
### **Objetivo:** Que recupere fragmentos relevantes de tus notas/proyectos.

#### *Entregables:*
- Indexador de documentos
- Embeddings
- Vector store simple
- Chunking de archivos
- Recuperación top-k
- Integración de contexto recuperado al prompt

### *Resultado:*

Rouse ya no depende solo del historial; puede buscar en tu material.


## Semana 8: "Ayuda técnica de verdad"
### **Objetivo:** Pasar de "chat con contexto" a asistente técnico usable.

### *Entregables:*
- Herramientas tipo:
        * Buscar texto en proyecto
        * Localizar archivos relacionados
        * Resumir módulo
        * Extraer stacktrace / error si se lo das
        * Plantilla de respuesta técnica
        * Prompts para debugging, refactor y explicación

### *Resultado:*

Aquí empieza a servir de verdad para programación.


## Semana 9: "Resúmenes y continuidad"
### **Objetivo:** Que no se vuelva amnésica con sesiones largas.

### *Entregables:*
- Resumen automático de sesión
- Resumen por proyecto
- Compresión de historial viejo
- Memoria de "pendientes / siguiente paso"

### *Resultados:*

Puedes retomar trabajo sin tener que reexplicarle toda tu existencia.


## Semana 10: "Móvil fuera de casa"
### **Objetivo:** Acceso desde Android sin depender solo de red local.

### *Entregables:*
- Acceso remoto seguro a tu backend
- Autenticación básica
- Pruebas desde datos móviles
- Ajustes de UI móvil

### *Resultado:*

Puedes escribirle desde la calle sin estar en la misma Wi-Fi.


## Semana 11: "Estabilización"
### **Objetivo:** Dejar de meter features y empezar a quitar fragilidad.

### *Entregibles:*
- Logs
- Manejo de errores
- Backups de SQLite/memoria
- Limpieza de prompts
- Pruebas con proyectos reales
- Pulido de latencia y respuestas

### *Resultado:*

Menos demo, más herramienta.


## Semana 12: "Cierre v1"
### **Objetivo:** Cerrar una v1 usable con criterio.

### *Entregibles:*
- Checklist de funcionalidades
- Documentación mínima del sistema
- Script de arranque limpio
- Export/import de memoria básica
- Plan de v1.1:
        * Voz
        * Mejor móvil
        * Automatizaciones
        * Mejoras de coding mode

### *Resultado:*

Rouse Local v1 ya existe y ya se puede usar en serio.