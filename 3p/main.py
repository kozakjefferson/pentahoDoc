import urlglobals as url
import models.model_util as utils

BULK_INSERT_SIZE = 90


#sellersIDsOK = utils.GetAllTotalSellers()
#utils.getComissaoFromSeller(sellersIDsOK)


#k=utils.set_produtos_wm()
#modprodutos = totalprodutos % limit_busca
#rest = totalprodutos-modprodutos

#for offset in range(2001, totalprodutos, limit):
#    url_products = url.setParamBusca(data_inicio, today, limit_busca, offset, tipo="produto")
#    utils.getproducts(url_products)
#    if offset == modprodutos:
#        url_products = url.setParamBusca(data_inicio, today, limit_busca, rest, tipo= "produto")
#        utils.getproducts(url_products)

utils.get_pedidos_wm()
