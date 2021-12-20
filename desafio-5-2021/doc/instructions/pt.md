[![](https://img.shields.io/badge/IBM%20Cloud-powered-blue.svg)](https://cloud.ibm.com)
[![](https://img.shields.io/discord/734849242153222221?logo=discord)](https://discord.gg/yJYmTGDWKH)

# Desafio 05 | SONDA

- [1. Sobre a SONDA](#1-sobre-a-sonda)
  - [1.1. Introdução](#11-introdução)
  - [1.2. Premiação](#12-premiação)
- [2. Desafio de negócio](#2-desafio-de-negócio)
- [3. Objetivo](#3-objetivo)
- [4. Tecnologias aplicadas](#4-tecnologias-aplicadas)
- [5. Desenvolvimento da solução](#5-desenvolvimento-da-solução)
  - [5.1. Pré-requisitos](#51-pré-requisitos)
  - [5.2. Resumo das tarefas](#52-resumo-das-tarefas)
  - [5.3. Desenvolvimento](#53-desenvolvimento)
- [6. Submissão](#6-submissão)
- [7. Sobre a avaliação](#7-sobre-a-avaliação)

## Para te ajudar

- [Material de Apoio](#material-de-apoio)

## 1. Sobre a SONDA

### 1.1. Introdução

A SONDA é a principal rede latino-americana de serviços de Tecnologias da Informação (TI). Em seus quase 45 anos de história na região, caracterizou-se por contar com uma oferta integral de serviços e soluções de TI, uma visão de aliado tecnológico para abordar projetos e uma sólida posição financeira, prestando de forma consistente serviços e soluções alinhadas com as estratégias de negócio de seus clientes.

Desde 1974, a missão da empresa tem sido agregar valor às atividades e negócios de nossos clientes e impulsionar seu crescimento através de uma melhor utilização das tecnologias da informação, construindo relações de longo prazo que se traduzem em uma proximidade com seu trabalho e evolução.

### 1.2. Premiação

As top 5 melhores pessoas colocadas vão receber um voucher de US$ 350 cada.

## 2. Desafio de negócio

O desafio consiste em um problema comum na área de Ciência de Dados. Um cliente expõe um problema específico de sua área e através da sua análise encontrar uma possível solução. Um cliente da área Telecomunicações reportou problema de perda de clientes (Churn) e gostaria de conseguir identificar essa possível perda antes que ela ocorra, por meio de inteligência artificial.

## 3. Objetivo

O desafio consiste de implementar um algoritmo de Machine Learning para classificação binária, capaz de identificar se um cliente será perdido ou não.

## 4. Tecnologias aplicadas

Para este desafio serão utilizados os seguintes serviços da IBM Cloud:

- [Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio), também conhecido como Cloud Pak for Data as a Service. Esse serviço permite o uso de uma gama de ferramentas relacionadas à Ciência de Dados, inclusive execução de Jupyter Notebooks com processadores na nuvem.

## 5. Desenvolvimento da solução

### 5.1. Pré-requisitos

Para realizar esse desafio você deverá cumprir os seguintes pré-requisitos:

- [Registrar-se na Maratona Behind the Code](https://maratona.dev/?register=true) e confirmar seu e-mail de cadastro;
- Possuir uma [conta na IBM Cloud](https://ibm.biz/Bdf8dW), podendo ser a conta Lite ou Pay-As-You-Go (não é necessário registrar-se no evento com o mesmo e-mail utilizado para criar sua conta na IBM Cloud).

### 5.2. Resumo das Tarefas

1. Instanciar os serviços do desafio na IBM Cloud: Object Storage e Watson Studio (opcionais);
2. Explorar e tratar a [base de dados disponível](../../assets/data/dataset.csv);
3. Criar um modelo de Machine Learning para realizar classificação binária;
4. Alterar, validar e testar o seu modelo de Machine Learning, até estar satisfeito com o resultado;
5. Alterar o [arquivo de respostas](../../assets/data/ANSWERS.csv), adicionando classificações de seu modelo;
6. Efetuar a submissão na [página do desafio](https://maratona.dev/challenge/5).

### 5.3. Desenvolvimento

O desafio consiste no uso de um algoritmo de Machine Learning de aprendizagem supervisionada, como o de [Árvore de Decisão](https://scikit-learn.org/stable/modules/tree.html), para realizar uma classificação binária que dirá se um cliente será perdido ou não.

As classificações devem ser salvas no arquivo [ANSWERS.csv](../../assets/data/ANSWERS.csv), da mesma forma como aparercem no dataset (`Yes` ou `No`). Todos os clientes precisam ter uma classificação.

O dicionário de [dados](../../assets/data/dataset.csv) é o seguinte:

| Coluna           | Descrição                                                                                                          |
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

**Atenção**: os dados disponibilizados neste desafio são fictícios, qualquer correlação com a realidade é mera coincidência.

## 6. Submissão

Com as respostas no arquivo, o último passo é realizar a submissão. Será aceita somente uma submissão para o desafio, então teste bem antes de fazer o envio.

Para realizar a submissão, você deverá acessar a página do desafio: [https://maratona.dev/challenge/5](https://maratona.dev/challenge/5) e enviar o arquivo CSV com as respostas, juntamente com um arquivo `.zip`, de até 10MB, contendo o código fonte da solução (lembre-se de remover dependências e datasets para não ocupar espaço). A página fará um teste para verificar se o arquivo CSV está no formato correto.

Você poderá acompanhar o status da submissão acessando a [página do desafio](https://maratona.dev/challenge/5), logando na sua conta.

## 7. Sobre a avaliação

Uma semana após o início do desafio, nosso sistema de avaliação automática começará as avaliações. Ele irá utilizar os dados enviados para calcular uma pontuação numérica de 1 até 100, baseada na métrica [F<sub>1</sub>](https://en.wikipedia.org/wiki/F-score). O arquivo `.zip` enviado deve conter todo o código utilizado para obter a solução. Caso contrário, a pontuação será zerada.

O desafio deve ser entregue até dia 12 de dezembro, e o participante receberá uma bonificação de 10% da pontuação total (10 pontos), independendo do resultado de seu desafio. A pontuação máxima possível, portanto, é 110 (100 de avaliação + 10 de bônus).

**Atenção**: o tempo de entrega é um critério de desempate, no caso de soluções com a mesma nota. Nos reservamos o direito de zerar a pontuação de uma submissão caso:

- O código fonte enviado não seja coerente com os resultados obtidos dos testes no modelo.
- Seja detectado plágio, de um ou mais participantes. Nesse caso, todos os participantes com a solução igual terão sua pontuação no desafio zerada.

## Material de apoio

- [Assuma o controle dos seus dados com o Watson Studio](https://developer.ibm.com/br/articles/overview-e-summary-ibm-watson-studio/)
- [Introdução ao IBM Watson Studio](https://developer.ibm.com/br/articles/introduction-to-ibm-watson-studio/)
- [Introdução ao IBM Cloud Pak for Data](https://developer.ibm.com/br/articles/get-started-with-ibm-cloud-pak-for-data/)
- [Desenvolva modelos de aprendizado de máquina com e sem AutoML](https://developer.ibm.com/br/articles/compare-model-building-with-and-without-automated-machine-learning/)
- [Desenvolva um modelo preditivo de aprendizado de máquina de forma rápida e fácil com o IBM SPSS Modeler](https://developer.ibm.com/br/tutorials/desenvolva-um-modelo-preditivo-de-aprendizado-de-mquina-de-forma-rpida-e-fcil-com-o-ibm-spss-modeler/)
- [Visualizar dados com Python](https://developer.ibm.com/br/patterns/visualize-data-with-python/)

Você também pode acessar o Discord oficial da Maratona 2021 para realizar perguntas e/ou interagir com outros participantes: [Discord](https://discord.gg/yJYmTGDWKH).

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
