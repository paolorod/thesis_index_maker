import indexmaker

import os
import sys
import argparse

from logging.config import dictConfig
import yaml
with open ( 'logging.yaml' ) as flog:
    dictConfig ( yaml.load ( flog ) )

import logging

log = logging.getLogger()

__doc__ = "Index Analyser"

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Word docx Input file to process")
    parser.add_argument('-s', '--style', help='the word style name to select paragraphs',default="List Paragraph")
    parser.add_argument('-t', '--type', help="the type of index generator, valid values: raw,structured,debug. \n If structured is specified then the structure file must be specified as well",default="raw")
    parser.add_argument('-y', '--structure', help='the YAML file that contains the structure')
    parser.add_argument('-o', '--outfile', help="the output file that will contain the index")

    args = parser.parse_args(arguments)
    if args.type=="raw":
        logging.info("Starting Raw Index Creation")
        indexmaker.create_raw_index(args.infile, args.outfile, args.style)
    elif args.type=="structured":
        logging.info("Starting Structured Index Creation")
        if(args.structure is None):
            print("Is necessary to define a structure file if the type is structured. See the help (launch with -h)")
        else:
            indexmaker.create_structured_index(args.infile, args.outfile, args.style, args.structure)
    elif args.type=="debug":
        logging.info("Starting Debugging Document Numeritation")
        indexmaker.debug_numeration(args.infile, args.style)

    else:
        print("index type not recognised")

    log.info("Finished")
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
