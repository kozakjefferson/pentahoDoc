import models.mysqlconnection as mysql


def InsertSeller(id_seller, token, nome,datahora_criacao,datahora_alteracao,pesquisa_satisfacao, status,slug,id_merchant,dia_fechamento_ciclo,dias_liberacao_saldo,dias_pagamento_repasse,ind_permite_sem_ean,rating):
    conm = mysql.openConMysql()
    print(id_seller)
    sqlInsertSellerQuery = '''INSERT INTO cubo.WM_SELLER(ID_SELLER,TOKEN,NOME,DATA_CRIACAO,DATA_ALTERACAO,PESQUISA_SATISFACAO,STATUS,SLUG,ID_MERCHANT,DIA_FECHAMENTO_CICLO,DIAS_LIBERACAO_SALDO,DIAS_PAGAMENTO_REPASSE,IND_PERMITE_SEM_AEN ,AVG_RATING)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur = conm.cursor()

    cur.execute(sqlInsertSellerQuery, (int(id_seller), token, str(nome), datahora_criacao, datahora_alteracao, pesquisa_satisfacao, status, slug,id_merchant, dia_fechamento_ciclo, dias_liberacao_saldo,dias_pagamento_repasse,ind_permite_sem_ean, rating))
    conm.commit()

    conm.close()


def InsertComissaoSeller(id_comissao, id_seller, id_categoria, comissionamento, id_nivel_1, id_nivel_2, id_nivel_3, id_nivel_4, id_nivel_5, id_nivel_6, id_nivel_7):
    conm = mysql.openConMysql()
    sqlInsertComissaoSellerQuery = '''
    INSERT INTO cubo.WM_COMISSAO
    (ID_COMISSAO, ID_SELLER, ID_CATEGORIA, COMISSIONAMENTO, ID_NIVEL_1, ID_NIVEL_2, ID_NIVEL_3, ID_NIVEL_4, ID_NIVEL_5, ID_NIVEL_6, ID_NIVEL_7)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur = conm.cursor()
    cur.execute(sqlInsertComissaoSellerQuery, (int(id_comissao), int(id_seller), int(id_categoria), float(comissionamento), int(id_nivel_1), int(id_nivel_2), int(id_nivel_3), int(id_nivel_4), int(id_nivel_5), int(id_nivel_6), int(id_nivel_7)))
    conm.commit()
    conm.close()

def insertNivel():
    conm = mysql.openConMysql()
    sqlInsertComissaoSellerQuery = '''
        INSERT INTO cubo.WM_NIVEL
        (ID,NIVEL, ID_CATEGORIA, COMISSIONAMENTO, ID_NIVEL_1, ID_NIVEL_2, ID_NIVEL_3, ID_NIVEL_4, ID_NIVEL_5, ID_NIVEL_6, ID_NIVEL_7)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur = conm.cursor()
    cur.execute(sqlInsertComissaoSellerQuery, (
    int(id_comissao), int(id_seller), int(id_categoria), float(comissionamento), int(id_nivel_1), int(id_nivel_2),
    int(id_nivel_3), int(id_nivel_4), int(id_nivel_5), int(id_nivel_6), int(id_nivel_7)))
    conm.commit()
    conm.close()

if(__name__== "__main__"):
    InsertComissaoSeller()
    InsertSeller()