import json
import argparse
import csv
import sys
from functools import partial


def base_map_char(key, char, alphabet_cardinality=26):
    if not char.isalpha():
        return char
    elif char.isupper():
        offset = 65
    else:
        offset = 97

    return chr(
        offset +
        (ord(char) - offset + key) % alphabet_cardinality
    )
    

def base_caesar_shift(key, string, alphabet_cardinality=26):
    """
    [65..90]
    [ A..Z ]

    [97..122]
    [ a..z ]
    """
    map_char = partial(base_map_char,
                       key,
                       alphabet_cardinality=alphabet_cardinality)
    return "".join([
        map_char(c) for c in string
    ])

caesar_shift = base_caesar_shift


if __name__ == "__main__":
    """
    """
    description = "process journal file."

    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument("-i", "--input_file", type=str, required=True)
    #parser.add_argument("-o", "--output_file", type=str, required=True)
    parser.add_argument("-e", "--entry_title", type=str, required=False)
    
    args = parser.parse_args()

    print("using input file: {}".format(args.input_file), file=sys.stderr)
    print("processing entry: '{}'".format(args.entry_title), file=sys.stderr)
    #print("using output file: {}".format(args.output_file), file=sys.stderr)
    print("="*80, "\n")
    
    with open(args.input_file, "r") as in_f:
        #with open(args.output_file, "w") as out_f:

        # filter "comment" rows from raw TSV file:
        filtered_comment_rows = map(
            json.loads,
            filter(lambda x: x[:1] != "#", in_f)
        )

        if args.entry_title:
            filtered_rows = filter(
                lambda x: x["title"] == args.entry_title,
                filtered_comment_rows
            )
        else:
            filtered_rows = filtered_comment_rows
            
        for l in filtered_rows:
            fragment = l["ciphertext"][0][:60]
            
            print("\nentry title: '{}'\nfragment:\t{}"
                  .format(l["title"], fragment))
            print("-"*80)
            
            for k in range(26):
                print("(key: {})\t{}"
                      .format(k, caesar_shift(k, fragment))
                )
            
