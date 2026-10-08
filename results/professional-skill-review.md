# Code Review and Quality Report

## Review Context
- **Target Repository:** `ada06-sample-repo`
- **Target Branch / PR:** `feature/discount-calc` (diff contra `main`, commit `f05d4ca`)
- **Review Skill:** `code-review-and-quality` (vía `addyosmani/agent-skills`)
- **Normative Document:** `SPEC.md` (REQ-003: Percentage Discount)
- **Change Size:** +23 líneas (+10 en `src/calculator.py`, +13 en `tests/test_calculator.py`). Tamaño óptimo (<100 líneas).

---

## Step 1: Context & Intent
El cambio implementa la funcionalidad solicitada en `SPEC.md` bajo el requerimiento `REQ-003: Percentage Discount (Issue #1)`. El objetivo es calcular y aplicar un porcentaje de descuento (0% a 100%) sobre un subtotal antes de aplicar impuestos, arrojando excepciones si los valores numéricos son negativos o si el porcentaje excede 100.

---

## Step 2: Test-First Review & Verification
- **Suite de pruebas:** `python -m unittest discover -s tests -v` ejecutó 7 pruebas con éxito.
- **Cobertura de comportamiento:** Las pruebas validan valores normales (10%), extremos (0%, 100%) y entradas inválidas (-5%, 105%, subtotal negativo).
- **Experimento de mutación conceptual:**
  - Si se modifica la condición `discount_percent < 0 or discount_percent > 100` por `discount_percent <= 0`, la prueba `test_apply_discount_valid` con 0% falla inmediatamente como se espera.
  - Si se omite la validación de `subtotal < 0`, `test_apply_discount_invalid` detecta la falla.
- **Brecha detectada en pruebas:** No existe una prueba de integración que verifique el encadenamiento explícito de `calculate_subtotal` -> `apply_discount` -> `apply_tax` para confirmar que el descuento se aplica efectivamente *antes* del impuesto según el flujo global del negocio.

---

## Step 3 & 4: Multi-Axis Findings Categorized by Severity

### Finding 1
- **Severity:** Required
- **Axis:** Correctness & Numeric Precision
- **File / Evidence:** `src/calculator.py:17` — `return round(discounted, 2)`
- **Engineering Rationale:** En cálculos financieros, aplicar `round(..., 2)` en pasos intermedios de una cadena de cálculo (antes de `apply_tax`) introduce pérdida prematura de precisión debido al truncamiento de centavos. La especificación REQ-003 indica que el descuento se aplica "before tax calculation". Si el subtotal con descuento se redondea antes del impuesto, el cálculo de impuestos sobre el redondeo intermedio difiere del impuesto sobre el valor exacto con descuento.
- **Recommended Action:** Mantener el valor flotante sin redondeo forzado en el paso intermedio o documentar contractualmente en el docstring que el servicio trunca centavos por etapa. A nivel de arquitectura de cálculo monetario, se sugiere delegar el redondeo a dos decimales al cálculo del total final.

### Finding 2
- **Severity:** Consider / Optional
- **Axis:** Architecture & API Composition
- **File / Evidence:** `src/calculator.py:11` — `def apply_discount(subtotal: float, discount_percent: float) -> float:`
- **Engineering Rationale:** La función opera de forma aislada. Para evitar que el llamador olvide el orden requerido ("descuento antes de impuestos"), convendría ofrecer una función de orquestación (e.g. `calculate_total(prices, discount_percent=0.0, tax_rate=0.0)`) que asegure el flujo de llamadas correcto sin exponer la secuencia manual al cliente.
- **Recommended Action:** Evaluar la introducción de una función de fachada de alto nivel en un PR posterior para formalizar el flujo `subtotal -> descuento -> impuesto`.

### Finding 3
- **Severity:** Nit
- **Axis:** Readability & Type Hinting
- **File / Evidence:** `src/calculator.py:11` — anotaciones de tipos primitivos `float`
- **Engineering Rationale:** En invocaciones típicas en Python, los porcentajes o precios pueden pasarse como enteros literales (e.g., `apply_discount(100, 15)`). Aunque Python admite enteros donde se esperan flotantes, herramientas como `mypy` emitirán advertencias si la configuración de tipos es estricta.
- **Recommended Action:** Usar anotaciones `float | int` o dejar una nota en la configuración del linter/type-checker.

---

## Step 5: Verification Checklist & Quality Gate

- [x] **Correctness:** El código satisface el requerimiento REQ-003 y cubre casos de borde.
- [x] **Readability:** Nombres claros, sin código muerto, flujo lineal y conciso.
- [x] **Architecture:** No introduce acoplamientos ni dependencias externas.
- [x] **Security:** No se manejan credenciales ni datos externos no saneados; validación de rangos presente.
- [x] **Performance:** Operación matemática $O(1)$ sin asignaciones de memoria excesivas.
- [x] **Tests:** 100% de pruebas pasando localmente.

### Verdict
- [x] **Approve** (Ready for Human Review & Merge following team agreement on intermediate rounding).
- [ ] **Request changes**

**Human Decision Required:** YES. El revisor humano debe decidir si acepta el redondeo intermedio a 2 decimales en `apply_discount` o si prefiere unificar la precisión monetaria antes de integrar a `main`.
