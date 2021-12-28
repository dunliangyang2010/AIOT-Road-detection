from google.cloud import storage
import os


def read_file():

    client = storage.Client()
    bucket = client.bucket('road-project-picture')
    blobs = bucket.list_blobs(prefix='U3dfebbd05927687e3e912e2d98f6905e/corrdinate')

    infos = []
    bdata = []
    for blob in blobs:
        infos.append(blob)

        for info in infos:
            data = []
            with info.open("rt") as f:
                for i in f.read().split('\n'):
                    data.append(i)
                    # data.append("dash") #以後作為分割用
                    data = list(filter(None, data)) # 去掉最後的空值
            bdata.append(data)
    tdata=[ bdata[0],bdata[1],bdata[3] ]
    return(tdata)
