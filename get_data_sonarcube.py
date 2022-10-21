import requests
import pandas as pd


def get_sonarcube_data():
    df = pd.DataFrame()
    for i in range(1, 201):
        print(f"====== Interation {i} ======")
        url = "https://sonarcloud.io/api/components/search_projects?boostNewProjects=false&facets=ncloc%2Clanguages&p=" + \
              str(i) + "&ps=50&f=analysisDate&s=analysisDate&asc=false"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = response.json()

        sub_df = pd.DataFrame(response['components'])
        df = pd.concat([df, sub_df])

    # print(df.head())

    df.to_csv('sonarcube_data.csv', index=False)


if __name__ == '__main__':
    get_sonarcube_data
