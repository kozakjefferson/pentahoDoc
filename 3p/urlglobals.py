##token dos ENDPOINTS

tokenSeller = "d2d47b0b-cfda-4154-a1e2-b8020f6d500e"
tokenProdutos = "5ad9acdd-329f-4798-83ae-a854a42cdbc9"
tokenDescricao = "d2d47b0b-cfda-4154-a1e2-b8020f6d500e"

url_wm_api_produtos = "https://war-machine.madeiramadeira.com.br/v1/store/produto/updates/date_from={}&date_to={}&limit={}&offset={}"
tokenMM = "TOKEN_MM_123"


def setParamBusca(dataInicio, dataFim, limit=2000, offset=0, tipo={"produto", "pedido"}):
    if(tipo == "produto"):
        url = url_wm_api_produtos.format(dataInicio, dataFim, limit, offset)
    elif(tipo == "pedido"):
        url = url_wm_api_pedidos.format(dataInicio, dataFim, limit, offset)
    return url


header_mm = {"Cache-Control": "no-cache", "Postman-Token": tokenProdutos, "TOKENMM": tokenMM}

url_MM_Api_Comissao = "https://war-machine.madeiramadeira.com.br/v1/comissao/"


url_MM_Api_Id_Seller = " https://war-machine.madeiramadeira.com.br/v1/seller/"


url_wm_api_pedidos= "https://war-machine.madeiramadeira.com.br/v1/pedido/from={}&to={}&limit={}&offset={}"


"""GET /v1/store/produto/updates/date_from=2010-01-01&amp;date_to=2018-05-01&amp;limit=4000&amp;offset=4000 HTTP/1.1
Host: war-machine.madeiramadeira.com.br
Cache-Control: no-cache
Postman-Token: 0942e47c-b7a5-4367-b364-32e921dc8775
TOKENMM: TOKEN_MM_123
"""
