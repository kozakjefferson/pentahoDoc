##token dos ENDPOINTS

tokenSeller = "d2d47b0b-cfda-4154-a1e2-b8020f6d500e"
tokenProdutos = "5ad9acdd-329f-4798-83ae-a854a42cdbc9"
tokenDescricao = "d2d47b0b-cfda-4154-a1e2-b8020f6d500e"

url_wm_api_produtos = "https://war-machine.madeiramadeira.com.br/v1/store/produto/updates/date_from={}&date_to={}&limit={}&offset={}"
tokenMM = "TOKEN_MM_123"


def setParamBusca(url,dataInicio, dataFim, limit=2000, offset=0):
    url_formated = url.format(dataInicio, dataFim, limit, offset)
    return url_formated


header_mm = {"Cache-Control": "no-cache", "Postman-Token": tokenProdutos, "TOKENMM": tokenMM}

wm_api_comissao = "https://war-machine.madeiramadeira.com.br/v1/comissao/"


mm_api_id_seller = " https://war-machine.madeiramadeira.com.br/v1/seller/"


wm_api_pedidos= "https://war-machine.madeiramadeira.com.br/v1/pedido/from={}&to={}&limit={}&offset={}"


"""GET /v1/store/produto/updates/date_from=2010-01-01&amp;date_to=2018-05-01&amp;limit=4000&amp;offset=4000 HTTP/1.1
Host: war-machine.madeiramadeira.com.br
Cache-Control: no-cache
Postman-Token: 0942e47c-b7a5-4367-b364-32e921dc8775
TOKENMM: TOKEN_MM_123
"""
