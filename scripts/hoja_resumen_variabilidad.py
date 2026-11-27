"""Hoja resumen del capítulo 15 (variabilidad), a página completa.

Genera imagenes/150/hoja-resumen-variabilidad.svg, .png y .pdf (A4).
Se ejecuta desde la raíz del libro:  python scripts/hoja_resumen_variabilidad.py

Todas las cifras proceden del libro: alturas del aula 1 (datos/aula1.csv, caps. 5 y 6),
llenado de yogures (Qn = 150 g, T1 = 143,2 g; etapa 1: media 153 g y σ = 2,5 g;
etapa 2: media 150,4 g y σ = 1,8 g; caps. 9 y 14).
"""
import os
import sys
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

SALIDA = sys.argv[1] if len(sys.argv) > 1 else os.path.join("imagenes", "150")

AZUL = "steelblue"
NARANJA = "darkorange"
VERDE = "#008b00"      # green4 de R
ROJO = "red"
GRIS = "0.35"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5,
                     "mathtext.fontset": "dejavusans"})

fig = plt.figure(figsize=(8.27, 11.69))          # A4 vertical


def normal(x, m, s):
    return np.exp(-0.5 * ((x - m) / s) ** 2) / (s * np.sqrt(2 * np.pi))


def limpiar(ax, ejex=True):
    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)
    ax.set_yticks([])
    if not ejex:
        ax.spines["bottom"].set_visible(False)
        ax.set_xticks([])
    ax.tick_params(labelsize=7)


def coma(v, dec=1):
    return f"{v:.{dec}f}".replace(".", ",")


_renderer = None


def ancho(texto, **kw):
    """Anchura de un texto en fracción de figura."""
    global _renderer
    if _renderer is None:
        _renderer = fig.canvas.get_renderer()
    t = fig.text(0, 0, texto, **kw)
    w = t.get_window_extent(renderer=_renderer).width / fig.bbox.width
    t.remove()
    return w


def parrafo(x, y, texto, wmax, tam=8.3, interlinea=0.0145):
    """Escribe un párrafo con ajuste de línea medido. Si empieza por «Etiqueta:»
    marcada con **, la etiqueta va en negrita. Devuelve la y siguiente."""
    etiqueta = ""
    if texto.startswith("**"):
        fin = texto.index("**", 2)
        etiqueta, texto = texto[2:fin], texto[fin + 2:].lstrip()
    if texto.startswith("$"):                       # fórmula: una sola línea
        fig.text(x, y, texto, va="top", fontsize=tam + 1)
        return y - 0.034
    xs = x
    if etiqueta:
        fig.text(x, y, etiqueta, va="top", fontsize=tam, fontweight="bold")
        xs = x + ancho(etiqueta + " ", fontsize=tam, fontweight="bold")
    linea = ""
    for palabra in texto.split():
        prueba = (linea + " " + palabra).strip()
        if ancho(prueba, fontsize=tam) > wmax - (xs - x):
            fig.text(xs, y, linea, va="top", fontsize=tam)
            y -= interlinea
            xs, linea = x, palabra
        else:
            linea = prueba
    if linea:
        fig.text(xs, y, linea, va="top", fontsize=tam)
        y -= interlinea
    return y - 0.004


def panel(num, titulo, lineas, x0, y0, w, h):
    """Dibuja el marco, la cabecera y el texto de un panel. Devuelve el eje para el gráfico."""
    fondo = FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=0.008",
                           transform=fig.transFigure, facecolor="white",
                           edgecolor=AZUL, linewidth=1.2, zorder=-2)
    fig.patches.append(fondo)
    cab = FancyBboxPatch((x0, y0 + h - 0.028), w, 0.028, boxstyle="square,pad=0",
                         transform=fig.transFigure, facecolor=AZUL, edgecolor=AZUL, zorder=-1)
    fig.patches.append(cab)
    fig.text(x0 + 0.012, y0 + h - 0.014, f"{num}. {titulo}", color="white",
             fontsize=10, fontweight="bold", va="center")
    y = y0 + h - 0.040
    for linea in lineas:
        y = parrafo(x0 + 0.012, y, linea, w - 0.024)
    alto = (y - 0.012) - (y0 + 0.032)
    return fig.add_axes([x0 + 0.03, y0 + 0.032, w - 0.06, alto])


