import requests
import json as js
import models.dao as dao
import urlglobals as url

_url = "0"
_header = ""


def get_total_objects(jsonObject):
    meta = jsonObject["meta"]
    count = meta["count"]
    return count


def getproducts(url_products):

    print(url_products, url.header_MM_Produtos)
    listaprodutos = requests.get(url_products, headers=url.header_MM_Produtos)
    print(listaprodutos)
    r2d = js.dumps(listaprodutos.json())
    json_obj = js.loads(r2d)

    total = int(get_total_objects(json_obj))
    print("Total de Produtos ", total)
    counter = 0

    for data in json_obj["data"]:
        counter += 1
        print('--- line 2', counter)
        id_produto = int(data["id_produto"])
        id_categoria = int(data["id_categoria"])
        id_nivel_1 = int(data["id_nivel_1"])
        id_nivel_2 = int(data["id_nivel_2"])
        id_nivel_3 = int(data["id_nivel_3"])
        id_nivel_4 = int(data["id_nivel_4"])
        id_nivel_5 = int(data["id_nivel_5"])
        id_nivel_6 = int(data["id_nivel_6"])
        id_nivel_7 = int(data["id_nivel_7"])
        nome = str(data["nome"]).encode('latin-1', 'ignore')
        descricao = "null"
        ean = data["ean"]
        marca = data["marca"]
        preco_de = data["preco_de"]
        preco_por = data["preco_por"]
        altura = data["altura"]
        largura = data["largura"]
        profundidade = data["profundidade"]
        peso = data["peso"]
        status = data["status"]
        datahora_criacao = data["datahora_criacao"]
        datahora_alteracao = data["datahora_alteracao"]

        dao.insert_products(id_produto, id_categoria, id_nivel_1, id_nivel_2, id_nivel_3,
                            id_nivel_4, id_nivel_5, id_nivel_6, id_nivel_7, nome, descricao,
                            ean, marca, preco_de, preco_por, altura, largura, profundidade,
                            peso, status, datahora_criacao, datahora_alteracao)

        for dtl in data["slug"]:
            print("SLUG:", str(dtl))
            idlistagemurl = dtl["idlistagemurl"]
            url_listagem = dtl["url_listagem"]
            fornecedor_id = dtl["fornecedor_id"]
            categoria_id = dtl["categoria_id"]
            departamento_id = dtl["departamento_id"]
            tipo_url = dtl["tipo_url"]
            nome_amigavel = dtl["nome_amigavel"]
            ordem = dtl["ordem"]
            breadcrumb = "null"
            top_menu = dtl["top_menu"]
            id_depdep = dtl["id_depdep"]
            departamento = dtl["departamento"]
            departamento_slug = dtl["departamento_slug"]
            id_depdep_pai = dtl["id_depdep_pai"]
            google_product_category = "null"

            dao.insert_slug(id_produto, idlistagemurl, url_listagem, fornecedor_id,
                            departamento_id, tipo_url, nome_amigavel, ordem, breadcrumb, top_menu,
                            id_depdep, departamento, departamento_slug, id_depdep_pai,
                            google_product_category, categoria_id)
            #print(str(dtl["buyBox"]))
            for dtbuybox in data["buyBox"]:
                print(len(dtbuybox))
                #print("buybox:", dtbuybox[buyBox]["id_seller"])
                #id_seller = dtbuybox["id_seller"]
                #preco_de = dtbuybox["preco_de"]
                #print(id_seller, preco_de)
        print('---------------------------- ')
    return total

def GetAllTotalSellers():
    c = 0
    url404 = 0
    err = []
    ok = []
    id = []
    while c < 3000:
        c += 1
        r = requests.get(url.url_MM_Api_Id_Seller + str(c), headers=url.header_MM_id_Seller)
        if r.status_code > 200:

            err.append(r.url)
            url404 += 1
            print(url404, "line", c, "url", r.url)
            if url404 > 5:
                # \limit not found page request
                break
        else:
            ok.append(r.url)
            id.append(c)
            url404 = 0

            # PARSING JSON SELLER TO DATABASE
            jsondump = js.dumps(r.json())
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
                # logo = str(data["logo"])
                # descricao = re.sub("[\\%/#$@&]"), '_', data["descricao"]
                # z=re.sub("a-z","","adasdasdsad")
                # print(z)
                slug = data["slug"]
                id_merchant = data["id_merchant"]
                dia_fechamento_ciclo = data["dia_fechamento_ciclo"]
                dias_liberacao_saldo = data["dias_liberacao_saldo"]
                dias_pagamento_repasse = data["dias_pagamento_repasse"]
                ind_permite_sem_ean = data["ind_permite_sem_ean"]
                rating = 0
                dao.InsertSeller(id_seller, token, nome, datahora_criacao, datahora_alteracao, pesquisa_satisfacao,
                                 status, slug, id_merchant, dia_fechamento_ciclo, dias_liberacao_saldo,
                                 dias_pagamento_repasse, ind_permite_sem_ean, rating)

    return (ok, id, err)


def getComissaoFromSeller(sellers):
    ## update COMISSAO SELLERS

    idSeller = sellers[1]
    input("debug")
    for id in idSeller:

        dataSeller = requests.get(url.url_MM_Api_Comissao + str(id), headers=url.header_MM_Comissao)
        jsd = js.dumps(dataSeller.json())
        json_obj = js.loads(jsd)

        ctrJson = 0

        for data in json_obj["data"]:
            if int(data["id_seller"]) > 25:
                ctrJson += 1
                id_comissao = int(data["id_comissao"])
                id_seller = int(data["id_seller"])
                id_categoria = int(data["id_categoria"])
                comissionamento = round(float(data["comissionamento"]), 2)
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
        ## dao.insertNivel(id_nivel_1, id_nivel_2, id_nivel_3, id_nivel_4, id_nivel_5, id_nivel_6, id_nivel_7)

        # cursor.executemany(sqlInsertSellerQuery)
