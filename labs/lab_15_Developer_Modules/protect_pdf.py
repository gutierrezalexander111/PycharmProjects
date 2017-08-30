#!/usr/bin/env python
"""protect_pdf.py pdf_file -p password [-o secure_pdf_file -v]

Puts password protection on the renamed pdf_file.

If secure_pdf_file is not given, it manufactures is as:
pdf_file - ".pdf" + '_protected' + ".pdf"

Demonstrates the optparse module for parsing the command line
options and putting them into suitably-named identifiers in a 
namespace. 
"""

import optparse  
import subprocess

def ProtectPDF(pdf_file, user_pw,
               secure_pdf_file=None, verbose=False):
    """
    pdf_file = file to be password protected
    user_pw = password
    secure_pdf_file = password protected version

    Note, the unprotected version still exists.
    """
    if not secure_pdf_file:
        front, back = pdf_file.rsplit('.', 1)
        secure_pdf_file = front + "_secured." + back
    command_sequence = ["pdftk", pdf_file,
                        "output", secure_pdf_file,
                        "owner_pw", "FriedFavors",
                        "user_pw", user_pw, "allow",
                        "Printing", "DegradedPrinting",
                        "ScreenReaders"]
    if verbose:
        print "Calling:"
        print " ".join(command_sequence)
    command_process = subprocess.Popen(command_sequence,
                                       stdout=subprocess.PIPE)
    if verbose:
        for line in command_process.stdout:
            print line,

def CollectCommand(parser):
    """Here we have the parser harvest the command line and
    we check that we have an appropriate arguements.
    """
    (options, args) = parser.parse_args()
    if len(args) != 1:  
        parser.error("A pdf file name is needed.")
    options.input_pdf = args[0]
    if not options.password:
        parser.error("A password is needed.")
    return (options, args)

def main():
    parser = SetUpParsing()
    (options, args) = CollectCommand(parser)
    ProtectPDF(options.input_pdf, options.password,
               options.secure_pdf, options.verbose)

def SetUpParsing():
    """Calls add_option repeatedly, once for every unix-style
    option we need. """

    parser = optparse.OptionParser(
        "%prog input_pdf_file -p password"
        " [-o secure_pdf_file -v]""")

    parser.add_option("-o", "--secure_pdf", dest="secure_pdf",
                      default=None,
                      help="write protected pdf_file"
                      " to secure_pdf")
    parser.add_option("-p", "--password", dest="password",
                      help="password for protecting pdf")
    parser.add_option("-v", "--verbose", dest="verbose",
                      action="store_true", default=False,
                      help="verbose output")
    return parser

if __name__ == "__main__":
    main()