# ---------------------------------------------------------------- título
fig.text(0.5, 0.972, "Hoja resumen: la variabilidad en la producción",
         ha="center", fontsize=16, fontweight="bold", color="0.15")
fig.text(0.5, 0.952, "La mejora continua en la producción quesera · Capítulo 15",
         ha="center", fontsize=9, color=GRIS)

W, H = 0.455, 0.296
X = [0.03, 0.515]
Y = [0.637, 0.326, 0.015]

# ---------------------------------------------------------------- 1. inevitable
ax = panel(1, "La variabilidad es inevitable", [
    "Ningún proceso da dos resultados idénticos. El objetivo no es eliminar la "
    "variabilidad, sino reducirla hasta un nivel compatible con la calidad y con el coste.",
    "Sus fuentes se agrupan en las 5M:",
], X[0], Y[0], W, H)
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
_ = ax.annotate("", xy=(7.5, 3), xytext=(0.8, 3),
                arrowprops=dict(arrowstyle="-|>", color=AZUL, linewidth=2))
_ = ax.text(7.65, 3, "Variabilidad\ndel resultado", va="center", fontsize=8.5, fontweight="bold")
espinas = [(2.2, "Materia prima", 1), (4.6, "Método", 1), (7.0, "Maquinaria", 1),
           (3.3, "Mano de obra", -1), (7.0, "Medio ambiente", -1)]
for xs, nombre, lado in espinas:
    _ = ax.plot([xs - 1.0, xs], [3 + lado * 2.2, 3], color=GRIS, linewidth=1.2)
    _ = ax.text(xs - 1.0, 3 + lado * 2.45, nombre, ha="center",
                va="bottom" if lado > 0 else "top", fontsize=8)

# ---------------------------------------------------------------- 2. medir
alturas = np.array([153, 135, 140, 140, 175, 138, 145, 154, 152, 159, 154])
media = alturas.mean()
s = alturas.std(ddof=1)
ax = panel(2, "Cómo se mide: media y desviación típica", [
    "**Media:** punto de equilibrio de los datos.",
    "**Desviación típica:** distancia cuadrática media de los datos a su media. "
    "Con una muestra se divide por n − 1: DESVEST.M en Excel, sd() en R, std() en pandas.",
], X[1], Y[0], W, H)
ys = np.arange(len(alturas))
for yi, v in zip(ys, alturas):
    _ = ax.plot([media, v], [yi, yi], color=GRIS, linestyle=":", linewidth=0.9)
_ = ax.scatter(alturas, ys, color="firebrick", s=22, zorder=3)
_ = ax.axvline(media, color="black", linewidth=1)
_ = ax.scatter([media], [-1.3], marker="^", s=120, color=AZUL, zorder=3, clip_on=False)
_ = ax.text(176, 1.2, f"media = {coma(media, 2)} cm\ns = {coma(s, 2)} cm",
            fontsize=7.5, va="center", ha="right",
            bbox=dict(facecolor="white", edgecolor="0.7", pad=2))
ax.set_ylim(-1.8, len(alturas))
ax.set_xlabel("Altura de los alumnos del aula 1 (cm)", fontsize=7.5)
limpiar(ax)

