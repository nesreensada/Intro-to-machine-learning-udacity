#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print sum([enron_data[data]["poi"] for data in enron_data ])
#print enron_data["PRENTICE JAMES"]
print sum([1 for data in enron_data if enron_data[data]['total_payments']!='NaN']), 'poi total_payments'
#print sum([1 for data in enron_data if enron_data[data]['salary']!='NaN']), 'salary'
#print enron_data[enron_data.keys()[0]]
print len(enron_data)
print sum([1 for data in enron_data if enron_data[data]['total_payments']=='NaN'])/float(len(enron_data))