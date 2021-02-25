import sys
import logging
import re
from booloader import BooLoader

class Boogie:

    def __init__(self, filename):
        self.program = BooLoader(filename)
        #|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|q|v|w|x|y|z"

def main(filename):
    print("Boogie v0.0.1")
    print("Running: " + filename)
    variables = {}
    Boogie(filename)
    
    file_name = open(filename,'r',encoding='UTF-8').readlines()
    for num,i in enumerate(file_name):
        if "//" in i:
            file_name[num] = ''
    
    for i in file_name:
        if "-X" in i:
            x = i.index("-X")
            x =x+2
            val = i[x]
            def repeat():
                if "print(\"" in i:
                    start = i.find("print(\"") +len("print(\"")
                    end = i.find("\")")
                    result = i[start:end]
                    print(result)
                elif "print(" in i:
                    start = i.find("print(") +len("print(")
                    end = i.find(")")
                    a = i[start:end]
                    result = variables[a]
                    print(result)
                if "a = " in i:
                    startc = i.find("a = ") +len("a = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["a"] = resultc
                elif "b = " in i:
                    startc = i.find("b = ") +len("b = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["b"] = resultc
                elif "c = " in i:
                    startc = i.find("c = ") +len("c = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["c"] = resultc
                elif "d = " in i:
                    startc = i.find("d = ") +len("d = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["d"] = resultc
                elif "e = " in i:
                    startc = i.find("e = ") +len("e = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["e"] = resultc
                elif "f = " in i:
                    startc = i.find("f = ") +len("f = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["f"] = resultc
                elif "g = " in i:
                    startc = i.find("g = ") +len("g = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["g"] = resultc
                elif "h = " in i:
                    startc = i.find("h = ") +len("h = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["h"] = resultc
                elif "i = " in i:
                    startc = i.find("i = ") +len("i = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["i"] = resultc
                elif "j = " in i:
                    startc = i.find("j = ") +len("j = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["j"] = resultc
                elif "k = " in i:
                    startc = i.find("k = ") +len("k = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["k"] = resultc
                elif "l = " in i:
                    startc = i.find("l = ") +len("l = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["l"] = resultc
                elif "m = " in i:
                    startc = i.find("m = ") +len("m = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["m"] = resultc
                elif "n = " in i:
                    startc = i.find("n = ") +len("n = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["n"] = resultc
                elif "o = " in i:
                    startc = i.find("o = ") +len("o = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["o"] = resultc
                elif "p = " in i:
                    startc = i.find("p = ") +len("p = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["p"] = resultc
                elif "q = " in i:
                    startc = i.find("q = ") +len("q = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["q"] = resultc
                elif "r = " in i:
                    startc = i.find("r = ") +len("r = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["r"] = resultc
                elif "s = " in i:
                    startc = i.find("s = ") +len("s = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["s"] = resultc
                elif "t = " in i:
                    startc = i.find("t = ") +len("t = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["t"] = resultc
                elif "u = " in i:
                    startc = i.find("u = ") +len("u = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["u"] = resultc
                elif "v = " in i:
                    startc = i.find("v = ") +len("v = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["v"] = resultc
                elif "w = " in i:
                    startc = i.find("w = ") +len("w = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["w"] = resultc
                elif "x = " in i:
                    startc = i.find("x = ") +len("x = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["x"] = resultc
                elif "y = " in i:
                    startc = i.find("y = ") +len("y = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["y"] = resultc
                elif "z = " in i:
                    startc = i.find("z = ") +len("z = ")
                    endc = i.find(",")
                    resultc = i[startc:]
                    variables["z"] = resultc
                
            for _ in range(1,int(val)):
                repeat()
            
                

        if "print(\"" in i:
            start = i.find("print(\"") +len("print(\"")
            end = i.find("\")")
            result = i[start:end]
            print(result)
        elif "print(" in i:
            start = i.find("print(") +len("print(")
            end = i.find(")")
            a = i[start:end]
            result = variables[a]
            print(result)
        if "a = " in i:
            startc = i.find("a = ") +len("a = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["a"] = resultc
        elif "b = " in i:
            startc = i.find("b = ") +len("b = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["b"] = resultc
        elif "c = " in i:
            startc = i.find("c = ") +len("c = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["c"] = resultc
        elif "d = " in i:
            startc = i.find("d = ") +len("d = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["d"] = resultc
        elif "e = " in i:
            startc = i.find("e = ") +len("e = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["e"] = resultc
        elif "f = " in i:
            startc = i.find("f = ") +len("f = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["f"] = resultc
        elif "g = " in i:
            startc = i.find("g = ") +len("g = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["g"] = resultc
        elif "h = " in i:
            startc = i.find("h = ") +len("h = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["h"] = resultc
        elif "i = " in i:
            startc = i.find("i = ") +len("i = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["i"] = resultc
        elif "j = " in i:
            startc = i.find("j = ") +len("j = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["j"] = resultc
        elif "k = " in i:
            startc = i.find("k = ") +len("k = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["k"] = resultc
        elif "l = " in i:
            startc = i.find("l = ") +len("l = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["l"] = resultc
        elif "m = " in i:
            startc = i.find("m = ") +len("m = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["m"] = resultc
        elif "n = " in i:
            startc = i.find("n = ") +len("n = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["n"] = resultc
        elif "o = " in i:
            startc = i.find("o = ") +len("o = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["o"] = resultc
        elif "p = " in i:
            startc = i.find("p = ") +len("p = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["p"] = resultc
        elif "q = " in i:
            startc = i.find("q = ") +len("q = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["q"] = resultc
        elif "r = " in i:
            startc = i.find("r = ") +len("r = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["r"] = resultc
        elif "s = " in i:
            startc = i.find("s = ") +len("s = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["s"] = resultc
        elif "t = " in i:
            startc = i.find("t = ") +len("t = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["t"] = resultc
        elif "u = " in i:
            startc = i.find("u = ") +len("u = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["u"] = resultc
        elif "v = " in i:
            startc = i.find("v = ") +len("v = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["v"] = resultc
        elif "w = " in i:
            startc = i.find("w = ") +len("w = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["w"] = resultc
        elif "x = " in i:
            startc = i.find("x = ") +len("x = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["x"] = resultc
        elif "y = " in i:
            startc = i.find("y = ") +len("y = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["y"] = resultc
        elif "z = " in i:
            startc = i.find("z = ") +len("z = ")
            endc = i.find(",")
            resultc = i[startc:]
            variables["z"] = resultc
        
        
            
           
            
if __name__ == "__main__":
    # Get the first command-line argument so we can pass a file
    # to run to our language processing.
    try:
        main(sys.argv[1])
    except IndexError:
        logging.fatal("no input file provided")
