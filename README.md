# COVID-19 Risk Factor Predictor (C-RFP)

## Overview

### Project Summary
Select corresponding information to see relative prediction for COVID-19 based on risk factors.

### Authors

* **Chenming Cao** - [Devpost ID](https://devpost.com/chenmcao) – chenmcao@seas.upenn.edu – [GitHub](https://github.com/chenming-cao/)
* **Valerie Sutera** - [Devpost ID](https://devpost.com/vsutera) – vsutera@seas.upenn.edu – [GitHub](https://github.com/valeriesutera/)
* **Cedric Vicera** - [Devpost ID](https://devpost.com/cedricvicera) – vicera@seas.upenn.edu – [GitHub](https://github.com/cedricvicera/)

## Usage

### Deployment
Requires Flask to be installed.
Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

````
$ pip install -U Flask
````

Run the following script and click the link:

````
$ python apprunner.py
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
````

Requires Pandas to be installed.
Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

````
$ pip install pandas
````

Requires downloading and storing the dataset [COVID-19_Case_Surveillance_Public_Use_Data.csv](https://data.cdc.gov/api/views/vbim-akqf/rows.csv?accessType=DOWNLOAD&bom=true&format=true) into the root directory for data processing.

### Tools Used

Which frameworks, libraries, or other tools did you use to create your project?

* [Flask](https://flask.palletsprojects.com/) - A lightweight [WGSI](https://wsgi.readthedocs.io/) web application framework.

### Acknowledgments

* [CDC COVID-19 Case Surveillance Public Use Data](https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf)
* Theme publicly available and modified from [Colorlib](https://colorlib.com/).
* Page loader from [w3schools](https://www.w3schools.com/).

### License

>This package is licensed under the MIT License (<a href="https://choosealicense.com/licenses/mit/" target="_blank">MIT</a>).
