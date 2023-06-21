import dns.resolver

res =dns.resolver.Resolver()

arquivo =open("/home/ayrton/Documentos/word.txt", "r")
subDom = arquivo.read().splitlines()

alvo="bancocn.com"

for subdominio in subDom:

    try:
        sub_alvo = subdominio + "."+ alvo
        resultado = res.resolve(sub_alvo, "A")
        for ip in resultado:
            print(sub_alvo,"-->" ,ip)
    except:
        pass
