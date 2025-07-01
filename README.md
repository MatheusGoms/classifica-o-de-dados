Passos para o Projeto
Definir os dados:

Vamos simular um conjunto de dados com as predições do modelo e os valores reais (labels).
Alternativamente, você pode usar dados reais se tiver um conjunto de resultados.
Criar funções para calcular as métricas:

Implementar fórmulas para cada métrica (acurácia, precisão, recall, especificidade, F1-score).
Exibir os resultados:

Mostrar os valores calculados das métricas.

Explicação do Código
1. Dados de exemplo
y_true: Representa os valores reais das classes (ex.: 1 para positivo e 0 para negativo).
y_pred: Representa as predições feitas pelo modelo.
2. Matriz de confusão
A matriz de confusão é calculada usando confusion_matrix() e decomposta em:

True Positive (TP): Predições corretas para a classe positiva.
False Positive (FP): Predições incorretas para a classe positiva.
False Negative (FN): Predições incorretas para a classe negativa.
True Negative (TN): Predições corretas para a classe negativa.
3. Métricas
Acurácia:
\[
\text{Acurácia} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}
\]
Mede a proporção de predições corretas.

Precisão:
\[
\text{Precisão} = \frac{\text{TP}}{\text{TP} + \text{FP}}
\]
Mede a proporção de predições positivas corretas.

Sensibilidade (Recall):
\[
\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
\]
Mede a capacidade do modelo de identificar as instâncias positivas.

Especificidade:
\[
\text{Especificidade} = \frac{\text{TN}}{\text{TN} + \text{FP}}
\]
Mede a capacidade do modelo de identificar as instâncias negativas.

F1-Score:
\[
\text{F1-Score} = 2 \times \frac{\text{Precisão} \times \text{Recall}}{\text{Precisão} + \text{Recall}}
\]
É a média harmônica entre a precisão e o recall.

4. Resultados
O código exibe as métricas calculadas, permitindo avaliar o desempenho do modelo.

