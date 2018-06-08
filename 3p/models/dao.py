import models.mysqlconnection as mysql
import pymysql.cursors
import time

format = '%Y-%m-%d'


def InsertSeller(id_seller, token, nome, datahora_criacao, datahora_alteracao, pesquisa_satisfacao, status, slug,
                 id_merchant, dia_fechamento_ciclo, dias_liberacao_saldo, dias_pagamento_repasse, ind_permite_sem_ean,
                 rating):
    conm = mysql.openConMysqlHome()
    print(id_seller)
    sqlInsertSellerQuery = '''INSERT INTO cubo.WM_SELLER(ID_SELLER,TOKEN,NOME,DATA_CRIACAO,DATA_ALTERACAO,PESQUISA_SATISFACAO,STATUS,SLUG,ID_MERCHANT,DIA_FECHAMENTO_CICLO,DIAS_LIBERACAO_SALDO,DIAS_PAGAMENTO_REPASSE,IND_PERMITE_SEM_AEN ,AVG_RATING)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur = conm.cursor()
    try:
        cur.execute(sqlInsertSellerQuery, (
            int(id_seller), token, str(nome), datahora_criacao, datahora_alteracao, pesquisa_satisfacao, status, slug,
            id_merchant, dia_fechamento_ciclo, dias_liberacao_saldo, dias_pagamento_repasse, ind_permite_sem_ean, rating))
        conm.commit()
    except:
        print("Error: unable to fecth data:", id_seller)
        conm.close()


def InsertComissaoSeller(id_comissao, id_seller, id_categoria, comissionamento, id_nivel_1, id_nivel_2, id_nivel_3,
                         id_nivel_4, id_nivel_5, id_nivel_6, id_nivel_7):
    conm = mysql.openConMysqlHome()
    sqlInsertComissaoSellerQuery = '''
    INSERT INTO cubo.WM_COMISSAO
    (ID_COMISSAO, ID_SELLER, ID_CATEGORIA, COMISSIONAMENTO, ID_NIVEL_1, ID_NIVEL_2, ID_NIVEL_3, ID_NIVEL_4, ID_NIVEL_5, ID_NIVEL_6, ID_NIVEL_7)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur = conm.cursor()
    try:
        cur.execute(sqlInsertComissaoSellerQuery, (
            int(id_comissao), int(id_seller), int(id_categoria), comissionamento, int(id_nivel_1), int(id_nivel_2),
            int(id_nivel_3), int(id_nivel_4), int(id_nivel_5), int(id_nivel_6), int(id_nivel_7)))
        conm.commit()
    except:
        print("Error: unable to fecth data:",id_comissao)
    conm.close()


def insertNivel(id_nivel_1, id_nivel_2, id_nivel_3, id_nivel_4, id_nivel_5, id_nivel_6, id_nivel_7):
    conm = mysql.openConMysqlHome()
    sqlInsertComissaoSellerQuery = '''
        INSERT INTO cubo.WM_NIVEL
        (ID,NIVEL, ID_CATEGORIA, COMISSIONAMENTO, ID_NIVEL_1, ID_NIVEL_2, ID_NIVEL_3, ID_NIVEL_4, ID_NIVEL_5, ID_NIVEL_6, ID_NIVEL_7)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur = conm.cursor()
    try:
        cur.execute(sqlInsertComissaoSellerQuery, (
            int(id_nivel_1), int(id_nivel_2), int(id_nivel_3), int(id_nivel_4), int(id_nivel_5), int(id_nivel_6),
            int(id_nivel_7)))
        conm.commit()
    except:
        print("Error: unable to fecth data:")
        conm.close()


def insert_products(id_produto, id_categoria, id_nivel_1, id_nivel_2, id_nivel_3,
                    id_nivel_4, id_nivel_5, id_nivel_6, id_nivel_7, nome, descricao,
                    ean, marca, preco_de, preco_por, altura, largura, profundidade,
                    peso, status, datahora_criacao, datahora_alteracao):
    conm = mysql.openConMysqlHome()
    sqlInsertComissaoSellerQuery = '''
            INSERT INTO cubo.WM_PRODUTOS
            (ID_PRODUTO, ID_CATEGORIA, ID_NIVEL_1, ID_NIVEL_2, ID_NIVEL_3, ID_NIVEL_4, ID_NIVEL_5, ID_NIVEL_6, ID_NIVEL_7, NOME, DESCRICAO, EAN, MARCA, PRECO_DE, PRECO_POR, ALTURA,LARGURA, PROFUNDIDADE, PESO, STATUS, DATAHORA_CRIACAO, DATAHORA_ALTERACAO)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur = conm.cursor()
    try:
        cur.execute(sqlInsertComissaoSellerQuery, (id_produto, id_categoria, id_nivel_1, id_nivel_2, id_nivel_3,
                                                   id_nivel_4, id_nivel_5, id_nivel_6, id_nivel_7, nome, descricao,
                                                   ean, marca, preco_de, preco_por, altura, largura, profundidade,
                                                   peso, status, datahora_criacao, datahora_alteracao))
        conm.commit()
    except:
        print("Error: unable to fecth data:", id_produto)
        conm.rollback()

    conm.close()


