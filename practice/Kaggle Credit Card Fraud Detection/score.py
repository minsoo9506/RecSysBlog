from sklearn.metrics import classification_report, roc_auc_score, average_precision_score

def printScore(pred_train, pred_test, pred_prob_train, pred_prob_test, y_train, y_test):
    print('Train')
    print(classification_report(y_train, pred_train))
    print('Test')
    print(classification_report(y_test, pred_test))
    print()
    print(f'ROC AUC Train = {roc_auc_score(y_train, pred_prob_train)}')
    print(f'ROC AUC Test = {roc_auc_score(y_test, pred_prob_test)}')
    print()
    print(f'Average precision socre Train = {average_precision_score(y_train, pred_prob_train)}')
    print(f'Average precision socre Test = {average_precision_score(y_test, pred_prob_test)}')