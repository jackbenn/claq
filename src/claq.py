#!python
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
    
    def command_print(self):
        self.df.to_csv(sys.stdout, index=False)

    def cut(self, cols):
        cols = [int(s) for s in cols.split(',')]
        return Data(self.df.iloc[:, cols])
    
    def command_sort(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('by', help='Columns')
        args = parser.parse_args(sys.argv[2:])
        cols = args.by.split(',')
        ascending = [col[0] != '-' for col in cols]
        cols = [col[1:] if col[0] == '-' else col for col in cols]
        return self.df.sort_values(by=cols,
                                   axis=0,
                                   ascending=ascending)

    
    def command_where(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('exp', help='Expression for selection')
        args = parser.parse_args(sys.argv[2:])
        return Data(self.df[self.df.apply(args.exp, axis=1)])
    
    def command_plot(self):
        parser = argparse.ArgumentParser()
        self.df.plot(0, 1)
        plt.show()

    def command_hist(self):
        parser = argparse.ArgumentParser()
        self.df.hist()
        plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='Subcommand to run')

    #parser.add_argument('hist', help="Show a histogram")
    #parser.add_argument('plot', help="Show a plot")
    print(sys.argv)
    args = parser.parse_args(sys.argv[1:2])
    data = Data()
    if not hasattr(data, "command_" + args.command):
        print(f"No such command: {args.command}")
        exit(1)
    data.load(sys.stdin)
    print(getattr(data, "command_" + args.command)())
    """
    if args.command == 'plot':
        data.plot()
    elif args.command == 'hist':
        data.hist()
    elif args.command == 'cut':
        parser.add_argument('-f', )
        cols = sys.argv[2]
        data = data.cut(cols)
    """
    #print(args.command)
    #print(sys.argv)
    #data.print()