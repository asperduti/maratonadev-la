[![](https://img.shields.io/badge/IBM%20Cloud-powered-blue.svg)](https://cloud.ibm.com)
[![](https://img.shields.io/discord/734849242153222221?logo=discord)](https://discord.gg/yJYmTGDWKH)

# Desafio 06 | Final

- [Premiação](#premiação)
- [Desafio de negócio](#desafio-de-negócio)
- [Objetivo](#objetivo)
- [Tecnologias aplicadas](#tecnologias-aplicadas)
- [Desenvolvimento da solução](#5esenvolvimento-da-solução)
  - [Resumo das tarefas](#resumo-das-tarefas)
  - [Desenvolvimento](#desenvolvimento)
- [Submissão](#submissão)
- [Sobre a avaliação](#sobre-a-avaliação)

## Para te ajudar

- [Material de Apoio](#material-de-apoio)

**Atenção**: esse desafio poderá ser enviado somente pelos Top 100 participantes finais da Maratona Behind the Code 2021, listados em https://maratona.dev/ranking.

### Premiação

A IT MIDIA tem o prazo de 15 dias para enviar o voucher de viagem a vocês. Os Top 100 vão ganhar um voucher de 1200 dólares e os Top 5 um voucher adicional de 1600 dólares. Os Top 5 então vão receber 2.800 dólares.

Os prêmios não incluem outros bens, benefícios, cobertura ou despesas, não podem ser revertidos em dinheiro ou qualquer outra forma que não viagem junto a agência de viagens indicada pela Organizadora da Maratona

## Desafio de negócio

O desafio consiste em auxiliar os agricultores de uma região em seus trabalhos, trazendo informações importantes para o cultivo de uma maneira de fácil acesso.

## Objetivo

O objetivo do desafio é criar um assistente virtual para auxílio na agricultura do município de Ribeirão Preto, que deve trazer informações para auxiliar os agricultores em seus trabalhos.

## Tecnologias aplicadas

Para este desafio serão utilizados os seguintes serviços da IBM Cloud:

- [Watson Assistant](https://cloud.ibm.com/catalog/services/watson-assistant), uma plataforma para criação de chatbots de forma fácil, por meio de intenções, entidades e fluxo de diálogos, e diversas possibilidades de integrações.
- [The Weather Company](https://docs.google.com/document/d/15Ru_3wdMgpbM4aOCm-4qNAnRfjx2w-Ruw3lnr8Hnodk/edit), um serviço de API que fornece informações climáticas.
- [Cloud Functions](https://cloud.ibm.com/functions), um serviço para execução de funções na nuvem, sem necessidade de um servidor (modelo conhecido como Serverless).
- [OpenShift](https://docs.openshift.com/container-platform/4.8/welcome/index.html), uma plataforma de orquestração de containers robusta, baseada em Kubernetes.

## Desenvolvimento da solução

### Resumo das Tarefas

1. Criar um assistente virtual, de acordo com as especificações abaixo;
2. Criar uma função capaz de capturar os dados da Weather API necessários;
3. Integrar a função ao assistente por meio de Webhook;
4. Criar uma aplicação capaz de enviar uma requisição HTTP para submeter o desafio;
5. Realizar o deploy da aplicação em um cluster OpenShift, submetendo o desafio.

### Desenvolvimento

Você deverá construir um assistente virtual, em **português brasileiro**, que será utilizado para auxílio na agricultura, e deverá ser capaz de responder os seguintes temas:

- Temperatura mínima e máxima, 15 dias no futuro
- Evapotranspiração da próxima hora para o cultivo de café
- Evapotranspiração da próxima hora para o cultivo de milho
- Evapotranspiração da próxima hora para o cultivo de soja
- Velocidade do vento durante o período diurno, 15 dias no futuro
- Direção do vento em notação magnética durante o período diurno, 15 dias no futuro

**Informações importantes**:

- As unidades de medidas devem estar no sistema métrico.
- Para todos os itens de cultivo, deve ser considerada uma maturidade de 50%.
- Todas as respostas do assistente devem ser do tipo texto. O assistente sempre deverá considerar o município de Ribeirão Preto - SP, Brasil para as consultas. As seguintes coordenadas devem ser consideradas:

```text
LATITUDE: -21.170401
LONGITUDE: -47.810326
```

- Nenhuma outra interação é necessária para o assistente, somente as das solicitadas acima. O assistente será sempre primeiramente abordado pelo nó Welcome, com um texto vazio, antes de alguma pergunta ser feita.
- Caso o assistente seja perguntado sobre evapotranspiração, mas sem nenhum item de cultivo especificado, ele deve solicitar o item de cultivo desejado.
- As temperaturas mínima e máxima sempre devem aparecer juntas nas respostas.

Para as informações, as seguintes APIs do Weather devem ser utilizadas:

- [Previsão de tempo diária para os próximos 15 dias](https://ibm.co/V3DFap)
- [Previsão para agricultura nos próximos 15 dias](https://ibm.co/v3rA15D)

As chaves de API para acesso à Weather API serão disponibilizadas pelo servidor Discord oficial da final.

Para a integração das informações com o assistente, você deverá utilizar um [Webhook](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-webhooks). Nossa sugestão para o Webhook é criar uma ação no [Cloud Functions](https://cloud.ibm.com/functions), ativando-a como Web Action. Lembre-se de adicionar um `.json` ao final da URL da Web Action, caso for utilizá-la. Essa ação deverá realizar chamadas para a Weather API para obter as informações solicitadas pelo assistente.

## Submissão

Com o assistente pronto, é hora de realizar a submissão. Será aceita somente uma submissão para o desafio, então teste bem antes de fazer o envio.

Para realizar a submissão, você deverá enviar uma requisição HTTP POST para um serviço que está em execução em nosso cluster OpenShift. Para isso, você precisará criar um container e subí-lo em nosso cluster OpenShift. Uma vez que ele subir, conseguirá acessar nosso serviço de submissão por meio da rede interna.

O serviço de submissão estará escutando por requisições HTTP POST na seguinte url: `http://172.21.188.211:3000/submit`. No body da requisição HTTP, deve ser enviado um objeto JSON contendo as seguintes informações:

- Seu e-mail registrado na Maratona Behind the Code 2021
- As credenciais para o seu Watson Assistant, que podem ser obtidas nos locais detalhados no [Desafio 4](https://github.com/maratonadev/desafio-4-2021/blob/main/doc/instructions/pt.md#6-submiss%C3%A3o). Lembre-se de associar sua skill do Watson Assistant a seu assistente.
- Uma confirmação de submissão, podendo ser `true` ou `false`. No caso de ser `false`, o sistema irá apenas avaliar se as credenciais estão corretas para submeter. No caso de `true`, o desafio será enviado de forma final.

O objeto JSON deve ter o seguinte formato:

```json
{
  "email": "seu@email.com",
  "assistantId": "ID do seu Assistant",
  "url": "URL do seu Watson Assistant",
  "skillId": "ID da sua Skill",
  "apiKey": "API key do seu Watson Assistant",
  "submitConfirmation": false
}
```

Lembre-se de alterar o `submitConfirmation` para `true` para fazer o envio final.

## Sobre a avaliação

O desafio será avaliado com base na assertividade das perguntas e respostas do assistente virtual implementado. As submissões serão avaliadas até o final do desafio, e o resultado será divulgado na Live final.

## Material de apoio

- [Tutorial OpenShift](https://github.com/MBTC-2020-TOP100/OPENSHIFT-TUTORIAL)
- [Documentação do Watson Assistant](https://cloud.ibm.com/docs/assistant?topic=assistant-getting-started&locale=pt-BR)
- [Seja bem-vindo ao Watson Assistant!](https://developer.ibm.com/br/articles/bem-vindo-ao-watson-assistant/)
- [Integre o robô de bate-papo de comunicação de crise da COVID-19 a um website](https://developer.ibm.com/br/tutorials/create-a-covid-19-chatbot-embedded-on-a-website/)
- [Desenvolva uma solução de atendimento ao cliente](https://developer.ibm.com/br/articles/insurance-industry-customer-care-solution/)
- [Documentação do Cloud Functions](https://cloud.ibm.com/docs/openwhisk?locale=pt-BR)

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
