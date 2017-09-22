# Fairness Measures - Code Repository

This code repository contains implementations of measures used to quantify discrimination.

For background information on the project, see http://fairness-measures.org/

For the measures that are implemented, see http://fairness-measures.org/Pages/Measures

## Expected input and output

These programs take as input a dataset in which each row represents a person.

We assume one of the attributes in the input is the *outcome* which we assume was produced by a predictive model (if we want to evaluate algorithmic fairness), or by a person (if we want to evaluate fairness of human decisions). For instance, an outcome could be binary such as whether a person got a scholarship or not, or numeric such as the credit score associated to a person. Some outcomes can be considered positive, such as when a benefit is received, while other outcomes are negative, such as when a benefit is denied.

We further assume there are *protected* attributes in the input, such as gender, race, age, or disability that should ideally not affect the outcome. Some values of the protected attribute are associated to potentially discriminated groups, such as *disability=yes*.

The output is a measure of fairness. Fairness can be measured in many ways, for instance one of the simplest cases is statistical parity, i.e., an equal distribution of protected and non-protected attributes for the elements that received the positive outcome. There are many other ways in which fairness can be measured, please refer to the code comments.

The rest of this page explains how to install and run the code.

## Data preparation

1. Packages accept datasets that already have a calculated score/outcome.
2. To use a dataset, each feature should be represented in a column with the first entry as the column name.
Protected attributes require the prefix ``protected``. The column to be examined requires the prefix ``target``.
For example, if you need to measure fairness rankings of a dataset with the columns ``sex`` and ``credit_score``,
please rename the first columns e.g. to ``protected_sex`` and ``target_credit_Score``
3. protected candidates' features index ranges from ``0``, to the <i> highest protected group index </i>, such that in the case of having ``sex`` as a protected feature,
we use ``1`` for women if <i>female</i> is the protected group and ``0`` for men provided they are the only unprotected group. In a different use case,
where age is the protected attribute in ascending order, we can use:
 - ``0`` for people up to 18 years of age, with ``3`` being the <i>lowest protected group index</i> (always ``0``)
 - ``1`` for people between 19 to 35 year,
 - ``2`` for people between 36 to 64 years,
 - ``3`` for people above 65 years, with these being as the group protected most, i.e. with a <i> highest protected group index </i> (higher number indicates a more protected group)

## Installation

### Prerequisites

* python version 3.5
* dataset to examine in csv format with features as described [above](#getting-started)

### Installing

* clone repository
* put into python path

## Running

### First example

* go to ``src/``
* call main.py to perform the tests on the provided example dataset
```
python3 main.py -d
```
* call ``main.py`` with your dataset file to perform t-test on your data
```
python3 main.py -f </PATH/TO/YOUR/CSV/FILE/datasetname.csv>
```

### Running unit tests

* unittests for the system
* go to ``test/``
* call ```python3 runner.py```

## Contributing

* you can upload your contributions on the ``Upload`` branch. After reviewing, we will merge it.
* For suggestions, please create a Github Issue.

### Versioning

* Check GitHub's [Version History](https://github.com/megantosh/fairness_measures/commits/Code_read_only/src)
<!--
* Do we have any special versioning tools? I guess it's just git, right?
-->

### Authors

* **Meike Zehlike** - *Initiator* - [MilkaLichtblau](https://github.com/MilkaLichtblau)

See also the list of [contributors](https://github.com/megantosh/fairness_measures/graphs/contributors) who participated in this project.

### License

This project is licensed under the GPL License <!-- - see the [LICENSE.md](LICENSE.md) file for details -->

## References

* “Žliobaitė, Indrė. “Measuring discrimination in algorithmic decision making.” Data Mining and Knowledge Discovery 31, no. 4 (July 31, 2017): 1060-089. doi:10.1007/s10618-017-0506-1.”
<!--
* cite Zliobaite paper here as inspiration
* Hat tip to anyone who's code was used
* more inspiration
* etc
-->

