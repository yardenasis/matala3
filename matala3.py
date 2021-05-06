file=open("WhatsApp.txt",encoding='utf8')
def BD_WHATSAPP (file):
    import json
    lst = []
    dictionary = dict()
    dict_id = 0
    for line in file:
            flag = None
            try:
                if ("הוסיף/ה" in line or "<נכללה" in line
                        or "מקצה-לקצה" in line or "נוצרה" in line):
                    continue
                notice = dict()
                index_date = line.index('-')
                date = line[0: index_date]
                num_phone = line[ index_date + 1:line.index(':',  index_date)]
                text = line[line.index(':',  index_date) + 1:]
                for key, value in dictionary.items():
                    if value ==  num_phone:
                        flag = key
                if flag is not None:
                    phone = flag
                else:
                    dictionary[dict_id] = num_phone
                    num_phone= dict_id
                    dict_id += 1
                notice['datetime'] = date
                notice['id'] =  num_phone
                notice['text'] = text
                lst.append(notice)
            except:
                lst[-1]['text'] += line
    
    
    file=open("WhatsApp.txt",encoding='utf8')       
    for line in file:
        try:
            if not  "נוצרה"  in line:
                continue
            
            metadata = dict()
            chatname_place = line.split('"')
            chatname=chatname_place[1]
            metadata["chat_name"] = chatname
            creationdate = line.split('-')
            metadata["creation_date"]=creationdate[0]
            creator = line.split()
            metadata["creator"]=line[65:81]
        except:
            continue
    all_information = dict()
    all_information["notice"] = lst 
    
    all_information["metadata"] = metadata
    BD_json = chatname+".txt"
    outputfile = open(BD_json , 'w', encoding='utf8')
    outputfile.write(json.dumps(all_information, indent=4, ensure_ascii=False))
    outputfile.close()
    
    return(all_information)

BD_WHATSAPP(file)