# ---------------------------------------------------------------- 3. causas
ax = panel(3, "Causas comunes y causas especiales", [
    "**Comunes:** propias del sistema. Solo se reducen cambiando el sistema, "
    "y eso es responsabilidad de la dirección.",
    "**Especiales:** concretas e identificables. Se investigan y se eliminan.",
    "El gráfico de control las distingue. Señales: un punto fuera de los límites "
    "o una racha larga al mismo lado de CL. Sin señales, no intervenir.",
], X[0], Y[1], W, H)
rng = np.random.default_rng(7)
v = rng.normal(0, 1, 30)
v[9] = 3.6                     # punto fuera de límites
v[19:28] = np.abs(v[19:28]) * 0.6 + 0.3   # racha por encima de CL
x = np.arange(1, 31)
_ = ax.plot(x, v, color=AZUL, linewidth=1, marker="o", markersize=3.5)
_ = ax.plot(x[9], v[9], "o", color=ROJO, markersize=6)
_ = ax.plot(x[19:28], v[19:28], "o", color=NARANJA, markersize=5)
for nivel, nombre in ((3, "UCL"), (0, "CL"), (-3, "LCL")):
    _ = ax.axhline(nivel, color="0.3" if nivel else "black",
                   linestyle="--" if nivel else "-", linewidth=0.9)
    _ = ax.text(31.3, nivel, nombre, va="center", fontsize=7,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.5))
