import cmd_parse
import sys

if __name__ == "__main__":
    #print(sys.argv)
    cmd_parse.CMDParse(sys.argv[1:]).parse()
