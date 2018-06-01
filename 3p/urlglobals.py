
##token dos ENDPOINTS

tokenSeller = "d2d47b0b-cfda-4154-a1e2-b8020f6d500e"
tokenProdutos = "5ad9acdd-329f-4798-83ae-a854a42cdbc9"
tokenDescricao = "d2d47b0b-cfda-4154-a1e2-b8020f6d500e"


tokenMM = "TOKEN_MM_123"


def setParamBuscaProdutos(dataInicio, dataFim, limit=1000, offset=0):
    print(dataFim, dataInicio, limit, offset)
    return _url_MM_Api.format(dataInicio, dataFim, limit, offset)


_url_MM_Api = "https://war-machine.madeiramadeira.com.br/v1/store/produto/updates/date_from={}&date_to={}&limit={}&offset={}"
_header_MM_Produtos = {"Cache-Control": "no-cache", "Pentaho-Token": tokenProdutos, "TOKENMM": tokenMM}


_url_MM_Api_Comissao ="https://war-machine.madeiramadeira.com.br/v1/comissao/"
_header_MM_Comissao = {"Cache-Control": "no-cache", "Pentaho-Token": tokenDescricao, "TOKENMM": tokenMM}


_url_MM_Api_Id_Seller=" https://war-machine.madeiramadeira.com.br/v1/seller/"
_header_MM_id_Seller = {"Cache-Control": "no-cache", "Pentaho-Token": tokenSeller, "TOKENMM": tokenMM}
