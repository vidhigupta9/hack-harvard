from keybert import KeyBERT
from flair.embeddings import TransformerDocumentEmbeddings
import requests

roberta = TransformerDocumentEmbeddings('roberta-base')
kw_model = KeyBERT(model=roberta)

def get_query(ques):
    topn = 5 if len(ques<=100) else 8

    keys = kw_model.extract_keywords(ques, keyphrase_ngram_range=(1,1), stop_words='english', top_n=topn)
    query = ""
    for i in range(len(keys)):
        query += keys[i][0]

    return query


def get_cases(ques, topn):
    URL = "https://api.case.law/v1/cases/?search=" + get_query(ques)
    response = requests.get(URL)
    res = response.json()["results"][:topn]

    cases = []
    keys = ["id", "name", "court", "jurisdiction", "web",  "pdf"]
    for i in range(len(res)):
        casedata = dict.fromkeys(keys, "")
        idurl = res[i]["url"]
        casedata["id"] = res[i]["id"]
        casedata["name"] = res[i]["name"]
        casedata["court"] = res[i]["court"]["name"]
        casedata["jurisdiction"] = res[i]["jurisdiction"]["name_long"]
        casedata["web"] = res[i]["frontend_url"]
        casedata["pdf"] = res[i]["frontend_pdf_url"]
        cases.append(casedata)

    return cases
