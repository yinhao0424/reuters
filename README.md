# reuster
***
- **Goal**:  tag news with high accuracy   
- **Challanges**:   1. too many classes and they are imbalanced 2. many methods to use (LDA, Embedding, one shot learner, few shot learner, Bert, t-sne, weak supervision) 3. 很多不会   
- **Experiments**: 1. TF-IDF 2.Multilabel Classification   


***
12/21/2020 周一
- Parse SGM   

reuters21578:  ModeApte split will be used in this research.  
    9603 training data with LEWISSPLIT = 'TRAIN' and 'TOPICS' = 'YES'  
    3299 testing data with LEWISSPLIT = 'TEST' and 'TOPICS' = 'YES'.  

    - Research on the dataset  
    - Parse single SGM file  
    - Parse multiple SGM files and generate a json file
    
***
- Reference: 
    - Parse SGM
        - https://dzlab.github.io/nlp/2018/11/17/parsing-xml-into-dataframe/   
        - https://github.com/ankailou/reuters-classification/blob/master/preprocessing/lexicon/lexicon.py    
    - Bert:  
        - Fine Tuning DistilBERT for MultiLabel Text Classification (DistilBERT) : https://github.com/DhavalTaunk08/NLP_scripts/blob/master/Transformers_multilabel_distilbert.ipynb 
        - Fine Tuning Transformer for MultiLabel Text Classification (BERT) :  https://github.com/abhimishra91/transformers-tutorials/blob/master/transformers_multi_label_classification.ipynb 

***


