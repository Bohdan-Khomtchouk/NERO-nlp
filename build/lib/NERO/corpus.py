from NERO.Core import Corpus


df_path = __file__.replace('corpus.py', "annotation_results.txt")
corpus = Corpus(
    df=df_path
)