# Professional Skill Anatomy: code-review-and-quality

Análisis de ingeniería inversa sobre la Skill profesional mantenida por Addy Osmani (`addyosmani/agent-skills`).

## Routing
- **Mecanismo de detección:** La descripción en el frontmatter YAML está redactada para capturar cualquier intención de revisión previa al merge ("Conducts multi-axis code review. Use before merging any change... Use when asked to review a diff or a pull request, even when the diff is pasted inline").
- **Estrategia de delimitación:** No intenta resolver la implementación ni ejecutar refactorizaciones de fondo; se posiciona estrictamente como una puerta de inspección de calidad antes de que el código ingrese a la rama principal.

## Workflow y Quality Gates
El procedimiento se estructura en cinco etapas secuenciales:
1. **Comprender el contexto:** Analizar qué problema resuelve el cambio antes de ver una sola línea de código (especificación, requisitos o bug report).
2. **Revisar las pruebas primero (Test-First Review):** Evaluar si las pruebas prueban comportamiento real y no detalles de implementación. Sugiere un experimento de mutación manual (invertir una condición para asegurar que la prueba falle).
3. **Revisar la implementación sobre 5 ejes:** Inspección sistemática archivo por archivo.
4. **Categorizar hallazgos:** Aplicar etiquetas de severidad sin dejar comentarios ambiguos.
5. **Verificar la verificación:** Comprobar la evidencia empírica (ejecución verde de pruebas, builds y pruebas manuales documentadas).
- **Quality Gate / Veredicto:** Termina con un veredicto binario explícito: `Approve` (si mejora la salud general del sistema) o `Request changes` (si existen bloqueadores críticos).

## Review Axes (Ejes de Revisión)
1. **Correctness (Corrección):** Alineación con la especificación, manejo de casos límite, caminos de error y ausencia de condiciones de carrera o *off-by-one*.
2. **Readability & Simplicity (Legibilidad y Simplicidad):** Claridad en nombres, flujo de control directo, justificación de abstracciones y eliminación de código muerto o ramas temporales.
3. **Architecture (Arquitectura):** Dirección de dependencias, límites modulares limpios y evaluación de si un refactor realmente reduce la carga conceptual o solo reubica la complejidad.
4. **Security (Seguridad):** Sanitización en fronteras del sistema, ausencia de credenciales embebidas, consultas parametrizadas y validación de datos externos no confiables.
5. **Performance (Rendimiento):** Identificación de patrones N+1, operaciones síncronas bloqueantes, re-renderizados innecesarios y ausencia de paginación en listas.

## Severity (Modelo de Severidad)
La Skill prescribe prefijos obligatorios para evitar que el autor pierda tiempo en nimiedades:
- `Critical:` Bloquea el merge. Aplica a vulnerabilidades de seguridad, pérdida de integridad o funcionalidad rota.
- `(Sin prefijo / Required):` Cambio obligatorio para cumplir el estándar antes del merge.
- `Nit:` Observación menor y opcional (estilo, formato). El autor puede ignorarla.
- `Optional:` / `Consider:` Sugerencia técnica valiosa pero no bloqueante.
- `FYI:` Informativo; contexto útil para futuras iteraciones.

## Verification
Exige verificar la evidencia antes de emitir veredicto:
- Pruebas ejecutadas y en verde.
- Build exitoso.
- Verificación de la historia de verificación del autor (si probó manualmente o adjuntó capturas).
- Experimento de mutación cuando la cobertura genera dudas sobre si detectaría una regresión.

## Composition (Composición con otras Skills)
Se integra dentro de una red de skills especializadas mediante enlaces a guías compartidas:
- `../../references/security-checklist.md` y la skill `security-and-hardening`.
- `../../references/performance-checklist.md` y la skill `performance-optimization`.
- `constraint-driven-development` para puntuación de mutaciones y contratos de calidad del proyecto.

## Boundaries y Límites de Autoridad
- **Decisión humana:** Establece el principio de que el humano tiene la última palabra (*Human makes the final call*).
- **Prohibición de mutaciones no acordadas:** Prohíbe borrar código muerto o cambiar arquitectura sin consultar al autor ("Ask before deleting").
- **Honestidad técnica:** Instruye al agente a evitar el *sycophancy* (adulación complaciente o dar un "LGTM" superficial sin evidencia). Si hay problemas estructurales, exige señalarlos directamente junto con una solución nombrada (*Structural Remedies*).
