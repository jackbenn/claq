import pandas as pd
import sys
import argparse
import matplotlib.pyplot as plt


class Data:
    def __init__(self, df=None):
        self.df = df

    def load(self, stream, sep=',', header='infer'):
        self.df = pd.read_csv(stream,
                              sep=sep,
                              header=header)
    
    def print(self):
        self.df.to_csv(sys.stdout, index=False)

    def cut(self, cols):
        cols = [int(s) for s in cols.split(',')]
        return Data(self.df.iloc[:, cols])
    
    def where(self, exp):
        return Data(self.df[self.df.apply(exp, axis=1)])
    
    def plot(self):
        self.df.plot(0, 1)
        plt.show()

    def hist(self):
        self.df.hist()
        plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='Subcommand to run')

    #parser.add_argument('hist', help="Show a histogram")
    #parser.add_argument('plot', help="Show a plot")
    args = parser.parse_args(sys.argv[1:2])
    data = Data()
    data.load(sys.stdin)
    if args.command == 'plot':
        data.plot()
    elif args.command == 'hist':
        data.hist()
    elif args.command == 'cut':
        cols = sys.argv[2]
        data = data.cut(cols)
    data.print()