<!-- http://www.tablesgenerator.com/markdown_tables# -->
With the unprecedented dependence on Machine Learning in our decision-making process and the increasing growth of discriminating models intentionally and unintentionally, this project is an attempt to evolve towards a fairness-aware ML.
By collecting discriminatory training sets in various fields of compentence, we aim at providing a foundation to develop ML models that can spot biased results and eventually contribute towards finding a balanced outcome.
We endeavour to set benchmarking techniques that contribute to algorithmic discrimination discovery with the help of available resources from around the web.

As it is undisputed that fairness tools are highly necessary in order to avoid disadvantaging and marginalizing minority groups, the flux and diversity of data behind Machine Learning models makes it difficult to find a norm to abide by if one is to reach a so-called fair scoring.
The Fairness Measures Project provides a platform for collecting datasets that could be used to develop such norms. If you believe your data can help this cause, please [share it](#).

# About The Data

The datasets were collected from various sources and show an element of discrimination with respect to certain minority individuals and groups. Each Dataset includes information about the respective discriminatory profile.


<a name ="datasets"><h1> Datasets </h1></a>

| Dataset                          	| Quality Criterion 	| # Entries 	| Format 	|
|----------------------------------	|-------------------	|-----------	|--------	|
| COMPAS Recidivism Risk           	| recidivism        	| 18K    	| csv    	|
| Statlog - German Credit (SCHUFA) 	| credit rating     	| 1k      	| csv    	|
| SAT                              	| test score        	| 1,600k 	| pdf      	|
|                                  	|                   	|           	|                    	|                                                                                                	|        	|
|                                  	|                   	|           	|                    	|                                                                                                	|        	|

#Citation
If you decide to use one of our datasets in your work, please consider using the following BibTeX citation:

```
@misc{fairness-Measures,
  author       = {Meike Zehlike and Carlos Castillo and Francesco Bonchi and Sara Hajian and Mohamed Megahed},
  title        = {{Fairness Measures Datasets}: {TU Berlin} %Dataset Collection%},
  howpublished = {\url{http://fairness-measures.org}},
  month        = jun,
  year         = 2017
}
```