import requests
import json as js


def getproducts(url, header):
    listaprodutos = requests.get(url, headers=header)
    r2d = js.dumps(listaprodutos.json())
    json_obj = js.loads(r2d)

    counter = 0
    for data in json_obj["data"]:
        counter += 1
        print('--- line 2', counter)
        print("id_produto:", data["id_produto"])
        print("id_produto_match:", data["id_produto_match"])
        print("id_categoria:", data["id_categoria"])
        print("id_nivel_1", data["nivel_1"])
        print("nivel_1", data["nivel_1"])
        print("id_nivel_2", data["id_nivel_2"])
        print('---------------------------- ')


def GetAllTotalSellers(url, header):
    c = 0
    url404 = 0
    err = []
    ok = []
    id = []
    while c < 300:
        c += 1
        r = requests.get(url+str(c), headers=header)
        if r.status_code > 200:
            err.append(r.url)
            url404 += 1
            print(url404, "line", c, "url", r.url)
            if url404 > 5:
                break
        else:
            ok.append(r.url)
            id.append(c)
            url404 = 0
    print(ok)
    print(id)
    print(err)
    return (ok, id, err)

if (__name__ == "__main__"):
    getproducts()
