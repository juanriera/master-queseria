# Registro de cambios

Historial de versiones del libro *La mejora continua en la producción quesera*.  
Los cambios menores (correcciones ortográficas, ajustes de formato, pequeñas aclaraciones) no se registran aquí; pueden consultarse en el [historial de commits del repositorio](https://github.com/juanriera/master-queseria/commits/main).

---
## Noviembre 2026 — revisión del análisis de rendimientos

### Capítulos ampliados o corregidos

- **Cap. 14 — El balance de materia:** eliminado el ejemplo del balance anual global (compra frente a venta); corregidas erratas de cálculo (44.850 kg de MP; pérdida anual de MG de 10.783 kg y 59.815 €; porcentajes referidos a lo comprado y a la MG en cuba); resumen ajustado al contenido del capítulo.
- **Cap. 15 — El rendimiento quesero** *(antes: Los rendimientos queseros)*: el cociente ESM/MP se presenta como coeficiente que puede superar el 100 %; nueva sección sobre la descomposición de la desviación por consumo en tabla de doble entrada (efecto EST, efecto rendimiento e interacción EST × rendimiento, con término de comprobación), que sustituye a los «efectos no explicados»; corregido el cálculo del efecto precio, que ahora se valora sobre los kilos de materia consumidos (−12,18 € MG, +20,30 € MP); planteamiento del ejemplo inicial reescrito; eliminada la sección de práctica en Google Colab.

### Recursos actualizados

- **`06-analisis-desviaciones-rendimientos_2x2.xlsx`** sustituye a `06-analisis-desviaciones-rendimientos.xlsx`: fórmulas corregidas del efecto precio y de la interacción, nueva hoja «Interacción 2x2» y eliminación de nombres definidos y vínculos externos obsoletos.

---

## Marzo 2026 — primera versión pública

### Capítulos nuevos

- **Cap. 11 — Comunicación de resultados:** principios de Tufte y chartjunk, gráficos a evitar, Visual Vocabulary del Financial Times, ejemplos comparativos, gráfico de control para panel de planta, informes reproducibles.
- **Cap. 19 — La variabilidad industrial:** fuentes de variabilidad (5M), costes de la variabilidad, recorrido por las herramientas del libro, reducción sistemática y seguimiento.
- **Cap. 20 — La mejora continua:** definición del problema, DMAIC, siete herramientas básicas, Lean, Six Sigma, dos casos de discusión queseros.

### Capítulos ampliados o corregidos

- **Cap. 5 — Exploración gráfica:** reescritura completa; eliminado el diagrama de sectores; ejemplos actualizados con *palmerpenguins*, La Liga y temperaturas de Oviedo; nueva sección «La forma de los datos» (simétrica, asimétrica, bimodal); series temporales con datos reales.
- **Cap. 8 — Correlación y regresión:** versión completa con correlaciones espurias (margarina/divorcios, queso/patentes), gráficos de regresión con datos reales, callout sobre r vs R² y varianza explicada.
- **Cap. 9 — Control estadístico de procesos:** gráficos X-barra y S con *qicharts2*, índices de capacidad Cp/Cpk, sección de variabilidad a corto y largo plazo, referencia al RD 1801/2008.
- **Cap. 10 — Diseño de experimentos:** diseño 2² con caso práctico quesero (temperatura × dosis de cuajo), métrica de retención de materia prima en ESM, explicación reforzada del OFAT, sección sobre diseños confundidos y DoE en la era de la IA.
- **Cap. 16 — Sistema de medición:** nueva sección de seguimiento temporal (12 meses, 5 analistas, dos intervenciones) con gráficos de evolución de sesgo y sigma.
- **Cap. 17 — RD 1801/2008** *(ahora: Proceso de dosificación y control de peso en el envasado)*: corrección del término EMDT (antes EMT), valores T1/T2 corregidos para yogur de 150 g (T1 = 143,2 g; T2 = 136,4 g), tabla completa de EMDT, gráficos de capacidad vinculados al capítulo de SPC.

### Recursos nuevos

- **Apéndice A — Glosario:** 130 términos ordenados alfabéticamente, cubriendo todos los capítulos.
- **Apéndice — Índice de datasets:** 5 datasets nuevos con enlaces de descarga individual y archivo ZIP.
- **Resumen del RD 1801/2008:** documento de dos páginas para estudiantes.
- **Datasets nuevos:** `llenado_yogures_muestra.csv` (SPC), `experimento_cuajo.csv` (DoE), `grr_gerber_temporal.csv` (sistema de medición).

### Otros cambios

- Objetivos de aprendizaje y resumen añadidos a los capítulos 12, 13 y 14.
- Recomendaciones Broman & Woo incorporadas al cap. 4 (organización de datos) y al cap. 3 (limitaciones de la hoja de cálculo).
- Introducción ampliada para reflejar los nuevos capítulos de SPC, DoE y síntesis final.



---
