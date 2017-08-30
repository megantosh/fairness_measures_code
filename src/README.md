# FAIRNESS AND DISCRIMINATION MEASURES

This project quantifies the fairness distribution of rankings in a dataset using simple statistical functions, e.g. Mean Average, as well as more advanced such as group fairness rankings. Fairness is measured for example if there is an equal distribution of protected and non-protected attributes in a dataset. Given a dataset with already definded protected attributes (e.g. sex, race, age) as an input, the output is the score of a function measuring the respective statistical key figure (e.g. Mean Value, Kendall's Tau) with respect to the protected elements. A more details are available in the respective functions, please refer to the code comments.


## Getting Started
1. Packages accept datasets that already have a calculated score that indicates a ranking.
2. to use a dataset, the first column should provide the attribute names. Protected attributes require the prefix ``protected``. The column with the calculated score requires a ``target``. For example, if you need to measure fairness rankings of a dataset with the columns ``sex`` and ``credit_score``, please rename the first columns e.g. to ``protected_sex`` and ``target_Score``

### Prerequisites

* python version 3.5
* dataset in csv format

```
maybe put python version checker for unix and windows terminal?
```

### Installing

* clone repository
* put into python path

```
command line code for both steps
```

And repeat

```
until finished
```

## Running first example
* go to src/
* call main.py to perform t-test on small example dataset 
```
python3 main.py 
```
* call main.py with your dataset file to perform t-test on your data
```
python3 main.py /PATH/TO/YOUR/CSV/FILE
```

## Running the tests

* unittests for the system
* go to test/
* call ```python3 runner.py```

## Built With

@Mohamed, these are just examples. In case you have anything to write here, use the following lines as examples. Otherwise delete this section

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

* write how people can participate in the project. Codes of Conduct?

## Versioning

* Do we have any special versioning tools? I guess it's just git, right?

## Authors

* **Meike Zehlike** - *Initiator* - [MilkaLichtblau](https://github.com/MilkaLichtblau)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GPL License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* cite Zliobaite paper here as inspiration
* Hat tip to anyone who's code was used
* more inspiration
* etc

