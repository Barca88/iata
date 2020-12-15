import pandas as pd
import sys

def main(argv):
    imput_file = argv[0]

    if len(argv) == 1:
        output_file = "output.csv"
    else:
        output_file = argv[1]

    df = pd.read_csv(imput_file, engine='python')
    df.drop_duplicates(subset=None, inplace=True)
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
   main(sys.argv[1:])