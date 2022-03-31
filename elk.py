from operator import index
from elasticsearch import Elasticsearch


es = Elasticsearch()
es.info()
print(es.info())