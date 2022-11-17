# sde-project

This project is using poetry for dependency management so you will have to install poetry on your local.

1. Install potery if not already present in your local system:
```
curl -sSL https://install.python-poetry.org | python3 -
```
2. Use poetry install to install the packages required.
```
poetry install  
```

Developement process:
1. Create a branch from main.
2. Do the developement work.
3. Merge to main.


If any new dependencies are added use this command to generate a requirement file.
    
    poetry export -f requirements.txt --without-hashes --output requirements.txt

**Scripts Used:** <br><br>
a) scripts/get_data_sonarcube.py - Uses SonarCube API to get a list of public projects and get attributes like key, organisation_name etc and generates files sonarcube_data_projects.csv.

b) scripts/get_data_links.py - Uses file generated from step a and get project link from SonarCloud API (different endpoint) using the project key generated from step a. It generates sonarcube_data_with_repo_link.csv.

c) scripts/get_data.py - Uses file from step b and filters all the github projects. Using the project url and SonarCloud API, gets different metrics for a project like complexity, bugs etc. It generates sonarcube_data.csv.

d) scripts/get_travis_data.py - uses file from step c and Travis CI API, get information of all the builds for that project_url. It generates travis_data.csv.

e) scripts/get_sonarcube_project_date.csv - Uses the file from step c and step d and merge them to have a single dataframe. Then using the project_key and SonarCloud API, gets all the dates when the quality profile was executed. It generates sonar_quality_profile.csv.

f) scripts/metrics.py - It uses file from step d and step e and creates a relation between dates of quality profile execution and dates when builds were executed and on the basis of that calculate values of different metrics.

