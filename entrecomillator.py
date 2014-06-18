__author__ = 'miguel'
import sys
import csv

def main(arg):
    reader = Entrecomillator(arg)
    reader.run()

class Entrecomillator(object):
    def __init__(self,file):
        self.file = file

    def run(self):
        lista= []
        with open(self.file,'rb') as csvfile:
            filreader = csv.reader(csvfile)
            for row in filreader:
                lista.append('"' + ''.join(row) + '"')
            print ','.join(lista)


if __name__ == "__main__":
    main(sys.argv[1])
