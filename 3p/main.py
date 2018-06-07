import urlglobals as url
import models.model_util as utils
import time

BULK_INSERT_SIZE = 90
today = time.strftime("%Y-%m-%d")
data_inicio = '2010-01-01'
limit_busca=2000

#sellersIDsOK = utils.GetAllTotalSellers()
#utils.getComissaoFromSeller(sellersIDsOK)


##pegar total de pedido generico

#total_itens=int(util.getTotalItensApi(url_products))
#mod_iten = total_itens % limit_busca

#if(total_itens < limit_busca):
#    limit_busca = total_itens
#else:
#    limit_busca = total_itens % limit_busca


url_products = url.setParamBusca(dataInicio=data_inicio, dataFim=today, tipo="produto")
totalprodutos = int(utils.getproducts(url_products))
limit = 2000
modprodutos = totalprodutos % limit_busca
rest = totalprodutos-modprodutos

for offset in range(2001, totalprodutos, limit):
    url_products = url.setParamBusca(data_inicio, today, limit_busca, offset, tipo="produto")
    utils.getproducts(url_products)
    if offset == modprodutos:
        url_products = url.setParamBusca(data_inicio, today, limit_busca, rest, tipo= "produto")
        utils.getproducts(url_products)


url_pedidos = url.setParamBusca(data_inicio, today, limit_busca, offset, "pedidos")
utils.get_pedidos(url_pedidos)