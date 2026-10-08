# Workflow Observation

Registro de la ejecución manual previa al diseño de la Skill para Pull Request Readiness Review.

## Trigger
¿Cuándo debería utilizarse este workflow?
Cuando un desarrollador termina una rama de trabajo (por ejemplo `feature/discount-calc`), abre un Pull Request preliminar o solicita verificar si sus cambios están listos para revisión humana sin tocar todavía el código en producción ni hacer merge automático.

## Inputs
¿Qué necesita para iniciar?
- Repositorio git con acceso al historial y al diff de la rama (`ada06-sample-repo`).
- Archivo normativo de especificación (`SPEC.md`).
- Suite de pruebas automatizadas del proyecto (`tests/test_calculator.py`).
- Identificador de la rama o PR a evaluar (`feature/discount-calc` contra `main`).

## Steps Performed
1. Identifiqué la rama de origen `feature/discount-calc` y su rama destino `main`. Ejecuté `git diff main..feature/discount-calc` para ver las líneas exactas añadidas y modificadas.
2. Revisé el documento `SPEC.md`. Localicé el requerimiento `REQ-003: Percentage Discount`, que exige aplicar un descuento entre 0% y 100% sobre el subtotal antes de impuestos, además de validar montos negativos.
3. Leí el código modificado en `src/calculator.py`. Se añadió la función `apply_discount(subtotal, discount_percent)`. Comprobé cómo gestiona validaciones (`ValueError` para subtotal < 0 y porcentaje fuera de [0, 100]).
4. Verifiqué las pruebas en `tests/test_calculator.py`. Noté casos para valores límite (0%, 100%, 10%) e inválidos (-5%, 105%, subtotal negativo).
5. Ejecuté la suite de pruebas localmente con `python -m unittest discover -s tests -v`. Pasaron las 7 pruebas sin errores.
6. Analicé aspectos no funcionales: legibilidad, redondeo a 2 decimales y consistencia con las otras funciones (`calculate_subtotal`, `apply_tax`).
7. Clasifiqué los hallazgos:
   - No hay bloqueadores críticos (MUST FIX).
   - Hallazgo menor (SHOULD FIX / OPTIONAL): la función redondea con `round(discounted, 2)`, lo cual es consistente con `calculate_subtotal`, pero en cálculos monetarios acumulados puede haber pequeños errores de precisión si se encadenan antes de impuestos; convendría documentar el orden de operaciones en el docstring.
8. Redacté un borrador de reporte estructurado para que el revisor humano tome la decisión final de aprobación.

## Decisions
¿Qué decisiones requieren criterio del LLM?
- Interpretar si la implementación de `apply_discount` satisface semánticamente el requerimiento `REQ-003` de `SPEC.md`.
- Juzgar si la cobertura de pruebas es suficiente en casos de borde (ej. 0.0, 100.0, valores atípicos).
- Asignar el nivel de severidad adecuado a las observaciones (diferenciar entre un fallo que rompe el contrato y una sugerencia de estilo o precisión numérica).
- Redactar explicaciones claras y sugerencias accionables para el equipo.

## Deterministic Work
¿Qué pasos deberían ser scripts/comandos?
- Extracción de diff y estado de ramas con `git`.
- Ejecución de la suite de pruebas (`pytest` o `python -m unittest`).
- Comprobación de que el reporte final tenga todas las secciones obligatorias y conteos válidos (script de validación).

## Reference Knowledge
¿Qué checklist, criterios o convenciones se consultaron?
- Criterios de aceptación del requerimiento `REQ-003` en `SPEC.md`.
- Reglas de clasificación de hallazgos (definición clara de MUST FIX vs. SHOULD FIX vs. OPTIONAL).
- Convención de manejo de errores en Python (lanzar `ValueError` ante entradas fuera de rango).
- Política de no realizar mutaciones remotas (Draft-Only: no merge, no comentar en la API de GitHub).

## Output
¿Qué artefacto produce?
Un archivo de reporte local en Markdown (`results/pr-readiness-review.md`) con el contexto del PR, mapeo de requerimientos, evidencia de pruebas, hallazgos clasificados por severidad y la confirmación explícita de que se requiere decisión humana.

## Stop Conditions
¿Cuándo debe detenerse y pedir intervención humana?
- Si `SPEC.md` contiene requerimientos contradictorios o no existe especificación clara para la nueva funcionalidad.
- Si las pruebas fallan o el código rompe el build.
- Si se detectan problemas de seguridad (credenciales, inyecciones) o violaciones críticas que requieran rediseño arquitectónico.
- Al terminar la redacción del reporte (la Skill jamás aprueba ni hace merge del PR).
