[![](https://img.shields.io/badge/IBM%20Cloud-powered-blue.svg)](https://cloud.ibm.com)
[![](https://img.shields.io/discord/734849242153222221?logo=discord)](https://discord.gg/yJYmTGDWKH)

# Desafío 05 | SONDA

- [1. Sobre SONDA](#1-sobre-sonda)
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

## 1. Sobre SONDA

SONDA es la principal red latinoamericana de servicios de Tecnología de la Información (TI). En sus casi 45 años de historia en la región, se ha caracterizado por contar con una oferta integral de servicios y soluciones de TI, una visión de aliado tecnológico para abordar proyectos y una sólida posición financiera, brindando consistentemente servicios y soluciones alineadas con el negocio. estrategias de sus clientes.

Desde 1974, la empresa tiene como misión agregar valor a las actividades y negocios de nuestros clientes e impulsar su crecimiento a través de un mejor uso de las tecnologías de la información, construyendo relaciones de largo plazo que se traduzcan en proximidad a su trabajo y evolución.

### 1.1. Introducción

### 1.2. Premiación

Las top 5 personas mejor puntuadas en su desafío recibirán un voucher de US$ 350 cada una.

## 2. Desafio de negocio

El desafío es un problema común en el campo de la ciencia de datos. Un cliente expone un problema específico en su área y mediante su análisis encuentra una posible solución. Un cliente del área de Telecomunicaciones reportó un problema de pérdida de cliente (Churn) y le gustaría poder identificar esta posible pérdida antes de que ocurra, utilizando inteligencia artificial.

## 3. Objetivo

El desafío es implementar un algoritmo de Machine Learning para la clasificación binaria, capaz de identificar si un cliente se abandonará la empresa o no.

## 4. Tecnologias aplicadas

Para este desafío se utilizarán los siguientes servicios de IBM Cloud:

- [Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio), también conocido como Cloud Pak for Data as a Service. Este servicio permite el uso de una variedad de herramientas relacionadas con la ciencia de datos, incluida la ejecución de Jupyter Notebooks con procesadores en la nube.

## 5. Desarrollo de la Solución

### 5.1. Pre-requisitos

Para realizar este desafío, deberás cumplir con los siguientes requisitos previos:

- Registrarte en la [Maratón Behind the Code](https://maratona.dev/?register=true) y confirmar tu correo electrónico de registro;
- Tener una [cuenta de IBM Cloud](https://ibm.biz/Bdf8dW), que puede ser Lite o Pay-As-You-Go (no es necesario registrarse para el evento con la misma dirección de correo electrónico utilizada para crear su cuenta de IBM Cloud).

### 5.2. Resumen de Tareas

1. Crear una instancia de los servicios de desafío en IBM Cloud: Object Storage y Watson Studio (opcionales);
2. Explorar y tratar [los datos disponibles](../../assets/data/dataset.csv) ;
3. Crear un modelo de aprendizaje automático para realizar una clasificación binaria;
4. Cambiar, validar y probar tu modelo de Machine Learning, hasta que estés satisfecho con el resultado;
5. Cambiar el [archivo de respuesta](../../assets/data/ANSWERS.csv) agregando las clasificaciones del modelo;
6. Enviar tu solución en la [página del desafío](https://maratona.dev/challenge/5).

### 5.3. Desarollo

El desafío es utilizar un algoritmo de aprendizaje automático de aprendizaje supervisado, como [Decision Tree](https://scikit-learn.org/stable/modules/tree.html), para realizar una clasificación binaria que dirá si un cliente va a ser perdido o no.

Las calificaciones deben guardarse en el archivo [ANSWERS.csv](../../assets/data/ANSWERS.csv), tal como aparecen en el conjunto de datos (`Yes` o` No`). Todos los clientes deben tener una calificación.

El diccionario de [los datos](../../assets/data/dataset.csv) es el siguiente:

| Columna          | Descripción                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| ID               | Customer ID                                                                                                        |
| GENDER           | Whether the customer is a male or a female                                                                         |
| SENIORCITIZEN    | Whether the customer is a senior citizen or not (1, 0)                                                             |
| PARTNER          | Whether the customer has a partner or not (Yes, No)                                                                |
| DEPENDENTS       | Whether the customer has dependents or not (Yes, No)                                                               |
| TENURE           | Number of months the customer has stayed with the company                                                          |
| PHONESERVICE     | Whether the customer has a phone service or not (Yes, No)                                                          |
| MULTIPLELINES    | Whether the customer has multiple lines or not (Yes, No, No phone service)                                         |
| INTERNETSERVICE  | Customer’s internet service provider (DSL, Fiber optic, No)                                                        |
| ONLINESECURITY   | Whether the customer has online security or not (Yes, No, No internet service)                                     |
| ONLINEBACKUP     | Whether the customer has online backup or not (Yes, No, No internet service)                                       |
| DEVICEPROTECTION | Whether the customer has device protection or not (Yes, No, No internet service)                                   |
| TECHSUPPORT      | Whether the customer has tech support or not (Yes, No, No internet service)                                        |
| STREAMINGTV      | Whether the customer has streaming TV or not (Yes, No, No internet service)                                        |
| STREAMINGMOVIES  | Whether the customer has streaming movies or not (Yes, No, No internet service)                                    |
| CONTRACT         | The contract term of the customer (Month-to-month, One year, Two year)                                             |
| PAPERLESSBILLING | Whether the customer has paperless billing or not (Yes, No)                                                        |
| PAYMENTMETHOD    | The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)) |
| MONTHLYCHARGES   | The amount charged to the customer monthly                                                                         |
| TOTALCHARGES     | The total amount charged to the customer                                                                           |
| CHURN            | Whether the customer churned or not (Yes or No)                                                                    |

**Atención**: los datos proporcionados en este desafío son ficticios, cualquier correlación con la realidad es mera coincidencia.

## 6. Envío

Con las respuestas en el archivo, el último paso es realizar el envío. Recuerda que **sólo se aceptará un envío para el desafío**, así que pruébalo bien antes de enviarlo.

Para realizar el envío, debes acceder a la [página de desafío](https://maratona.dev/challenge/5) y enviar el archivo CSV con las respuestas, junto con un archivo `.zip`, de hasta 10 MB, conteniendo el código fuente de la solución (recuerda eliminar dependencias y conjuntos de datos para que no ocupen espacio). La página probará el archivo CSV para verificar que se encuentra en el formato correcto.

Podrás seguir el estado de la entrega accediendo a la [página del desafío](https://maratona.dev/challenge/5), iniciando sesión en tu cuenta.

## 7. Sobre la evaluación

Una semana después del inicio del desafío, nuestro sistema de evaluación automatizado iniciará las evaluaciones. Utilizará los datos para calcular una puntuación numérica del 1 al 100, basado en la métrica [F<sub>1</sub>](https://en.wikipedia.org/wiki/F-score). El archivo `.zip` enviado debe contener todo el código utilizado para obtener la solución. De lo contrario, la puntuación será cero.

El desafío debe ser entregado hasta el 12 de diciembre, y el participante recibirá una bonificación del 10% de la puntuación total (10 puntos), independientemente del resultado de su desafío. Por tanto, la puntuación máxima posible es 110 (puntuación de 100 + bonificación de 10).

Después del plazo de envío, el participante aún puede realizar su envío hasta el 12 de diciembre, pero sin recibir la bonificación.

**Atención**: el tiempo de entrega es un criterio de desempate, en caso de dos soluciones con la misma puntuación. Nos reservamos el derecho de darle a um envío cero de puntuación si:

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
