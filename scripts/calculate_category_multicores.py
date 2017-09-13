from multiprocessing import Pool
from pymongo import MongoClient
from gensim.models import Word2Vec
import time
model = Word2Vec.load('word2vector3.model')
client = MongoClient('127.0.0.1',27017)
db = client.intbee_match
my_category= db.category
my_similarity = db.category_similarity1

def get_data():
    
    data = list(my_category.find({},{'one':1,'two':1,'three':1,'similar':1,'two_id':1,'category_id':1,"_id":0}))
    return data
    
def calculate_category_similarity(b):
      similarity_tag=[]
      for w in str(b['similar']).split(" "):
        if w in model:
            similarity_tag.append(w)
      for i in my_category.find({},{'one':1,'two':1,'three':1,'similar':1,'two_id':1,'category_id':1,"_id":0}):
           similarity_with_tag=[]
           for w in str(i['similar']).split(" "):
               if w in model:
                   similarity_with_tag.append(w)
           #print(similarity_tag,similarity_with_tag)
           score=(model.n_similarity(similarity_tag,similarity_with_tag))
           if(my_similarity.find({"category_id": b['category_id'],"category_with_id": i['category_id']}).count()<1):  
               my_similarity.insert_one({"one": b['one'],"two": b['two'],"name": b['three'],"with_name": i['three'],\
               "category_id": b['category_id'],"category_with_id": i['category_id'],"similarity": score})
           else:
               pass
    
    
def multi_pro():
    pool = Pool(2)
    mongo_data = get_data()
    for data in mongo_data:
        pool.apply_async(calculate_category_similarity, (data,))
    pool.close()
    pool.join()
if __name__ =='__main__':
     t0 = time.time()
     multi_pro()
     print("Run Time Costs"+str(time.time()-t0))