import pickle

class Dataset:
    def __init__(self,train,val,test):
        self.train = train
        self.val = val
        self.test = test
        
class Subset:
    def __init__(self,data,labels):
        self.data = data
        self.labels = labels
        
def load_data(data_path):
    dataset = []
    for data in data_path:
        file = open(data+"_data",'r',encoding = 'UTF-8-sig')
        data_train = [line.rstrip(' \n') for line in file.readlines()]
        file.close()
    
        file = open(data+"_labels","rb")
        labels_train = pickle.load(file)
        file.close()
        
        subset = Subset(data_train,labels_train)
        dataset.append(subset)
    return Dataset(dataset[0],dataset[1],dataset[2])