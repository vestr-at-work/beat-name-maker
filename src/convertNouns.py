#!/usr/bin/env python3

import json

def main():
    with open("nouns.txt", 'r') as inputNounsFile:
        lines = inputNounsFile.readlines()

    nounList = []
    for line in lines:
        line = line.split('.')
        nounList.append(line[1].strip())

    print(json.dumps(nounList, indent=4))


if __name__ == '__main__':
    main()