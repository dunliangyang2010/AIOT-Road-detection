from google.cloud import firestore
import json
# 待加入storage imgurl

def read_file():
    num = 0
    data = []

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
            # 若要呈現在網頁,經緯度不須太精準,取到第3位還要記得補0
            # lat = str(round(float(csys.split(',')[0]),3))
            # lng = str(round(float(csys.split(',')[1]),3))
            # csys = lat+' , '+lng
            
            # 若資料要供Map API使用,則需要取精準位數
            lat = csys.split(',')[0]
            lng = csys.split(',')[1]
            csys = [lat,lng]

        num += 1
        data.append( [str(num), date, time, address, count, csys] )

    # # to json
    # data = json.dumps(data, ensure_ascii=False)
    return data