_ = ax.text(x[9] + 0.8, 4.1, "punto fuera de los límites", fontsize=7, color=ROJO, va="center")
_ = ax.text(25.5, -2.3, "racha al mismo lado de CL", fontsize=7, color=NARANJA, ha="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=1))
ax.set_xlim(0, 34); ax.set_ylim(-3.6, 4.6)
ax.set_xlabel("Subgrupo", fontsize=7.5)
limpiar(ax)

# ---------------------------------------------------------------- 4. capacidad
ax = panel(4, "Capacidad del proceso", [
    r"$C_p = \frac{LSE - LIE}{6\sigma} \qquad C_{pk} = \mathrm{min}\left(\frac{LSE - \mu}{3\sigma},\ \frac{\mu - LIE}{3\sigma}\right)$",
    "Cp mide si la variabilidad cabe entre los límites; Cpk tiene en cuenta además el "
    "centrado. Referencia habitual: Cpk ≥ 1,33. Solo tiene sentido si el proceso está bajo control.",
], X[1], Y[1], W, H)
xs = np.linspace(-5, 7, 400)
mu, sig, lie, lse = 1.0, 1.0, -4.0, 4.0
yv = normal(xs, mu, sig)
_ = ax.fill_between(xs, yv, color=AZUL, alpha=0.35)
_ = ax.plot(xs, yv, color=AZUL, linewidth=1.2)
_ = ax.fill_between(xs[xs > lse], yv[xs > lse], color=ROJO)
for lim, nombre in ((lie, "LIE"), (lse, "LSE")):
    _ = ax.axvline(lim, color=ROJO, linewidth=1.3)
    _ = ax.text(lim, yv.max() * 1.15, nombre, ha="center", fontsize=7.5, color=ROJO,
                bbox=dict(facecolor="white", edgecolor="none", pad=1))
_ = ax.axvline(mu, color="black", linewidth=1)
_ = ax.text(mu, yv.max() * 1.15, "μ", ha="center", fontsize=8,
            bbox=dict(facecolor="white", edgecolor="none", pad=1))
yb = yv.max() * 0.55
_ = ax.annotate("", xy=(lse, yb), xytext=(mu, yb), arrowprops=dict(arrowstyle="<->", color=GRIS))
_ = ax.text((mu + lse) / 2, yb * 1.06, "LSE − μ", ha="center", fontsize=7, color=GRIS, va="bottom")
_ = ax.annotate("", xy=(lie, yb), xytext=(mu, yb), arrowprops=dict(arrowstyle="<->", color=GRIS))
_ = ax.text((mu + lie) / 2, yb * 1.06, "μ − LIE", ha="center", fontsize=7, color=GRIS, va="bottom")
_ = ax.text(5.9, yv.max() * 0.7, "Media descentrada:\nCp = 1,33\nCpk = 1,00", fontsize=7, ha="center")
ax.set_ylim(0, yv.max() * 1.3)
limpiar(ax, ejex=False)

# ---------------------------------------------------------------- 5. veracidad y precisión
ax = panel(5, "Veracidad y precisión (ISO 5725-1)", [
    "**Sesgo:** distancia entre la media de los resultados y el valor de referencia (veracidad).",
    "**Dispersión:** anchura de los resultados (precisión).",
    "Son independientes y se corrigen de forma distinta: el sesgo, con una causa concreta; "
    "la falta de precisión, revisando todo el procedimiento.",
], X[0], Y[2], W, H)
xs = np.linspace(-4.5, 6, 400)
ref = 0.0
y1 = normal(xs, 2.4, 0.45)
y2 = normal(xs, 0.0, 1.4)
_ = ax.fill_between(xs, y1, color=NARANJA, alpha=0.3); _ = ax.plot(xs, y1, color=NARANJA)
_ = ax.fill_between(xs, y2, color=AZUL, alpha=0.3); _ = ax.plot(xs, y2, color=AZUL)
_ = ax.axvline(ref, color="black", linewidth=1.1)
_ = ax.text(ref, y1.max() * 1.12, "valor de\nreferencia", ha="center", fontsize=7, va="bottom",
            bbox=dict(facecolor="white", edgecolor="none", pad=1))
_ = ax.annotate("", xy=(2.4, y1.max() * 1.03), xytext=(ref, y1.max() * 1.03),
                arrowprops=dict(arrowstyle="<->", color=NARANJA))
_ = ax.text(1.2, y1.max() * 0.93, "sesgo", ha="center", fontsize=7, color=NARANJA, va="top")
_ = ax.text(3.0, y1.max() * 0.6, "con sesgo,\npreciso", fontsize=7, color=NARANJA)
_ = ax.text(-3.9, y2.max() * 1.4, "sin sesgo,\npoco preciso", fontsize=7, color=AZUL)
ax.set_ylim(0, y1.max() * 1.45)
limpiar(ax, ejex=False)

# ---------------------------------------------------------------- 6. reducir
ax = panel(6, "Cómo reducirla: cinco pasos", [
    "1. Medir: σ, Cpk, porcentaje de no conformes.",
    "2. Eliminar las causas especiales (gráfico de control).",
    "3. Priorizar: pocas causas explican la mayor parte (Pareto).",
    "4. Actuar sobre las causas comunes, cambiando el sistema.",
    "5. Verificar y mantener: seguir la tendencia, no solo el valor.",
    "Menos variabilidad permite acercar la media a Qn sin incumplir: menos producto regalado.",
], X[1], Y[2], W, H)
xs = np.linspace(140, 162, 500)
qn, t1 = 150.0, 143.2
for m, sg, col, nombre in ((153.0, 2.5, AZUL, "Etapa 1: μ = 153 g, σ = 2,5 g"),
                           (150.4, 1.8, NARANJA, "Etapa 2: μ = 150,4 g, σ = 1,8 g")):
    yv = normal(xs, m, sg)
    _ = ax.fill_between(xs, yv, color=col, alpha=0.3, label=nombre)
    _ = ax.plot(xs, yv, color=col, linewidth=1)
_ = ax.axvline(qn, color=VERDE, linestyle="--", linewidth=1)
_ = ax.axvline(t1, color="orange", linewidth=1.3)
top = normal(150.4, 150.4, 1.8)
_ = ax.text(qn - 0.3, top * 1.25, "Qn", color=VERDE, fontsize=7.5, ha="right")
_ = ax.text(t1 + 0.3, top * 1.25, "T1", color="orange", fontsize=7.5)
_ = ax.legend(fontsize=6.5, frameon=False, loc="upper right", bbox_to_anchor=(1.04, 1.04), handlelength=1.2)
ax.set_ylim(0, top * 1.75)
ax.set_xticks([140, 145, 150, 155, 160])
ax.set_xlabel("Peso del yogur (g); etapas de mejora del capítulo 14", fontsize=7.5)
limpiar(ax)

os.makedirs(SALIDA, exist_ok=True)
for ext in ("svg", "png", "pdf"):      # el PDF, en A4, para imprimir
    fig.savefig(os.path.join(SALIDA, f"hoja-resumen-variabilidad.{ext}"), dpi=200)
print("Hoja resumen guardada en", SALIDA)
