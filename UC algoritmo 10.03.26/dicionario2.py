#sem dicionario
matricula1 = 2026001
nome1 = "Ana Silva"
telefone1= "9999-8888"

#com dicionario
aluno = {
    "matricula": 2026001,
    "nome": "Ana Silva",
    "telefone": "9999-8888",
}

print(aluno)

contato = {
    "@camilaqueiroz": "Camila Queiroz",
    "@brunamarquezine": "Bruna m.",
    "@sheronmenezes": "Sheron M.",
    "@paolaoliveira": "Paola O.",
    "@joao": "Jõao"
}

print(contato)
print(type(contato))

#acesso direto
print(contato["@camilaqueiroz"])

#acesso seguro com o get()
print(contato.get("@paolaoliveira"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "não encontrado"))

#add novo elemento
contato["@giovanna"] = "Giovanna"
print("Após add: ", contato)

#atualizar elemento existente 
contato["@paolaoliveira"] = "Paola Oliveira"
print("Após add: ", contato)

contato.update({
    "@brunamarquezine" : "Bruna Marquezine",
    "@camilaqueiroz" : "Camila Q."
})
print("Após atualização: ", contato)

#pop remove e retorna
removido = contato.pop("@paolaoliveira")
print(f"Removido: {removido}")
print("Após o pop: ", contato)

#del remove sem retornar
del contato["@camilaqueiroz"]
print("Após o del:", contato)

#clear esvazia tudo
copia = dict(contato)
contato.clear()
print("Após clear: ", contato)
print("Cópia: ", copia)

print("Número de contato: ", len(contato))#tamanho dicio

#verificar existência
if "@joao" in contato:
    print(f"Encontrado: {contato["@joao"]}" )

if "@inesistente" in contato:
    print("Existe")
else:
    print("Não existe")