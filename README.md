# reuters
***
- **Goal**:  reuters news classification
- **Challanges**:   
    - Multiple topics (over 100)
    - Imbalanced topics distribution
    - One news belong to multiple topics

- **Experiments**: 
    1. TF-IDF embeding -- base line
    2. First laryer model: Multilabel classification --  multiple topics / topics overlapping
    3. Seconde laryer model: Few shot learner -- for topics with few training samples


***
Time line
|  Time   | Tasks  |
|  ----  | ----  |
| 12/21/2020 - 12/23/2020 | understand Dataset, study weak supervision |
| 12/24/2020 - 12/27/2020 | parse sgm file, build tf-idf model, study few shot learner  |
| 12/27/2020 - 12/30/2020 | prepare data, build multilabel classifier, study hugging face  |
| 12/30/2020 - 01/05/2021 | build few shot learner, study hugging face and few shot learner |
| 01/05/2021 - 01/10/2021| refine model, prepare presentation |

    
***
- Reference: 
    - [parse xml](https://dzlab.github.io/nlp/2018/11/17/parsing-xml-into-dataframe/) 
    - [reuters-classification](https://github.com/ankailou/reuters-classification/blob/master/preprocessing/lexicon/lexicon.py)   
    - [Fine Tuning DistilBERT for MultiLabel Text Classification (DistilBERT)]( https://github.com/DhavalTaunk08/NLP_scripts/blob/master/Transformers_multilabel_distilbert.ipynb) 
    - [Fine Tuning Transformer for MultiLabel Text Classification (BERT)](https://github.com/abhimishra91/transformers-tutorials/blob/master/transformers_multi_label_classification.ipynb)
    - [Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) 
   - [DistilBERT, a distilled version of BERT](https://arxiv.org/pdf/1910.01108.pdf)
   - [Transformers Tutorial](https://huggingface.co/transformers/notebooks.html)
   - [Introducing DistilBERT, a distilled version of BERT](https://medium.com/huggingface/distilbert-8cf3380435b5)
   - [Cost-Sensitive BERT for Generalisable Sentence Classification with Imbalanced Data](https://deepai.org/publication/cost-sensitive-bert-for-generalisable-sentence-classification-with-imbalanced-data )
    - [Transformers](https://github.com/huggingface/transformers/blob/master/notebooks/02-transformers.ipynb)
    - [Fine Tuning Transformer for MultiLabel Text Classification](https://github.com/abhimishra91/transformers-tutorials/blob/master/transformers_multi_label_classification.ipynb)


***


