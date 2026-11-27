"""Figura del capítulo 15: dos líneas de llenado con la misma media y distinta variabilidad.

Genera imagenes/150/variabilidad-dos-lineas.svg y .png.
Se ejecuta desde la raíz del libro:  python scripts/figura_variabilidad_dos_lineas.py

Parámetros coherentes con la simulación del llenado de yogures (caps. 9, 11 y 14):
Qn = 150 g, T1 = 143,2 g, media 153 g; σ = 1,8 g y σ = 2,5 g (las dos σ de las etapas de mejora).
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

SALIDA = sys.argv[1] if len(sys.argv) > 1 else os.path.join("imagenes", "150")
SEMILLA = 2024
N = 9600            # envases de un turno, como en llenado_yogures.csv
MEDIA = 153.0
QN, T1 = 150.0, 143.2
LINEAS = [("Línea A", 1.8), ("Línea B", 2.5)]

rng = np.random.default_rng(SEMILLA)
bins = np.arange(140, 166.01, 0.5)
coma = mticker.FuncFormatter(lambda x, _: f"{x:g}".replace(".", ","))
miles = mticker.FuncFormatter(lambda x, _: f"{x:,.0f}".replace(",", "."))

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
fig, axes = plt.subplots(2, 1, figsize=(8, 5.6), sharex=True, sharey=True)

intervalos = []
for ax, (nombre, sigma) in zip(axes, LINEAS):
    pesos = rng.normal(MEDIA, sigma, N)
    intervalos.append(np.percentile(pesos, [2.5, 97.5]))
    _ = ax.hist(pesos, bins=bins, color="steelblue", edgecolor="white", linewidth=0.4)
    _ = ax.axvline(MEDIA, color="black", linewidth=1.2)
    _ = ax.axvline(QN, color="#008b00", linestyle="--", linewidth=1.2)
    _ = ax.axvline(T1, color="orange", linewidth=1.5)
    _ = ax.set_title(f"{nombre}: media = 153 g, σ = {sigma:.1f} g".replace(".", ","),
                     loc="left", fontsize=10.5)
    ax.grid(color="0.88", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.yaxis.set_major_formatter(miles)
    ax.set_ylabel("Envases")
    ax.set_xlim(140, 166)

ymax = axes[0].get_ylim()[1]
for ax, (lo, hi) in zip(axes, intervalos):
    ax.set_ylim(0, ymax * 1.30)
    yb = ymax * 1.08
    # intervalo que contiene el 95 % central de los envases simulados (percentiles 2,5 y 97,5)
    _ = ax.annotate("", xy=(lo, yb), xytext=(hi, yb),
                    arrowprops=dict(arrowstyle="<->", color="0.25", linewidth=1))
    _ = ax.text((lo + hi) / 2, ymax * 1.15,
                f"95 % de los envases entre {lo:.1f} y {hi:.1f} g".replace(".", ","),
                ha="center", va="bottom", fontsize=8.5, color="0.25",
                bbox=dict(facecolor="white", edgecolor="none", pad=1))
    _ = ax.text(QN - 0.2, ymax * 0.55, "Qn = 150 g", fontsize=8.5, color="#008b00", ha="right")
    _ = ax.text(T1 + 0.2, ymax * 0.85, "T1 = 143,2 g", fontsize=8.5, color="orange")
    _ = ax.text(MEDIA + 0.2, ymax * 0.98, "Media", fontsize=8.5, color="black", va="bottom")

axes[1].xaxis.set_major_formatter(coma)
axes[1].set_xlabel("Peso del envase (g)")
fig.suptitle("Misma media, distinta variabilidad: dos líneas de llenado de yogures (9.600 envases cada una)",
             fontsize=11, x=0.02, ha="left")
fig.tight_layout()

os.makedirs(SALIDA, exist_ok=True)
for ext in ("svg", "png"):
    fig.savefig(os.path.join(SALIDA, f"variabilidad-dos-lineas.{ext}"), dpi=150)
print("Figura guardada en", SALIDA)
