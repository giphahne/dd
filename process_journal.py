import json
import argparse
import csv
import sys
from functools import partial
#import heapq

from caesar_cipher import base_map_char, caesar_shift
from cipher_utils import load_words, base_score_text


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

        ref_words = load_words()
        print("using reference words: {}".format(len(ref_words)))
        print("using reference words: {}".format(list(ref_words)[:4]))
        score_text = partial(base_score_text, ref_words)
            
        for l in filtered_rows:
            #fragment = l["ciphertext"][0][:80]
            fragment = l["ciphertext"][0]
            
            print("\nentry title: '{}'\nfragment:\t{}"
                  .format(l["title"], fragment[:80]))
            print("-"*80)

            fragments = []
            for k in range(26):
                shifted_fragment = caesar_shift(k, fragment) 

                fragments.append((
                    score_text(shifted_fragment),
                    k,
                    shifted_fragment
                ))
                
            fragments.sort(reverse=True)

            for f in fragments[:1]:
                print("{}\tkey: {}\t{}"
                      .format(f[0], f[1], f[2])
                )

