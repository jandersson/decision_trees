__author__ = 'jonas'

import monkdata as m
import dtree

if __name__ == "__main__":

    data = {
        'monk1': {
            'name': 'MONK-1',
            'data': m.monk1,
            'entropy': 'NA'
        },
        'monk2': {
            'name': "MONK-2",
            'data': m.monk2,
            'entropy': 'NA'
        },
        'monk3': {
            'name': 'MONK-3',
            'data': m.monk3,
            'entropy': 'NA'
        }
    }
    for set in data:
        data[set]['entropy'] = dtree.entropy(data[set]['data'])
        print(data[set]['name'] + " entropy: ", data[set]['entropy'])