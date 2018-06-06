import urlglobals as url
import models.model_util as utils
import time

BULK_INSERT_SIZE = 90
today = time.strftime("%Y-%m-%d")
data_inicio = '2010-01-01'

#sellersIDsOK = utils.GetAllTotalSellers()
#utils.getComissaoFromSeller(sellersIDsOK)

url_products = url.setParamBuscaProdutos(dataInicio=data_inicio, dataFim=today)
totalprodutos = int(utils.getproducts(url_products))
limit=2000
modprodutos = totalprodutos % limit
rest=totalprodutos-modprodutos

for offset in range(2001, totalprodutos, limit):
    url_products = url.setParamBuscaProdutos(data_inicio, today, limit, offset)
    utils.getproducts(url_products)
    if offset == modprodutos:
        url_products = url.setParamBuscaProdutos(data_inicio, today, limit, rest)
        utils.getproducts(url_products)
