#!/usr/bin/env python
"""
Music store classes.
"""
import os
import glob
DATA_EXT = ".data"
SUPPORTED_COUNTRIES = ('Mexico', 'Bulgaria')

class Instrument:
    def PrintMe(self):
        print "%(id_)4s %(genre)12s %(name)30s\
 $%(price)8.2f %(weight)5.1f" % (self.__dict__)

class MexicoInstrument(Instrument):
    def __init__(self, line):
        id_, weight, price, self.name = line.split(None, 3)
        self.id_ = 'M' + id_
        self.weight = float(weight)
        self.price = float(price[1:])
        self.genre = "Mexican"

class BulgariaInstrument(Instrument):
    def __init__(self, line):
        id_, self.name, price, weight = line.split()
        self.id_ = 'B' + id_
        self.price = float(price)
        self.weight = float(weight)
        self.genre = "Bulgarian"

class Stock:
    def __init__(self):
        self.instruments = []

    def LoadInstruments(self, path):
        globber = os.path.join(path, "*" + DATA_EXT)
        for file_path in glob.glob(globber):
            file_name = os.path.split(file_path)[1]
            country, ext = file_name.rsplit('.', 1)
            if country not in SUPPORTED_COUNTRIES:
                print "Error:"
                print country, "not supported."
                print file_path, "can't be used."
                print
                continue
            file_object = open(file_path)
            # Throwing away the first line
            file_object.next() 
            for line in file_object:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                self.instruments += [eval(
                    "%sInstrument('%s')" \
                    % (country, line))]
    def SortBy(self, field="id"):
        if field not in self.instruments[0].__dict__:
            raise ValueError, \
                  "unsupported field %s" % field
        self.instruments.sort(
            key=lambda x:getattr(x, field))

    def PrintThem(self):
        print "  id        genre                           name     price    kg"
        for instrument in self.instruments:
            instrument.PrintMe()

def main():
    stock = Stock()
    stock.LoadInstruments('.')
    for each in stock.instruments[0].__dict__:
        print "Sorted by %s:" % each
        stock.SortBy(each)
        stock.PrintThem()

if __name__ == '__main__':
    main()
