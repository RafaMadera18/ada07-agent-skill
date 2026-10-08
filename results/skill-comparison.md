# Professional Skill Study & Comparison — ADA-07

## Source & Identification
- **Repository:** `https://github.com/addyosmani/agent-skills`
- **Skill:** `code-review-and-quality`
- **Version / Commit:** `1401c8b8030e023baeebb31781a6653fe8e93026`
- **Installed Path:** `.agents/skills/code-review-and-quality/` (y referencias compartidas en `.agents/references/`)

## Why this Skill was Selected
Se eligió porque encapsula un proceso estándar de la industria para revisión de código antes de merge. Su enfoque cubre de forma exhaustiva cinco dimensiones críticas de calidad de software y maneja un sistema de puertas de calidad (*quality gates*) maduro, lo que ofrece un contraste directo frente al flujo de preparación de PRs que construimos en el curso.

---

## Comparativa Dimensional: Mi Skill vs. Skill Profesional

| Dimensión | Mi Skill (`reviewing_pull_requests`) | Profesional (`code-review-and-quality`) | Conclusión / Aprendizaje |
|---|---|---|---|
| **Trigger / Routing** | Enfocado en preparación de PR y readiness para revisión humana. | Orientado a revisión profunda multi-eje previa al merge de cualquier cambio. | La profesional tiene un espectro de disparo más amplio; mi skill es más precisa para flujos previos a la intervención humana. |
| **Scope / Boundaries** | Estrictamente *Draft-Only*; prohíbe comentar en GitHub, modificar código o hacer merge. | Asume un rol de evaluador con estándar de aprobación (*Approve / Request changes*), delegando la decisión final al humano. | Mi skill impone barreras deterministas más cerradas para prevenir cualquier mutación accidental en repositorios. |
| **Workflow Depth** | 10 pasos lineales con validación determinista por script al final. | 5 fases metodológicas con énfasis en "Test-First" y experimentos de mutación. | La profesional profundiza más en la lógica analítica; mi skill destaca por su verificación de formato asistida por código. |
| **Correctness** | Comprueba conformidad directa contra requisitos normativos (`SPEC.md`). | Analiza requisitos, caminos de error, casos límite, condiciones de carrera y mutaciones. | Ambas garantizan la corrección, pero la profesional indaga más en riesgos sutiles de concurrencia e invariantes. |
| **Architecture** | Revisa límites documentados y actualización de `ARCHITECTURE.md`. | Evalúa si un refactor reduce conceptos o solo reubica complejidad; aplica remedios estructurales nombrados. | La profesional aporta un marco conceptual superior para juzgar deuda técnica y abstracciones prematuras. |
| **Security** | Verificación básica: credenciales expuestas y sanitización general. | Revisa superficies de ataque, flujos de datos no confiables y se apoya en `security-checklist.md`. | La profesional tiene una cobertura de seguridad más rigurosa para código productivo expuesto a internet. |
| **Performance** | Revisión empírica no exhaustiva orientada a pruebas funcionales. | Revisa patrones N+1, paginación, operaciones síncronas bloqueantes y coste en rutas críticas. | La profesional está mejor armada para backends de alto rendimiento y aplicaciones web complejas. |
| **Tests / Verification** | Ejecuta la suite de pruebas automatizadas con el runner (`unittest`/`pytest`). | Revisa tests primero y promueve verificar la robustez invirtiendo condiciones para comprobar si fallan. | El enfoque de mutación manual antes de mirar el código fuente eleva el escepticismo técnico del agente. |
| **Severity Model** | 3 niveles: MUST FIX, SHOULD FIX, OPTIONAL. | 5 niveles: Critical, Required (sin prefijo), Nit, Optional/Consider, FYI. | El modelo de 5 niveles distingue claramente los nits cosméticos de los cambios indispensables. |
| **Human Review** | Requiere explícitamente `Human decision required: YES` verificado por script. | Fomenta la resolución colaborativa de desacuerdos dejando el veredicto en manos del humano. | La verificación determinista de la intervención humana en mi skill previene automatizaciones peligrosas. |
| **References / Composition** | Checklist específico de ingeniería y guía de severidad desacoplados en `references/`. | Se compone con múltiples skills del ecosistema (`security-and-hardening`, `performance-optimization`). | La composición modular del repositorio profesional muestra cómo escalar un conjunto completo de capacidades. |
| **Reusability** | Alta en proyectos del curso con especificación formal y suites de pruebas locales. | Universal para cualquier proyecto o lenguaje, independientemente de la tecnología. | La profesional es agnóstica del stack; mi skill está mejor adaptada a los estándares de entrega del laboratorio. |

---

## Análisis Crítico y Preguntas de la Práctica

### 1. ¿Qué hace la Skill profesional que mi Skill no contempló?
Propone la técnica de **Test-First Review con mutación experimental**. En lugar de asumir que porque una suite pasa el código es confiable, sugiere invertir deliberadamente una condición booleana para comprobar si las pruebas realmente atrapan el fallo. Asimismo, incorpora el catálogo de **Structural Remedies**, que exige al revisor no limitarse a quejarse de la complejidad, sino sugerir una reestructuración con nombre propio (por ejemplo, reemplazar condicionales con un despachador tipado).

