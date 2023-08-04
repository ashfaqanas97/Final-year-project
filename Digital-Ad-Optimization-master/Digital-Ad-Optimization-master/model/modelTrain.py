from avitoData import AvitoData
from logitModel import LRModel

class ModelTrainer:
	def __init__(self):

		self.model = LRModel()
		
		self.X_train = None
		self.y_train = None
		self.X_test = None
		self.y_test = None

	def mainTrain(self):
		avitoData = AvitoData()
		avitoData.prepareData()
		self.X_train, self.y_train, self.X_test, self.y_test = avitoData.splitData()

		self.model.train(self.X_train, self.y_train)
		preds = self.model.predict(self.X_test)
		auc = self.model.getROC(self.y_test, preds)
