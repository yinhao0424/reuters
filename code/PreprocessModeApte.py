import numpy as np
import pandas as pd
import json


from pandas.io.json import json_normalize
import time


"""
Preprocessing Json file to dataframe based on ModeApte split.
input file name and output training and testing csv files.

- Read Json File
- Generate Dataframe
- Generate training and testing set based on ModeApte split
- Select useful columns, flatten data, Drop None
"""

def read_json(metadata):
    """
    :param metadata: json file store reuters data
    :return: a list of documents
    """
    with open(metadata, 'r') as json_file:
        data = json.load(json_file)

    documents = data['reuters']
    return documents

def generate_df(documents):
    """
    :param documents: a list of documents
    :return: a dataframe
    """
    reuters = pd.json_normalize(documents)

    return reuters


def modeapte_split(reuters):
    """ func: parse reuters and generate training and testing data based on ModeApte split
    :param reuters: original dataframe
    :return:
    """
    # generate training data
    reuters_train = reuters[(reuters['identity.lewis_split'] == 'train') & (reuters['identity.topics'] == 'yes')]
    # print('The shape of training file is {}.'.format(reuters_train.shape))

    # generate testing data
    reuters_test = reuters[(reuters['identity.lewis_split'] == 'test') & (reuters['identity.topics'] == 'yes')]
    # print('The shape of testing file is {}.'.format(reuters_test.shape))

    return reuters_train, reuters_test

def preprocess_df(df):
    """
    :param df
    :return:
    """
    # select topics, id, text.title and text.body
    df['texts'] = df['texts.title'] + df['texts.body']
    df = df[['identity.new_id', 'topics', 'texts']]
    df = df.rename(columns={"identity.new_id": "id"})

    # flatten dataset based on topics
    df = df.explode('topics')

    # remove Nan
    df = df.dropna()
    return df

def generate_final_df(metadata):
    """
    :param metadata: input json file
    :return: final train and test data set
    """
    documents = read_json(metadata)
    reuters = generate_df(documents)
    train,test = modeapte_split(reuters)

    reuters_train = preprocess_df(train)
    reuters_test = preprocess_df(test)

    return reuters_train, reuters_test

def save_csv(reuters_train, reuters_test):

    reuters_train.to_csv('result/reuters_final_train.csv', index=False)
    reuters_test.to_csv('result/reuters_final_test.csv', index=False)



if __name__ == '__main__':
    metadata = 'reuters.json'
    reuters_train, reuters_test = generate_final_df(metadata)
    save_csv(reuters_train, reuters_test)
    # print(pd.show_versions())

