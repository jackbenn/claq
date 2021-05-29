import pandas as pd
import sys
import argparse


class Data:
    def __init__(self, df=None):
        self.df = df

    def load(self, stream, sep=','):
        self.df = pd.read_csv(stream,
                              sep=sep,
                              header=None)
    
    def print(self):
        self.df.to_csv(sys.stdout)

    def cut(self, cols):
        return Data(self.df.iloc[:cols])
    
    def where(self, exp):
        return Data(self.df[self.df[exp]])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='Subcommand to run')

    #parser.add_argument('hist', help="Show a histogram")
    #parser.add_argument('plot', help="Show a plot")
    args = parser.parse_args(sys.argv[1:2])
    print(args)
    data = Data()
    data.load(sys.stdin)
    data = data.where(lambda x: x[0] > 2)
    data.print()