class univariate():
   
    def quanqual(dataset):
        quan=[];
        qual=[];
        for i in dataset.columns:
            if(dataset[i].dtype=="O"):
                quan.append(i)
            else:
                qual.append(i)
            return quan,qual
    
    
    def freqtable(columnname,dataset):
        freqtable=pd.DataFrame(columns=['Unique values','Frequency','Relative frequency','cumsum'])

        freqtable["Unique values"]=dataset[columnname].value_counts().index
        freqtable["Frequency"]=dataset[columnname].value_counts().values
        freqtable["Relative frequency"]=freqtable["Frequency"]/103
        freqtable["cumsum"]=freqtable["Relative frequency"].cumsum()
        return freqtable
        
        
    def univariate(dataset,quan):
                descriptive=pd.DataFrame(index['Mean','Median','Mode','25%','50%','75%','100%','IQR','1.5Rule','lesser','greater','Min','Max'],columns=quan)
        for columnname in quan:
            descriptive[columnname]['Mean']=dataset[columnname].mean()
            descriptive[columnname]['Median']=dataset[columnname].median()
            descriptive[columnname]['Mode']=dataset[columnname].mode()[0]
            descriptive[columnname]['25%']=dataset.describe()[columnname]['25%']
            descriptive[columnname]['50%']=dataset.describe()[columnname]['50%']
            descriptive[columnname]['75%']=dataset.describe()[columnname]['75%']
            descriptive[columnname]['100%']=dataset.describe()[columnname]['max']
            descriptive[columnname]['IQR']=descriptive[columnname]['75%']-descriptive[columnname]['25%']
            descriptive[columnname]['1.5 Rule']=1.5*descriptive[columnname]['IQR']
            descriptive[columnname]['lesser']=descriptive[columnname]['25%']-descriptive[columnname]['1.5 Rule']
            descriptive[columnname]['greater']=descriptive[columnname]['75%']+descriptive[columnname]['1.5 Rule']
            descriptive[columnname]['Min']=dataset[columnname].min()
            descriptive[columnname]['Max']=dataset[columnname].max()
        return descriptive
    
    
    def outlier_columnnames():
        global lesser,greater
        lesser=[]
        greater=[]
        for columnname in quan:
            if(descriptive[columnname]['Min']<descriptive[columnname]['lesser']):
                lesser.append(columnname)
            if(descriptive[columnname]['Max']<descriptive[columnname]['greater']):
                greater.append(columnname)
        return lesser,greater
       
        
    def replace_outliers():
        for columnname in lesser:
            dataset[columnname][dataset[columnname] < descriptive[columnname]['lesser']] = descriptive[columnname]['lesser']

        for columnname in greater:
            dataset[columnname][dataset[columnname] < descriptive[columnname]['greater']] = descriptive[columnname]['greater']
