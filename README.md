# Algoritmo VIKOR

O método VIKOR foi introduzido por Serafim Opricovic em 1998. Esta técnica é uma das abordagens compensatórias nos modelos de compensação, onde a alternativa mais próxima da solução ideal é preferida dentro desse grupo. Em geral, o método foca na classificação das alternativas e na seleção de uma alternativa que apresente um conjunto de atributos contraditórios, oferecendo assim uma solução de compromisso que ajuda o tomador de decisão a alcançar a solução final. Desde sua introdução, o VIKOR tem sido amplamente aplicado em tomadas de decisão para selecionar a alternativa ideal e tem sido utilizado na análise de terceirização logística, seleção de fornecedores e escolha de localização de aeroportos. Esta técnica possui as seguintes características:

- É um dos métodos compensatórios;
- Os atributos devem ser independentes;
- Os atributos qualitativos devem ser convertidos em atributos quantitativos.

Além disso, a matriz de decisão utilizada no método VIKOR é baseada nas informações fornecidas pelo tomador de decisão.

Este repositório fornece uma implementação em Python do algoritmo do método, com suporte para tratamento de exceções e verificação de entrada.

## Funcionalidades

- **Calculo dos Índices**: Calcula os índices \(Q\), \(S\) e \(R\) para avaliar as alternativas.
- **Classificação**: Classifica as alternativas com base nos índices calculados.
- **Comparação**: Gera strings de comparação para os índices \(Q\), \(S\) e \(R\) com base em suas ordens.

## Instalação

Para usar este código, você precisa ter o Python instalado em seu sistema. Você pode instalar as dependências necessárias usando o `pip`. A principal dependência é o `numpy`.

```bash
pip install numpy
```

## Uso

Aqui está um exemplo básico de como usar a função `vikor`:

```python
import numpy as np
from vikor import vikor, generate_comparison_string

# Definir a matriz de decisão
matrix = np.array([
    [1, 3000],
    [2, 3750],
    [5, 4500]
])

# Estabelecer os pesos
weights = np.array([0.5, 0.5])

# Definir os tipos de critério
criteria_type = ['minimização', 'maximização']

# Executar o algoritmo VIKOR
rank_Q, rank_S, rank_R, Q, S, R = vikor(matrix, weights, criteria_type)

if rank_Q is not None:
    print("Valores S:", S)
    print("Valores R:", R)
    print("Valores Q:", Q)
    print()

    print("Ranking S:", rank_S)
    print("Ranking R:", rank_R)
    print("Ranking Q:", rank_Q)
    print()

    comparison_string_S = generate_comparison_string(S, "S")
    comparison_string_R = generate_comparison_string(R, "R")
    comparison_string_Q = generate_comparison_string(Q, "Q")

    print("Ranking Final das Alternativas:")
    print(comparison_string_S)
    print(comparison_string_R)
    print(comparison_string_Q)
```

### Funções

- **`vikor(matrix, weights, criteria_type, v=0.5)`**: Calcula os índices \(Q\), \(S\) e \(R\) e classifica as alternativas. 
  - `matrix`: Matriz de decisão (n x m), onde n é o número de alternativas e m é o número de critérios.
  - `weights`: Array dos pesos dos critérios (m).
  - `criteria_type`: Lista dos tipos de critérios (`'maximização'` ou `'minimização'`).
  - `v`: Parâmetro de comprometimento (valor entre 0 e 1).

- **`generate_comparison_string(values, label)`**: Gera uma string de comparação dos valores fornecidos.
  - `values`: Array de valores a serem comparados.
  - `label`: Rótulo a ser usado na comparação (ex.: `'Q'`, `'S'`, `'R'`).

## Tratamento de Exceções

O código inclui tratamento de exceções para garantir que as entradas estejam corretas. Caso os dados fornecidos não estejam corretos, o código exibirá mensagens de erro apropriadas.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
