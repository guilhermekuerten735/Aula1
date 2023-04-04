def interface():
    nota1 = input("Digite a primeira nota:")
    nota2 = input("Digite a primeira nota:")
    calculoMedia(nota1, nota2)

def calculoMedia(nota1, nota2):
    media = (nota1, nota2)/2
    salvaMedia (media)

def salvaMedia(media):
    sql = "insert media into notas value {media}"
    
    