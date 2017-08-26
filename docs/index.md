<!-- http://www.tablesgenerator.com/markdown_tables# -->
With the unprecedented dependence on Machine Learning in our decision-making process and the increasing growth of discriminating models intentionally and unintentionally, this project is an attempt to evolve towards a fairness-aware ML.
By collecting discriminatory training sets in various fields of compentence, we aim at providing a foundation to develop ML models that can spot biased results and eventually contribute towards finding a balanced outcome.
We endeavour to set benchmarking techniques that contribute to algorithmic discrimination discovery with the help of available resources from around the web.

As it is undisputed that fairness tools are highly necessary in order to avoid disadvantaging and marginalizing minority groups, the flux and diversity of data behind Machine Learning models makes it difficult to find a norm to abide by if one is to reach a so-called fair scoring.
The Fairness Measures Project provides a platform for collecting datasets that could be used to develop such norms.

While part of our project is to avail data sets showing discriminatory patterns, we focus more importantly on developing and maintaining benchmarking tools to analyze and quantify bias in raw and processed data. We include common tests like AUC and nDCG as well as more specialized methods like individual and group fairness metrics to dispute the results. More on that in [Measures](Pages/Measures.md)

By doing so, we target data collected from various areas of interest (e.g. in finance, law, Human Resources).
If you believe your data can help this cause, please [contribute with a dataset](src/Drop Box)  or [get in touch with us](mailto:meike.zehlike@tu-berlin.de)  if you can be of any enrichment to the project. Also feel free to share the work!

<a href="https://www.facebook.com/sharer/sharer.php?u=http%3A//fairness-measures.org"  target="_blank" >Share on Facebook</a> | <a href="https://twitter.com/home?status=Discrimination%20Discovery%20can%20be%20quantified%20-%20http%3A//fairness-measures.org"  target="_blank">Share on Twitter</a> | <a href="https://www.linkedin.com/shareArticle?mini=true&url=http%3A//fairness-measures.org&title=Fairness%20Measures%20Project&summary=&source="  target="_blank">Share on LinkedIn</a>

# About The Data

The datasets were collected from various sources and show an element of discrimination with respect to certain minority individuals and groups. Each Dataset includes information about the respective discriminatory profile. For data protection reasons, some of the collected datasets are available only upon requests.


<h1><a name ="datasets"> Datasets </a></h1>

| Dataset                          	                            | Quality Criterion 	| # Entries 	| Format |
|----------------------------------	                            |-------------------	|-----------	|--------|
| [COMPAS Recidivism Risk](Pages/Datasets/Compas.md)           	| recidivism        	| 18K    	    | csv |
| [Statlog (German Credit -SCHUFA)](Pages/Datasets/Schufa.md) 	| credit rating     	| 1k        	| csv |
| [SAT](Pages/Datasets/SAT.md)                              	| test score        	| 1,600k 	    | pdf |
| [SAT-Chile](Pages/Datasets/SATChile.md)                       | test score            |               | csv |
| [Adult Census ](Pages/Datasets/censusincome.md)               | income                | 48842         | csv |

