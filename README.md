# ADA-07: Build an Agent Skill

Proyecto de diseño, implementación y evaluación de una **Agent Skill** para el proceso de **Pull Request Readiness Review**.

Curso: **Ingeniería de Software asistida por IA · UADY**  
Autor: Estudiante de Ingeniería de Software  

---

## 📁 Estructura del Repositorio

El proyecto sigue la estructura requerida en la práctica:

```text
ada-07-agent-skill/
├── .agents/
│   ├── references/                                # Referencias compartidas del ecosistema
│   └── skills/
│       ├── reviewing_pull_requests/              # Skill desarrollada (Parte I)
│       │   ├── SKILL.md                          # Workflow compacto, routing y boundaries
│       │   ├── references/
│       │   │   ├── review_checklist.md           # Checklist de ingeniería de software
│       │   │   └── severity_guide.md             # Guía de clasificación de severidades
│       │   ├── scripts/
│       │   │   └── validate_review_report.py     # Validador determinista en Python
│       │   ├── assets/
│       │   │   └── review_report_template.md     # Plantilla de reporte
│       │   └── evals/
│       │       ├── trigger_cases.json            # Casos de activación y no-activación
│       │       └── execution_cases.json          # Casos de prueba y boundary case
│       └── code-review-and-quality/              # Skill profesional adoptada (Parte II)
│           └── SKILL.md                          # Skill de Addy Osmani (commit 1401c8b)
├── docs/
│   ├── skill_workflow_observation.md             # Observación del flujo manual de revisión
│   ├── third_party_skill_audit.md                # Auditoría de seguridad previa a instalación
│   └── professional_skill_anatomy.md             # Análisis de ingeniería inversa
├── results/
│   ├── pr-readiness-review.md                    # Reporte generado por la Skill propia
│   ├── skill-evaluation-report.md                # Resultados de pruebas e iteración
│   ├── professional-skill-review.md              # Reporte generado por la Skill profesional
│   └── skill-comparison.md                       # Matriz comparativa entre ambas soluciones
├── AI_USAGE_LOG.md                               # Bitácora de uso de IA en primera persona
└── README.md                                     # Descripción del repositorio
```

---

## 🛠️ Validación del Reporte

Para comprobar de forma determinista la estructura del reporte generado por la Skill:

```bash
python .agents/skills/reviewing_pull_requests/scripts/validate_review_report.py results/pr-readiness-review.md
```

Salida esperada:
```text
VALID: PR readiness review structure is complete.
```
