def retornaHtml(string, comandoGaleria):
  #deixa so o "miolo"
  string = string.replace("https://drive.google.com/file/d/", "")
  string = string.replace("/view?usp=sharing", "")

  #adiciona o link de amostra
  cod = "http://drive.google.com/uc?export=view&id=ADDHERE"
  cod = cod.replace("ADDHERE", string)

  #adiciona o link de amostra à tag a e ao à tag img

  if comandoGaleria == 1:
    codHtmlA = "<a class='imagemGaleria' href='LINK' data-lightbox='galeria' data-title='Toque para alterar'>IMG</a>"
  else:
    codHtmlA = "<a href='LINK' data-lightbox='galeria' data-title='Toque para alterar'>IMG</a>"
    
  codHtmlImg = "<img src='LINK'>"
  codHtmlA = codHtmlA.replace('LINK', cod)
  codHtmlImg = codHtmlImg.replace('LINK', cod)

  #adiciona a tag img dentro da tag a, substitui os parenteses simples por parenteses duplos
  codFinal = codHtmlA.replace("IMG", codHtmlImg)
  return codFinal.replace("'", '"')

#criacao da lista grande com todos os links
file = open('entrada.txt')
listaLinks = file.read().splitlines()

numero = listaLinks[0] + ", "
listaNumero = numero.split(", ")

entrada = int(input("1- Galeria / 0- Normal: "))

contador = 0

for link in listaNumero:
  if link == "":
    pass
  else:

    if contador == 0:
      contador = 1
      file3 = open('saida.txt', 'w')
      file3.close()
      
    linkModificado = retornaHtml(link,entrada)
    file3 = open('saida.txt', 'a')
    file3.write(linkModificado + "\n" + "\n")  
      
    

file3.close()
print("feito!")
  

  





#codFinal = codHtmlA.replace("IMG", "\n\t" + codHtmlImg + "\n")


