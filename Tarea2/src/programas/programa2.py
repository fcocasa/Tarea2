# -*- coding: utf-8 -*-

import sys
import io
import nltk
from nltk.tree import Tree

def tokenize(text):
    return list(text)
#'A' Q | 'B' Q | 
def parse(s):
    grammarString = """
    S -> 'a' | 'b' | '('S A | S '.' S | S '|' S
    A -> ')' '*' | ')'
    """
    grammar = nltk.CFG.fromstring(grammarString)
    s_tok = tokenize(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = [t for t in parser.parse(s_tok)][:1]
    return tree

def reemplazar(t):
    if t is Tree:
        for node in t:
            reemplazar (node)
    else:
        print("hoja:",t)
        if t=='|':
            t='.'
        else:
            if t=='.':
                t='|'


if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      separator=""
      tree = parse(s)
      if tree:
        t=tree[0]
        for leafPos in t.treepositions('leaves'):
            if t[leafPos] == '|':
               t[leafPos] = "."
            else:
                if t[leafPos] == '.':
                    t[leafPos] = "|"
        salida=separator.join(t.leaves())
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()