### 2. ¿Qué elementos de mi Skill son más específicos al curso/proyecto y conviene conservar?
1. **La validación determinista del reporte (`validate_review_report.py`):** Ninguna instrucción en lenguaje natural garantiza al 100% que el modelo no olvide un encabezado o una métrica; un script sí lo asegura.
2. **La cláusula `Human decision required: YES`:** Mantiene la garantía inquebrantable de que el sistema opera en nivel *Draft-Only*.
3. **El mapeo explícito contra `SPEC.md` / `REQUIREMENTS.md`:** La skill profesional asume que la especificación puede ser tácita o provenir del commit; en nuestro entorno académico, el contrato de especificación es la fuente de verdad.

### 3. ¿Qué agregaría a una versión 2 de mi Skill?
- Incorporar el paso de **análisis de mutación en pruebas**: antes de certificar que un test es suficiente, verificar qué pasaría si se altera una rama condicional.
- Ampliar el catálogo de severidades incorporando la etiqueta `Nit:` para separar claramente el formato y el estilo de los problemas funcionales o arquitectónicos.
- Añadir verificación de dimensionamiento del diff (*change sizing*) para advertir cuando una rama introduce demasiadas líneas en un solo cambio.

### 4. ¿Qué NO copiaría y por qué?
No copiaría el tamaño monolítico de su `SKILL.md` (casi 400 líneas y más de 20 KB de texto directo en el archivo principal). Esto contradice el principio de **Progressive Disclosure**, saturando la ventana de contexto del agente en cada activación. Es mucho más limpio conservar el procedimiento en 80-100 líneas y mover las listas de verificación de arquitectura, seguridad y rendimiento a archivos individuales en `references/`.

### 5. ¿Cuál produjo hallazgos más accionables? (Dos ejemplos concretos)
Ambas produjeron hallazgos valiosos sobre el cambio de `feature/discount-calc`, pero la Skill profesional aportó mayor precisión en los siguientes puntos:

1. **Hallazgo de precisión numérica y redondeo intermedio:**
   - *Mi Skill:* Identificó que `round(discounted, 2)` podía generar diferencias de centavos y sugirió documentarlo como `SHOULD FIX`.
   - *Skill Profesional:* Argumentó bajo el eje de *Correctness* que truncar centavos antes de calcular impuestos (`apply_tax`) altera el resultado fiscal final acumulado, clasificándolo como un cambio obligatorio (`Required`) y proponiendo delegar el redondeo a la función de liquidación final. Fue un análisis más riguroso.
2. **Hallazgo de diseño de API y orquestación:**
   - *Mi Skill:* No cuestionó la conveniencia de exponer la función aislada.
   - *Skill Profesional:* Señaló que dejar que el llamador calcule manualmente el orden expone al sistema a que otro desarrollador calcule impuestos antes de descuentos, sugiriendo crear una función orquestadora de alto nivel (`calculate_total`).

---

## Hallazgos Únicos de Cada Skill

### Hallazgos únicos de la Skill Profesional:
1. **Observación sobre el orden de orquestación:** Planteó la necesidad de proteger la API pública para que el consumidor no deba recordar manualmente aplicar el descuento antes del impuesto.
2. **Detección de falta de pruebas de mutación:** Señaló que no hay pruebas de integración que conecten el flujo completo (`subtotal -> discount -> tax`) en un solo caso automatizado.

### Hallazgos únicos de mi Skill:
1. **Contraste normativo directo con `REQ-003` de `SPEC.md`:** Rastreó explícitamente el identificador de requerimiento y los criterios de aceptación del archivo del proyecto.
2. **Garantía verificada de no-modificación:** Confirmó de forma determinista mediante el script la presencia de la decisión humana y el recuento exacto de incidencias en el artefacto final.

---

## Evaluación de Supply Chain y Seguridad (II.6)

| Control | Evidencia en la Auditoría |
|---|---|
| **Source** | Repositorio público oficial `addyosmani/agent-skills` (mantenedor de Google / Chrome Engineering). |
| **Pinning** | Commit exacto documentado: `1401c8b8030e023baeebb31781a6653fe8e93026`. |
| **Audit** | Inspección completa de los 399 renglones de `SKILL.md` y archivos auxiliares en `references/`. |
| **Secrets** | No solicita, no requiere ni contiene tokens, variables de entorno sensibles ni credenciales API. |
| **Commands** | No ejecuta scripts binarios compilados ni comandos en segundo plano con privilegios elevados. |
| **Permissions** | Opera exclusivamente con herramientas de inspección de archivos locales (`read-only`). |
| **Change control** | La instalación quedó congelada localmente en `.agents/skills/code-review-and-quality/` sin auto-actualización silenciosa. |

---

## Conclusión Humana
Adoptar y contrastar una Skill profesional demostró que una Skill no es un prompt largo, sino un procedimiento estructurado. La Skill de Addy Osmani sobresale en su rigor metodológico y en sus criterios de ingeniería de software madura (ejes de calidad, mutación de tests y remedios estructurales). Por su parte, la Skill que diseñamos en la Parte I demostró la enorme ventaja de la **arquitectura modular con Progressive Disclosure** y del **Shift Intelligence Left**: confiar en un script determinista para validar la integridad del artefacto reduce drásticamente las fallas que un modelo de lenguaje comete al redactar salidas estructuradas. Una versión 2 ideal combinaría la profundidad analítica de la primera con la validación determinista y la economía de tokens de la segunda.
