from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc

class LRModel:
	def __init__(self):
		self.model = LogisticRegression()


	def train(self, X_train, y_train):
		self.model.fit(X_train, y_train)

	def predict(self, X_test):
		preds = self.model.predict_proba(X_test)[:,1]
		return preds

	def getROC(self, y_test, predictions):
		fpr_test, tpr_test, thresholds_test = roc_curve(y_test, predictions)
		result = auc(fpr_test, tpr_test)
		print('AUC SCORE: ', result)
		return result
