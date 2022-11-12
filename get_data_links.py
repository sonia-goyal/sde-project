import requests
import pandas as pd


def get_data():
    df = pd.read_csv('sonarcube_data_1.csv')
    # print(df.head())

    project_keys = df['key']

    ls = []
    for project_key in project_keys[:10]:
        dict1 = {}
        print(project_key)
        url = 'https://sonarcloud.io/api/navigation/component?component=' + project_key

        response = requests.request("GET", url, headers={}, data={})
        response = response.json()
        dict1['project_key'] = project_key

        try:
            dict1['project_url'] = response['alm']['url']
            dict1['project_type'] = response['alm']['key']
        except KeyError:
            dict1['project_url'] = None
            dict1['project_type'] = None

        language_list = ''
        try:
            for qp in response['qualityProfiles']:
                language_list = language_list + qp['language'] + '|'
            dict1['languages'] = language_list
        except KeyError:
            dict1['languages'] = language_list

        ls.append(dict1)

    print(ls)
    df1 = pd.DataFrame(ls)
    print(df1.head())
    # df = df.sort_values(by='organization')
    # df.to_csv('sonarcube_data_1.csv', index=False)


if __name__ == '__main__':
    get_data()
