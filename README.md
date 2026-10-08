# ADA-07: Build an Agent Skill

Proyecto de diseño, implementación, evaluación y adopción comparativa de una **Agent Skill** orientada a un proceso profesional de Ingeniería de Software: **Pull Request Readiness Review**.

Curso: **Ingeniería de Software asistida por IA · UADY**  
Autor: Estudiante de Ingeniería de Software  

---

## 📁 Estructura del Proyecto

El repositorio cumple de forma exacta la estructura requerida en la especificación de la práctica:

```text
ada-07-agent-skill/
├── .agents/
│   ├── references/                                # Referencias compartidas del ecosistema
│   └── skills/
│       ├── reviewing_pull_requests/              # Skill construida en Parte I
│       │   ├── SKILL.md                          # Workflow compacto, routing y boundaries
│       │   ├── references/
│       │   │   ├── review_checklist.md           # Checklist de ingeniería de software
│       │   │   └── severity_guide.md             # Guía de clasificación de severidades
│       │   ├── scripts/
│       │   │   └── validate_review_report.py     # Validador determinista en Python
│       │   ├── assets/
│       │   │   └── review_report_template.md     # Plantilla estandarizada de reporte
│       │   └── evals/
│       │       ├── trigger_cases.json            # 3 casos positivos y 3 negativos
│       │       └── execution_cases.json          # Casos de ejecución y boundary case
│       └── code-review-and-quality/              # Skill profesional adoptada en Parte II
│           └── SKILL.md                          # Skill de Addy Osmani (commit 1401c8b)
├── docs/
│   ├── skill_workflow_observation.md             # Observación del flujo manual de revisión
│   ├── third_party_skill_audit.md                # Auditoría de seguridad antes de instalar
│   └── professional_skill_anatomy.md             # Análisis de ingeniería inversa
├── results/
│   ├── pr-readiness-review.md                    # Reporte de revisión de mi Skill
│   ├── skill-evaluation-report.md                # Resultados de pruebas de la Skill e iteración
│   ├── professional-skill-review.md              # Reporte de revisión con la Skill profesional
│   └── skill-comparison.md                       # Matriz comparativa y lecciones aprendidas
├── AI_USAGE_LOG.md                               # Bitácora con 6 entradas significativas
└── README.md                                     # Documentación general y respuestas de reflexión
```

---

## 🛠️ Verificación Rápida de la Skill

Para validar de forma determinista la estructura del reporte generado:

```bash
python .agents/skills/reviewing_pull_requests/scripts/validate_review_report.py results/pr-readiness-review.md
```

Salida esperada:
```text
VALID: PR readiness review structure is complete.
(Exit code: 0)
```

---

## 🧠 Respuestas a las Preguntas de Reflexión (Sección 22)

### 1. ¿Qué parte del workflow pertenece al juicio del LLM y cuál debe ser determinista?
El juicio del LLM es ideal para el análisis semántico: contrastar la intención de un requisito con el código escrito, evaluar si un nombre es descriptivo, estimar el impacto arquitectónico y redactar recomendaciones claras. Por el contrario, la extracción de diffs (`git diff`), la ejecución de la suite de pruebas y la comprobación de que el reporte contenga las secciones requeridas y conteos íntegros deben ser estrictamente deterministas mediante comandos y scripts.

### 2. ¿Qué información moviste de SKILL.md a references/ y por qué?
Moví el checklist detallado de revisión (`review_checklist.md`) y las descripciones extensas de severidad (`severity_guide.md`). Mantenerlos en el archivo principal saturaría la ventana de contexto cada vez que el agente solo necesita decidir si activar o no la Skill. Bajo el principio de *Progressive Disclosure*, el archivo principal conserva únicamente el flujo de control, cargando las referencias bajo demanda solo durante la ejecución.

### 3. ¿Qué función cumple la description del frontmatter en el routing?
Funciona como el algoritmo de selección y enrutamiento del agente. No es solo un resumen documental; el modelo lee esa descripción para evaluar si la petición del usuario encaja con la habilidad. Incluir cláusulas afirmativas ("Use when...") y negativas ("Do NOT use to...") reduce drásticamente las activaciones falsas o prematuras.

### 4. ¿Qué prompt negativo fue más difícil de evitar que activara la Skill?
El caso *"Merge PR #42"*. Al contener las palabras clave "PR" y un número de pull request, el modelo tiende por asociación léxica a relacionarlo con una tarea de revisión. Para contenerlo, fue necesario explicitar en el frontmatter que las operaciones de merge y mutación no forman parte de las atribuciones de la Skill.

