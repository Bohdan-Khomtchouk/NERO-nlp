NERO is a biomedical Named Entity (Recognition) Ontology.


Using NERO, we annotated a large biomedical corpus to enable a broad spectrum of natural language processing and
biomedical machine learning tasks.


NERO-nlp is a wrapper around this corpus.


Sample usage:



	# access basic dataframe attributes directly
	In [4]: corpus.columns 

	In [5]: corpus.shape

	# access to the whole dataframe
	In [6]: corpus._data

	# Having directly access to columns by calling then as an attribute
	In [7]: corpus.semantic_class_actionType

	In [8]:                                                                                                                                                                                                     

	# Using documentation in order to gain more insight into
	# functionality of the attribute.
	In [8]: corpus.procset_topic_bd.__doc__                                                                                                                                                        

	# other generic and multipurpose functionalions
	In [9]: corpus.procset_topic_bd('aut')                                                                                                                                                               

	In [10]: corpus.plot_protein_domain_entity() 



Installation:

For running the NERO-nlp you need to have python3.7+ and pandas installed. For installation you can use `pip` or `pip3` for installation. 

    # Install
	sudo pip3 install NERO-nlp
	# or
	sudo python3 -m pip install NERO-nlp
	# Upgrade
	sudo pip3 install NERO-nlp --upgrade
