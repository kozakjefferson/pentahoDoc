
##token dos ENDPOINTS

pentahoTokenSeller = "d2d47b0b-cfda-4154-a1e2-b8020f6d500e"
pentahoTokenProdutos = "5ad9acdd-329f-4798-83ae-a854a42cdbc9"

tokenMM = "TOKEN_MM_123"
def setParamBuscaProdutos(dataInicio,dataFim,limit=1000,offset=0):
    print(dataFim,dataInicio,limit,offset)
    return _url_MM_Api.format(dataInicio, dataFim, limit, offset)


_url_MM_Api = "https://war-machine.madeiramadeira.com.br/v1/store/produto/updates/date_from={}&date_to={}&limit={}&offset={}"
_header_MM_Produtos = {"Cache-Control": "no-cache", "Pentaho-Token": pentahoTokenProdutos, "TOKENMM": "TOKEN_MM_123"}

_url_MM_Api_Seller="https://war-machine.madeiramadeira.com.br/v1/comissao/"

_header_MM_Seller={"Cache-Control": "no-cache", "Pentaho-Token": pentahoTokenSeller, "TOKENMM": tokenMM}


if(__name__=="__main__"):
    setParamBuscaProdutos()