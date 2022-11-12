import requests
import pandas as pd


def get_data():
    df = pd.read_csv('sonarcube_data_1.csv')
    print(df.head())

    # print(df[['key']].head())

    dict1 = []
    for project_key in df[['key']][:2]:
        url = 'https://sonarcloud.io/api/measures/component?' \
              'component=' + project_key + '&metricKeys=ncloc,complexity,violations,bugs,code_smells'
        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.json())
        response = response.json()
        measures = response['component']['measures']
        print(response)
        # for measure in measures:
        #     if
        # dict1['project_key'] = project_key
        # dict1['ncloc'] = response[]
    #     if response.status_code == 400:
    #         break
    #     else:
    #         response = response.json()
    #         sub_df = pd.DataFrame(response['components'])
    #         df = pd.concat([df, sub_df])
    #
    # # print(df.head())
    # df = df.sort_values(by='organization')
    # df.to_csv('sonarcube_data_1.csv', index=False)


if __name__ == '__main__':
    get_data()
