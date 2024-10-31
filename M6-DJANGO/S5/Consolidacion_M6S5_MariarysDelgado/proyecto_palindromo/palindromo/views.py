from django.http import HttpResponse
from django.shortcuts import render

def verificar_palindromo(request, palabra):
    # Procesa la palabra quitando espacios y poniéndola en minúsculas
    palabra_procesada = ''.join(palabra.split()).lower()
    resultado = ""
    
    # Verifica si es un palíndromo
    if palabra_procesada == palabra_procesada[::-1]:
        resultado = f"{palabra}, ES PALÍNDROMO"
    else:
        resultado = f"{palabra}, NO ES PALÍNDROMO"

    # Generar HTML con el resultado
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Verificar Palíndromo</title>
        <link rel="stylesheet" href="{request.scheme}://{request.get_host()}/static/css/style.css">
    </head>
    <body>
        <h1 class="titulo">Verificación de Palíndromos</h1>
        <p class="texto-grande">{resultado}</p>
    </body>
    </html>
    """
    
    return HttpResponse(html)
