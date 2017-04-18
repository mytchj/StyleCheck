import argparse
import pprint

def main(args):
    style_check, file_in = find_style_errors(args)
    print("Line Length: " + str(style_check['length']))
    print("White Space: " + str(style_check['whitespace']))
    print("Indentation: " + str(style_check['indentation']))


# void --> cmd line args
# returns formatted command line args
def cmd_io():
    
    parser = argparse.ArgumentParser(description="Style checks a file")
    
    # required args
    parser.add_argument('inFile', type = argparse.FileType('r'),\
            help = "input file to style check")
    
    # optional args
    parser.add_argument('-maxlen', type = int, default = 80,\
            help = "'length': line length check (default=80)")
    parser.add_argument('-indspace', type = int, default = 4,\
            help = "'indent space': number of spaces per indent (default=4)")
    parser.add_argument('-ws', action = 'store_false',\
            help = "'whitespace': turn off whitespace check")
    parser.add_argument('-ind', action = 'store_false',\
            help = "'indentation': turn off indentation check")
 
    return parser.parse_args()


# String int --> Bool
# returns True when length of string is less than threshold
def check_len(in_str, threshold):
    return len(in_str.rstrip('\n')) > threshold


# String --> Bool
# returns True when string has no whitespace at right end
def check_ws(in_str):
    in_str = in_str.rstrip('\n').lstrip(' ')
    return not (in_str == in_str.rstrip(' '))

# String int --> Bool
# returns True when left whitespace is devisable by tabspacing int
def check_ind(in_str, tabspacing):
    return (len(in_str) - len(in_str.lstrip(' '))) % tabspacing 


# Namespace --> Dict
# returns a dict with the line numbers for each style check error
def find_style_errors(args):
    style_breaks = {'length': [], 'whitespace': [], 'indentation': []}
    
    file_in = args.inFile.readlines()

    line_num = 1   
    for line in file_in:
        if args.maxlen:
            if check_len(line, args.maxlen):
                style_breaks['length'].append(line_num)

        if args.ws:
            if check_ws(line):
                style_breaks['whitespace'].append(line_num)

        if args.ind:
            if check_ind(line, args.indspace):
                style_breaks['indentation'].append(line_num)

        line_num += 1
    
    return style_breaks, file_in

def fix_style_errors(args, style_breaks, file_in):
    pass 


if __name__ == '__main__':
    main(cmd_io())

