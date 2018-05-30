import requests
import json as js
import urlglobals as url
import models.model_util as utils
import models.mysqlconnection as mysql

BULK_INSERT_SIZE = 90

def getDataFromSeller(sellers):
    idSeller=sellers[1]
    print(idSeller)
    input("debug")
    for id in idSeller:
        dataSeller = requests.get("https://war-machine.madeiramadeira.com.br/v1/comissao/{}".format(int(id)),
                 headers={"Cache-Control": "no-cache", "Pentaho-Token": "d2d47b0b-cfda-4154-a1e2-b8020f6d500e",
                          "TOKENMM": "TOKEN_MM_123"})
        js1 = dataSeller.json()
        jsd = js.dumps(dataSeller.json())
        id = js.dumps("id_seller")
        json_obj = js.loads(jsd)

        ctrJson = 0
        for data in json_obj["data"]:
            ctrJson += 1
            #cursor.executemany(sqlInsertSellerQuery)
            print('--- line', ctrJson)
            print("id_seller:", data["id_seller"])
            print("id_categoria:", data["id_categoria"])
            print("id_comissao:", data["id_comissao"])
            print("comissionamento", data["comissionamento"])
            print("nivel_1", data["nivel_1"])
            print("nivel_2", data["nivel_2"])
            print('---------------------------- ')

def InsertSeller(param):
    sqlInsertSellerQuery = '''INSERT INTO cubo.WM_SELLER
    (ID_SELLER, TOKEN, NOME, DATA_CRIACAO, DATA_ALTERACAO, 
    PESQUISA_SATISFACAO, STATUS, LOGO, descricao, SLUG,
    ID_MERCHANT, DIA_FECHAMENTO_CICLO, DIAS_LIBERACAO_SALDO, 
    DIAS_PAGAMENTO_REPASSE, IND_PERMITE_SEM_AEN, AVG_RATING)
    VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});'''.format(param)

#sellersOk = utils.GetAllTotalSellers(url._url_MM_Api_Seller, url._header_MM_Seller)
#getDataFromSeller(sellersOk)
url.setParamBuscaProdutos("2016-01-01", "2018-01-01")
produtos = utils.getproducts(url._url_MM_Api, url._header_MM_Produtos)


