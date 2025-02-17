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