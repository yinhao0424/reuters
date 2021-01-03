# reuster
***
- **Goal**:  tag news
- **Challanges**:   
    1. Multiple topics (over 100)
    2. Imbalanced topics distribution
    3. One news belong to multiple topics

- **Experiments**: 
    1. TF-IDF embeding -- base line
    2. Multilabel classification --  multiple topics / topics overlapping
    3. Few shot learner


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


