from google.cloud import storage
from controller import read_from_storage
from controller import read_from_firestore
import os
# x = read_from_storage.read_file()
# # print(x[0])
# print(x)

x = read_from_firestore.read_file()
# print(x[1][5][0],x[1][5][1])
print(x)