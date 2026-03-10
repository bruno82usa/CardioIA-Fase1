import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base_dir = r"C:\Users\Bruno\.gemini\antigravity\playground\velvet-star\CardioIA-Fase1"
docs_dir = os.path.join(base_dir, "docs")
num_dir = os.path.join(base_dir, "dados_numericos")
vis_dir = os.path.join(base_dir, "dados_visuais")

os.makedirs(docs_dir, exist_ok=True)
os.makedirs(num_dir, exist_ok=True)
os.makedirs(vis_dir, exist_ok=True)

# 1. Generate Numerical Data (cardio_data.csv)
np.random.seed(42)
n_samples = 150
data = {
    "id_paciente": range(1, n_samples + 1),
    "idade": np.random.randint(30, 85, n_samples),
    "sexo": np.random.choice(["M", "F"], n_samples),
    "pressao_sistolica": np.random.randint(110, 180, n_samples),
    "pressao_diastolica": np.random.randint(70, 110, n_samples),
    "colesterol_total": np.random.randint(150, 300, n_samples),
    "frequencia_cardiaca": np.random.randint(60, 110, n_samples),
    "historico_familiar": np.random.choice(["Sim", "Nao"], n_samples, p=[0.4, 0.6]),
    "dor_peito": np.random.choice(["Assintomatico", "Dor Atipica", "Dor Nao Anginosa", "Angina Tipica"], n_samples),
    "glicemia_jejum_alta": np.random.choice([0, 1], n_samples, p=[0.85, 0.15]), # 1 se > 120 mg/dl
    "risco_cardiaco": np.random.choice(["Baixo", "Medio", "Alto"], n_samples, p=[0.5, 0.3, 0.2])
}
df = pd.DataFrame(data)
df.to_csv(os.path.join(num_dir, "cardio_data_simulated.csv"), index=False)

# 2. Textual Data
texto1 = """Doenças Cardiovasculares e Saúde Pública

As doenças cardiovasculares (DCV) continuam sendo a principal causa de mortalidade em todo o mundo. A prevenção primária, com foco na redução de fatores de risco como hipertensão, tabagismo, sedentarismo e dietas inadequadas, é a pedra angular da saúde pública para mitigar este impacto. 

Sintomas comuns de problemas cardíacos incluem dor no peito (angina), falta de ar, palpitações e fadiga extrema. O diagnóstico precoce através de eletrocardiogramas (ECG), ecocardiogramas e exames de sangue que medem biomarcadores (como a troponina) pode alterar drasticamente o prognóstico do paciente.

A introdução de tecnologias inteligentes nos hospitais e de algoritmos baseados em Inteligência Artificial pode auxiliar não apenas na triagem inicial, mas também na predição de eventos agudos, como o infarto do miocárdio, usando grandes volumes de dados de pacientes (Big Data). Governança de dados e ética no tratamento destas informações pessoais de saúde são desafios prementes para as próximas décadas.
"""

texto2 = """Tratamentos Modernos e Monitoramento Contínuo em Cardiologia

Com o avanço da Internet das Coisas (IoT) médica, dispositivos vestíveis (wearables) estão se tornando cruciais para o monitoramento contínuo de pacientes de risco. Relógios inteligentes e sensores em forma de adesivo conseguem capturar uma infinidade de dados fisiológicos em tempo real, desde a variabilidade da frequência cardíaca até a saturação de oxigênio.

Para pacientes diagnosticados com arritmias ou em reabilitação pós-infarto, o acompanhamento remoto reduz a necessidade de internações prolongadas. Se os algoritmos embarcados detectarem uma anomalia nos sinais vitais, um alerta imediato pode ser enviado à equipe médica.

Contudo, para que esses modelos de Machine Learning sejam precisos e não gerem um excesso de alarmes falsos, eles precisam ser treinados com dados diversificados, evitando o viés demográfico que prejudica minorias. A qualidade do dado (limpeza, anotação correta por especialistas) torna-se, portanto, tão importante quanto o algoritmo em si.
"""
with open(os.path.join(docs_dir, "texto1_doencas_cardiovasculares.txt"), "w", encoding="utf-8") as f:
    f.write(texto1)

with open(os.path.join(docs_dir, "texto2_monitoramento_iot.txt"), "w", encoding="utf-8") as f:
    f.write(texto2)

# 3. Visual Data (100 mock ECG images)
print("Gerando 100 imagens de ECG simuladas...")
t = np.linspace(0, 2*np.pi, 200)
for i in range(1, 101):
    fig, ax = plt.subplots(figsize=(4, 2))
    # Gerando um sinal que parece vagamente com um batimento incluindo ruído
    noise = np.random.normal(0, 0.1, 200)
    signal = np.sin(t*3) + np.where((t>np.pi) & (t<np.pi+0.2), 3, 0) + noise
    ax.plot(t, signal, color='blue', linewidth=1)
    ax.axis('off')
    plt.savefig(os.path.join(vis_dir, f"ecg_simulado_{i:03d}.jpg"), bbox_inches='tight', pad_inches=0)
    plt.close(fig)

# 4. README.md
readme_content = """# CardioIA - A Nova Era da Cardiologia Inteligente 🫀🤖

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
"""
with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"Estrutura gerada com sucesso em {base_dir}!")
