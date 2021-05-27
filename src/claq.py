import pandas as pd
import sys

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
        return Data(self.df[exp, axis=1))

if __name__ == '__main__':
    data = Data()
    data.load(sys.stdin)
    data = data.where(lambda x: x[0] > 2)
    data.print()