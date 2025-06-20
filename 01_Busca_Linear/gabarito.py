def encontrar_produto_por_id(inventario, id_produto):
  for produto in inventario:
    if produto['id_produto'] == str(id_produto):
      return produto
  return None

inventario = [
    {'id_produto':'1',' nome': 'produto 1'},
    {'id_produto':'2',' nome': 'produto 2'},
]

print(encontrar_produto_por_id(inventario,id_produto="1")) #
print(encontrar_produto_por_id(inventario,id_produto= "4"))

""" Esse escript implementa o algoritimo """