

import spacy

nlp = spacy.load("pt_core_news_lg")
import pt_core_news_lg

nlp = pt_core_news_lg.load()

doc = nlp("O Marcelo pegou COVID-19 em setembro de 2019, porem não teve problemas com isso")

for token in doc:
    print("Token:"+token.text)
    print("Pos:"+token.pos_)

