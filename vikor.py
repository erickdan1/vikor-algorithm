import numpy as np


def vikor(matrix, weights, criteria_type, v=0.5):
    try:
        # Verificar se a matriz é um array numpy
        assert isinstance(matrix, np.ndarray), "A matriz deve ser um array numpy."

        # Verificar se os pesos são um array numpy
        assert isinstance(weights, np.ndarray), "Os pesos devem ser um array numpy."

        # Verificar se criteria_type é uma lista
        assert isinstance(criteria_type, list), "O tipo de critério deve ser uma lista."

        # Número de alternativas e critérios
        n, m = matrix.shape

        # Verificar se os pesos somam 1
        assert np.isclose(np.sum(weights), 1), "Os valores dos pesos devem somar 1."

        # Verificar se a quantidade de pesos corresponde à quantidade de critérios
        assert m == len(weights), "A quantidade de pesos fornecida é diferente da quantidade de critérios na matriz."

        # Verificar se a quantidade de critérios corresponde ao tipo de critério
        assert m == len(
            criteria_type), "A quantidade de critérios fornecida é diferente da quantidade de tipos de critérios."

        # Passo 1: Determinar os valores ideais e anti-ideais
        ideal_best = np.zeros(m)
        ideal_worst = np.zeros(m)

        for j in range(m):
            if criteria_type[j] == 'maximização':
                ideal_best[j] = np.max(matrix[:, j])
                ideal_worst[j] = np.min(matrix[:, j])
            elif criteria_type[j] == 'minimização':
                ideal_best[j] = np.min(matrix[:, j])
                ideal_worst[j] = np.max(matrix[:, j])
            else:
                raise ValueError("Os critérios devem ser 'maximização' ou 'minimização'.")

        # Passo 2: Calcular S e R para cada alternativa
        s = np.zeros(n)
        r = np.zeros(n)
        for i in range(n):
            for j in range(m):
                if criteria_type[j] == 'maximização':
                    s[i] += weights[j] * (ideal_best[j] - matrix[i, j]) / (ideal_best[j] - ideal_worst[j])
                    r[i] = max(r[i], weights[j] * (ideal_best[j] - matrix[i, j]) / (ideal_best[j] - ideal_worst[j]))
                elif criteria_type[j] == 'minimização':
                    s[i] += weights[j] * (matrix[i, j] - ideal_best[j]) / (ideal_worst[j] - ideal_best[j])
                    r[i] = max(r[i], weights[j] * (matrix[i, j] - ideal_best[j]) / (ideal_worst[j] - ideal_best[j]))

        # Passo 3: Calcular Q para cada alternativa
        s_star = np.min(s)
        s_worst = np.max(s)
        r_star = np.min(r)
        r_worst = np.max(r)

        q = np.zeros(n)
        for i in range(n):
            q[i] = v * (s[i] - s_star) / (s_worst - s_star) + (1 - v) * (r[i] - r_star) / (r_worst - r_star)

        # Classificar as alternativas
        rank_s = np.argsort(s)
        rank_r = np.argsort(r)
        rank_q = np.argsort(q)

        return rank_q, rank_s, rank_r, q, s, r

    except AssertionError as e:
        print(f"Erro de verificação: {e}")
        return None
    except ValueError as e:
        print(f"Erro de valor: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None


def generate_comparison_string(values, label):
    sorted_indices = np.argsort(values)
    comparison = []
    for i in range(len(sorted_indices)):
        if i > 0:
            if values[sorted_indices[i]] == values[sorted_indices[i - 1]]:
                comparison.append(f" = {label}{sorted_indices[i]}")
            else:
                comparison.append(f" < {label}{sorted_indices[i]}")
        else:
            comparison.append(f"{label}{sorted_indices[i]}")
    return "".join(comparison)


# Exemplo de uso

# Definir a matriz de decisão
mtx = np.array([
    [1, 3000],
    [2, 3750],
    [5, 4500]
])

# Estabelecer os pesos
w = np.array([0.5, 0.5])

# Definir os tipos de critério
ctr_type = ['minimização', 'maximização']

rk_Q, rk_S, rk_R, Q, S, R = vikor(mtx, w, ctr_type)

if rk_Q is not None:
    print("Valores S:", S)
    print("Valores R:", R)
    print("Valores Q:", Q)
    print()

    print("Ranking S:", rk_S)
    print("Ranking R:", rk_R)
    print("Ranking Q:", rk_Q)
    print()

    comparison_string_S = generate_comparison_string(S, "S")
    comparison_string_R = generate_comparison_string(R, "R")
    comparison_string_Q = generate_comparison_string(Q, "Q")

    print("Ranking Final das Alternativas:")
    print(comparison_string_S)
    print(comparison_string_R)
    print(comparison_string_Q)
