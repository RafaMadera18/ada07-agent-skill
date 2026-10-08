# PR Readiness Review

## Review Context
PR / Branch: `feature/discount-calc` (comparado contra `main` en `ada06-sample-repo`)
Reviewer Agent: reviewing-pull-requests skill
Date: 2026-10-08

## Requirements / Acceptance Criteria Reviewed
- **REQ-001 (Subtotal Calculation):** Verificado como contexto base; calcula la suma de precios y valida números no negativos.
- **REQ-002 (Tax Application):** Verificado como contexto base; aplica tasa de impuesto a un monto.
- **REQ-003 (Percentage Discount - Issue #1):**
  - La función `apply_discount(subtotal, discount_percent)` aplica un porcentaje de descuento (entre 0% y 100%) sobre el subtotal antes del cálculo de impuestos.
  - Se valida que `subtotal >= 0`, lanzando `ValueError("Subtotal cannot be negative")` si es menor que 0.
  - Se valida que `0 <= discount_percent <= 100`, lanzando `ValueError("Discount percent must be between 0 and 100")` si está fuera de rango.

## Test Evidence
- Comando ejecutado: `python -m unittest discover -s tests -v`
- Resultado: 7 pruebas ejecutadas con éxito (0 fallos, 0 errores, duración 0.001s).
- Casos probados para la nueva funcionalidad (`tests/test_calculator.py`):
  - `test_apply_discount_valid`: Casos válidos con 10% (100.0 -> 90.0), 0% (100.0 -> 100.0) y 100% (100.0 -> 0.0).
  - `test_apply_discount_invalid`: Casos de error esperados con -5%, 105% y subtotal negativo (-50.0).

## MUST FIX
No se identificaron problemas bloqueantes de severidad MUST FIX. La implementación satisface los criterios de aceptación de REQ-003, no rompe compatibilidad con funciones existentes y pasa todas las pruebas automatizadas.

## SHOULD FIX
### SF-01
Requirement / AC: REQ-003 / Mantenibilidad y Precisión Numérica
File: `src/calculator.py:17`
Evidence: `return round(discounted, 2)`
Problem: La función redondea inmediatamente el subtotal con descuento a 2 decimales. Aunque esto mantiene consistencia con `calculate_subtotal`, realizar redondeos intermedios antes de aplicar impuestos (`apply_tax`) puede generar variaciones de centavos en liquidaciones acumuladas.
Recommended next step: Documentar en el docstring que el resultado es un monto monetario redondeado para presentación o evaluar si en versiones futuras el redondeo debe delegarse a la liquidación final del carrito.

## OPTIONAL
### OP-01
Requirement / AC: Claridad de tipado
File: `src/calculator.py:11`
Evidence: `def apply_discount(subtotal: float, discount_percent: float) -> float:`
Problem: Quien llame a la función podría pasar valores enteros (e.g. `10` en vez de `10.0`). Python lo admite sin inconvenientes en tiempo de ejecución, pero herramientas de análisis estático como `mypy` son más estrictas con tipos primitivos numéricos.
Recommended next step: Considerar el uso de `float | int` o `numbers.Real` en anotaciones si se implementa type checking estricto en el pipeline de CI.

## Open Questions
- ¿Existe algún caso donde un cupón o descuento comercial deba aplicarse por ítem en lugar de a nivel de subtotal acumulado?
- ¿Se requerirá a futuro soporte para descuentos por monto fijo adicional al porcentaje?

## Final Review Summary
MUST FIX count: 0
SHOULD FIX count: 1
OPTIONAL count: 1

Human decision required:
YES
