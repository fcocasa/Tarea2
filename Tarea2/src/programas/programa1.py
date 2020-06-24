# -*- coding: utf-8 -*-

import sys
import io
import nltk

def tokenize(text):
    return list(text)

def parse(s):
   grammarString = """
    S-> 'A' Q | 'B' Q | 'C' R | 'A' | 'B' 
    P-> 'A' Q | 'B' Q | 'C' R | 'A' | 'B' 
    Q-> 'C'U | 'A'R | 'B'R 
    R-> 'A'T | 'B'T | 'C'P | 'A' | 'B' | 'C'
    U-> 'A'P | 'B'P | 'C'Q | 'A' | 'B' | 'C'
    T-> 'A'P | 'B'P | 'C'Q | 'A' | 'B' | 'C'
    """
    grammar = nltk.CFG.fromstring(grammarString)
    s_tok = tokenize(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = [t for t in parser.parse(s_tok)][:1]  # [:1] toma el primer tree q encuentra
    return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1] # "../entradas/p1entrada1.txt" 
    archivo_salida = sys.argv[2] # "programa1-entrada1.txt" 

    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s)
      if tree:
          salida = "PERTENECE"
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()





