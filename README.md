# CardioIA - A Nova Era da Cardiologia Inteligente 🫀🤖

Este repositório contém os artefatos correspondentes à **Fase 1 - Batimentos de Dados** do projeto acadêmico **CardioIA**. O objetivo desta fase é levantar, organizar e entender dados cardiológicos que alimentarão os módulos inteligentes nas próximas etapas do projeto, aplicando desde já conceitos básicos de Governança de Dados para IA.

## 📂 Organização do Repositório

O projeto está dividido na coleta de três modalidades de dados essenciais:

### Parte 1 – Dados Numéricos (IoT)
Nesta etapa foi gerado um dataset simulado com 150 registros contendo as seguintes variáveis clínicas: `idade`, `sexo`, `pressão arterial (sistólica/diastólica)`, `colesterol`, `frequência cardíaca`, `histórico familiar`, `dor no peito`, `glicemia` e `risco cardíaco`.

- **Origem dos Dados**: Dados simulados algoritmocamente (Mock Data) utilizando Python, com o objetivo de mimetizar distribuições reais de pacientes.
- **Variáveis mais Relevantes (Clínicas)**:
  - **Pressão Arterial e Colesterol**: Fundamentais, pois são os principais fatores de risco tratáveis associados à insuficiência cardíaca e AVCs.
  - **Dor no Peito (Sintoma)**: Serve como o "gatilho" para o algoritmo classificar urgências. 
- **Importância para a IA na Saúde**: Tais variáveis tabulares são a base para o treinamento de modelos de *Machine Learning* supervisionados (como Random Forest ou Regressão Logística) na Fase 2 do projeto, visando estratificar o risco do paciente.
- **Acesso**: [Substitua por Link do OneDrive/Google Drive aqui contendo a pasta dados_numericos]

### Parte 2 – Dados Textuais (NLP)
Foram coletados dois textos de caráter médico e de saúde pública para compor a base textual do projeto. Ambos os arquivos encontram-se na subpasta [`docs/`](./docs).

- **Exploração por NLP**: Textos desta natureza podem ser processados por tecnologias de Processamento de Linguagem Natural (NLP) para realizar:
  - Extração de Entidades Nomeadas (NER) focadas na área médica, capturando automaticamente menções a novos sintomas em prontuários eletrônicos.
  - Classificação de Tópicos e Modelagem de Assuntos em artigos ou perguntas recebidas por assistentes virtuais (chatbots), encaminhando o paciente para o fluxo de atendimento digital adequado.
- **Justificativa**: NLP permite transformar dados desestruturados (a voz de um paciente, as notas médicas de um prontuário) em dados estruturados valiosos, apoiando o **Suporte Digital ao Paciente** (Fase 5).

### Parte 3 – Dados Visuais (Visão Computacional)
Reunimos uma amostra simulada representativa de 100 imagens de Eletrocardiogramas (ECGs).

- **Como as imagens serão analisadas por VC (Visão Computacional)**:
  - Algoritmos de redes neurais convolucionais (CNNs) podem processar essas formas de onda (quando dispostas como imagem) ou exames como raio-x para detecção de anomalias espaciais (ex: cardiomegalia, arritmias).
  - Outros modelos de detecção de padrões podem segmentar a imagem, identificando picos R-R irregulares, atuando como um "segundo olhar" de apoio ao médico.
- **Importância**: O diagnóstico por imagem é uma das áreas mais bem-sucedidas em IA aplicada à medicina moderna. Reduzir a carga cognitiva do radiologista e agilizar o atendimento de urgência são os principais impactos esperados.
- **Acesso**: [Substitua por Link do OneDrive/Google Drive aqui contendo a pasta dados_visuais]

---
*Construído como parte da avaliação em PBL do curso de Inteligência Artificial da FIAP.*
