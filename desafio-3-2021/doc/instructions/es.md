[![](https://img.shields.io/badge/IBM%20Cloud-powered-blue.svg)](https://cloud.ibm.com)
[![](https://img.shields.io/discord/734849242153222221?logo=discord)](https://discord.gg/yJYmTGDWKH)

# Desafío 03 | GFT

- [1. Sobre GFT](#1-sobre-gft)
  - [1.1. Introducción](#11-introducción)
  - [1.2. Premiación](#12-premiación)
- [2. Desafio de negocio](#2-desafio-de-negocio)
- [3. Objetivo](#3-objetivo)
- [4. Tecnologias aplicadas](#4-tecnologias-aplicadas)
- [5. Desarrollo de la Solución](#5-desarrollo-de-la-solución)
  - [5.1. Pre-requisitos](#51-pre-requisitos)
  - [5.2. Resumen de Tareas](#52-resumen-de-tareas)
  - [5.3. Desarollo](#53-desarollo)
- [6. Envío](#6-envío)
- [7. Sobre la evaluación](#7-sobre-la-evaluación)

## Para ayudarte

- [Material de Apoyo](#materiales-de-apoyo)

## 1. Sobre GFT

### 1.1. Introducción

GFT es una empresa especializada en servicios de TI para el sector financiero, enfocada
en apoyar los procesos de transformación digital de los clientes, ofreciendo innovación,
calidad y tecnología de punta con agilidad y escala.

Posee una amplia experiencia en el sector financiero, desde la banca minorista hasta los
mercados de capitales. Además, también está impulsando la transformación digital de
los sectores industrial y de seguros.

GFT lleva 34 años innovando, desde 1987 dando forma al progreso tecnológico en el
mundo. Está presente en 15 países, con más de 7000 empleados en todo el mundo, y
solo en Brasil cuenta con más de 2500 personas. GFT cree en un mundo digital y que
para un crecimiento exponencial es necesario ser innovador en el campo de las
tecnologías de la información.

Con GFT, la tecnología ofrece un valor comercial claro, lo que permite a los clientes ser
líderes en sus mercados.

<div align="center">
    <a href="https://youtu.be/zxKtukevSHk">
        <img width="375" src="../img/video.jpg" alt='video'>
    </a>
</div>

### 1.2. Premiación

GFT premiará a las 3 (tres) personas mejor puntuadas en su desafío a través de tarjetas de regalo (en dólares) en el siguiente orden:

- Top 1 - US$ 850
- Top 2 - US$ 460
- Top 3 - US$ 350.

## 2. Desafio de negocio

El desafío GFT Open Finance permitirá a los participantes enfrentar la nueva realidad del intercambio de información, confrontando bases de datos de tres instituciones diferentes, dos bancos y una compañía de seguros y, a partir de estos datos, desarrollar una visión holística mejorada del cliente y a través de la Ciencia de los datos, realizar el modelado de la mejor oferta y canasta de productos para estos clientes. ¡Se practicarán habilidades de ingeniería de datos y ciencia de datos!

Open Finance es la evolución de Open Banking, es el sistema financiero abierto que traerá más transparencia y autonomía a los usuarios. Con él, será posible que un individuo decida qué instituciones tendrán acceso a su información, para qué fines específicos, y período. A medida que evolucione la implementación de Open Finance, existirá la posibilidad de compartir datos sobre seguros, inversiones, fondos de pensiones y fondos de pensiones. La implementación de Open Finance en Brasil se dividió en cuatro fases. Ellas son:

1. **Apertura de los datos de las instituciones**
    - La primera fase, que comenzó el 21 de febrero, fue cuando las instituciones financieras pusieron a disposición del público información básica, como los canales de atención y los servicios ofrecidos.
2. **Compartir datos de clientes**
    - Los clientes ahora toman un papel activo en compartir su información, pudiendo, si así lo desean, compartir datos que marcan la diferencia al momento de ofrecer mejores productos (datos de registro, transacciones de cuentas, datos de tarjetas y datos de transacciones de crédito). El paso se implementó el pasado 13 de agosto.
3. **Presentación de propuesta de inicio de pago y operación de crédito**
    - En esta fase se inicia la integración de los servicios con las operaciones de pago y el envío de propuestas para operaciones de crédito, que se desarrolla en un entorno unificado.
4. **Otros datos de productos y servicios**
    - Esta fase, que se implementará a partir del 15 de diciembre, será responsable de la inclusión de servicios más complejos (como inversiones, pensiones, seguros y cambio de divisas) en el sistema.

En una visión financiera abierta, el Banco Minorista (RetailBankEFG) tiene acceso a través de financiamiento abierto, con el debido consentimiento de los clientes, a la información de la institución financiera (InvestmentBankCDE), un banco de inversión y la información de estos clientes sobre otra institución financiera y compañía de seguros (InsuranceCompanyABC).

## 3. Objetivo

El desafío consiste en agregar las bases de estas instituciones que brinda el nuevo entorno Open Finance, procesar los datos y desarrollar modelos de recomendación de productos utilizando algoritmos como [Apriori](https://en.wikipedia.org/wiki/Apriori_algorithm) y [AssociationRules](https://en.wikipedia.org/wiki/Association_rule_learning), considerando una confianza en la regla del 80% y un soporte mínimo del 10% con un máximo de 5 antecedentes.

Las personas de la base estarán respaldadas por este modelo y se deberá someter a análisis el archivo de respuestas con las recomendaciones, con lo cual se verificará el porcentaje de respuestas correctas para cada recomendación.

Recuerda que muchas personas se quedarán sin una recomendación.

## 4. Tecnologias aplicadas

Para este desafío se utilizarán los siguientes servicios de IBM Cloud:

-  [Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio), también conocido como Cloud Pak for Data as a Service. Este servicio permite el uso de una variedad de herramientas relacionadas con la ciencia de datos, incluida la ejecución de Jupyter Notebooks con procesadores en la nube.
-  SPSS Modeler Flow

## 5. Desarrollo de la Solución

### 5.1. Pre-requisitos

Para realizar este desafío, deberás cumplir con los siguientes requisitos previos:

- Registrarte en la [Maratón Behind the Code](https://maratona.dev/?register=true) y confirmar su correo electrónico de registro;
- Tener una [cuenta de IBM Cloud](https://ibm.biz/Bdf8dW), que puede ser Lite o Pay-As-You-Go (no es necesario registrarse para el evento con la misma dirección de correo electrónico utilizada para crear su cuenta de IBM Cloud).

### 5.2. Resumen de Tareas

1. Crea una instancia de los servicios de desafío en IBM Cloud: Object Storage y Watson Studio (opcionales);
2. Explora y trabaja con las bases de datos disponibles;
3. Crea reglas de asociación basadas en los datos propuestos;
4. Crea recomendaciones de productos para los clientes, basadas en reglas de asociación creadas;
5. Cambia el [archivo de respuesta](../../assets/data/ANSWERS.csv) agregando las recomendaciones creadas junto con sus niveles de confianza;
6. Envía tu solución en la [página del desafío](https://maratona.dev/challenge/3).

### 5.3. Desarollo

Los conjuntos de datos [InvestmentBankCDE](../../assets/data/InvestmentBankCDE.csv) y [RetailBankEFG](../../assets/data/RetailBankEFG.csv) contienen datos de compras de clientes anteriores, al igual que el conjunto de datos [InsuranceCompanyABC](../../assets/data/InsuranceCompanyABC.csv), que también incluye algunos datos demográficos de sus clientes.

El desafío es utilizar un algoritmo de aprendizaje automático de aprendizaje no supervisado, como los de [Reglas de Asociación](https://en.wikipedia.org/wiki/Association_rule_learning#Algorithms), para crear recomendaciones de productos para los clientes de las bases de datos. Se deben utilizar los datos de clientes recopilados de las tres instituciones y se pueden hacer hasta tres recomendaciones de productos. Para recomendaciones, deberás considerar una **confianza de regla del 80%** y un **soporte mínimo del 10%**, con un máximo de 5 antecedentes.

Tu tarea es analizar los datos y crear un modelo para recomendaciones a partir de esos datos. Las recomendaciones (hasta 3 por cliente) deben guardarse en el archivo [ANSWERS.csv](../../assets/data/ANSWERS.csv). Ten en cuenta que no todos los clientes necesitan necesariamente una recomendación.

Los siguientes nombres de los productos en las recomendaciones deben aparecer **exactamente** como están en las columnas del conjunto de datos:

```python
[
  "seguro auto",
  "seguro vida Emp",
  "seguro vida PF",
  "Seguro Residencial",
  "Investimento Fundos_cambiais",
  "Investimento Fundos_commodities",
  "Investimento LCI",
  "Investimento LCA",
  "Investimento Poupanca",
  "Investimento Fundos Multimercado",
  "Investimento Tesouro Direto",
  "Financiamento Casa",
  "Financiamento Carro",
  "Emprestimo _pessoal",
  "Emprestimo _consignado",
  "Emprestimo _limite_especial",
  "Emprestimo _educacao",
  "Emprestimo _viagem",
  "Investimento CDB",
  "Investimento Fundos"
]
```

**Atención**: los datos proporcionados en este desafío son ficticios, cualquier correlación con la realidad es mera coincidencia.

## 6. Envío

Una vez tengas el modelo listo, el último paso es realizar el envío. Recuerda que **sólo se aceptará un envío para el desafío**, así que pruébalo bien antes de enviarlo.

Para entregar el desafío, debes cambiar el archivo con la tabla de respuestas disponible en ese repositorio, completando el valor de las columnas de recomendación y confianza, sólo cuando ocurra una recomendación. Evaluaremos tu solución en base a las respuestas en el archivo CSV.

Para realizar el envío, debes acceder a la [página de desafío](https://maratona.dev/challenge/3) y enviar el archivo CSV con las respuestas, junto con un archivo `.zip`, de hasta 10 MB, conteniendo el código fuente de la solución (recuerda eliminar dependencias y conjuntos de datos para que no ocupen espacio). La página probará el archivo CSV para verificar que se encuentra en el formato correcto.

Podrás seguir el estado de la entrega accediendo a la [página del desafío](https://maratona.dev/challenge/3), iniciando sesión en tu cuenta.

## 7. Sobre la evaluación

Una semana después del inicio del desafío, nuestro sistema de evaluación automatizado iniciará las evaluaciones. Utilizará los datos para calcular una puntuación numérica del 1 al 100, basado en el nível de asertividad de las recomendaciones, junto con el nível de confianza de las mismas. El archivo `.zip` enviado debe contener todo el código utilizado para obtener la solución. De lo contrario, la puntuación será cero.

Si el desafío se entrega dentro del plazo de envío (hasta el 05 de diciembre), el participante recibirá una bonificación del 10% de la puntuación total (10 puntos), independientemente del resultado de su desafío. Por tanto, la puntuación máxima posible es 110 (puntuación de 100 + bonificación de 10).

Después del plazo de envío, el participante aún puede realizar su envío hasta el 12 de diciembre, pero sin recibir el bono.

**Atención**: el tiempo de entrega es un criterio de desempate, en caso de dos soluciones con la misma puntuación. Nos reservamos el derecho de darle a um envío cero de puntuación si:

- El código fuente enviado no es consistente con los resultados obtenidos de las pruebas en el modelo.
- Se detecta plagio, de uno o más participantes. En este caso, se dará cero puntos al desafio entregado por todos los participantes con la misma solución.

## Materiales de apoyo

- [Introducción a IBM Watson Studio](https://developer.ibm.com/es/articles/introduction-watson-studio/)
- [Toma el control de tus datos con Watson Studio](https://developer.ibm.com/es/series/learning-path-watson-studio/)
- [Visualizar datos con Python](https://developer.ibm.com/es/patterns/visualize-data-with-python/)
- [Introducción a IBM Cloud Pak for Data](https://developer.ibm.com/es/articles/get-started-with-ibm-cloud-pak-for-data/)
- [Creación de flujos de SPSS Modeler en IBM Watson Studio](https://developer.ibm.com/es/tutorials/watson-studio-spss-modeler-flow/)

Recuerda que puedes acceder al Discord oficial del Maratón 2021 para hacer preguntas y/o interactuar con otros participantes: [Discord](https://discord.gg/yJYmTGDWKH).

## License

Copyright 2021 Maratona Behind the Code

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
