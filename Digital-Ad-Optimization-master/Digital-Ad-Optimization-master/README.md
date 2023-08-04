# Digital Ad Optimization
------------------------------------

This project mainly serves as a data analysis project to discover insights into user click behavior on ads. The [data](https://www.kaggle.com/c/avito-context-ad-clicks/data) was provided by Avito, Russia's largest general classified website.  Additionally, a logistic regression model is trained to predict whether a user will click on a given ad. Please go [here](https://jleung46.github.io/Ad_Optimization.html) for the full writeup, including analysis and results.

### Installation
The program requires the following dependencies:

 * python 3.5
 * numpy
 * pandas
 * sklearn
 * sqlite3
 * datetime

Run `pip3 install -r requirements.txt` to install requirements.

### Data

* Download the database [here](https://www.kaggle.com/c/avito-context-ad-clicks/data).
* Extract the downloaded file into `data` directory.
* Extract the database.sqlite file.

The sample data used for the exploratory analysis can be obtained [here](https://drive.google.com/open?id=1dLldcIZg0eNTTiVIi0p-ENCHuH0RinMG) which should be extracted to the `data` directory.

### Running

```
python main.py
```

The program will then output the AUC score of the trained model.
