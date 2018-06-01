import urlglobals as url
import models.model_util as utils

BULK_INSERT_SIZE = 90


sellersIDsOK = utils.GetAllTotalSellers()


utils.getComissaoFromSeller(sellersIDsOK)


url.setParamBuscaProdutos("2016-01-01", "2018-01-01")
produtos = utils.getproducts()

