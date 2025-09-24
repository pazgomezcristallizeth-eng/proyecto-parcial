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
            "titulo": "Al Aire (En vivo)",
            "lanzamiento": "14 de diciembre de 2018",
            "canciones": 23,
            "descripcion": "Quinto album de Siddhartha. Disco en vivo que captura la energía de Siddhartha sobre el escenario, incluyendo una selección de sus mejores canciones.",
            "imagen": " "
        },
        {
            "titulo": "Memoria Futuro",
            "lanzamiento": "2019 - 2020",
            "canciones": 10,
            "descripcion":"Sexto album de Siddhartha. Memoria Futuro se lanzó en dos partes y nos muestra una exploración de sonidos más electrónicos y experimentales.",
            "imagen": "https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/MemoriaFuturo.jpg"
        },
        {
            "primera parte": "Memoria Futuro – Vol. 1",
            "título": "Memoria Futuro – Memoria",
            "lanzamiento": "17 de noviembre de 2019",
            "canciones": 5,
            "descripcion": "Primer volumen. Memoria marca el inicio de una narrativa dividida en capítulos, se enfoca en la introspección, los recuerdos, temas de amor, nostalgia y reflexión. Cada cancion funciona como un capítulo en una narrativa mas amplia",
            "imagen":"https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/memoria.jpeg"
        },
        {
            "segunda parte": "Memoria Futuro - Vol. 2",
            "titulo": "Memoria Futuro - Futuro",
            "lanzamiento": "4 de marzo de 2020", 
            "canciones": 5,
            "descripcion": "Segundo voumen. Futuro complementa la historia iniciada en el primero, profundizando en temas de conexión y crecimiento personal. El disco cierra con la cancion; Memoria Futuro, que plasma la idea central: la memoria y el futuro como dos planos que conviven.",
            "imagen": "https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/Futuro.jpg"
        }, 
        {
            "titulo": "00:00",
            "lanzamiento": "31 de marzo de 2022",
            "canciones": 10,
            "descripcion": "Septimo album de Siddhartha. Explora temas como el amor, el desamor, la esperanza y la madurez, con un sonido que mezcla elementos tradicionales mexicanos y pop.",
            "imagen": "https://github.com/pazgomezcristallizeth-eng/proyecto-parcial/blob/main/Sexto00.jpeg"
        }
    ]
    
    indice_actual = [0]

    contenedor=ft.Container(
             content=ft.Column([]),
             widht=300
             height=300
             bgcolor=ft.Colors.
             alignment=ft.alignment.center
             padding=
    )

    boton_siguiente = ft.ElevatedButton(text="Ver albums")

    def mostrar_artista():
        artista = cantante[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=album["imagen"],widht=300,height=400,fit=ft.ImageFit.CONTAIN),
            ft.Text(album["titulo"],size=20,weight=ft.FontWeight.BOLD),
            ft.Text(f"descripcion: {album['descripcion']}",size=16),
            ft.Text(f"lanzamiento: {album['lanzamiento']}",size=16),
            ft.Text(f"canciones: {album['canciones']}",size=14,italic=True)
        ],alignment=ft.MainAxisAligment.CENTER)

        if indice_actual[0]==len(album)-1:
        
        ft.app(main)






















