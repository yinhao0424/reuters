from bs4 import BeautifulSoup
import glob
import json

def init_document():
    """
    function: initialize a document
    :return: a document dictionary with identity, topics and texts
    """
    document = {'identity': dict(), 'topics': [], 'texts': dict()}
    document['identity']['new_id'] = ''
    document['identity']['lewis_split'] = ''
    document['identity']['topics'] = ''

    document['texts']['title'] = ''
    document['texts']['body'] = ''
    return document


def add_identity(document, article):
    """ function: add newid, lewissplit and topics to the dictionary
    :param document: a document dictionary
    :param article: a single reuters article
    :return:
    """
    document['identity']['new_id'] = article['newid']
    document['identity']['lewis_split'] = article['lewissplit']
    document['identity']['topics'] = article['topics']


def add_topic(document, article):
    """ function: add topics to the dictionary
    :param document: a document dictionary
    :param article: a single reuters article
    :return:
    """
    for topic in article.topics.children:
        document['topics'].append(topic.text)


def add_text(document, article):
    """ function: add title and body of an article to the dictionary
    :param document: a document dictionary
    :param article: a single reuters article
    :return:
    """
    text = article.find('text')

    title = text.title
    body = text.body

    if title:
        document['texts']['title'] = title.text
    if body:
        document['texts']['body'] = body.text.replace('\n','').replace('\'', '')


def parse_documents(path):
    """
    function: given a reuters path, parse each article and write it to dictionary 'documents'
    :param path:  'reuters21578'
    :return: documents
    """
    documents = {'reuters': []}

    for file in glob.glob(path+'/*.sgm'):
        # open 'reuters21578/reut2-001.sgm' file
        data = open(file, 'rb')
        text = data.read()
        data.close()

        # parse sgm file
        tree = BeautifulSoup(text.lower(), "html.parser")

        for reuter in tree.find_all('reuters'):
            document = init_document()
            add_identity(document, reuter)
            add_topic(document, reuter)
            add_text(document, reuter)
            documents['reuters'].append(document)
    return documents

def output_json(documents,filename = 'reuters.json'):
    """
    :param documents: the final json
    :param filename: output filename
    :return:
    """
    with open(filename, 'w') as f:
        json.dump(documents, f)

if __name__ == '__main__':
    reuters_path = 'reuters21578'
    # generate json
    documents = parse_documents(reuters_path)

    # output to json
    output_json(documents)
