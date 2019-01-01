# IReporter_API

[![Build Status](https://travis-ci.org/ManuelDominic/IReporter_API.svg?branch=develop)](https://travis-ci.org/ManuelDominic/IReporter_API) [![Test Coverage](https://api.codeclimate.com/v1/badges/b1d60dcdfe7abdbbfdd6/test_coverage)](https://codeclimate.com/github/ManuelDominic/IReporter_API/test_coverage) [![Coverage Status](https://coveralls.io/repos/github/ManuelDominic/IReporter_API/badge.svg?branch=develop)](https://coveralls.io/github/ManuelDominic/IReporter_API?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/b1d60dcdfe7abdbbfdd6/maintainability)](https://codeclimate.com/github/ManuelDominic/IReporter_API/maintainability) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/50263e1fad074ebb8f914be692d1fadc)](https://www.codacy.com/app/ManuelDominic/IReporter_API?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ManuelDominic/IReporter_API&amp;utm_campaign=Badge_Grade)

## About

-   IReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

## Features

-   Users can create an account and log in
-   Users can create a red-flag record (An incident linked to corruption
-   Users can create intervention record (a call for a government agency to intervene e.g repair bad road sections, collapsed bridges, flooding e.t.c)
-   Users can edit their red-flag or intervention records
-   Users can delete their red-flag or intervention records
-   Users can add geolocation (Lat Long Coordinates) to their red-flag or intervention records
-   Users can change the geolocation (Lat Long Coordinates) attached to their red-flag or intervention records
-   Admin can change the status of a record to either under investigation, rejected (in the event of a false claim) or resolved (in the event that the claim has been investigated and resolved)
-   Users can add images to their red-flag or intervention records, to support their claims
-   Users can add videos to their red-flag or intervention records, to support their claims

## Getting Started

-   Clone the project from this [[link](https://github.com/ManuelDominic/IReporter_API.git)]

## Prerequisites

-   A computer with an operating system (Linux, MacOS or Windows can do the job) Python 3.6.6
-   Pytest or any other preffered python tesing tool
-   Postman to test the API endpoints
-   A preffered text editor
-   Git to keep track of the different project branches

## Installing

-   Clone the project from this [[link](https://github.com/ManuelDominic/IReporter_API.git)]
-   Open your terminal or command prompt for linux users

### Type

-   $ cd IReporter_API
-   $ virtualenv venv
-   ($ . venv/bin/activate/ $ source venv/Scripts/activate)
-   $ git checkout develop
-   ($ pip install -r requirements.txt)
-   $ python run.py

## Deployment

-   The API is hosted on Heroku. Use the [[link](https://query-api.herokuapp.com/api/v1/)] below to navigate to it.

## Testing the Api

-   Run the command below to install pytest in your virtual environment
```
$ pip install pytest
```
-   Run the tests
```
$ pytest -vv --cov
```

## Versioning

-   This is version one "v1" of the API

## End Points(Required Features)

|                   End Point                               |           Functionality       |
|  ---------------------------------------------------------|-------------------------------
| POST   api/v1/auth/login                                  | Login to application          |
| POST   api/v1/auth/signup                                 | Register an account           |
| POST   api/v1/red-flags                                   | Create a red-flag             |
| GET    api/v1/red-flags                                   | Fetch all red-flags           |
| GET    api/v1/red-flags/<int:redflag_Id>                  | Fetch a red-flag              |
| PATCH  api/v1/red-flags/<int:redflag_Id>location          | Edit red-flag location        |
| PATCH  api/v1/red-flags/<int:redflag_Id>comment           | Edit red-flag comment         |
| POST   api/v1/intervention                                | Create a intervention         |
| GET    api/v1/intervention                                | Fetch all intervention        |
| GET    api/v1/intervention/<int:intervention_Id>          | Fetch a intervention          |
| PATCH  api/v1/intervention/<int:intervention_Id>location  | Edit intervention location    |
| PATCH  api/v1/intervention/<int:intervention_Id>comment   | Edit intervention comment     |
| PATCH  api/v1/red-flags/<int:redflag_Id>status            | Edit red-flag status          |
| PATCH  api/v1/intervention/<int:intervention_Id>status    | Edit intervention status      |

## Built With

-   Python 3.6.6 Flask (A python microframework)

## Tools Used

-   Pylint
-   Pytest
-   Virtual environment

## Authors

-   Matembu Emmanuel Dominic
-   Email : ematembu2@gmail.com

## Acknowledgements

-   Acknowledgement to the Almighty God and Andela for making cohort 15/Andela 35 possible where cadidates are motivated.
