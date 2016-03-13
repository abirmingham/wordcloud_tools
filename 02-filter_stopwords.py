import argparse, fileinput

parser = argparse.ArgumentParser(description='Filter out stopwords',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('file',
                    nargs=1,
                    type=file,
                    help='file containing stopwords')
parser.add_argument('begin',
                    nargs='?',
                    type=int,
                    default=0,
                    help='first message index (zero-based)')
parser.add_argument('end',
                    nargs='?',
                    type=int,
                    default=max,
                    help='last message index (exclusive)')

args = parser.parse_args()

stopwords = set()

for line in args.file[0]:
    stopwords.add(line.rstrip)

msg_idx = 0

for line in fileinput.input():
    if line == "<BREAK>\n":
        msg_idx += 1
        continue

print msg_idx
