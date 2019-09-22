import pickle

punctuation = '⊙∩～~`!@#$%^&*()_-+={}[]|\:;\"\'<>＜＞≪≫,.?/~·•！@#￥%……&*（）\\\
——-—+=｛【】｝』『「」〖〗|、：；“”‘’《》，。？、/*-+.\t\r\n'

def Preprocess(path_list):
    for path in path_list:
        file = open(path,'r',encoding = 'UTF-8-sig')
        content = file.readlines()
        file.close()
        
        trans = str.maketrans(punctuation,' '*len(punctuation))
        content_cleaned = [line.translate(trans).split()+['\n'] for line in content]
        labels = []
        
        file = open(path+'_data','w',encoding = 'UTF-8-sig')
        for line in content_cleaned:
            label = int(line[0])
            labels.append(label)
            del(line[0])
            file.write(" ".join(line))
        file.close()
        
        file = open(path+'_labels','wb')
        pickle.dump(labels,file)
        file.close()
        
        print('Preprocess results:',path+'_data','and',path+'_labels')