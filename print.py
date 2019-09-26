#!/usr/bin/env python3
"""Print labels on Zebra GK420t"""
__author__ = "CTMR, Fredrik Boulund"
__date__ = "2019"

from sys import argv, exit
import textwrap
import argparse
import subprocess


def parse_args():
    desc = f"{__doc__}. Copyright {__date__} {__author__}."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("BARCODES", metavar="FILE", 
            help="Text file with one barcode per line")
    parser.add_argument("--output-zpl", dest="output_zpl", 
            default="output.zpl",
            help="Output filename of ZPL commands that are sent to printer "
                 "[%(default)s].") 
    parser.add_argument("--print", action="store_true",
            default=False,
            help="Send ZPL file directly to printer [%(default)s].")
    parser.add_argument("--printer-name", dest="printer_name",
            default="zebra-raw", 
            help="Name of raw CUPS printer to use, must be installed on system "
                 "[%(default)s].")

    if len(argv) < 2:
        parser.print_help()
        exit()

    return parser.parse_args()


def generate_ZPL(payloads, darkness=25):
    """ Generate ZPL to print Code 128 barcodes.

    ^FX Approximate coordinates to label corners
    ^FX 
    ^FX  300,25-----500,25
    ^FX     |          |
    ^FX     |          |
    ^FX  300,80-----500,80
    ^FX 
    """

    base_zpl = """
    ^XA
    ~SD{darkness}
    ^FO310,20
    ^BY1
    ^BCN,50,N,N,Y,N
    ^FD{text}^FS
    ^CFC,10,5
    ^FO310,80
    ^FD{text}^FS
    ^XZ
    """

    for payload in payloads:
        yield textwrap.dedent(base_zpl.format(darkness=darkness, text=payload))


def generate_payloads(textfile):
    """ Generate payloads from lines in textfile. """

    with open(textfile) as f:
        for line in f:
            yield line.strip()


def main(args):

    payloads = generate_payloads(args.BARCODES)
    zpls = generate_ZPL(payloads)
    with open(args.output_zpl, "w") as outf:
        for label in zpls:
            outf.write(f"{label}")

    if args.print:
        subprocess.run(f"lp -d {args.printer_name} {args.output_zpl}".split())


if __name__ == "__main__":
    args = parse_args()
    main(args)
