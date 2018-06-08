import requests
import json as js
import models.dao as dao
import urlglobals as url
import time
import settings

today = time.strftime("%Y-%m-%d")
data_inicio = '2016-01-01'
limit_busca_default = settings.PARAM_API_DEFAULT["limit"]

_step = 0
_offset = settings.PARAM_API_DEFAULT["ofsset"]
_vezes = 0
_mod = 0
_total = 0
_full=0

##pegar total de pedido generico


def check_diff_limit_busca(limit, total_itens):
    seq_total=0
    mod_total = total_itens % limit
    full= total_itens-mod_total
    if (total_itens < limit):
        limit_busca = total_itens
        seq_total = 1
    else:
        limit_busca = limit
        seq_total = round(total_itens/limit)
    print("limit busca: ", limit_busca, "mod: ", mod_total, "seq_total: ",seq_total,"total:",total_itens, "full:",full)
    input("222")
    return limit_busca, mod_total, seq_total, total_itens, full

def dump_list_to_json(lista):
    print(lista)
    r2d = js.dumps(lista.json())
    json_obj = js.loads(r2d)
    return json_obj


def get_total_objects(url1, tipo_consulta):
    # pega total de item desde inicio do por tipo de consulta
    url_formated = url.setParamBusca(url1, data_inicio, today)
    print("======ok", url_formated)
    listaprodutos = requests.get(url_formated, headers=url.header_mm)
    r2d = js.dumps(listaprodutos.json())
    json_obj = js.loads(r2d)
    meta = json_obj["meta"]
    return check_diff_limit_busca(limit=limit_busca_default, total_itens=int(meta["count"]))


def get_pedidos_wm():
     tipo_consulta = "pedido"
     print(tipo_consulta)
     url_pedidos = url.wm_api_pedidos

     _limit, _mod, _vezes, _total , _full= get_total_objects(url_pedidos, tipo_consulta)

     print("Total de pedidos wm ", _total)
     counter = 0

     if _vezes==1:
         _step = 1
         _total=1

     else:
         _step = _limit

     for listas in range(0,_total,_step):

        print("offset:",listas,"total:", _total,"step: ",_step,"mod" ,_mod)
        if (listas==_full):
            listas == _mod

        url_formated = url.setParamBusca(url_pedidos, dataInicio=data_inicio,dataFim=today,limit=_limit,offset=listas)
        print(url_formated)
        input("333")
        listapedidos = requests.get(url_formated, headers=url.header_mm)
        json_obj = dump_list_to_json(listapedidos)

        for data in json_obj["data"]:
            counter+=1
            print('--- line{} from {}'.format(counter, _total))
            id_pedido = data["id_pedido"]
            id_seller = data["id_seller"]
            pedido_wd = data["pedido_wd"]
            comissao = data["comissao"]
            data_criacao = data["data_criacao"]
            datahora_aprovacao = data["datahora_aprovacao"]
            ultima_atualizacao = data["ultima_atualizacao"]
            status = data["status"]

            uf_comprador = "null"
            cep_comprador = "null"
            uf_entrega = "null"
            cep_entrega = "null"
            nome = "null"
            tipo_pessoa = "null"

            entrega = data["entrega"]
            subtotal = data["subtotal"]
            frete = data["frete"]
            total = data["total"]

            tipo_pagagemto_1 = "null"
            tipo_pagamento_2 = "null"
            faturamento = data["faturamento"]
            envio = data["envio"]

            datahora_confirmacao = " "
            datahora_cancelamento = "null"
            datahora_faturamento = "null"

            data_previsao_entrega = data["data_previsao_entrega"]
            datahora_entrega = "null"
            pedido_mm = data["pedido_mm"]
            id_lancamento_financeiro = data["id_lancamento_financeiro"]
            print(id_pedido,id_seller,pedido_wd,comissao,data_criacao,datahora_aprovacao, ultima_atualizacao,status,uf_comprador,cep_comprador,uf_entrega,cep_entrega,
                  nome,tipo_pessoa,entrega,subtotal,frete,total,tipo_pagagemto_1, tipo_pagamento_2,faturamento, envio, datahora_confirmacao,datahora_cancelamento, datahora_faturamento,
                  datahora_entrega,pedido_mm,id_lancamento_financeiro)
            dao.insert_pedidos(id_pedido,id_seller,pedido_wd,comissao,subtotal,frete,total,pedido_mm)



def set_produtos_wm():
    tipo_consulta = "produto"
    print(tipo_consulta)
    url_produtos = url.url_wm_api_produtos

    _limit, _mod, _vezes, _total , _full= get_total_objects(url_produtos, tipo_consulta)

    print("Total de Produtos ", _total)
    counter = 0

    if _vezes==1:
        _step = 1
        _total+=1
    else:
        _step = _limit

    for listas in range(1,_total,_step):

        print("offset:",listas,"total:", _total,"step: ",_step,"mod" ,_mod)
        if (listas==_full):
            listas == _mod

        url_formated = url.setParamBusca(url_produtos, dataInicio=data_inicio,dataFim=today,limit=_limit,offset=listas)
        listaprodutos = requests.get(url_formated, headers=url.header_mm)
        json_obj = dump_list_to_json(listaprodutos)

        for data in json_obj["data"]:
             counter += 1
             print('--- line{} from {}'.format(counter,_total))
             id_produto = int(data["id_produto"])
             print(id_produto)
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

    #         # dao.insert_products(id_produto, id_categoria, id_nivel_1, id_nivel_2, id_nivel_3,
    #         #                     id_nivel_4, id_nivel_5, id_nivel_6, id_nivel_7, nome, descricao,
    #         #                     ean, marca, preco_de, preco_por, altura, largura, profundidade,
    #         #                     peso, status, datahora_criacao, datahora_alteracao)
    #
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

    #             # dao.insert_slug(id_produto, idlistagemurl, url_listagem, fornecedor_id,
    #             #                 departamento_id, tipo_url, nome_amigavel, ordem, breadcrumb, top_menu,
    #             #                 id_depdep, departamento, departamento_slug, id_depdep_pai,
    #             #                 google_product_category, categoria_id)
    #             # print(str(dtl["buyBox"]))
                 for dtbuybox in data["buyBox"]:
                     print(len(dtbuybox))
                     # print("buybox:", dtbuybox[buyBox]["id_seller"])
                     # id_seller = dtbuybox["id_seller"]
                     # preco_de = dtbuybox["preco_de"]
                     # print(id_seller, preco_de)
             print('---------------------------- ')
    return _total


def GetAllTotalSellers():
    c = 0
    url404 = 0
    err = []
    ok = []
    id = []
    while c < 3000:
        c += 1
        r = requests.get(url.url_MM_Api_Id_Seller + str(c), headers=url.header_mm)
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

        dataSeller = requests.get(url.url_MM_Api_Comissao + str(id), headers=url.header_mm)
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
