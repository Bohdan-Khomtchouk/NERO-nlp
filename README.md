# NERO-nlp

### `NERO-nlp` is a biomedical Named Entity (Recognition) Ontology.


Using `NERO-nlp`, we annotated a large biomedical corpus to enable a broad spectrum of natural language processing and biomedical machine learning tasks.


`NERO-nlp` is a wrapper around this corpus.


## Sample usage:



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



## Installation:

For running the `NERO-nlp` you need to have python3.7+ and pandas installed. For installation you can use `pip` or `pip3`. 

    # Install
	sudo pip3 install NERO-nlp
	# or
	sudo python3 -m pip install NERO-nlp
	# Upgrade
	sudo pip3 install NERO-nlp --upgrade

## Contact

You are welcome to:

* submit suggestions and bug-reports at: <https://github.com/Bohdan-Khomtchouk/NERO-nlp/issues>
* send a pull request on: <https://github.com/Bohdan-Khomtchouk/NERO-nlp>
* compose an e-mail to: <bohdan@uchicago.edu>


## Code of conduct

Please note that this project is released with a [Contributor Code of Conduct](CONDUCT.md). By participating in this project you agree to abide by its terms.
