# -*- coding: utf-8 -*-

import sys
import io
import nltk

def tokenize(text):
    return list(text)
#'A' Q | 'B' Q | 
def parse(s):
    grammarString = """
    S -> 'A' | 'B' | 'A' P | 'B' P | 'C' Q
    P -> 'C' U | 'A' Q | 'B' Q
    U -> 'A' | 'B' | 'C' | 'A' T | 'B' T | 'C' P
    T -> 'A' | 'B' | 'C' Q | 'A' P | 'B' P
    Q -> 'A' | 'B' | 'C' | 'A' R | 'B' R | 'C' T
    R -> 'C' | 'A' Q | 'B' Q
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
          salida = "PERTENECE"
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()





