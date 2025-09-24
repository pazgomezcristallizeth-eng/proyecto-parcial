import flet as ft


def main(page: ft.Page):
    page.title="Siddhartha"
    page.bgcolor=ft.Colors.YELLOW_50
    
    cantante = [
        {
          "titulo": "Siddhartha",
          "descripcion": "Jorge Siddhartha Gonzalez Ibarra, conocido artísticamente como Siddhartha, es un músico solista de Indie Rock nacido el 25 de agosto de 1977 en Jalisco-Guadalajara, México.",
          "imagen": ""
        },
        {
            "titulo": "Why You?",
            "lanzamiento": 2008,
            "descripcion":"Es catalogado como una de las mejores producciones del año por las revistas especializadas Warp, Marvin, Rolling Stone, Sonika y Círculo Mixup.",
            "imagen": "https://raw.githubusercontent.com/pazgomezcristallizeth-eng/proyecto-parcial/refs/heads/main/Why%20You.jpeg" 
        },
        {
            "titulo": "Náufrago",
            "lanzamiento":2011,
            "descripcion": "Es el segundo álbum de estudio del cantante mexicano Siddhartha lanzado en 2011, el disco está compuesto por 11 canciones originalmente",
            "imagen": "https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/naufrago.jpg"
        },
        {
            "titulo": "El vuelo del pez",
            "lanzamiento":2014,
            "descripcion":"Es el tercer álbum de estudio del cantante mexicano Siddhartha lanzado el 14 de enero de 2014. El disco está compuesto por 11 canciones.",
            "imagen": ""
        },
        {
            "titulo": "Únicos",
            "lanzamiento":2016,
            "descripcion":"",
            "imagen": ""
        },
        {
            "titulo": "",
            "lanzamiento":"",
            "descripcion":"",
            "imagen": ""
        },
    ]
    
ft.app(main)
