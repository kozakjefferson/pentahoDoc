import urlglobals as url
import models.model_util as utils

BULK_INSERT_SIZE = 90

sellersIDsOK = utils.GetAllTotalSellers()
utils.getComissaoFromSeller(sellersIDsOK)
url_products = url.setParamBuscaProdutos("2016-01-01", "2018-05-01")
produtos = utils.getproducts(url_products)
