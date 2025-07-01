from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Etapa 1: Simular os dados (valores reais e predições do modelo)
# Valores reais (labels)
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]

# Predições do modelo
y_pred =<details><summary>Raciocínio</summary>Este modelo de raciocínio não disponibiliza via API o raciocínio utilizado para esta resposta.</details>

 [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

# Etapa 2: Calcular a matriz de confusão
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Etapa 3: Calcular as métricas
# Acurácia
accuracy = accuracy_score(y_true, y_pred)

# Precisão
precision = precision_score(y_true, y_pred)

# Sensibilidade (Recall)
recall = recall_score(y_true, y_pred)

# Especificidade
specificity = tn / (tn + fp)

# F1-Score
f1 = f1_score(y_true, y_pred)

# Etapa 4: Exibir os resultados
print("Métricas de Avaliação:")
print(f"Acurácia: {accuracy:.2f}")
print(f"Precisão: {precision:.2f}")
print(f"Recall (Sensibilidade): {recall:.2f}")
print(f"Especificidade: {specificity:.2f}")
print(f"F1-Score: {f1:.2f}")
