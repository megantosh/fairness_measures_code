# FAIRNESS AND DISCRIMINATION MEASURES


This project quantifies the fairness distribution of rankings in a dataset using simple statistical functions,
e.g. Mean Average, as well as more advanced such as group fairness rankings. Fairness is measured for example if there is an equal distribution of protected and non-protected attributes in a dataset.
Given a dataset with already definded protected attributes (e.g. sex, race, age) as an input, the output is the score of a function measuring the respective statistical key figure
(e.g. Mean Value, Kendall's Tau) with respect to the protected elements. More details are available in the respective functions, please refer to the code comments.


## Getting Started
1. Packages accept datasets that already have a calculated score indicating a ranking.
2. to use a dataset, each feature should be represented in a column with the first entry as the column name.
Protected attributes require the prefix ``protected``. The column to be examined requires the prefix ``target``.
For example, if you need to measure fairness rankings of a dataset with the columns ``sex`` and ``credit_score``,
please rename the first columns e.g. to ``protected_sex`` and ``target_credit_Score``
3. protected candidates' features index ranges from ``0``, to the <i> lowest protected group index </i>, such that in the case of having sex as a protected feature,
we use ``0`` for women if <i>female</i> is the protected group and ``1`` for men provided they are the only unprotected group. In a different use case,
where age is the protected attribute in ascending order, we can use:
 - ``3`` for people up to 18 years of age, with ``3`` being the <i>lowest protected group index</i>
 - ``2`` for people between 19 to 35 year,
 - ``1`` for people between 36 to 64 years,
 - ``0`` for people above 65 years, with these being as the group protected most, i.e. with a <i> highest protected group index </i> (always ``0``)

### Prerequisites

* python version 3.5
* dataset to examine in csv format with features as described [above](#getting-started)

<!--maybe put python version checker for unix and windows terminal?
@mega: included now in Main.py
-->

### Installing

* clone repository
* put into python path
<!--
```
command line code for both steps
```
@mega: Dependencies

And repeat

```
until finished
```
-->

## Running first example
* go to ``src/``
* call main.py to perform t-test on small example dataset
```
python3 main.py
```
* call ``main.py`` with your dataset file to perform t-test on your data
```
python3 main.py  </PATH/TO/YOUR/CSV/FILE/datasetname.csv>
```

## Running the tests

* unittests for the system
* go to ``test/``
* call ```python3 runner.py```


## Contributing

* you can upload your contributions on the ``Upload`` branch. After reviewing, we will merge it.
* For suggestions, please create a Github Issue.

## Versioning

* Check GitHub's [Version History](https://github.com/megantosh/fairness_measures/commits/Code_read_only/src)
<!--
* Do we have any special versioning tools? I guess it's just git, right?
-->

## Authors

* **Meike Zehlike** - *Initiator* - [MilkaLichtblau](https://github.com/MilkaLichtblau)

See also the list of [contributors](https://github.com/megantosh/fairness_measures/graphs/contributors) who participated in this project.

## License

This project is licensed under the GPL License <!-- - see the [LICENSE.md](LICENSE.md) file for details -->

## Acknowledgments
* “Žliobaitė, Indrė. “Measuring discrimination in algorithmic decision making.” Data Mining and Knowledge Discovery 31, no. 4 (July 31, 2017): 1060-089. doi:10.1007/s10618-017-0506-1.”
<!--
* cite Zliobaite paper here as inspiration
* Hat tip to anyone who's code was used
* more inspiration
* etc
-->

<!--
# How to Install

# How to run

# License
make sure access rights are correct
-->
