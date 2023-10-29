"""
NOTE FOR GITHUB:
I am not able to include files or information referencing app user data and, as such, will be including the tag <fake> to all filenames, including user data
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

def h_termcount(question, term):
    #helper -- count occurrences of a term in a string
    return question.lower().count(term)

def q1(apologetic_terms):
    #objective: link apologetic language with a type of question 
    directory = '<fake>_output'

    #itterate over clusters of questions
    for filename in os.listdir(directory):
        #count rate of apologetic talk
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            df = pd.read_csv(f)
            print(f'begin {filename}:')
            #itterate over terms, questions
            for term in apologetic_terms:
                df[term] = df['question'].apply(lambda x: h_termcount(x, term))
            
            word_counts = {term: df[term].sum() for term in apologetic_terms}
            #display count on 
            for term, count in word_counts.items():
                print(f"{term}: {count}")

    return

def h_join(base,cols):
    #helper -- add more raw data to a cluster
    data_path = '<fake>questions_extract/questions_extract_2023-09-07.csv'
    add = pd.read_csv(data_path)
    base.set_index('question')
    base = base.join(add.set_index('question'), on='question')
    return base[cols]
    
def q2():
    #which question categories are being asked about during what part of the day?
    directory = '<fake>_output/'

    #itterate over clusters of questions
    hour = []
    for filename in os.listdir(directory):
        #concatinate the hour the post was created
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            df = pd.read_csv(f)
            df = h_join(df,['question','createdAt'])
            #save median hour of asked questions
            df['createdAt'] = pd.to_numeric(df['createdAt'].str[11:13])
            hour.append(df['createdAt'].median())
    #bar graph X=hours Y=number of clusters 
    df = pd.DataFrame(hour, columns=['hour'])     
    df['hour'] = df['hour'].astype(int)
    df['hour'].value_counts().sort_index().plot(title='Questions Asked by Catagory: Average Question Hour of the Day',xlabel='Average Hour of Question Asked',ylabel='Num Catagories',kind='bar')
    plt.show()

    


"""
Use instructions:
Uncomment lines below
q1 = term search across clusters 
q2 = average questions ask time per cluster
"""
#q1(['sorry', 'embarrassing', 'awkward', 'dumb question'])
#q1(['doctor', 'pediatrician', 'hospital'])
#q2()
