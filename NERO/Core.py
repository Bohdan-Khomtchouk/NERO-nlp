"""
The topic area of the Named Entity Recognition Ontology (NERO) is the lexical representation
of entities, rather than the entities themselves. For example, we want vocabulary to represent the
set of protein names found in a text, rather than the protein that information content represents.
Thus, the main aim of NERO is to enable text annotators or text annotation tools to mark up
the a text’s lexical content as to the nature of that lexical entity.
For example, in the sentence:

>> Activation of NF-κB2 and RelB was found in 53.7 and 49.2 % of the 121 ER+

tumours analyzed, with similar levels to `ER-breast` tumours analysed in parallel for
comparisons. (1)

Here, `NF-κB2` and `RelB` can be either a gene or protein.


This module is the main wrapper over the corpus created using NERO.

"""





import pandas as pd
import matplotlib.pyplot as plt







class Corpus:
    """
    The Corpus class containing functions to extract data from the corpus.
    """

    def __init__(self, *args, **kwargs):
        self._data = self._load_data(kwargs['df'])
        # Main corpus/dataframe properties
        self.columns = self._data.columns
        self.shape = self._data.shape
        self.size = self._data.size
        self.values = self._data.values

    def __getattribute__(self, attr):
        """
        If a given attribute is a column name we return the respective 
        column. Otherwise the attribute will be called directly.
        """

        try:
            return super(Corpus, self).__getattribute__(attr)
        except AttributeError:
            if attr in self.columns:
                return self._data[attr]
        
        return super(Corpus, self).__getattribute__(attr)

    def _load_data(self, _path):
        """
        Reading the raw corpus and returning a pandas dataframe.
        """
    
        df = pd.read_csv(
            _path, 
            delimiter='\t',
            encoding='latin1'
        )
        return df

    def procset_bind(self):
        """Returns the rows with their procset column set to bind."""

        return self._data[self._data['procset'] == 'bind']

    def procset_gene_phenotype(self):
        """Returns the rows with their procset column set to gene_phenotype."""
        
        return self._data[self._data['procset'] == 'gene_phenotype']

    def procset_topic_bd(self, topic):
        """
        Returns the rows that have a procset column set to the topic argument. 
        topic could be any of following variables: bd, ccc, aut, sch, bc, mrs,
        ll.
        """
        col = f"topic_{topic}"
        return self._data[self._data['procset'] == col]
    
    def procset_transcription(self):
        """
        Returns the rows with their procset column set to transcription.
        """
            
        return self._data[self._data['procset'] == 'transcription']
   

    def plot_semantic_class(self):
        """
        Plot a bar chart of semantic_class column based on the frequency
        of semantic classes.
        """

        gg = self._data['semantic_class_entity1'].value_counts()
        gg.plot.bar()
        plt.show()
    
    def plot_protein_domain_entity(self, num=20):
        """
        Plot a bar chart of top `num` protein_domain_entity fields
        based on thir frequencies.
        """
        col_names = [i for i in self.columns if i.startswith('protein_domain_entity')]

        out = pd.Series()

        for col in col_names:
            out = out.add(self._data[col].value_counts(), fill_value=0)
        
        out[:num].plot.bar()
        plt.show()
        