import pandas as pd
import numpy as np

# =============================================================================
# SIMULADOR DE SEGUIMIENTO TEMPORAL - MÉTODO GERBER (GRASA EN LECHE)
# =============================================================================
# Diseño: 5 analistas x 3 muestras x 3 repeticiones x 12 meses = 540 análisis
#
# El estudio de repetibilidad se repite mensualmente durante un año.
# Se simulan dos intervenciones de mejora:
#
#   - Analista 4 (sesgo sistemático): recibe formación específica en lectura
#     del butirómetro en el mes 4. Su sesgo se reduce progresivamente desde
#     -0,35% hasta -0,05% entre los meses 4 y 8, y se estabiliza.
#
#   - Analista 5 (alta variabilidad): recibe formación en técnica de análisis
#     (temperatura del baño maría, homogeneización) en el mes 6. Su desviación
#     típica se reduce progresivamente desde 0,25% hasta 0,08% entre los
#     meses 6 y 10, y se estabiliza.
#
# Los analistas 1, 2 y 3 mantienen sus parámetros estables a lo largo del año.
# Esto permite comparar la evolución de los analistas con problemas frente
# a los de referencia, y ver el efecto de las intervenciones en los gráficos.
# =============================================================================

np.random.seed(42)

muestras = {
    'A_baja':  3.4,
    'B_media': 3.8,
    'C_alta':  4.5,
}

# Parámetros base de cada analista
analistas_base = {
    'Analista_1': {'sesgo':  0.00, 'sigma': 0.04},
    'Analista_2': {'sesgo':  0.00, 'sigma': 0.08},
    'Analista_3': {'sesgo': +0.10, 'sigma': 0.12},
    'Analista_4': {'sesgo': -0.35, 'sigma': 0.06},
    'Analista_5': {'sesgo':  0.00, 'sigma': 0.25},
}

meses = range(1, 13)  # 12 meses
repeticiones = 3

def sesgo_analista4(mes):
    """
    Analista 4: formación en mes 4.
    Mejora progresiva del sesgo de -0,35% a -0,05% entre meses 4 y 8.
    """
    if mes < 4:
        return -0.35
    elif mes <= 8:
        # Interpolación lineal entre -0,35 y -0,05
        return -0.35 + (mes - 4) * (0.30 / 4)
    else:
        return -0.05

def sigma_analista5(mes):
    """
    Analista 5: formación en mes 6.
    Mejora progresiva de sigma de 0,25% a 0,08% entre meses 6 y 10.
    """
    if mes < 6:
        return 0.25
    elif mes <= 10:
        # Interpolación lineal entre 0,25 y 0,08
        return 0.25 - (mes - 6) * (0.17 / 4)
    else:
        return 0.08

filas = []
for mes in meses:
    fecha = pd.Timestamp(f'2024-{mes:02d}-15')  # día 15 de cada mes

    for analista, base in analistas_base.items():
        # Calcular parámetros del mes actual
        if analista == 'Analista_4':
            sesgo = sesgo_analista4(mes)
            sigma = base['sigma']
        elif analista == 'Analista_5':
            sesgo = base['sesgo']
            sigma = sigma_analista5(mes)
        else:
            sesgo = base['sesgo']
            sigma = base['sigma']

        for muestra, valor_referencia in muestras.items():
            for rep in range(1, repeticiones + 1):
                resultado = (
                    valor_referencia
                    + sesgo
                    + np.random.normal(0, sigma)
                )
                filas.append({
                    'fecha':            fecha.strftime('%d/%m/%Y'),
                    'mes':              mes,
                    'analista':         analista,
                    'muestra':          muestra,
                    'valor_referencia': valor_referencia,
                    'repeticion':       rep,
                    'resultado':        round(resultado, 2),
                })

df = pd.DataFrame(filas)
nombre_fichero = '/home/claude/datos/grr_gerber_temporal.csv'
df.to_csv(nombre_fichero, index=False, sep=';', decimal=',', encoding='ISO-8859-1')

print(f"Dataset temporal generado: {nombre_fichero}")
print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
print(f"\nPrimeras filas:")
print(df.head(6).to_string(index=False))
print(f"\nÚltimas filas:")
print(df.tail(6).to_string(index=False))

# Verificación: sesgo medio del analista 4 por mes
print("\nEvolución del sesgo medio del Analista 4 (muestra B_media):")
check = df[(df['analista']=='Analista_4') & (df['muestra']=='B_media')]
for mes in meses:
    datos_mes = check[check['mes']==mes]
    sesgo_obs = datos_mes['resultado'].mean() - 3.8
    print(f"  Mes {mes:2d}: sesgo observado = {sesgo_obs:+.3f}%")
