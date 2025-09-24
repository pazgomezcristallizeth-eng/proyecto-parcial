import flet as ft


def main(page: ft.Page):
    page.title="Siddhartha"
    page.bgcolor=ft.Colors.YELLOW_50
    
    cantante = [
        {
          "titulo": "Siddhartha",
          "descripcion": "Jorge Siddhartha Gonzalez Ibarra, conocido artísticamente como Siddhartha, es un músico solista de Indie Rock nacido el 25 de agosto de 1977 en Jalisco-Guadalajara, México. Sus letras son introspectivas y sus melodías combinan rock, pop y elementos electrónicos.",
          "imagen": "https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/Siddhartha.jpeg"
        },
        {
            "titulo": "Why You?",
            "lanzamiento": "26 de septiembre de 2008",
            "canciones": 11,
            "descripcion":"Primer álbum de Siddhartha como solista. Es el álbum uno de su carrera, con un sonido introspectivo y melódico que le dio reconocimiento en la escena indie mexicana y una nominación al Latin Grammy.",
            "imagen": "https://raw.githubusercontent.com/pazgomezcristallizeth-eng/proyecto-parcial/refs/heads/main/Why%20You.jpeg" 
        },
        {
            "titulo": "Náufrago",
            "lanzamiento": "14 de septiembre de 2011",
            "canciones": 11,
            "descripcion": "Segundo álbum de Siddhartha. Más maduro y experimental que el primero, consolidó su lugar en el rock alternativo mexicano y tuvo gran recepción crítica y comercial.",
            "imagen": "https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/naufrago.jpg"
        },
        {
            "titulo": "El vuelo del pez",
            "lanzamiento":"14 de enero de 2014",
            "canciones": 11,
            "descripcion":"Tercer álbum de Siddhartha. Marca una evolución sonora con elementos electrónicos y atmosféricos. Alcanzó el No.1 en el Top Chart de iTunes Rock Latino.",
            "imagen": "https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/Elvuelodelpez.jpeg"
        },
        {
            "titulo": "Únicos",
            "lanzamiento": "23 de septiembre de 2016",
            "canciones": 10,
            "descripcion":"Cuarto álbum de Siddhartha. Con un sonido más pulido y accesible, explora temas de identidad y conexión. Recibió elogios por su producción y cohesión artística.",
            "imagen": "https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/unicos.jpg"
        },
        {
            "titulo": "Memoria futuro, vol. 1",
            "lanzamiento": "17 de mayo de 2019",
            "canciones": 5,
            "descripcion":"Primer volumen de un álbum conceptual dividido en dos partes. Memoria Futuro (Vol. 1), explora la introspección, la nostalgia y los recuerdos. Cada canción funciona como un capítulo en una narrativa más amplia.",
            "imagen": "https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/memoria.jpeg"
        },
        {
            "titulo": "Memoria futuro, vol 2.",
            "lanzamiento": "4 de marzo de 2020",
            "canciones": 5,
            "descripción": "Segundo volumen de la obra conceptual. Memoria Futuro (Vol. 2), complementa la historia iniciada en el primero. Aquí se refleja el futuro, con un sonido más expansivo y colaboraciones notables. El disco cierra con la canción homónima “Memoria Futuro”, que integra la idea central: la memoria y el futuro como dos planos que conviven.",
            "imagen": "https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/Futuro.jpg"
        },
        {
            "titulo": " ",
            "lanzamiento": " ",
            "canciones": "",
            "descripción": " ",
            "imagen": " "
        },
    ]
    
ft.app(main)














