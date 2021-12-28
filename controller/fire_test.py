from google.cloud import firestore
import json
# 待加入storage imgurl

num = 0
db = firestore.Client()
doc_ref = db.collection(u'pothole') # get colletion
doc = doc_ref.stream() # get key id & value
for d in doc:
    # print(f'{d.id} => {d.to_dict()}')
    # print(d.to_dict().get('count'))

    # date
    date = d.to_dict().get('date_time')
    if date is not None:
        date = date.split('_')[0] # yyyymmdd
        date = [date[0:4], date[4:6], date[6:]]
        date = '/'.join(date) 
               
    # time
    time = d.to_dict().get('date_time')
    if time is not None:
        time = time.split('_')[1]
    
    # address
    address = d.to_dict().get('address')

    # count
    count = d.to_dict().get('count')

    # coordinate
    csys = d.to_dict().get('lat,lng')
    if csys is not None:
        lat = str(round(float(csys.split(',')[0]),3))
        lng = str(round(float(csys.split(',')[1]),3))
        csys = lat+' , '+lng
    num += 1
    data = [str(num), date, time, address, count, csys]

    print(data)
    