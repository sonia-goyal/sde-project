import requests
import pandas as pd


def get_data():
    # Need to change to get data from get_data_links and filter for github project with python language
    df = pd.read_csv('sonarcube_data_1.csv')

    project_keys = df['key']

    ls = []
    for project_key in project_keys[:10]:
        dict1 = {}
        print(project_key)
        url = 'https://sonarcloud.io/api/measures/component?' \
              'component=' + str(project_key) + '&metricKeys=ncloc,complexity,violations,bugs,code_smells'

        response = requests.request("GET", url, headers={}, data={})
        response = response.json()
        print(response)
        if response['component']['measures']:
            measures = response['component']['measures']
            dict1['project_key'] = project_key
            for i in measures:
                if i['metric'] == 'complexity':
                    dict1['complexoty'] = i['value']
                elif i['metric'] == 'bugs':
                    dict1['bugs'] = i['value']
                elif i['metric'] == 'code_smells':
                    dict1['code_smell'] = i['value']
                elif i['metric'] == 'ncloc':
                    dict1['ncloc'] = i['value']
                elif i['metric'] == 'violations':
                    dict1['violations'] = i['value']


        ls.append(dict1)
    print(ls)


if __name__ == '__main__':
    get_data()