### 5. ¿Qué diferencia práctica observaste entre una Skill y un MCP Server?
El MCP Server proporciona **alcance y capacidades** (por ejemplo, herramientas para leer ramas, listar issues o comunicarse con la API de GitHub). La Skill proporciona el **procedimiento y conocimiento metodológico** (*know-how*) sobre cómo, cuándo y en qué orden emplear esas capacidades dentro de un estándar de ingeniería.

### 6. ¿Qué aporta el script que no conviene resolver con instrucciones de lenguaje natural?
Garantía absoluta de consistencia. El lenguaje natural está sujeto a variabilidad probabilística: un modelo puede omitir un encabezado, redactar de forma distinta una etiqueta o alterar un formato JSON sin darse cuenta. Un script en Python verifica reglas deterministas de manera implacable mediante expresiones regulares y códigos de salida binarios (`0` o `1`).

### 7. ¿Qué riesgo existiría si esta Skill pudiera comentar o hacer merge en GitHub?
Riesgo de automatización descontrolada (*runaway actions*). Si el agente malinterpreta un requisito o pasa por alto un caso de prueba sutil, podría fusionar a la rama productiva código incompleto o publicar comentarios confusos en el repositorio del equipo sin supervisión humana. Mantener la Skill en nivel *Draft-Only* asegura que el juicio humano permanezca en el bucle (*Human-in-the-loop*).

### 8. ¿Qué cambió entre la primera y la última versión de tu Skill?
En la versión 1.0.0, la frontera de parada era débil y el validador en Python solo revisaba encabezados de nivel 2. En la versión 1.0.1, endurecimos el frontmatter con anti-triggers tajantes, explicitamos la prohibición de escrituras en la sección de seguridad y añadimos al validador expresiones regulares para forzar la declaración `Human decision required: YES` y el conteo de hallazgos.

### 9. ¿Qué evidencia te permite afirmar que la Skill es reutilizable?
La separación de responsabilidades: `SKILL.md` no contiene rutas quemadas (*hardcoded*) ni nombres de funciones específicos de una sola aplicación. Puede ejecutarse sobre cualquier repositorio Git que contenga código, pruebas y un documento de especificaciones normativo.

### 10. ¿Qué otro proceso profesional de Ingeniería de Software convertirías en una Skill?
El proceso de **Análisis de Impacto y Generación de Migraciones de Base de Datos**. Un flujo donde el agente revise modelos ORM cambiados, verifique si la migración es destructiva (e.g. eliminación de columnas), consulte una guía de compatibilidad hacia atrás y genere un script SQL seguro con una prueba de *rollback*.

### 11. ¿Qué diferencia de diseño fue más evidente entre tu Skill y code-review-and-quality?
El nivel de densidad y estructuración de archivos. Mi Skill aplica un diseño modular y compacto con *Progressive Disclosure* y validación determinista por script. La Skill profesional de Addy Osmani es un manual exhaustivo y monolítico de casi 400 líneas en un solo archivo, con una profundidad analítica impresionante pero con un consumo mucho mayor de contexto inicial.

### 12. ¿Qué ventaja y qué costo observaste al usar una Skill mucho más extensa y opinionated?
- **Ventaja:** Establece criterios de ingeniería de altísimo nivel (como la técnica de pruebas de mutación y remedios estructurales con nombres estándar), guiando al agente hacia un análisis más profundo y menos superficial.
- **Costo:** Consume más de 20 KB de contexto en cada invocación, lo que eleva el costo de tokens, puede ralentizar la respuesta del agente y diluye el enfoque si la tarea a revisar es pequeña.

### 13. ¿Qué controles aplicarías antes de adoptar una Skill de terceros en un repositorio empresarial?
1. **Auditoría de fuente y mantenedor:** Verificar la reputación del repositorio origen.
2. **Fijación de versión (Pinning):** Registrar el commit hash específico para evitar modificaciones silenciosas aguas arriba.
3. **Inspección de scripts ejecutables:** Asegurar que no contenga llamadas de red, descarga de binarios opacos ni recolección de telemetría.
4. **Verificación de permisos y secretos:** Confirmar que no requiera variables de entorno sensibles ni credenciales de producción.

### 14. Después de estudiar la Skill profesional, ¿qué cambiarías en una versión 2 de tu Skill y cómo evaluarías que realmente mejoró?
En una versión 2 incorporaría la técnica de **Test-First Review con pruebas de mutación** y añadiría el nivel de severidad `Nit:` para separar comentarios estilísticos de problemas funcionales. Evaluaría la mejora introduciendo intencionalmente una regresión lógica en una rama de prueba donde los tests unitarios pasen por accidente; si la versión 2 detecta la debilidad del test mediante el análisis de mutación y la versión 1 no, la mejora estará empíricamente comprobada.
