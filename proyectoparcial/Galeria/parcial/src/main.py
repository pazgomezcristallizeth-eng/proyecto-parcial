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
            "descripcion":"Why You? es el álbum debut del cantante mexicano Siddhartha lanzado en 2008. Éste está compuesto por un cuadernillo de 11 imágenes principales que hacen referencia a la pregunta del mismo nombre que el álbum: Why You?.",
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
            "descripcion":"Únicos es el cuarto álbum de estudio del cantante mexicano Siddhartha lanzado el 23 de septiembre de 2016. El disco cuenta con 10 canciones.",
            "imagen": ""
        },
        {
            "titulo": "Memoria futuro, vol. 1",
            "lanzamiento":2019,
            "descripcion":"Memoria futuro es el quinto álbum de estudio del cantante mexicano Siddhartha,[1] publicado el 2 de noviembre de 2020. por Sony Music",
            "imagen": ""
        },
        {
            "titulo": " ",
            "lanzamiento": " ",
            "descripción": " ",
            "imagen": " "
        },
        {
            "titulo": " ",
            "lanzamiento": " ",
            "descripción": " ",
            "imagen": " "
        },
    ]
    
ft.app(main)



