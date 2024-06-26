import requests

url = 'https://fakestoreapi.com/products'

response = requests.get(url)
categorias = {
        "electronics", 
        "jewelery",
        "men's clothing",
        "women's clothing"
    }


usuario = str(int(input('elegir la cantidad de productos que decea de cada categoria:  ')))
used_categoria = input(f'elija una categoria: {categorias}   ')

datos_usuario = (usuario, used_categoria)


if response.status_code == 200:
    data = response.json()
    
    if datos_usuario  not in categorias:
        print(f'el filtro de los datso del usuario son: {data}')
    else:
         print(f'products{datos_usuario}')

        

    print(f'el filtro de los productos{datos_usuario}')
else:
    print('error al cargar los productos')



