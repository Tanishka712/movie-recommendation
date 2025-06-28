#%%
import pandas as pd

data=pd.read_csv('data/dataset.csv')
data
# %%
data.describe()
# %%
data.info()
# %%
data.columns
# %%
data= data[['id','title','overview','genre']]
# %%
data['tags']= data['overview']+data['genre']
newdata= data.drop(columns=['overview','genre'])
newdata
# %%
from sklearn.feature_extraction.text import CountVectorizer
# %%
cv=CountVectorizer(max_features=10000, stop_words= 'english')
# %%
vector=cv.fit_transform(newdata['tags'].values.astype("U")).toarray()
# %%
vector.shape
# %%
from sklearn.metrics.pairwise import cosine_similarity
similarity= cosine_similarity(vector)
# %%
similarity


# %%
newdata=pd.DataFrame(newdata)
newdata.info()
# %%
index=newdata[newdata['title']=="The Godfather"].index[0]
# %%
print(index)

# %%
distance=sorted(list(enumerate(similarity[2])), reverse=True, key=lambda vector:vector[1])
for i in distance[0:5]:
    print(newdata.iloc[i[0]].title)
# %%
def recommend (movies):
    index=newdata[newdata['title']==movies].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    for i in distance[0:5]:
        print(newdata.iloc[i[0]].title)
# %%
recommend("Iron Man")
# %%
import pickle
pickle.dump(newdata,open('movies_list.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))
# %%
