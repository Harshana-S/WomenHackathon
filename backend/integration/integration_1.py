import os
from os import listdir
from os.path import isfile, join
import pickle
import numpy as np
import pandas as pd
dir_path = os.path.dirname(os.path.realpath('__file__'))

def return_dictionary(user_id, user_input):
    pickle_path = dir_path + '/Final_Models/'
    print(pickle_path)
    pickle_files = [
        l for l in listdir(pickle_path) if isfile(join(pickle_path, l)) if l.split(".")[-1] == "pkl"
    ]
    len(pickle_files)
    cluster_model_name = dir_path + '/cluster_model'
    model = pickle.load(open(cluster_model_name,'rb'))

    cluster_id = model.predict([user_input]).tolist()
    print(cluster_id)
    cluster_dict = {}
    features = ['Amusement_Parks', 'Bars', 'Galleries', 'Hotels_and_Restaurants', 'Monuments', 'Museums', 'Parks_and_Lakes',
        'Places_of_Worship', 'Shopping_and_bazaar', 'Street_food','Wildlife']
    mypath = dir_path + '/Final Models'
    for i in range(10):
        cluster_dict[i] = {}
        pickle_files.sort()
        for j in range(11):
            cluster_dict[i][features[j]] = pickle_files[j]
            
    rating = []
    sorted_rates = []
    response = {}
    r = 0
    z = 0
    response['Info'] = np.zeros(sum(user_input)).tolist()
    original_data = pd.read_csv('/home/hana/flaskvue2/backend/integration/Original data.csv')
    csv_path = '/home/hana/flaskvue2/backend/integration/places_data/unique_place_ids.csv'
    df = pd.read_csv(csv_path)
    for i in range(len(user_input)):
        if user_input[i] == 1:
            rating = []
            unique_id = df.iloc[:,i].dropna().values
            algo = pickle.load(open(pickle_path + cluster_dict[cluster_id[0]][features[i]],'rb'))
            for j in unique_id:
                rating.append(algo.predict(user_id,j))
            sorted_rates += sorted(rating, key=lambda x: x[3],reverse=True)[0:3]
            p = sorted_rates[z][1]
            q = sorted_rates[z+1][1]
            k = sorted_rates[z+2][1]
            response['Info'][r]= {
            'Feature' : features[i],
            'Data' : [
                {
                    'Place' : original_data[original_data['ID']==p]['NAME'].tolist()[0],
                    'LatLng' : { 'lat' : original_data[original_data['ID']==p]['LAT'].tolist()[0],
                                 'lng' : original_data[original_data['ID']==p]['LNG'].tolist()[0]
                                }
                },
                {
                    'Place' : original_data[original_data['ID']==q]['NAME'].tolist()[0],
                    'LatLng' : { 'lat' : original_data[original_data['ID']==q]['LAT'].tolist()[0],
                                 'lng' : original_data[original_data['ID']==q]['LNG'].tolist()[0]
                                }
                },
                {
                    'Place' : original_data[original_data['ID']==k]['NAME'].tolist()[0],
                    'LatLng' : { 'lat' : original_data[original_data['ID']==k]['LAT'].tolist()[0],
                                 'lng' : original_data[original_data['ID']==k]['LNG'].tolist()[0]
                                }
                }
            ]
            }
            r = r + 1
            z = z + 3
    print(response)
    
return_dictionary(12342,[1,0,0,0,0,0,0,0,0,0,1])
