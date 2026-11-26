"""Simula un turno de llenado de yogures de 150 g (media sin incidentes 153 g, σ = 2,5 g) (1/10/2024, 08:00-16:00, un envase cada 3 s)
y extrae la muestra para gráficos de control (5 envases cada 3 min, separados ~45 s).
Uso, desde la carpeta raíz del libro: python python/generar_llenado_yogures.py
(escribe en datos/; se puede indicar otra carpeta como argumento)"""
import sys, numpy as np, pandas as pd

# Semilla elegida entre varias para que la Fase I (08:00-08:30) represente bien el proceso
# sin incidentes (media ~153 g, σ ~2,5 g) y cada incidente deje una señal clara
SEMILLA = int(sys.argv[2]) if len(sys.argv) > 2 else 103
rng = np.random.default_rng(SEMILLA)
N = 9600
t = pd.date_range("2024-10-01 08:00:00", periods=N, freq="3s")
h = (t.hour + t.minute / 60 + t.second / 3600).to_numpy()   # hora decimal

MU0, S0 = 153.0, 2.5
mu = np.full(N, MU0); sd = np.full(N, S0)

# 1. Deriva ascendente 08:30-08:39 (+6 g)
k = (h >= 8.5) & (h < 8.65); mu[k] = MU0 + 6 * (h[k] - 8.5) / 0.15
# 2. Sobrecorrección 08:39-08:54 (media 143 g, más dispersión) y recuperación gradual hasta 09:03
k = (h >= 8.65) & (h < 8.9); mu[k] = 143.0; sd[k] = 3.5
k = (h >= 8.9) & (h < 9.05); mu[k] = 143.0 + 10 * (h[k] - 8.9) / 0.15
# 4. Alta variabilidad 10:00-10:45 sin cambio de media
k = (h >= 10.0) & (h < 10.75); sd[k] = 5.5
# 5. Deriva descendente lenta 11:00-12:30 (-3 g); se mantiene hasta 13:30
k = (h >= 11.0) & (h < 12.5); mu[k] = MU0 - 3 * (h[k] - 11.0) / 1.5
k = (h >= 12.5) & (h < 13.5); mu[k] = MU0 - 3
# 6. Escalón brusco 13:30 (cambio de turno): +4,5 g; se mantiene hasta el final
k = h >= 13.5; mu[k] = MU0 + 1.5
# 7. Oscilación periódica 14:00-14:30 (amplitud 4 g, periodo 12 min)
k = (h >= 14.0) & (h < 14.5); mu[k] += 4.0 * np.sin(2 * np.pi * (h[k] - 14.0) / 0.2)

peso = np.round(rng.normal(mu, sd), 2)
df = pd.DataFrame({"hora_envasado": t.strftime("%Y-%m-%d %H:%M:%S"),
                   "n_envase": np.arange(1, N + 1),
                   "subgrupo": np.arange(N) // 5 + 1,
                   "pos_subgrupo": np.arange(N) % 5 + 1,
                   "peso_g": peso})
pos_iv = np.arange(N) % 60                        # 60 envases por intervalo de 3 min
muestra = df[np.isin(pos_iv, [0, 15, 30, 44, 59])].copy()
muestra["muestra"] = np.arange(len(muestra)) // 5 + 1

out = sys.argv[1] if len(sys.argv) > 1 else "datos"
kw = dict(sep=";", decimal=",", index=False, encoding="ISO-8859-1")
df.to_csv(f"{out}/llenado_yogures.csv", **kw)
muestra.to_csv(f"{out}/llenado_yogures_muestra.csv", **kw)
