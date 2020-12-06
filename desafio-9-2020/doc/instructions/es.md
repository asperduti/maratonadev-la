[![](https://img.shields.io/badge/IBM%20Cloud-powered-blue.svg)](https://cloud.ibm.com) [![](https://img.shields.io/badge/deploy%20on-OpenShift-red)]()

# Maratón BTC 2020 | Desafío Final Red Hat

- [1. Acerca de Red Hat](#1-acerca-de-red-hat)
- [2. Resumen del desafío](#2-resumen-del-desafio)
    - [2.1. Introducción](#21-introducción)
    - [2.2. Objetivo](#22-objetivo)
- [3. Desarrollo](#3-desarollo)
    - [3.1. Construcción del pipeline de ML](#31-construcción-del-pipeline-de-ml)
    - [3.2. Aplicación en contenedor en OpenShift](#32-aplicação-en-contenedor-en-openshift)
- [4. Sobre la evaluación](#4-sobre-la-evaluación)
- [5. Soporte](#5-soporte)

<hr>

## 1. Acerca de Red Hat

Red Hat Inc. comenzó cuando un pequeño empresario conoció a un geek en una conferencia de tecnológica. Marc Ewing era el tecnólogo ocupado en hackear, depurar y hacer funcionar su propia distribución de Linux® en CDs desde su casa en Raleigh, Carolina del Norte.

Red Hat continúa transformando el futuro de la tecnología de código abierto al unir fuerzas con IBM. En 2019, IBM adquirió Red Hat por aproximadamente US$34 mil millones, rompiendo el récord de la mayor adquisición de software de la historia. Juntos, IBM y Red Hat continuarán innovando con una plataforma multicloud híbrida de próxima generación con el objetivo de redefinir el mercado de la nube para las empresas. A medida que la empresa mira hacia el futuro, Red Hat sigue siendo Red Hat y sigue manteniendo los mismos valores y principios que guían su marca.

En más de 25 años, Red Hat ha pasado de ser una pequeña empresa desde el hogar a ser el principal proveedor mundial de soluciones empresariales de código abierto. La percepción ha pasado de ver a Red Hat como un rebelde disruptivo a un asesor de confianza. La compañía se ha movido mucho más allá de Red Hat Enterprise Linux hacia la virtualización, middleware, desarrollo de aplicaciones, almacenamiento, computación en la nube y administración. Como siempre, todo sigue siendo Open Source.

La plataforma de contenedores OpenShift, construida sobre la base de Kubernetes, es uno de los productos que ofrece Red Hat para la gestión empresarial de aplicaciones en contenedores, y tendrá acceso a esta excelente herramienta para ayudarlo a completar el DESAFÍO FINAL del Maratón Detrás del Código 2020.

## 2. Resumen del desafío

### 2.1. Introducción 

Hace muchos años ocurria que los principales descubrimientos en astronomía se hacian a simple vista. Hoy en día, la astronomía moderna está hecha con herramientas de alta tecnología como un potente telescopio que amplifica un punto pequeño en una galaxia lejana, radiotelescopios que obtienen señales de radio del espacio profundo y mapean el universo observable, una red completa de telescopios que observan el mismo punto y luego forman una imagen de agujero negro, o en un telescopio en órbita como el Hubble.

Machine Learning es una tecnología emergente que puede ayudar en muchas áreas de la ciencia, como la astronomía. Hoy en día, los Atrónomos tienen una gran cantidad de datos disponibles de muchas fuentes diferentes y con muchos tipos diferentes de propósitos. Un campo interesante de la atronomía es la exploración de planetas que consiste en encontrar nuevos planetas para mapear nuestro vecindario cósmico y obtener una mejor comprensión del universo.

Encontrar un nuevo planeta es una tarea difícil porque la tecnología para encontrarlos se creó hace algunas décadas y algunos de ellos ni siquiera podemos verlos. Todavía hay preguntas abiertas en cuanto al descubrimiento de un planeta sin verlo. Afortunadamente, cada nuevo posible descubrimiento ha sido catalogado, lo que significa que hay muchos datos disponibles para diseñar un modelo de clasificación capaz de indicar si los datos realmente son un planeta, un falso positivo o un posible candidato a ser planeta y requieren más estudios y atención.

Con todo este nuevo mundo de posibilidades que los modelos de IA pueden aportar, ¿qué piensas que dirían Ptlomeu y Galileo sobre hasta dónde llegamos en ciencia y tecnología para mirar el cielo?

### 2.2. Objetivo

El objetivo del desafío es, en resumen, diseñar e implementar un modelo de clasificación de cuerpos celestes como una **Pinepline de Machine Learning para scikit-learn** en Watson Machine Learning Service (WML), y realizar la corrección de errores, pruebas y implementación de una aplicación en contenedores en OpenShift, capaz de realizar solicitudes HTTP para enviar su solución. La descripción general de la arquitectura de la solución construida se presenta en el siguiente diagrama:

![](../../doc/source/architecture.jpg)

## 3. Desarrollo

### 3.1. Construcción del pipeline de ML

Para la construcción de la Pipeline de ML, se proporcionan un <a href="../../data/dataset/dataset.csv">conjunto de datos</a> y un [Notebook Jupyter](../../data/notebook/notebook.ipynb), con gran parte del código boilerplate para comunicarse con la versión más reciente de WML, lanzado en octubre de 2020. Debe crear una instancia de <a href="https://cloud.ibm.com/catalog/services/watson-studio">Watson Studio</a>, <a href="https://cloud.ibm.com/catalog/services/machine-learning">Watson Machine Learning</a> y <a href="https://cloud.ibm.com/objectstorage/create">Cloud Object Storage</a>; cree un proyecto en blanco en Watson Studio e importe el conjunto de datos y el Notebook; construya la Pipeline de ML e impleméntela en WML siguiendo las instrucciones contenidas en el Notebook proporcionado. A continuación se enumeran algunos puntos importantes relacionados con la Parte 1 del desafío:

- En el Notebook proporcionado, se entrega parte del código Python para construir una Pipeline compatible con WML basada en scikit-learn 0.23.2.
- El Pipeline debe almacenarse en Watson Machine Learning. Cualquiera de los frameworks soportados oficialmente por WML será aceptado como solución, siempre que su pipeline esté completamente de acuerdo con lo que se especifica en este documento.
- El Pipeline debe aceptar como parámetros de entrada **todas las columnas del conjunto de datos proporcionado, excepto la columna `TARGET`**.
- No cambie bajo ninguna circunstancia el nombre de las variables en el conjunto de datos de entrada. Puede crear nuevas variables durante los pasos dentro de su Pipeline, pero las **variables de entrada deben ser exactamente las que se han definido**.
- No podrá crear instancias de Watson Studio y WML en la cuenta proporcionada para acceder al clúster de OpenShift, así que prepare su cuenta personal para crear los servicios.
- Para crear una instancia de los servicios de ML (Watson Studio, COS y WML), puede utilizar cualquier cuenta de IBM Cloud de su elección, incluida la creación de una nueva si ya no tiene CUHs disponibles en el nivel gratuito de este mes.
- Está permitido ejecutar el Notebook Jupyter fuera de Watson Studio, sin embargo, el equipo técnico no proporcionará soporte y **la implementación de una Pipeline compatible en WML sigue siendo obligatoria**.

Después de implementar su Pipeline de ML, puede pasar al segundo paso, que se realizará en el clúster de OpenShift proporcionado.

### 3.2. Aplicación en contenedor en OpenShift

En la última semana, se envió un tutorial para familiarizarlo con el entorno OpenShift. Este tutorial es simple y rápido de realizar y todavía está disponible en: https://github.com/MBTC-2020-TOP100/OPENSHIFT-TUTORIAL. Si no ha completado el tutorial, es muy recomendable que lo haga antes de continuar.

Con las credenciales y la URL principal de su Pipeline de ML encapsulada en Watson Machine Learning en la mano, ahora deberá implementar una aplicación capaz de realizar una solicitud HTTP **POST** a un servicio interno de OpenShift. Dicho servicio se expone a través de la siguiente URL:

<h4 style="color: blue">http://172.21.86.186:5000/submit</h4>

El *header* **Content-Type** de la solicitud HTTP debe ser del tipo **application/json** y el cuerpo de la solicitud debe ser un JSON con la siguiente estructura:
```
{
       email_addr: string,
       wml_url: string,
       iam_token: string,
       submit_confirmation: bool
}
```
- El parámetro **email_addr** debe ser de tipo *string*, que contenga su correo electrónico de IBM Cloud (el mismo que se completó en el formulario para acceder al clúster de OpenShift);
- El parámetro **wml_url** debe ser de tipo *string*, que contenga la *URL endpoint* de su Pipeline encapsulada en WML en el Paso 1 del Desafío;
- El parámetro **iam_token** debe ser de tipo *string* y contener una señal de autenticación de IBM Cloud de tipo IAM. Para generar este token es necesario realizar una solicitud previa, cuyos detalles se describen en la siguiente documentación: https://cloud.ibm.com/docs/account?topic=account-iamtoken_from_apikey;
- El parámetro **submit_confirmation** debe ser un valor de tipo *bool* (true o false). El valor "false" indica que desea realizar solo una prueba y saber si su Pipeline es válida y puede registrarse como una solución final; el valor "true" indica que desea enviar su solución para su puntuación. **ATENCIÓN: PUEDE REALIZAR CUÁNTAS PRUEBAS QUIERA, SIN EMBARGO, PUEDE ENVIAR UN ENVÍO VÁLIDO SOLO UNA VEZ**.

Debes investigar el resultado de las solicitudes realizadas por tu aplicación directamente en los registros de tus Deployment Pods en OpenShift. Recuerde el tutorial y las funciones manuales para reinicializar sus Pods.

Para ayudarlo en el desarrollo de la aplicación, algunas plantillas se proporcionan en diferentes lenguajes de programación que se enumeran a continuación. Pero tenga cuidado, las plantillas contienen errores que se insertaron intencionalmente y, si elige usarlos, primero debe corregir los errores y, en algunos casos, insertar parte de la lógica necesaria que falta.

- La aplicación se puede crear desde cero, en cualquier lenguaje de programación, pero la creación de contenedores y la implementación en OpenShift depende completamente de usted.
- A los participantes que creen loops infinitos de solicitudes al URL dado se les eliminarán sus Deployments automáticamente.

Enlaces al repositorio de las plantillas de solicitud de envío disponibles:

- [Clojure](https://github.com/MBTC-2020-TOP100/Clojure-Template)
- [Julia](https://github.com/MBTC-2020-TOP100/Julia-Template)
- [Rust](https://github.com/MBTC-2020-TOP100/Rust-Template)
- [Python](https://github.com/MBTC-2020-TOP100/Python-Template)
- [Node.js](https://github.com/MBTC-2020-TOP100/Node-Template)

Recuerde que cada plantilla tiene sus peculiaridades, con diferentes cantidades y tipos de errores. Incluso si nunca ha visto algunos de los idiomas, las aplicaciones son lo suficientemente simples como para que la sintaxis se aprenda rápidamente (¡Google y Stackoverflow son sus aliados!). Preste atención a los Dockerfiles suministrados, que al igual que los códigos, **no están listos** y necesitan ajustes en la mayoría de los casos.

## 4. Sobre la evaluación

La puntuación final del desafío se calculará en su totalidad en función de la "**puntuación f_beta**" de su modelo de ML. La *puntuación f_beta* es una variante de *"f_score"*. El *puntuación f_beta* se calcula usando una media armónica basada en la **Precisión**, el **Recall** del modelo evaluado y un parámetro beta. Para la puntuación de los modelos en este desafío, el parámetro beta se establece en **1.5**. Si lo desea, puede leer los detalles sobre la *puntuación f_beta* en el <a href="https://en.wikipedia.org/wiki/F-score">Wikipédia</a> o en <a href="https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html">documentación del método en scikit-learn</a>. En resumen, su modelo debe tener una buena **Recuperación** además de una buena **Precisión** para obtener una buena puntuación.

La construcción de la aplicación en contenedor es solo una "barrera" para la presentación de su solución y no vale puntos en el desafío; sin embargo, si no la completa, no podrá enviar su solución para que se califique.

Los campeones serán los participantes que produzcan los mejores modelos de ML. El tiempo de entrega del desafío se utilizará solo como criterio de desempate.

## 5. Soporte

El equipo de la Maratón estará brindando soporte en ambos servidores de discord, por lo que en caso de cualquier problema que tenga con la plataforma o los servicios, contáctenos e intentaremos ayudarlo. Busca **en el canal de dudas públicas** por Daniel o Ricardo.

**Recordando que no se responderán preguntas sobre el desafío o dudas sobre la plataforma y servicios que se enviarán en privado a cualquier miembro de la organización del evento.**

A continuación, encontrará un enlace a la documentación de los servicios y algunos tutoriales sobre cómo implementar otras bibliotecas en Watson Machine Learning que pueden ser útiles y cómo acceder al servicio a través de la API HTTP REST.

- [Documentación de Watson Studio (Cloud Pak for Data as a Service)](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/wml-ai.html)
- [Documentación de SDK Python do Watson Machine Learning](http://ibm-wml-api-pyclient.mybluemix.net)
- [Documentación de API REST do Watson Machine Learning](https://cloud.ibm.com/apidocs/machine-learning)
- [Tutoriales Watson Machine Learning](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-samples-overview.html)
- [Docker Hub](https://hub.docker.com/)

¡Buena suerte!

<hr>

## Licença

Copyright 2020 Maratona Behind the Code

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
