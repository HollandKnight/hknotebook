import csv
import os
import os.path
import re

import nltk as nltk
#import textract
from bs4 import BeautifulSoup as BeautifulSoup
from openpyxl import Workbook as Workbook


def save_list_as_excel(path, clean_sent_list, raw_sent_list):
    wb = Workbook()
    ws = wb.active
    column_cell_A = 'A'
    column_cell_B = 'B'
    column_cell_C = 'C'
    ws[column_cell_A + str(1)] = 'text'
    ws[column_cell_B + str(1)] = 'label'
    ws[column_cell_C + str(1)] = 'raw'
    list_len = len(clean_sent_list)
    for i in range(0, list_len):
        ws[column_cell_A + str(i + 2)] = clean_sent_list[i]
        ws[column_cell_B + str(i + 2)] = 'label'
        ws[column_cell_C + str(i + 2)] = raw_sent_list[i]
    wb.save(path)
    print('Excel write complete')


def html_from_file_no_tags(file_path):
    with open(file_path, 'rb') as myfile:
        raw_text = myfile.read()
    bsObj = BeautifulSoup(raw_text, 'lxml').text
    return bsObj


def normalize_sent(sent):
    wpt = nltk.WordPunctTokenizer()
    stop_words = nltk.corpus.stopwords.words('english')
    sent = re.sub(r'[^a-zA-Z\s]', '', sent, re.I | re.A)
    sent = sent.strip()
    tokens = wpt.tokenize(sent)
    filtered_tokens = [token for token in tokens if token not in stop_words]
    sent = ' '.join(filtered_tokens).lower()
    return sent


def html_from_file_no_tags(file_path):
    with open(file_path, 'rb') as myfile:
        raw_text = myfile.read()
    bsObj = BeautifulSoup(raw_text, 'lxml').text
    return bsObj


def load_normal_with_stopwords(path):
    doc = str(load_raw(path))
    return normalize_document_return_list(doc)


def load_normal_no_stopwords(path):
    doc = load_raw(path)
    norm = normalize_document_return_list(doc)
    clean_sent = []
    for sent in norm:
        clean = remove_stop_words(sent)
        clean_sent.append(clean)
    return clean_sent


def list_from_directory(path):
    list_of_text = []
    for file in os.listdir(path):
        filename = os.fsdecode(file)
        file_path = path + filename
        text = load_raw(file_path)
        text = str(text)
        list_of_text.append(text)


def load_excel(path):
    print('finish')


def load_list_from_csv(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        list_raw = list(reader)
        list_clean = []
        for i in list_raw:
            x = ''.join(i)
            list_clean.append(x)
        list_clean_two = []
        for i in list_clean:
            x = ''.join(i)
            list_clean_two.append(x)
        return list_clean_two


def load_raw(path, tags=False):
    if path.endswith('html'):
        if (tags):
            return html_from_file_tags(path)
        else:
            return html_from_file_no_tags(path)
    elif path.endswith('.txt'):
        return str(text_from_file(path))
    else:
        try:
            return str(text_from_binary(path))
        except:
            print(
                'Failed to load as binary. Try reader that accepts url as argument (e.g., html_from_web_tags(url) or html_from_web_no_tags(url)).')


def text_from_binary(file_path):
    #text = textract.process(file_path, method='tesseract', language='eng')
    text = 'Not set up for binary'
    return text.decode('unicode_escape').encode('utf-8', 'ignore').strip()


def html_from_file_tags(file_path):
    with open(file_path, 'rb') as myfile:
        raw_text = myfile.read()
    return raw_text


def html_from_web_no_tags(url):
    response = urlopen(url)
    bsObj = BeautifulSoup(response, 'lxml').text
    return bsObj


def html_from_web_tags(url):
    response = urlopen(url)
    tagged_text = response.read()
    return tagged_text


def text_from_file(file_path):
    with open(file_path, 'rb') as myfile:
        raw_text = myfile.read()
    return raw_text


def remove_stop_words(doc):
    wpt = nltk.WordPunctTokenizer()
    stop_words = nltk.corpus.stopwords.words('english')
    tokens = wpt.tokenize(doc)
    filtered_tokens = [token for token in tokens if token not in stop_words]
    doc = ' '.join(filtered_tokens).lower()
    return doc


def normalize_document_return_list(doc):
    wpt = nltk.WordPunctTokenizer()
    stop_words = nltk.corpus.stopwords.words('english')
    list_of_clean_sents = []
    sent_list = tokenize.sent_tokenize(str(doc))
    for sent in sent_list:
        sent = re.sub(r'[^a-zA-Z\s]', '', sent, re.I | re.A)
        sent = sent.strip()
        tokens = wpt.tokenize(sent)
        filtered_tokens = [token for token in tokens if token not in stop_words]
        sent = ' '.join(filtered_tokens).lower()
        list_of_clean_sents.append(sent)
    return list_of_clean_sents


def tokenize_and_stem(text):
    stemmer = SnowballStemmer("english")
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    joined_text = " ".join(stems)
    print(joined_text)
    return joined_text
