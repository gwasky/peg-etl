import json
data={}
with open("es.txt","r") as f, open('output.txt', 'w+') as output:
    for line in f:
       sp=line.split('|~')
       data.setdefault("data",[]).append(
            {"TRANSACTION_DATE": sp[0],
            "TRANSNUMBER": sp[1],
            "TRNTYPE": sp[2],
            "MEMO": sp[3],
            "SRC_DEVICENUMBER": sp[4],
            "TGT_DEVICENUMBER": sp[5],
            "STATUS": sp[6],
            "GROSS_AMOUNT": sp[7],
            "FEE_AMOUNT": sp[8],
            "SRC_ENDBALANCE": sp[9],
            "TGT_ENDBALANCE": sp[10],})
    json.dump(data,output)
#print(data)