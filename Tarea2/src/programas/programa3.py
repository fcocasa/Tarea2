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
      separator=""
      tree = parse(s)
      if tree:
        t=tree[0]
        contAster=0;
        contGuion=0;
        for leafPos in t.treepositions('leaves'):
            
            if t[leafPos] == '*':
                if contAster % 2 == 0:
                    t[leafPos] = "\\textbf{"
                else:
                     t[leafPos] ="}"
                contAster+=1
                
            if t[leafPos] == '_':
                if contGuion % 2 == 0:
                    t[leafPos] = "\\emph{"
                else:
                     t[leafPos] ="}"
                contGuion+=1
                
            if t[leafPos] == '(':
                t[leafPos] = "\\("
                
            if t[leafPos] == ')':
                t[leafPos] = "\\)"
               
                
                
                
        salida=separator.join(t.leaves())
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()





