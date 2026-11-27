# Gráficos de contenido efectivo según el RD 1801/2008 (yogur de 150 g)
# Genera dos figuras en SVG:
#   imagenes/rd-1801-limite.svg : caso límite (media = Qn, 2,5 % bajo T1)
#   imagenes/rd-1801-proceso.svg: proceso real centrado por encima de Qn

library(ggplot2)
library(dplyr)

# --- Parámetros del producto y normativa ---
Qn   <- 150            # peso nominal (g)
emdt <- ceiling(0.045 * Qn * 10) / 10   # 4,5 % de 150 = 6,75 → redondeo por exceso (art. 8) = 6,8 g
T1   <- Qn - emdt      # límite de envase deficiente: 143,2 g
T2   <- Qn - 2 * emdt  # límite de envase no conforme: 136,4 g

# Formato numérico con coma decimal
num <- function(x, d = 1) formatC(x, format = "f", digits = d, decimal.mark = ",")

# --- Función que dibuja la curva del proceso con los límites ---
grafico_rd <- function(media, sd, titulo) {

  # Rango del eje: incluye siempre T2 con margen, aunque la curva esté alejada
  x_min <- min(T2 - 2, media - 4 * sd)
  x_max <- media + 4 * sd
  df <- tibble(x = seq(x_min, x_max, length.out = 2000),
               y = dnorm(x, mean = media, sd = sd))

  p_T1 <- pnorm(T1, media, sd) * 100   # % de envases deficientes (bajo T1)
  y_rot <- max(df$y) * 0.04            # altura de los rótulos verticales
  # Los rótulos de T1 y T2 empiezan por encima de la curva para no taparla
  y_T1 <- dnorm(T1, media, sd) + max(df$y) * 0.04
  y_T2 <- dnorm(T2, media, sd) + max(df$y) * 0.04

  p <- ggplot(df, aes(x = x, y = y)) +
    # Áreas de incumplimiento
    geom_area(data = filter(df, x <= T1), fill = "orange", alpha = 0.5) +
    geom_area(data = filter(df, x <= T2), fill = "red", alpha = 0.6) +
    geom_line(linewidth = 1.1, color = "grey20") +
    # Límites legales
    geom_vline(xintercept = T1, color = "darkorange", linewidth = 0.8) +
    geom_vline(xintercept = T2, color = "red", linewidth = 0.8) +
    geom_vline(xintercept = Qn, linetype = "dashed", color = "blue", linewidth = 0.8) +
    annotate("text", x = T1, y = y_T1, angle = 90, vjust = -0.5, hjust = 0,
             label = paste0("T1: envase deficiente (", num(T1, 1), " g)"),
             color = "darkorange", fontface = "bold") +
    annotate("text", x = T2, y = y_T2, angle = 90, vjust = -0.5, hjust = 0,
             label = paste0("T2 (", num(T2, 1), " g)"),
             color = "red", fontface = "bold") +
    annotate("label", x = (T1 + T2) / 2, y = max(df$y) * 0.30,
             label = paste0("Envases\ndeficientes\n", num(p_T1), " %"),
             fill = "white", size = 3.5, linewidth = 0.2)

  # Rótulo de Qn y, si es distinta, línea de la media del proceso
  if (isTRUE(all.equal(media, Qn))) {
    p <- p + annotate("text", x = Qn, y = y_rot, angle = 90, vjust = -0.5, hjust = 0,
                      label = paste0("Qn = media del proceso (", num(Qn, 0), " g)"),
                      color = "blue", fontface = "bold")
  } else {
    p <- p +
      geom_vline(xintercept = media, linetype = "dotted", color = "black", linewidth = 0.8) +
      annotate("text", x = Qn, y = y_rot, angle = 90, vjust = -0.5, hjust = 0,
               label = paste0("Qn (", num(Qn, 0), " g)"),
               color = "blue", fontface = "bold") +
      annotate("text", x = media, y = y_rot, angle = 90, vjust = -0.5, hjust = 0,
               label = paste0("Peso medio del proceso (", num(media), " g)"),
               color = "black")
  }

  p +
    scale_y_continuous(labels = scales::label_number(decimal.mark = ",")) +
    labs(title = titulo,
         subtitle = paste0("Yogur de ", num(Qn, 0), " g: EMDT = ", num(emdt, 1),
                           " g; media = ", num(media), " g; σ = ", num(sd, 2), " g"),
         x = "Peso (g)", y = "Densidad de probabilidad") +
    theme_minimal() +
    theme(panel.grid.minor = element_blank())
}

# --- Figura 1: caso límite ---
# Media igual a Qn y σ tal que exactamente el 2,5 % de los envases queda bajo T1
sd_limite <- emdt / qnorm(0.975)   # 6,8 / 1,96 = 3,47 g
g_limite <- grafico_rd(media = Qn, sd = sd_limite,
                       titulo = "Límites T1 y T2 del RD 1801/2008: caso límite")

# --- Figura 2: proceso centrado por encima de Qn ---
g_proceso <- grafico_rd(media = 152.5, sd = 4,
                        titulo = "Límites T1 y T2 del RD 1801/2008: proceso real")

ggsave("imagenes/rd-1801-limite.svg",  g_limite,  width = 8, height = 4.5)
ggsave("imagenes/rd-1801-proceso.svg", g_proceso, width = 8, height = 4.5)

ggsave("imagenes/rd-1801-limite.png", g_limite, width = 8, height = 4.5, dpi = 300, bg = "white")
ggsave("imagenes/rd-1801-proceso.png", g_proceso, width = 8, height = 4.5, dpi = 300, bg = "white")
