##token dos ENDPOINTS

tokenSeller = "d2d47b0b-cfda-4154-a1e2-b8020f6d500e"
tokenProdutos = "5ad9acdd-329f-4798-83ae-a854a42cdbc9"
tokenDescricao = "d2d47b0b-cfda-4154-a1e2-b8020f6d500e"

url_MM_Api = "https://war-machine.madeiramadeira.com.br/v1/store/produto/updates/date_from={}&date_to={}&limit={}&offset={}"
tokenMM = "TOKEN_MM_123"


def setParamBuscaProdutos(dataInicio, dataFim, limit=2000, offset=6000):
    url = url_MM_Api.format(dataInicio, dataFim, limit, offset)
    return url


header_MM_Produtos = {"Cache-Control": "no-cache", "Postman-Token": tokenProdutos, "TOKENMM": tokenMM}

url_MM_Api_Comissao = "https://war-machine.madeiramadeira.com.br/v1/comissao/"
header_MM_Comissao = {"Cache-Control": "no-cache", "Pentaho-Token": tokenDescricao, "TOKENMM": tokenMM}

url_MM_Api_Id_Seller = " https://war-machine.madeiramadeira.com.br/v1/seller/"
header_MM_id_Seller = {"Cache-Control": "no-cache", "Pentaho-Token": tokenSeller, "TOKENMM": tokenMM}

"""GET /v1/store/produto/updates/date_from=2010-01-01&amp;date_to=2018-05-01&amp;limit=4000&amp;offset=4000 HTTP/1.1
Host: war-machine.madeiramadeira.com.br
Cache-Control: no-cache
Postman-Token: 0942e47c-b7a5-4367-b364-32e921dc8775
TOKENMM: TOKEN_MM_123
"""
