# -*- coding: utf-8 -*-

import sys
import io
import nltk

def tokenize(text):
    return list(text)
#'A' Q | 'B' Q | 
def parse(s):
    grammarString = """
    S -> E S | '*' C | '_' N | E
    C -> E C | '*' S | '*'
    N -> E N | '_' S | '_'
    E -> '.'|' '|','|')'|'('|'a'|'b'|'c'|'d'|'e'|'f'|'g'|'h'|'i'|'j'|'k'|'l'|'m'|'n'|'o'|'p'|'q'|'r'|'s'|'t'|'u'|'v'|'w'|'x'|'y'|'z'|'A'|'B'|'C'|'D'|'E'|'F'|'J'|'H'|'I'|'J'|'K'|'L'|'M'|'N'|'O'|'P'|'Q'|'R'|'S'|'T'|'U'|'V'|'W'|'X'|'Y'|'Z'
    
    """
    grammar = nltk.CFG.fromstring(grammarString)
    s_tok = tokenize(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = [t for t in parser.parse(s_tok)][:1]
    return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s)
      if tree:
          nuevo = s.replace('(','\\(')#para poder usar un expresion regular con \w, que este reconoce el barrabaja para cuando suplante
          nuevo = nuevo.replace(')','\\)')
          i=0
          index=0
          while index!=-1 :
              index = nuevo.find('_', index)
              #print(index)
              #print(i % 2)
              if(i % 2 == 0):
                  nuevo = nuevo.replace('_','\\emph{',1)
                  #print('entro par')
              else:
                  nuevo = nuevo.replace('_','}',1)
                  #print('entro impar')
              i = i + 1
              
          i = 0
          index = 0
          while index!=-1 :
              index = nuevo.find('*', index)
              #print(index)
              #print(i % 2)
              if(i % 2 == 0):
                  nuevo = nuevo.replace('*','\\textbf{',1)
                  #print('entro par')
              else:
                  nuevo = nuevo.replace('*','}',1)
                  #print('entro impar')
              i = i + 1
          #nuevo = re.sub(r'\*\w*\*',' \\textbf{}')
          salida = nuevo
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()





