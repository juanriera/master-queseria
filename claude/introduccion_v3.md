---
lang: es
---

# Introducción

La industria alimentaria genera cada vez más datos: sensores, líneas automatizadas, sistemas de trazabilidad. Transformar esos datos en información útil para la toma de decisiones es ya una competencia esencial para cualquier técnico de planta, tanto en el trabajo diario como en la presentación de resultados ante la Dirección.

Este libro aborda las herramientas y métodos del análisis de datos en la producción industrial. La hoja de cálculo es el eje central, complementada con una introducción progresiva a los lenguajes **Python** y **R**. El enfoque es práctico: se hace hincapié en los métodos gráficos y en el análisis exploratorio, reduciendo al mínimo la estadística formal.

Una idea recorre todo el libro: entender *en qué consiste* un estadístico es más importante que saber *cómo se calcula*. Se busca desarrollar el juicio analítico del estudiante, no memorizar fórmulas. Un buen ejemplo es la media aritmética: veremos que su valor equivale al centro de gravedad de los datos —como el punto de equilibrio de una palanca— y eso explica de forma intuitiva por qué los valores extremos la distorsionan, y cuándo conviene usar otros estadísticos como la mediana. Este tipo de razonamiento práctico, apoyado en analogías físicas concretas, es el que se utiliza a lo largo de todo el libro.


## Por qué aprender Python y R, además de la hoja de cálculo

La hoja de cálculo sigue siendo imprescindible en la empresa, y en este libro se trata con detalle. Pero los lenguajes de programación tienen una ventaja práctica que no puede ignorarse: el código documenta cada paso del análisis, lo que permite verificarlo, repetirlo y compartirlo. Esto es la **reproducibilidad** —concepto que se desarrolla en el capítulo 3—, y es cada vez más valorada tanto en la industria como en las auditorías de calidad.

Hay además una razón muy concreta para el sector alimentario: las normas de calidad y seguridad alimentaria —IFS, BRC, ISO 22000— exigen que los datos de proceso estén documentados y sean verificables. Un flujo de trabajo basado en código cumple ese requisito de forma natural, y quien sepa trabajar así tendrá una ventaja real en cualquier auditoría.

Otras razones de peso:

- **Python** es el lenguaje de referencia en inteligencia artificial y el más extendido en la industria. Su conocimiento, aunque sea básico, representa un valor diferencial en cualquier currículum técnico.
- **R** es el lenguaje de referencia en análisis estadístico y de datos, con uno de los mayores índices de crecimiento entre los lenguajes de programación.
- Ambos son gratuitos y de código abierto. En este libro se usa **Google Colab**, que permite ejecutar scripts Python en el navegador sin instalar nada.

Este libro no pretende formar programadores. El código se usa como sucesión de órdenes sencillas en scripts cortos, al servicio de la comprensión del análisis. La programación en Excel —macros, Visual Basic— queda fuera del alcance.


## Recursos adicionales

Para quienes deseen ampliar su formación, plataformas como Datacamp, edX, Udemy y Coursera ofrecen cursos gratuitos de Python, R y estadística aplicada. La editorial **OpenStax** ([openstax.org](https://openstax.org/), Universidad Rice, EE. UU.) publica recursos educativos abiertos de alta calidad, algunos en español, que pueden complementar el estudio:

- *Workplace Software and Skills*
- *Principles of Data Science*
- *Introduction to Python Programming*
- *Introducción a la estadística empresarial*
- *Introductory Business Statistics 2e*

Todos los datos de los ejemplos están disponibles en hojas de cálculo y ficheros CSV, accesibles mediante enlaces directos en el texto desde el repositorio GitHub del libro. Al final se incluye la bibliografía completa.


---

## Nota para los equipos docentes

Esta sección recoge argumentos y referencias pensados para apoyar la inclusión de estas materias en los ciclos formativos de la rama alimentaria, tanto en la programación didáctica como en la justificación ante equipos directivos o claustros.

### Demanda del mercado laboral

El último *Informe sobre el futuro del empleo* del Foro Económico Mundial (WEF, junio de 2025) sitúa el **pensamiento analítico** como la principal habilidad básica demandada por los empleadores, e identifica el **análisis de datos** y la **inteligencia artificial** como las dos competencias con mayor crecimiento en los últimos dos años:

> «El pensamiento analítico sigue siendo la principal habilidad básica para los empleadores: siete de cada diez empresas lo consideran esencial. [...] La capacidad de resolución de problemas y la resiliencia personal son críticas para el éxito.»
>
> — WEF, *Future of Jobs Report* 2025

Python ocupa el primer puesto en el índice TIOBE de lenguajes de programación, y R figura entre los diez primeros con uno de los mayores índices de crecimiento. El Principado de Asturias ha establecido el desarrollo de competencias en inteligencia artificial como línea prioritaria para la FP, y varias empresas de la región ya están implantando experiencias en esa dirección.

### Digitalización industrial y trazabilidad

La transformación digital de la industria alimentaria —Industria 4.0, sistemas MES (*Manufacturing Execution Systems*), sensores conectados— está generando volúmenes de datos de proceso que las empresas necesitan analizar para mejorar su competitividad. Los técnicos que salgan de la FP se incorporarán a plantas donde esta realidad ya es cotidiana.

Por otro lado, el Reglamento (CE) 178/2002 y las normas de certificación del sector —IFS, BRC, ISO 22000— exigen trazabilidad documental completa y datos de proceso verificables. Un técnico que trabaje con flujos de análisis reproducibles y documentados en código responde a esa exigencia de forma natural, y aporta una garantía adicional de rigor frente a los errores habituales de las hojas de cálculo no controladas.

### El problema de los errores en hojas de cálculo

La literatura académica sobre fiabilidad de hojas de cálculo es inequívoca: estudios sistemáticos estiman que entre el 20 % y el 90 % de las hojas de uso profesional contienen errores, la mayoría silenciosos y difíciles de detectar [@panko2008; @powell2009]. En un entorno donde una decisión basada en datos erróneos puede afectar a la seguridad del producto o a la conformidad con una auditoría, este no es un argumento menor.

El código en Python o R, al ser revisable paso a paso y ejecutable de forma reproducible, reduce estructuralmente ese riesgo. No se trata de abandonar la hoja de cálculo, sino de complementarla con herramientas que aporten trazabilidad y control al proceso de análisis.

### Orientación didáctica

Algunas sugerencias para el uso de este libro en el aula:

- Los capítulos de hoja de cálculo y los de Python/R son en gran medida independientes. Es posible trabajar solo con Excel/Calc en un primer curso e introducir el código en un segundo, o alternar ambos a lo largo del mismo módulo.
- Google Colab no requiere instalación ni cuenta de pago. Basta con una cuenta Google estándar, lo que elimina barreras técnicas en el aula.
- Los informes automatizados con Quarto o Colab (código + texto + resultados en un único documento) pueden usarse como formato de entrega de prácticas, facilitando la corrección y la evaluación entre pares.
- Los recursos de OpenStax mencionados anteriormente están disponibles en abierto e incluyen materiales para el docente (guías, bancos de ejercicios). El Gobierno de España también ofrece cursos de R dentro de su iniciativa de datos abiertos ([datos.gob.es](https://datos.gob.es/es/noticia/cursos-para-aprender-mas-sobre-r)).

Todos los conjuntos de datos usados en los ejemplos están disponibles en el repositorio GitHub del libro con licencia abierta, y pueden reutilizarse libremente para diseñar nuevos ejercicios o adaptar los existentes.
