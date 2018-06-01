import requests
import json as js
import models.dao as dao
import urlglobals as url

_url="0"
_header=""

def getproducts():
    listaprodutos = requests.get(url._url_MM_Api, headers=url._header_MM_Produtos)
    r2d = js.dumps(listaprodutos.json())
    json_obj = js.loads(r2d)

    counter = 0
    for data in json_obj["data"]:
        counter += 1
        print('--- line 2', counter)
        print("id_produto:", data["id_produto"])
        print("id_produto_match:", data["id_produto_match"])
        print("id_categoria:", data["id_categoria"])
        print("id_nivel_1", data["nivel_1"])
        print("nivel_1", data["nivel_1"])
        print("id_nivel_2", data["id_nivel_2"])
        print('---------------------------- ')


def GetAllTotalSellers():
    c = 0
    url404 = 0
    err = []
    ok = []
    id = []
    while c < 3000:
        c += 1
        r = requests.get(url._url_MM_Api_Id_Seller +str(c), headers=url._header_MM_id_Seller)
        if r.status_code > 200:
            err.append(r.url)
            url404 += 1
            print(url404, "line", c, "url", r.url)
            if url404 > 5:
                #\limit not found page request
                break
        else:
            ok.append(r.url)
            id.append(c)
            url404 = 0

            #PARSING JSON SELLER TO DATABASE
            jsondump=js.dumps(r.json())
            json_obj = js.loads(jsondump)

            for data in json_obj["data"]:

                id_seller = int(data["id_seller"])
                token = str(data["token"]).replace(' ', '_')
                slug = str(data["slug"]).replace(' ', '_')
                nome = slug
                datahora_criacao = str(data["datahora_criacao"])
                datahora_alteracao = data["datahora_alteracao"]
                pesquisa_satisfacao = str(data["pesquisa_satisfacao"])
                status = str(data["status"])
                #logo = str(data["logo"])
                #descricao = re.sub("[\\%/#$@&]"), '_', data["descricao"]
                #z=re.sub("a-z","","adasdasdsad")
                #print(z)
                slug = data["slug"]
                id_merchant = data["id_merchant"]
                dia_fechamento_ciclo = data["dia_fechamento_ciclo"]
                dias_liberacao_saldo = data["dias_liberacao_saldo"]
                dias_pagamento_repasse = data["dias_pagamento_repasse"]
                ind_permite_sem_ean = data["ind_permite_sem_ean"]
                rating = 0
                dao.InsertSeller(id_seller, token, nome,datahora_criacao,datahora_alteracao, pesquisa_satisfacao, status, slug, id_merchant, dia_fechamento_ciclo,dias_liberacao_saldo,dias_pagamento_repasse,ind_permite_sem_ean,rating)

    return (ok,id,err)


def getComissaoFromSeller(sellers):
    ## update COMISSAO SELLERS

    idSeller=sellers[1]
    input("debug")
    for id in idSeller:

        dataSeller = requests.get(url._url_MM_Api_Comissao+str(id), headers = url._header_MM_Comissao)
        js1 = dataSeller.json()
        jsd = js.dumps(dataSeller.json())
        id = js.dumps("id_seller")
        json_obj = js.loads(jsd)
        print("============ debug1")
        ctrJson = 0
        for data in json_obj["data"]:
            ctrJson += 1
            id_comissao = int(data["id_comissao"])
            id_seller = int(data["id_seller"])
            id_categoria = int(data["id_categoria"])
            comissionamento = float(data["comissionamento"])
            id_nivel_1 = int(data["id_nivel_1"])
            id_nivel_2 = int(data["id_nivel_2"])
            id_nivel_3 = int(data["id_nivel_3"])
            id_nivel_4 = int(data["id_nivel_4"])
            id_nivel_5 = int(data["id_nivel_5"])
            id_nivel_6 = int(data["id_nivel_6"])
            id_nivel_7 = int(data["id_nivel_7"])
            nivel_7 = data["id_nivel_1"]
            nivel_7 = data["id_nivel_2"]
            nivel_7 = data["id_nivel_3"]
            nivel_7 = data["id_nivel_4"]
            nivel_7 = data["id_nivel_5"]
            nivel_7 = data["id_nivel_6"]
            nivel_7 = data["id_nivel_7"]

            dao.InsertComissaoSeller(id_comissao, id_seller, id_categoria, comissionamento, id_nivel_1, id_nivel_2,
                                     id_nivel_3, id_nivel_4, id_nivel_5, id_nivel_6, id_nivel_7)
            dao.insertNivel(id_nivel_1, id_nivel_2, id_nivel_3, id_nivel_4, id_nivel_5, id_nivel_6, id_nivel_7)

            #cursor.executemany(sqlInsertSellerQuery)



