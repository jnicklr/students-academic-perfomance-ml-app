# Student Performance Predictor

Este projeto é uma aplicação desenvolvida com Flask que utiliza um modelo de regressão treinado com Random Forest para prever a nota final de um estudante com base em seus hábitos de vida, como horas de estudo, sono, uso de redes sociais, saúde mental, entre outros.

## Objetivo

Oferecer uma interface simples para que aplicações clientes possam enviar dados de entrada e receber como resposta a predição da nota final de um aluno, utilizando um modelo `.pkl` previamente treinado em um notebook Jupyter.

## Tecnologias utilizadas

- Python
- Flask
- Scikit-learn
- Pandas
- Numpy
- Joblib (para carregar o modelo)

## Estrutura do projeto

```
students-academic-perfomance-ml-app/
│
├── data/
│ └── student_habits_performance.csv
│
├── notebooks/
│ └── students_perfomance.ipynb
│
├── src/
│ ├── app.py
│ ├── run.py
│ ├── templates/
│ ├────  index.html
│ ├── model/
│ └────  students_habits_perfomance.pkl
│
├── README.md
├── .gitignore
└── requirements.txt
```

## Requisitos

- Python 3.10 ou superior ([Link para a página oficial do python](https://www.python.org/))

## Como executar

1. Clone o repositório

```bash
git clone https://github.com/jnicklr/students-academic-perfomance-ml-app.git
cd students-academic-perfomance-ml-app
```

2. Crie um ambiente virtual e instale as dependências

```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3. Inicie a aplicação Flask

```bash
python src/run.py
```

A aplicação estará disponível na rota `http://localhost:5000`.