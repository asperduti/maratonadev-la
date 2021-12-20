[![](https://img.shields.io/badge/IBM%20Cloud-powered-blue.svg)](https://cloud.ibm.com)
[![](https://img.shields.io/discord/734849242153222221?logo=discord)](https://discord.gg/yJYmTGDWKH)

# Desafio 06 | Final

- [Premiación](#premiación)
- [Desafío de negocio](#desafío-de-negocio)
- [Objetivo](#objetivo)
- [Tecnologias aplicadas](#tecnologias-aplicadas)
- [Desarrollo de la solución](#desarrollo-de-la-solución)
  - [Resumen de tareas](#resumen-de-tareas)
  - [Desarrollo](#desarrollo)
- [Envío](#envío)
- [Sobre la evaluación](#sobre-la-evaluación)

## Para ayudarte

- [Material de Apoyo](#material-de-apoyo)

**Ten en cuenta**: Este desafío solo puede ser presentado por los participantes finales Top 100 Maratón Behind the Code 2021 enumerados en https://marathon.dev/ranking.

### Premiación

IT MEDIA dispone de 15 días para enviarle el bono de viaje. Los Top 100 obtendrán un cupón de $ 1200 y los Top 5 recibirán un cupón adicional de $ 1600. El Top 5 recibirá $ 2800.

Los premios no incluyen otros bienes, beneficios, coberturas o gastos, no se pueden revertir en efectivo ni en ningún otro medio que no sea viajar con la agencia de viajes indicada por el Organizador del Maratón.

## Desafío de negocio

El desafío es ayudar a los agricultores de una región en su trabajo, brindando información importante para el cultivo de una manera fácilmente accesible.

## Objetivo

El objetivo del desafío es crear un asistente virtual para ayudar en la agricultura en el municipio de Ribeirão Preto, que debe traer información para ayudar a los agricultores en su trabajo.

## Tecnologias aplicadas

Para este desafío serán utilizados los siguientes servicios:

- [Watson Assistant](https://cloud.ibm.com/catalog/services/watson-assistant), una plataforma para la creación de chatbots de manera fácil, a través de intenciones, entidades y flujo de diálogo, y varias posibilidades de integración.
- [The Weather Company](https://docs.google.com/document/d/15Ru_3wdMgpbM4aOCm-4qNAnRfjx2w-Ruw3lnr8Hnodk/edit), un servicio API que proporciona información meteorológica.
- [Cloud Functions](https://cloud.ibm.com/functions), un servicio para execución de funciones en la nube sin necesidad de un servidor (modelo conocido como Serverless).
- [Red Hat OpenShift](https://docs.openshift.com/container-platform/4.8/welcome/index.html), una robusta plataforma de orquestación de contenedores basada en Kubernetes.

## Desarrollo de la solución

### Resumen de Tareas

1. Crea un asistente virtual según las especificaciones siguientes;
2. Crea una función capaz de capturar los datos necesarios de la API meteorológica;
3. Integra la función al asistente a través de Webhooks;
4. Crea una aplicación capaz de enviar una solicitud HTTP para enviar el desafío;
5. Despliega la aplicación en un clúster de OpenShift y envía el desafío.

### Desarrollo

Tendrás que construir un asistente virtual, en **español**, que se utilizará para ayudar en la agricultura, y que debería poder brindar respuestas a los siguientes temas:

- Temperatura mínima y máxima, 15 días en el futuro
- Evapotranspiración en la próxima hora para el cultivo del café
- Evapotranspiración en la próxima hora para el cultivo de maíz
- Evapotranspiración en la próxima hora para el cultivo de soja
- Velocidad del viento durante el día, 15 días en el futuro
- Dirección del viento en notación magnética durante el día, 15 días en el futuro

**Informaciones importantes**:

- Las unidades de medida deben utilizar el sistema métrico.
- Para todos los artículos de cultivo, se debe considerar una madurez del 50%.
- Todas las respuestas del asistente deben ser de tipo texto. El asistente siempre debe considerar el municipio de Ribeirão Preto - SP, Brasil para consultas. Deben considerarse las siguientes coordenadas:

```text
LATITUD: -21.170401
LONGITUD: -47.810326
```

- No se requieren otras interacciones para el asistente, sólo las solicitadas anteriormente. El asistente siempre será abordado primero por el nodo Welcome, con texto vacío, antes de que se le hagan preguntas.
- Si se le pregunta al asistente sobre la evapotranspiración, pero no se especifica ningún elemento de cultivo, debe solicitar el elemento de cultivo deseado.
- Las temperaturas mínima y máxima deben aparecer siempre juntas en las respuestas.

Para obtener información, se deben utilizar las siguientes API de Weather:

- [Previsión meteorológica diaria para los próximos 15 días](https://ibm.co/V3DFap)
- [Pronóstico para la agricultura en los próximos 15 días](https://ibm.co/v3rA15D)

Las claves API para acceder a la API Weather estarán disponibles a través del servidor oficial de Finals Discord.

Para la integración de información con el asistente, debes utilizar un [Webhook](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-webhooks). Nuestra sugerencia para Webhooks es crear una acción en [Cloud Functions](https://cloud.ibm.com/functions), activándola como una acción web. Recuerda agregar un `.json` al final de la URL de acción web si lo vas a utilizar. Esta acción debe realizar llamadas a la API Weather para obtener la información solicitada por el asistente.

## Envío

Con el asistente listo, es hora de enviar. **Sólo se aceptará un envío para el desafío, así que pruébalo bien antes de enviarlo.**

Para realizar el envío, deberás enviar una solicitud HTTP POST a un servicio que se esté ejecutando en nuestro clúster de OpenShift. Para eso, deberá crear un contenedor y cargarlo en nuestro clúster de OpenShift. Una vez que se cargue, podrás acceder a nuestro servicio de envío a través de la red interna.

El servicio de envío estará a la escucha de solicitudes HTTP POST en la siguiente URL: `http://172.21.188.211:3000/submit`. En el cuerpo de la solicitud HTTP, se debe enviar un objeto JSON que contenga la siguiente información:

- Tu **correo electrónico** registrado para el Maratón Behind the Code 2021
- Las **credenciales de Watson Assistant**, que se pueden obtener en las ubicaciones detalladas en [Desafio 4](https://github.com/maratonadev/desafio-4-2021/blob/main/doc/instructions/pt.md#6-submiss%C3%A3o). Recuerda asociar tu Skill de Watson Assistant con el asistente.
- Una confirmación de envío, que puede ser `true` o `false`. En caso de que sea `false`, el sistema sólo evaluará si las credenciales son correctas para enviar. En el caso de `true`, los datos se enviarán en la forma final.

El objeto JSON debe tener el siguiente formato:

```json
{
  "email": "tu@email.com",
  "assistantId": "ID del Assistant",
  "url": "URL del Watson Assistant",
  "skillId": "ID de la Skill",
  "apiKey": "API key del Watson Assistant",
  "submitConfirmation": false
}
```

Recuerda cambiar `submitConfirmation` a `true` para realizar el envío final.

## Sobre la evaluación

El desafío será evaluado en base a la asertividad de las preguntas y respuestas del asistente virtual implementado. Las entregas se evaluarán hasta el final del desafío y el resultado se anunciará en el Live final.

## Material de Apoyo

- [Tutorial OpenShift](https://github.com/MBTC-2020-TOP100/OPENSHIFT-TUTORIAL)
- [Documentación de Watson Assistant](https://cloud.ibm.com/docs/assistant?topic=assistant-getting-started&locale=es)
- [Actualiza tu chatbot en WhatsApp con IBM Watson Assistant](https://developer.ibm.com/es/tutorials/integrating-ibm-watson-assistant-with-whatsapp/)
- [Crea un asistente de voz con Watson Assistant](https://developer.ibm.com/es/tutorials/crea-un-asistente-de-voz-para-una-pizzeria-con-watson-assistant/)
- [Cómo crear un chatbot utilizando Watson Assistant y Discovery.](https://developer.ibm.com/es/patterns/como-crear-un-chatbot-utilizando-watson-assistant-y-discovery/)
- [Documentación de Cloud Functions](https://cloud.ibm.com/docs/openwhisk?locale=pt-BR)

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
