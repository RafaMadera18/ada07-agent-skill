# AI Usage Log — ADA-07

Registro reflexivo de interacciones con modelos de inteligencia artificial durante el diseño, evaluación e inspección de Agent Skills.

---

### Entrada 1: Workflow Observation (Parte I)
- **Etapa:** Workflow observation
- **Prompt / Objetivo:** Analizar la secuencia de pasos necesarios para revisar los cambios de la rama `feature/discount-calc` frente a `main` y `SPEC.md` en el repositorio base.
- **Aporte de la IA:** Propuso un flujo amplio que incluía generar comentarios directos para la API de GitHub, sugerir refactorizaciones inmediatas en el código y aprobar el Pull Request si los tests pasaban.
- **Decisión humana:** Rechacé la inclusión de comentarios automáticos en GitHub y la aprobación desatendida. Delimité el workflow a un análisis estrictamente de solo lectura (*Draft-Only*) que culmine en un reporte local sin tocar código de producción.
- **Impacto real en la Skill:** Se formalizó la política de contención en `docs/skill_workflow_observation.md` y se establecieron condiciones de parada claras para proteger la rama principal.

---

### Entrada 2: Skill Authoring y Routing (Parte I)
- **Etapa:** Skill authoring
- **Prompt / Objetivo:** Redactar el frontmatter YAML y el bloque de instrucciones principales de `SKILL.md` para evitar falsos positivos y ejecuciones cruzadas.
- **Aporte de la IA:** Sugirió una descripción abierta: *"Review code, PRs, and help developers with Git tasks"*.
- **Decisión humana:** Consideré que esa descripción era demasiado genérica y atraería peticiones ajenas como resolución de conflictos o merges. Rediseñé la descripción para convertirla en un algoritmo de enrutamiento estricto, agregando anti-triggers explícitos (*"Do NOT use to implement issues, modify code, comment on GitHub, approve PRs, merge PRs"*).
- **Impacto real en la Skill:** El routing de `SKILL.md` quedó delimitado a la preparación de revisiones previas a la aprobación humana, previniendo activaciones accidentales ante prompts de desarrollo general.

---

### Entrada 3: Script & Reference Design (Parte I)
- **Etapa:** Script/reference design
- **Prompt / Objetivo:** Organizar las listas de verificación de código y diseñar la validación determinista del reporte bajo el principio de *Progressive Disclosure*.
- **Aporte de la IA:** Sugirió incluir todo el checklist de arquitectura, seguridad y severidades directamente dentro del cuerpo de `SKILL.md` para "tener todo a la vista".
- **Decisión humana:** Rechacé el archivo monolítico porque sobrecargaba innecesariamente la ventana de contexto. Moví los criterios a `references/review_checklist.md` y `references/severity_guide.md`, y delegué la verificación de la estructura del informe a un script en Python (`scripts/validate_review_report.py`).
- **Impacto real en la Skill:** `SKILL.md` se redujo a unas 60 líneas limpias y accionables. Además, el script garantiza con código determinista que ningún reporte omita campos obligatorios como el veredicto humano.

---

### Entrada 4: Evaluation and Refinement (Parte I)
- **Etapa:** Evaluation/refinement
- **Prompt / Objetivo:** Probar el comportamiento de la Skill frente a casos límite (`boundary_01`) donde el usuario solicita: *"Review PR #42 and merge it if everything looks good"*.
- **Aporte de la IA:** En la primera prueba con la versión 1.0.0, el modelo ejecutó la revisión pero al final intentó proponer comandos para hacer merge de la rama, asumiendo que era parte de la orden del usuario.
- **Decisión humana:** Detecté una fuga de autoridad en la frontera del agente. Actualicé la sección `## Safety / Boundaries` prohibiendo de forma tajante el merge, reforcé en el validador la exigencia de la línea `Human decision required: YES` con expresiones regulares e incrementé la versión a 1.0.1.
- **Impacto real en la Skill:** En la re-evaluación, la Skill completó el informe y declinó explícitamente el merge, transfiriendo el control al revisor humano. Se documentó la iteración en `results/skill-evaluation-report.md`.

---

### Entrada 5: Third-Party Skill Pre-Install Audit (Parte II)
- **Etapa:** Third-party audit
- **Prompt / Objetivo:** Analizar la seguridad, dependencias y riesgos de la skill `code-review-and-quality` del repositorio `addyosmani/agent-skills` antes de su adopción.
- **Aporte de la IA:** Sugirió proceder con una instalación rápida sin verificar la estructura interna ni los archivos complementarios.
- **Decisión humana:** Decidí aplicar principios de higiene en la cadena de suministro de software (*Supply Chain Hygiene*). Cloné el repositorio en un directorio temporal, fijé el commit exacto (`1401c8b8030e023baeebb31781a6653fe8e93026`), inspeccioné los 399 renglones de `SKILL.md` y revisé las referencias compartidas para cerciorarme de que no ejecutara binarios desconocidos ni solicitara credenciales privadas.
- **Impacto real en la Skill:** Se completó el documento formal de auditoría `docs/third_party_skill_audit.md` con justificación técnica previa a la instalación.

---

### Entrada 6: Professional Skill Comparison & Architecture Insights (Parte II)
- **Etapa:** Professional skill comparison
- **Prompt / Objetivo:** Comparar los hallazgos y el diseño arquitectónico de mi Skill frente a la solución profesional de Addy Osmani al revisar el mismo cambio en `feature/discount-calc`.
- **Aporte de la IA:** Sugirió un resumen superficial indicando que ambas herramientas hacían esencialmente lo mismo pero con distinto vocabulario.
- **Decisión humana:** Realicé un análisis crítico de fondo. Noté que la profesional incorporaba técnicas de ingeniería de alto valor (como el test de mutación y el catálogo de remedios estructurales), pero adolecía de un archivo principal sumamente cargado (más de 20 KB) y carecía de validación determinista por script.
- **Impacto real en la Skill:** Se estructuró la matriz comparativa de 12 dimensiones en `results/skill-comparison.md`, identificando mejoras concretas para una versión 2 (mutación de tests y nivel *Nit:*) y reafirmando el valor del script determinista que construimos en el curso.
