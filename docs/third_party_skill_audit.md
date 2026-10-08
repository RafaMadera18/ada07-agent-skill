# Third-Party Skill Pre-Install Audit

Repository: https://github.com/addyosmani/agent-skills
Selected skill: code-review-and-quality
Version / commit inspected: `1401c8b8030e023baeebb31781a6653fe8e93026` (rama `main`, Addy Osmani)

## Purpose
Estandarizar y guiar una revisión de código multidimensional antes de realizar merge a la rama principal. La Skill evalúa cinco ejes técnicos: corrección, legibilidad/simplicidad, arquitectura, seguridad y rendimiento, aplicando puertas de calidad (*quality gates*) y etiquetado explícito de severidad.

## Trigger / Description
- **Description en frontmatter:** "Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enters the main branch. Use when asked to review a diff or a pull request, even when the diff is pasted inline."
- **Tareas que la activan:** Peticiones de revisión de Pull Requests, diffs en ramas de trabajo, revisión de cambios tras implementar una funcionalidad o corregir un bug, y evaluación de código generado por otros agentes o humanos.
- **Tareas que quedan fuera:** Implementación de código nuevo desde cero, refactorizaciones no solicitadas, resolución automática de conflictos de git o despliegue en ambientes de producción.

## Supporting References
La Skill hace referencia a recursos complementarios compartidos en el repositorio:
- `../../references/security-checklist.md`: Criterios detallados de seguridad y sanitización de entradas.
- `../../references/performance-checklist.md`: Detección de patrones N+1 y cuellos de botella.
- Referencias conceptuales a otras skills del ecosistema (`security-and-hardening`, `performance-optimization`, `constraint-driven-development`).

## Tools / Commands / Permissions
- **Lectura:** Requiere herramientas de lectura de archivos locales (`view_file`), inspección de diffs (`git diff`) y herramientas de acceso a repositorios/PRs si se opera vía GitHub MCP.
- **Ejecución:** No incluye scripts binarios propios embebidos con permisos elevados, pero instruye al agente a ejecutar comandos de prueba locales (como suites de testing y mutaciones controladas para verificar que las pruebas fallen ante cambios adversos).
- **Escritura:** No ejecuta mutaciones de archivos ni escrituras automáticas a menos que se le solicite explícitamente atender un hallazgo.

## Potential Risks
1. **Amplitud excesiva de instrucciones (token overhead):** El archivo `SKILL.md` supera los 20 KB de texto con lineamientos densos y múltiples checklist inline, lo que puede saturar la ventana de contexto del agente si se carga indiscriminadamente en tareas triviales.
2. **Dependencias relativas rotas:** Si la skill se instala de manera aislada sin las carpetas compartidas de `references/`, los enlaces a `security-checklist.md` y `performance-checklist.md` quedarán rotos.
3. **Ausencia de scripts de validación deterministas:** Depende enteramente de la disciplina interpretativa del LLM; no incluye un script validador ejecutable como el desarrollado en nuestra Skill.

## Decision
[X] Install
[ ] Do not install

Reason:
El código fuente proviene de un mantenedor reconocido en la industria de ingeniería de software (Addy Osmani) y opera como un procedimiento estricto en lenguaje natural. No inyecta código malicioso, scripts ejecutables opacos ni llamadas de red externas no autorizadas. Se instala manteniendo el commit fijo inspeccionado para garantizar reproducibilidad en la evaluación académica.
