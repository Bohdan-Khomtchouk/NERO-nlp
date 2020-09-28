from NERO.corpus import corpus


print(corpus.columns)                                                                                                                                                                               
# Index(['amId', 'assignedId', 'sdocId', 'userId', 'editorUserId',
#        'indexActionMentionId', 'external_id', 'dbActionMentionId', 'entity1',
#        'semantic_class_entity1', 'modifier_entity1', 'actionType',
#        'semantic_class_actionType', 'modifier_actionType',
#        'protein_domain_entity1', 'gene_region_entity1', 'entity2',
#        'semantic_class_entity2', 'modifier_entity2', 'protein_domain_entity2',
#        'gene_region_entity2', 'topic', 'statement_context', 'negative',
#        'certainty_level', 'derived_certainty_level', 'applied_rule',
#        'indexSentenceId', 'pmid', 'sentenceText', 'procset'],
#       dtype='object')

print(corpus.shape)                                                                                                                                                                                 
# (362740, 31)

print(corpus._data)                                                                                                                                                                                 
#           amId  assignedId    sdocId userId  editorUserId  ... applied_rule                           indexSentenceId        pmid                                       sentenceText procset
# 0        44403           2      12.0      6          10.0  ...          NaN  gw60_biochmbiophyrescomm_295_4_1027_s_40  12127999.0  `Microsomal` membrane prepared as described fr...    bind
# 1         1040           3      12.0      7          10.0  ...          NaN  gw60_biochmbiophyrescomm_295_4_1027_s_40  12127999.0  `Microsomal` membrane prepared as described fr...    bind
# 2        57771           1     201.0      5           NaN  ...          NaN                gw60_embo_17_18_5273_s_218   9736607.0  ( A) Amph2 SH3 and Amph2-SH3deltaDAPS domains ...    bind
# 3        57772           2     201.0      5           NaN  ...          NaN                gw60_embo_17_18_5273_s_218   9736607.0  ( A) Amph2 SH3 and Amph2-SH3deltaDAPS domains ...    bind
# 4         1108           1     201.0      6           NaN  ...          NaN                gw60_embo_17_18_5273_s_218   9736607.0  ( A) Amph2 SH3 and Amph2-SH3deltaDAPS domains ...    bind
# ...        ...         ...       ...    ...           ...  ...          ...                                       ...         ...                                                ...     ...
# 362735     NaN  manualset3       NaN    NaN           NaN  ...          NaN                                       NaN         NaN                                                NaN     NaN
# 362736  235155           2  428230.0     15           NaN  ...          NaN                                       NaN         NaN  Further , Trace Amine-Associated Receptor 1 ( ...     NaN
# 362737     NaN  manualset3       NaN    NaN           NaN  ...          NaN                                       NaN         NaN                                                NaN     NaN
# 362738  235156           3  428230.0     15           NaN  ...          NaN                                       NaN         NaN  Further , Trace Amine-Associated Receptor 1 ( ...     NaN
# 362739     NaN  manualset3       NaN    NaN           NaN  ...          NaN                                       NaN         NaN                                                NaN     NaN

# [362740 rows x 31 columns]

print(corpus.semantic_class_actionType)                                                                                                                                                             
# 0         NaN
# 1         NaN
# 2         NaN
# 3         NaN
# 4         NaN
#          ... 
# 362735    NaN
# 362736    NaN
# 362737    NaN
# 362738    NaN
# 362739    NaN
# Name: semantic_class_actionType, Length: 362740, dtype: object

# In [8]:                                                                                                                                                                                                     
print(corpus.procset_topic_bd.__doc__)
    # Returns the rows that have a procset column set to the topic argument. 
    # topic could be any of following variables: bd, ccc, aut, sch, bc, mrs,
    # ll.
        

print(corpus.procset_topic_bd('aut'))                                                                                                                                                               
#         amId assignedId    sdocId userId  editorUserId indexActionMentionId  ...  derived_certainty_level  applied_rule indexSentenceId pmid                                       sentenceText    procset
# 66643  73707          1  354681.0      5           NaN                  NaN  ...                      NaN           NaN             NaN  NaN  Mutations in the gene encoding the synaptic sc...  topic_aut
# 66644  73708          2  354681.0      5           NaN                  NaN  ...                      NaN           NaN             NaN  NaN  Mutations in the gene encoding the synaptic sc...  topic_aut
# 66645  73709          1  354682.0      5           NaN                  NaN  ...                      NaN           NaN             NaN  NaN  X-Linked Mental Retardation and Autism Are Ass...  topic_aut
# 66646  73710          2  354682.0      5           NaN                  NaN  ...                      NaN           NaN             NaN  NaN  X-Linked Mental Retardation and Autism Are Ass...  topic_aut
# 66647  73711          3  354682.0      5           NaN                  NaN  ...                      NaN           NaN             NaN  NaN  X-Linked Mental Retardation and Autism Are Ass...  topic_aut
# ...      ...        ...       ...    ...           ...                  ...  ...                      ...           ...             ...  ...                                                ...        ...
# 71288  78572          2  356314.0      5           NaN                  NaN  ...                      NaN           NaN             NaN  NaN  Restricted and repetitive behaviors (RRBs) are...  topic_aut
# 71289  78573          3  356314.0      5           NaN                  NaN  ...                      NaN           NaN             NaN  NaN  Restricted and repetitive behaviors (RRBs) are...  topic_aut
# 71290  78574          1  356315.0      5           NaN                  NaN  ...                      NaN           NaN             NaN  NaN  Recent evidence points to white-matter abnorma...  topic_aut
# 71291  78575          1  356316.0      5           NaN                  NaN  ...                      NaN           NaN             NaN  NaN  By contrast, the ASD participants did not show...  topic_aut
# 71292  78577          1  356317.0      5           NaN                  NaN  ...                      NaN           NaN             NaN  NaN  However, the participants with High-Functionin...  topic_aut

# [807 rows x 31 columns]

corpus.plot_protein_domain_entity()