def insert_buybox(id_seller, precode, precopor, estoque,
                  sku, tipo_entrega, nome, logo,
                  pesquisa_satisfacao, score, slug, percentual_desconto_frete,
                  percentual_desconto_sku, precopromocional, id_produto):
    conm = mysql.openConMysqlHome()
    print(id_seller)
    sqlInsertSellerQuery = '''INSERT INTO cubo.WM_BUYBBOX(ID_SELLER,PRECO_DE, PRECO_POR, ESTOQUE, SKU, TIPO_DE_ENTREGA, NOME, LOGO, PESQUISA_SATISFACAO,SCORE, SLUG,PERCENTUAL_DESCONTO_FRETE, PERCENTUAL,DESCONTO_SKU, PRECO_PROMOCIONAL, ID_PRODUTO)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur = conm.cursor()
    try:
        cur.execute(sqlInsertSellerQuery, (int(id_seller), precode, precopor, estoque,
                                           sku, tipo_entrega, nome, logo,
                                           pesquisa_satisfacao, score, slug, percentual_desconto_frete,
                                           percentual_desconto_sku, precopromocional, id_produto))
        conm.commit()
    except:
        print("Error: unable to fecth data:", id_produto)
        conm.close()


def insert_slug(id_produto, idlistagemurl, url_listagem, fornecedor_id,
                departamento_id, tipo_url, nome_amigavel, ordem,
                breadcrumb, top_menu, id_depdep, departamento, departamento_slug, id_depdep_pai,
                google_product_category, categoria_id):
    conm = mysql.openConMysqlHome()
    sqlInsertSellerQuery = '''INSERT INTO cubo.WM_SLUG(ID_PRODUTO,
ID_LISTAGEM_URL, URL_LISTAGEM, FORNECEDOR_ID, ID_DEPARTAMENTO, TIPO_URL,
NOME_AMIGAVEL, ORDEM, BREADCRUMB, TOP_MENU, ID_DEPDEP, DEPARTAMENTO,
DEPARTAMENTO_SLUG, ID_DEPARTAMENTO_PAI, GOOGLE_PRODUCTS_CATEGORY, ID_CATEGORIA_SLUG)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur = conm.cursor()
    try:
        cur.execute(sqlInsertSellerQuery, (id_produto, idlistagemurl, url_listagem, fornecedor_id,
                                           departamento_id, tipo_url, nome_amigavel, ordem,
                                           breadcrumb, top_menu, id_depdep, departamento, departamento_slug, id_depdep_pai,
                                           google_product_category, categoria_id))
        conm.commit()
    except:
        print("Error: unable to fecth data:", id_produto)
        conm.close()

def insert_pedidos(id_pedido,id_seller,pedido_wd,comissao,subtotal,frete,total,pedido_mm):
    conm = mysql.openConMysqlHome()
    sqlInsertSellerQuery = """INSERT INTO cubo.WM_PEDIDOS(ID_PEDIDO_WM,ID_SELLER,ID_PEDIDO,TOTAL_COMISSAO,SUBTOTAL,FRETE,TOTAL_PEDIDO,ID_PEDIDO_PAI) 
VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"""
    cur = conm.cursor()

    cur.execute(sqlInsertSellerQuery,(int(id_pedido),
                                      id_seller,
                                      pedido_wd,
                                      comissao,
                                      subtotal,
                                      frete,
                                      total,
                                      pedido_mm))
    conm.commit()


    conm.close()


if (__name__ == "__main__"):
    print("begin")
