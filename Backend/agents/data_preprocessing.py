import pandas as pd 
#loading the data from the csv file
data = pd.read_csv('/home/ahmed/Desktop/AI-Agent-DeepMind/Backend/agents/data.csv')
data.head()

#dropping all rows that doesnt have description
train_better = data[data["descriptions"]!= "This edition doesn't have a description yet. Can you add one?"]
train_better.isnull().sum()

#dropping all rows that have NaN values
train_dropNaN = train_better.dropna(axis=0, how="any")
train_dropNaN.info()

#dropping the columns that are not needed
train_dropNaN = train_dropNaN.drop(columns = ['title_id', 'author_id', 'cover_url'])

#combining all the text columns into one for embedding
train_dropNaN["text"] = "title : " + train_dropNaN["title"] + " - " + "author : " + train_dropNaN["author"] + "category : " + train_dropNaN["category"] + "description : " + train_dropNaN["descriptions"]
train_dropNaN.head()

train_dropNaN.to_csv('data_cleaned.csv', index=False)