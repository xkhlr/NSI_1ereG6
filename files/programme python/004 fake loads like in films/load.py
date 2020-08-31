import os, platform, random
from time import sleep
from codecs import*
import codecs
# list1=["### Decoding Table\n","'\x00'     #  0x00 -> NULL\n","'\x01'     #  0x01 -> START OF HEADING\n","'\x02'     #  0x02 -> START OF TEXT\n","'\x03'     #  0x03 -> END OF TEXT\n","'\x04'     #  0x04 -> END OF TRANSMISSION\n","'\x05'     #  0x05 -> ENQUIRY\n","'\x06'     #  0x06 -> ACKNOWLEDGE\n","'\x07'     #  0x07 -> BELL\n","'\x08'     #  0x08 -> BACKSPACE\n","'\t'       #  0x09 -> HORIZONTAL TABULATION\n","'\\n'       #  0x0A -> LINE FEED\n","'\x0b'     #  0x0B -> VERTICAL TABULATION\n","'\x0c'     #  0x0C -> FORM FEED\n","'\r'       #  0x0D -> CARRIAGE RETURN\n","'\x0e'     #  0x0E -> SHIFT OUT\n","'\x0f'     #  0x0F -> SHIFT IN\n","'\x10'     #  0x10 -> DATA LINK ESCAPE\n","'\x11'     #  0x11 -> DEVICE CONTROL ONE\n","'\x12'     #  0x12 -> DEVICE CONTROL TWO\n","'\x13'     #  0x13 -> DEVICE CONTROL THREE\n","'\x14'     #  0x14 -> DEVICE CONTROL FOUR\n","'\x15'     #  0x15 -> NEGATIVE ACKNOWLEDGE\n","'\x16'     #  0x16 -> SYNCHRONOUS IDLE\n","'\x17'     #  0x17 -> END OF TRANSMISSION BLOCK\n","'\x18'     #  0x18 -> CANCEL\n","'\x19'     #  0x19 -> END OF MEDIUM\n","'\x1a'     #  0x1A -> SUBSTITUTE\n","'\x1b'     #  0x1B -> ESCAPE\n","'\x1c'     #  0x1C -> FILE SEPARATOR\n","'\x1d'     #  0x1D -> GROUP SEPARATOR\n","'\x1e'     #  0x1E -> RECORD SEPARATOR\n","'\x1f'     #  0x1F -> UNIT SEPARATOR\n","' '        #  0x20 -> SPACE\n","'!'        #  0x21 -> EXCLAMATION MARK\n","""'"'        #  0x22 -> QUOTATION MARK\n""","'#'        #  0x23 -> NUMBER SIGN","\n'$'        #  0x24 -> DOLLAR SIGN\n","'%'        #  0x25 -> PERCENT SIGN\n","'&'        #  0x26 -> AMPERSAND\n",""""'"        #  0x27 -> APOSTROPHE\n""","'('        #  0x28 -> LEFT PARENTHESIS\n","')'        #  0x29 -> RIGHT PARENTHESIS\n","'*'        #  0x2A -> ASTERISK","\n'+'        #  0x2B -> PLUS SIGN\n","','        #  0x2C -> COMMA\n","'-'        #  0x2D -> HYPHEN-MINUS\n","'.'        #  0x2E -> FULL STOP\n","'/'        #  0x2F -> SOLIDUS\n","'0'        #  0x30 -> DIGIT ZERO\n","'1'        #  0x31 -> DIGIT ONE\n","'2'        #  0x32 -> DIGIT TWO\n","'3'        #  0x33 -> DIGIT THREE\n","'4'        #  0x34 -> DIGIT FOUR\n","'5'        #  0x35 -> DIGIT FIVE\n","'6'        #  0x36 -> DIGIT SIX\n","'7'        #  0x37 -> DIGIT SEVEN\n","'8'        #  0x38 -> DIGIT EIGHT\n","'9'        #  0x39 -> DIGIT NINE\n","':'        #  0x3A -> COLON\n","';'        #  0x3B -> SEMICOLON\n","'<'        #  0x3C -> LESS-THAN SIGN\n","'='        #  0x3D -> EQUALS SIGN\n","'>'        #  0x3E -> GREATER-THAN SIGN\n","'?'        #  0x3F -> QUESTION MARK\n","'@'        #  0x40 -> COMMERCIAL AT\n","'A'        #  0x41 -> LATIN CAPITAL LETTER A\n","'B'        #  0x42 -> LATIN CAPITAL LETTER B\n","'C'        #  0x43 -> LATIN CAPITAL LETTER C\n","'D'        #  0x44 -> LATIN CAPITAL LETTER D\n","'E'        #  0x45 -> LATIN CAPITAL LETTER E\n","'F'        #  0x46 -> LATIN CAPITAL LETTER F\n","'G'        #  0x47 -> LATIN CAPITAL LETTER G\n","'H'        #  0x48 -> LATIN CAPITAL LETTER H\n","'I'        #  0x49 -> LATIN CAPITAL LETTER I\n","'J'        #  0x4A -> LATIN CAPITAL LETTER J\n","'K'        #  0x4B -> LATIN CAPITAL LETTER K\n","'L'        #  0x4C -> LATIN CAPITAL LETTER L\n","'M'        #  0x4D -> LATIN CAPITAL LETTER M\n","'N'        #  0x4E -> LATIN CAPITAL LETTER N\n","'O'        #  0x4F -> LATIN CAPITAL LETTER O\n","'P'        #  0x50 -> LATIN CAPITAL LETTER P\n","'Q'        #  0x51 -> LATIN CAPITAL LETTER Q\n","'R'        #  0x52 -> LATIN CAPITAL LETTER R\n","'S'        #  0x53 -> LATIN CAPITAL LETTER S\n","'T'        #  0x54 -> LATIN CAPITAL LETTER T\n","'U'        #  0x55 -> LATIN CAPITAL LETTER U\n","'V'        #  0x56 -> LATIN CAPITAL LETTER V\n","'W'        #  0x57 -> LATIN CAPITAL LETTER W\n","'X'        #  0x58 -> LATIN CAPITAL LETTER X\n","'Y'        #  0x59 -> LATIN CAPITAL LETTER Y\n","'Z'        #  0x5A -> LATIN CAPITAL LETTER Z\n'['        #  0x5B -> LEFT SQUARE BRACKET\n","'\\'       #  0x5C -> REVERSE SOLIDUS\n","']'        #  0x5D -> RIGHT SQUARE BRACKET\n","'^'        #  0x5E -> CIRCUMFLEX ACCENT\n","'_'        #  0x5F -> LOW LINE\n","'`'        #  0x60 -> GRAVE ACCENT\n","'a'        #  0x61 -> LATIN SMALL LETTER A\n","'b'        #  0x62 -> LATIN SMALL LETTER B\n","'c'        #  0x63 -> LATIN SMALL LETTER C\n","'d'        #  0x64 -> LATIN SMALL LETTER D\n","'e'        #  0x65 -> LATIN SMALL LETTER E\n","'f'        #  0x66 -> LATIN SMALL LETTER F\n","'g'        #  0x67 -> LATIN SMALL LETTER G\n","'h'        #  0x68 -> LATIN SMALL LETTER H\n","'i'        #  0x69 -> LATIN SMALL LETTER I\n","'j'        #  0x6A -> LATIN SMALL LETTER J\n","'k'        #  0x6B -> LATIN SMALL LETTER K\n","'l'        #  0x6C -> LATIN SMALL LETTER L\n","'m'        #  0x6D -> LATIN SMALL LETTER M\n","'n'        #  0x6E -> LATIN SMALL LETTER N\n","'o'        #  0x6F -> LATIN SMALL LETTER O\n","'p'        #  0x70 -> LATIN SMALL LETTER P\n","'q'        #  0x71 -> LATIN SMALL LETTER Q\n","'r'        #  0x72 -> LATIN SMALL LETTER R\n","'s'        #  0x73 -> LATIN SMALL LETTER S\n","'t'        #  0x74 -> LATIN SMALL LETTER T\n","'u'        #  0x75 -> LATIN SMALL LETTER U\n","'v'        #  0x76 -> LATIN SMALL LETTER V\n","'w'        #  0x77 -> LATIN SMALL LETTER W\n","'x'        #  0x78 -> LATIN SMALL LETTER X\n","'y'        #  0x79 -> LATIN SMALL LETTER Y\n","'z'        #  0x7A -> LATIN SMALL LETTER Z\n","'{'        #  0x7B -> LEFT CURLY BRACKET\n","'|'        #  0x7C -> VERTICAL LINE\n","'}'        #  0x7D -> RIGHT CURLY BRACKET\n","'~'        #  0x7E -> TILDE\n","'\x7f'     #  0x7F -> DELETE\n","'\u20ac'   #  0x80 -> EURO SIGN\n","'\ufffe'   #  0x81 -> UNDEFINED\n","'\u201a'   #  0x82 -> SINGLE LOW-9 QUOTATION MARK\n","'\u0192'   #  0x83 -> LATIN SMALL LETTER F WITH HOOK\n","'\u201e'   #  0x84 -> DOUBLE LOW-9 QUOTATION MARK\n","'\u2026'   #  0x85 -> HORIZONTAL ELLIPSIS\n","'\u2020'   #  0x86 -> DAGGER\n","'\u2021'   #  0x87 -> DOUBLE DAGGER\n","'\u02c6'   #  0x88 -> MODIFIER LETTER CIRCUMFLEX ACCENT\n","'\u2030'   #  0x89 -> PER MILLE SIGN\n","'\u0160'   #  0x8A -> LATIN CAPITAL LETTER S WITH CARON\n","'\u2039'   #  0x8B -> SINGLE LEFT-POINTING ANGLE QUOTATION MARK\n","'\u0152'   #  0x8C -> LATIN CAPITAL LIGATURE OE\n","'\ufffe'   #  0x8D -> UNDEFINED\n","'\u017d'   #  0x8E -> LATIN CAPITAL LETTER Z WITH CARON\n","'\ufffe'   #  0x8F -> UNDEFINED\n","'\ufffe'   #  0x90 -> UNDEFINED\n","'\u2018'   #  0x91 -> LEFT SINGLE QUOTATION MARK\n","'\u2019'   #  0x92 -> RIGHT SINGLE QUOTATION MARK\n","'\u201c'   #  0x93 -> LEFT DOUBLE QUOTATION MARK\n","'\u201d'   #  0x94 -> RIGHT DOUBLE QUOTATION MARK\n","'\u2022'   #  0x95 -> BULLET\n","'\u2013'   #  0x96 -> EN DASH\n","'\u2014'   #  0x97 -> EM DASH\n","'\u02dc'   #  0x98 -> SMALL TILDE\n","'\u2122'   #  0x99 -> TRADE MARK SIGN\n","'\u0161'   #  0x9A -> LATIN SMALL LETTER S WITH CARON\n","'\u203a'   #  0x9B -> SINGLE RIGHT-POINTING ANGLE QUOTATION MARK\n","'\u0153'   #  0x9C -> LATIN SMALL LIGATURE OE\n","'\ufffe'   #  0x9D -> UNDEFINED\n","'\u017e'   #  0x9E -> LATIN SMALL LETTER Z WITH CARON\n","'\u0178'   #  0x9F -> LATIN CAPITAL LETTER Y WITH DIAERESIS\n","'\xa0'     #  0xA0 -> NO-BREAK SPACE\n","'\xa1'     #  0xA1 -> INVERTED EXCLAMATION MARK\n","'\xa2'     #  0xA2 -> CENT SIGN\n","'\xa3'     #  0xA3 -> POUND SIGN\n","'\xa4'     #  0xA4 -> CURRENCY SIGN\n","'\xa5'     #  0xA5 -> YEN SIGN\n","'\xa6'     #  0xA6 -> BROKEN BAR\n","'\xa7'     #  0xA7 -> SECTION SIGN\n","'\xa8'     #  0xA8 -> DIAERESIS\n","'\xa9'     #  0xA9 -> COPYRIGHT SIGN\n","'\xaa'     #  0xAA -> FEMININE ORDINAL INDICATOR\n","'\xab'     #  0xAB -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK\n","'\xac'     #  0xAC -> NOT SIGN\n","'\xad'     #  0xAD -> SOFT HYPHEN\n","'\xae'     #  0xAE -> REGISTERED SIGN\n","'\xaf'     #  0xAF -> MACRON\n","'\xb0'     #  0xB0 -> DEGREE SIGN\n","'\xb1'     #  0xB1 -> PLUS-MINUS SIGN\n","'\xb2'     #  0xB2 -> SUPERSCRIPT TWO\n","'\xb3'     #  0xB3 -> SUPERSCRIPT THREE\n","'\xb4'     #  0xB4 -> ACUTE ACCENT\n","'\xb5'     #  0xB5 -> MICRO SIGN\n","'\xb6'     #  0xB6 -> PILCROW SIGN\n","'\xb7'     #  0xB7 -> MIDDLE DOT\n","'\xb8'     #  0xB8 -> CEDILLA\n","'\xb9'     #  0xB9 -> SUPERSCRIPT ONE\n","'\xba'     #  0xBA -> MASCULINE ORDINAL INDICATOR\n","'\xbb'     #  0xBB -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK\n","'\xbc'     #  0xBC -> VULGAR FRACTION ONE QUARTER\n","'\xbd'     #  0xBD -> VULGAR FRACTION ONE HALF\n","'\xbe'     #  0xBE -> VULGAR FRACTION THREE QUARTERS\n","'\xbf'     #  0xBF -> INVERTED QUESTION MARK\n","'\xc0'     #  0xC0 -> LATIN CAPITAL LETTER A WITH GRAVE\n","'\xc1'     #  0xC1 -> LATIN CAPITAL LETTER A WITH ACUTE\n","'\xc2'     #  0xC2 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX\n","'\xc3'     #  0xC3 -> LATIN CAPITAL LETTER A WITH TILDE\n","'\xc4'     #  0xC4 -> LATIN CAPITAL LETTER A WITH DIAERESIS\n","'\xc5'     #  0xC5 -> LATIN CAPITAL LETTER A WITH RING ABOVE\n","'\xc6'     #  0xC6 -> LATIN CAPITAL LETTER AE\n","'\xc7'     #  0xC7 -> LATIN CAPITAL LETTER C WITH CEDILLA\n","'\xc8'     #  0xC8 -> LATIN CAPITAL LETTER E WITH GRAVE\n","'\xc9'     #  0xC9 -> LATIN CAPITAL LETTER E WITH ACUTE\n","'\xca'     #  0xCA -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX\n","'\xcb'     #  0xCB -> LATIN CAPITAL LETTER E WITH DIAERESIS\n","'\xcc'     #  0xCC -> LATIN CAPITAL LETTER I WITH GRAVE\n","'\xcd'     #  0xCD -> LATIN CAPITAL LETTER I WITH ACUTE\n","'\xce'     #  0xCE -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX\n","'\xcf'     #  0xCF -> LATIN CAPITAL LETTER I WITH DIAERESIS\n","'\xd0'     #  0xD0 -> LATIN CAPITAL LETTER ETH\n","'\xd1'     #  0xD1 -> LATIN CAPITAL LETTER N WITH TILDE\n","'\xd2'     #  0xD2 -> LATIN CAPITAL LETTER O WITH GRAVE\n","'\xd3'     #  0xD3 -> LATIN CAPITAL LETTER O WITH ACUTE\n","'\xd4'     #  0xD4 -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX\n","'\xd5'     #  0xD5 -> LATIN CAPITAL LETTER O WITH TILDE\n","'\xd6'     #  0xD6 -> LATIN CAPITAL LETTER O WITH DIAERESIS\n","'\xd7'     #  0xD7 -> MULTIPLICATION SIGN\n","'\xd8'     #  0xD8 -> LATIN CAPITAL LETTER O WITH STROKE\n",
# "'\xd9'     #  0xD9 -> LATIN CAPITAL LETTER *U WITH GRAVE\n","'\xda'     #  0xDA -> LATIN CAPITAL LETTER U WITH ACUTE\n","'\xdb'     #  0xDB -> LATIN CAPITAL LETTER U WITH CIRCUMFLEX\n","'\xdc'     #  0xDC -> LATIN CAPITAL LETTER U WITH DIAERESIS\n","'\xdd'     #  0xDD -> LATIN CAPITAL LETTER Y WITH ACUTE\n","'\xde'     #  0xDE -> LATIN CAPITAL LETTER THORN\n","'\xdf'     #  0xDF -> LATIN SMALL LETTER SHARP S\n","'\xe0'     #  0xE0 -> LATIN SMALL LETTER A WITH GRAVE\n","'\xe1'     #  0xE1 -> LATIN SMALL LETTER A WITH ACUTE\n","'\xe2'     #  0xE2 -> LATIN SMALL LETTER A WITH CIRCUMFLEX\n","'\xe3'     #  0xE3 -> LATIN SMALL LETTER A WITH TILDE\n","'\xe4'     #  0xE4 -> LATIN SMALL LETTER A WITH DIAERESIS\n","'\xe5'     #  0xE5 -> LATIN SMALL LETTER A WITH RING ABOVE\n","'\xe6'     #  0xE6 -> LATIN SMALL LETTER AE\n","'\xe7'     #  0xE7 -> LATIN SMALL LETTER C WITH CEDILLA\n","'\xe8'     #  0xE8 -> LATIN SMALL LETTER E WITH GRAVE\n","'\xe9'     #  0xE9 -> LATIN SMALL LETTER E WITH ACUTE\n","'\xea'     #  0xEA -> LATIN SMALL LETTER E WITH CIRCUMFLEX\n","'\xeb'     #  0xEB -> LATIN SMALL LETTER E WITH DIAERESIS\n","'\xec'     #  0xEC -> LATIN SMALL LETTER I WITH GRAVE\n","'\xed'     #  0xED -> LATIN SMALL LETTER I WITH ACUTE\n","'\xee'     #  0xEE -> LATIN SMALL LETTER I WITH CIRCUMFLEX\n","'\xef'     #  0xEF -> LATIN SMALL LETTER I WITH DIAERESIS\n","'\xf0'     #  0xF0 -> LATIN SMALL LETTER ETH\n","'\xf1'     #  0xF1 -> LATIN SMALL LETTER N WITH TILDE\n","'\xf2'     #  0xF2 -> LATIN SMALL LETTER O WITH GRAVE\n","'\xf3'     #  0xF3 -> LATIN SMALL LETTER O WITH ACUTE\n","'\xf4'     #  0xF4 -> LATIN SMALL LETTER O WITH CIRCUMFLEX\n","'\xf5'     #  0xF5 -> LATIN SMALL LETTER O WITH TILDE\n","'\xf6'     #  0xF6 -> LATIN SMALL LETTER O WITH DIAERESIS\n","'\xf7'     #  0xF7 -> DIVISION SIGN\n","'\xf8'     #  0xF8 -> LATIN SMALL LETTER O WITH STROKE\n","'\xf9'     #  0xF9 -> LATIN SMALL LETTER U WITH GRAVE\n","'\xfa'     #  0xFA -> LATIN SMALL LETTER U WITH ACUTE\n","'\xfb'     #  0xFB -> LATIN SMALL LETTER U WITH CIRCUMFLEX\n","'\xfc'     #  0xFC -> LATIN SMALL LETTER U WITH DIAERESIS\n","'\xfd'     #  0xFD -> LATIN SMALL LETTER Y WITH ACUTE\n","'\xfe'     #  0xFE -> LATIN SMALL LETTER THORN\n","'\xff'     #  0xFF -> LATIN SMALL LETTER Y WITH DIAERESIS"]
# for letter in list1:
#     print(letter)

# pause=input("Appuyez sur entré pour continuer")
# pause=input("Appuyez sur entré pour continuer")
Time=0
spaces=["                                                                                                     ", "                                                                                                    ", "                                                                                                   ", "                                                                                                  ", "                                                                                                 ", "                                                                                                ", "                                                                                               ", "                                                                                              ", "                                                                                             ", "                                                                                            ", "                                                                                           ", "                                                                                          ", "                                                                                         ", "                                                                                        ", "                                                                                       ", "                                                                                      ", "                                                                                     ", "                                                                                    ", "                                                                                   ","                                                                                  ","                                                                                 ", "                                                                                ", "                                                                               ", "                                                                              ", "                                                                             ", "                                                                            ", "                                                                           ", "                                                                          ", "                                                                         ", "                                                                        ", "                                                                       ", "                                                                      ", "                                                                     ", "                                                                    ", "                                                                   ", "                                                                  ", "                                                                 ", "                                                                ", "                                                               ", "                                                              ", "                                                             ", "                                                            ", "                                                           ", "                                                          ", "                                                         ", "                                                        ", "                                                       ", "                                                      ", "                                                     ", "                                                    ", "                                                   ", "                                                  ", "                                                 ", "                                                ", "                                               ", "                                              ", "                                             ", "                                            ", "                                           ", "                                          ", "                                         ", "                                        ", "                                       ", "                                      ", "                                     ", "                                    ", "                                   ", "                                  ", "                                 ", "                                ", "                               ", "                              ", "                             ", "                            ", "                           ", "                          ", "                         ", "                        ", "                       ", "                      ", "                     ", "                    ", "                   ", "                  ", "                 ", "                ", "               ", "              ", "             ", "            ", "           ", "          ", "         ", "        ", "       ", "      ", "     ", "    ", "   ", "  ", "",""]
# ping=random.randint(5, 10)
load_sentence=[" ","S","'","i","l"," ","v","o","u","s"," ","p","l","a","i","t"," ","m","e","r","c","i"," ","d","e"," ","b","i","e","n"," ","v","o","u","l","o","i","r"," ","p","a","t","i","e","n","t","e","r"," ","p","e","n","d","a","n","t"," ","q","u","e"," ","v","o","t","r","e"," ","f","i","c","h","i","e","r"," ","e","s","t"," ","e","n","t","r","a","i","n"," ","d","e"," ","c","h","a","r","g","e","r"," ",".",".",".","."," "]
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","é","ê","è","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","#","@"]
# emoji=["😀","😃","😄","😁","😆","😅","😂","🤣","☺️","😊","😇","🙂","🙃","😉","😌","😍","🥰","😘","😗","😙","😚","😋","😛","😝","😜","🤪","🤨","🧐","🤓","😎","🤩","🥳","😏","😒","😞","😔","😟","😕","🙁","☹️","😣","😖","😫",😩","🥺","😢","😭","😤","😠","😡","🤬","🤯","😳","🥵","🥶","😱","😨","😰","😥","😓","🤗","🤔","🤭","🤫","🤥","😶","😐","😑","😬","🙄","😯","😦","😧","😮","😲","😴","🤤","😪","😵","🤐","🥴","🤢","🤮","🤧","😷","🤒","🤕","🤑","🤠","😈","👿","👹","👺","🤡","💩","👻","💀","☠️","👽","👾","🤖","🎃","😺","😸","😹","😻","😼","😽","🙀","😿","😾","🤲","👐","🙌","👏","🤝","👍","👎","👊","✊","🤛","🤜","🤞","✌️","🤟","🤘","👌","👈","👉","👆","👇","☝️","✋","🤚","🖐️","🖖","👋","🤙","💪","🖕","✍️","🙏","🦶","🦵","💄","💋","👄","🦷","👅","👂","👃","👣","👁️","👀","🧠","🗣️","👤","👥","👶","👧","🧒","👦","👩","🧑","👨","👩‍🦱","👨‍🦱","👩‍🦰","👨‍🦰","👱‍♀️","👱","👩‍🦳","👨‍🦳","👩‍🦲","👨‍🦲","🧔","👵","🧓","👴","👲","👳‍♀️","👳","🧕","👮‍♀️","👮","👷‍♀️","👷","💂‍♀️","💂","🕵️‍♀️","🕵️","👩‍⚕️","👨‍⚕️","👩‍🌾","👨‍🌾","👩‍🍳","👨‍🍳","👩‍🎓","👨‍🎓","👩‍🎤","👨‍🎤","👩‍🏫","👨‍🏫","👩‍🏭","👨‍🏭","👩‍💻","👨‍💻","👩‍💼","👨‍💼","👩‍🔧","👨‍🔧","👩‍🔬","👨‍🔬","👩‍🎨","👨‍🎨","👩‍🚒","👨‍🚒","👩‍✈️","👨‍✈️","👩‍🚀","👨‍🚀","👩‍⚖️","👨‍⚖️","👰","🤵","👸","🤴","🦸‍♀️","🦸‍♂️","🦹‍♀️","🦹‍♂️","🤶","🎅","🧙‍♀️","🧙‍♂️","🧝‍♀️","🧝‍♂️","🧛‍♀️","🧛‍♂️","🧟‍♀️","🧟‍♂️","🧞‍♀️","🧞‍♂️","🧜‍♀️","🧜‍♂️","🧚‍♀️","🧚‍♂️","👼","🤰","🤱","🙇‍♀️","🙇","💁","💁‍♂️","🙅","🙅‍♂️","🙆","🙆‍♂️","🙋","🙋‍♂️","🤦‍♀️","🤦‍♂️","🤷‍♀️","🤷‍♂️","🙎","🙎‍♂️","🙍","🙍‍♂️","💇","💇‍♂️","💆","💆‍♂️","🧖‍♀️","🧖‍♂️","💅","🤳","💃","🕺","👯","👯‍♂️","🕴️","🚶‍♀️","🚶","🏃‍♀️","🏃","👫","👭","👬","💑","👩‍❤️‍👩","👨‍❤️‍👨","💏","👩‍❤️‍💋‍👩","👨‍❤️‍💋‍👨","👪","👨‍👩‍👧","👨‍👩‍👧‍👦","👨‍👩‍👦‍👦","👨‍👩‍👧‍👧","👩‍👩‍👦","👩‍👩‍👧","👩‍👩‍👧‍👦","👩‍👩‍👦‍👦","👩‍👩‍👧‍👧","👨‍👨‍👦","👨‍👨‍👧","👨‍👨‍👧‍👦","👨‍👨‍👦‍👦","👨‍👨‍👧‍👧","👩‍👦","👩‍👧","👩‍👧‍👦","👩‍👦‍👦","👩‍👧‍👧","👨‍👦","👨‍👧","👨‍👧‍👦","👨‍👦‍👦","👨‍👧‍👧","🧶","🧵","🧥","🥼","👚","👕","👖","👔","👗","👙","👘","🥿","👠","👡","👢","👞","👟","🥾","🧦","🧤","🧣,"🎩","🧢","👒","🎓","⛑️","👑","💍","👝","👛","👜","💼","🎒","🧳","👓","🕶️","🥽","🌂"]
simp_emojies=["●","○","■","□","°","¤","¡","¿","¥","£","€","$","•","%","&","@",chr(9794),chr(9792),"\u2122", "\xae", "\xa9","^","_","\u201a",chr(6553),"\u201e","\u2026","\u2026","\u2020","\u2021","\u2030","\u0160","\u2039","\u017d","\u2018","\u2019","\u201c","\u201d","\u2014",]
"\u02dc","\u0161","\u203a","\u017e","\u0178","\xa1","\xa2","\xa6","\xa7",chr(169),"\xaa","\xab","\xae""\xaf","'\xb0'     #  0xB0 -> DEGREE SIGN\n","'\xb1'     #  0xB1 -> PLUS-MINUS SIGN\n","'\xb2'     #  0xB2 -> SUPERSCRIPT TWO\n","'\xb3'     #  0xB3 -> SUPERSCRIPT THREE\n","'\xb4'     #  0xB4 -> ACUTE ACCENT\n","'\xb5'     #  0xB5 -> MICRO SIGN\n","'\xb6'     #  0xB6 -> PILCROW SIGN\n","'\xb7'     #  0xB7 -> MIDDLE DOT\n","'\xb8'     #  0xB8 -> CEDILLA\n","'\xb9'     #  0xB9 -> SUPERSCRIPT ONE\n","'\xba'     #  0xBA -> MASCULINE ORDINAL INDICATOR\n","'\xbb'     #  0xBB -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK\n","'\xbc'     #  0xBC -> VULGAR FRACTION ONE QUARTER\n","'\xbd'     #  0xBD -> VULGAR FRACTION ONE HALF\n","'\xbe'     #  0xBE -> VULGAR FRACTION THREE QUARTERS\n","'\xbf'     #  0xBF -> INVERTED QUESTION MARK\n","'\xc0'     #  0xC0 -> LATIN CAPITAL LETTER A WITH GRAVE\n","'\xc1'     #  0xC1 -> LATIN CAPITAL LETTER A WITH ACUTE\n","'\xc2'     #  0xC2 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX\n","'\xc3'     #  0xC3 -> LATIN CAPITAL LETTER A WITH TILDE\n","'\xc4'     #  0xC4 -> LATIN CAPITAL LETTER A WITH DIAERESIS\n","'\xc5'     #  0xC5 -> LATIN CAPITAL LETTER A WITH RING ABOVE\n","'\xc6'     #  0xC6 -> LATIN CAPITAL LETTER AE\n","'\xc7'     #  0xC7 -> LATIN CAPITAL LETTER C WITH CEDILLA\n","'\xc8'     #  0xC8 -> LATIN CAPITAL LETTER E WITH GRAVE\n","'\xc9'     #  0xC9 -> LATIN CAPITAL LETTER E WITH ACUTE\n","'\xca'     #  0xCA -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX\n","'\xcb'     #  0xCB -> LATIN CAPITAL LETTER E WITH DIAERESIS\n","'\xcc'     #  0xCC -> LATIN CAPITAL LETTER I WITH GRAVE\n","'\xcd'     #  0xCD -> LATIN CAPITAL LETTER I WITH ACUTE\n","'\xce'     #  0xCE -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX\n","'\xcf'     #  0xCF -> LATIN CAPITAL LETTER I WITH DIAERESIS\n","'\xd0'     #  0xD0 -> LATIN CAPITAL LETTER ETH\n","'\xd1'     #  0xD1 -> LATIN CAPITAL LETTER N WITH TILDE\n","'\xd2'     #  0xD2 -> LATIN CAPITAL LETTER O WITH GRAVE\n","'\xd3'     #  0xD3 -> LATIN CAPITAL LETTER O WITH ACUTE\n","'\xd4'     #  0xD4 -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX\n","'\xd5'     #  0xD5 -> LATIN CAPITAL LETTER O WITH TILDE\n","'\xd6'     #  0xD6 -> LATIN CAPITAL LETTER O WITH DIAERESIS\n","'\xd7'     #  0xD7 -> MULTIPLICATION SIGN\n","'\xd8'     #  0xD8 -> LATIN CAPITAL LETTER O WITH STROKE\n",
# "'\xd9'     #  0xD9 -> LATIN CAPITAL LETTER *U WITH GRAVE\n","'\xda'     #  0xDA -> LATIN CAPITAL LETTER U WITH ACUTE\n","'\xdb'     #  0xDB -> LATIN CAPITAL LETTER U WITH CIRCUMFLEX\n","'\xdc'     #  0xDC -> LATIN CAPITAL LETTER U WITH DIAERESIS\n","'\xdd'     #  0xDD -> LATIN CAPITAL LETTER Y WITH ACUTE\n","'\xde'     #  0xDE -> LATIN CAPITAL LETTER THORN\n","'\xdf'     #  0xDF -> LATIN SMALL LETTER SHARP S\n","'\xe0'     #  0xE0 -> LATIN SMALL LETTER A WITH GRAVE\n","'\xe1'     #  0xE1 -> LATIN SMALL LETTER A WITH ACUTE\n","'\xe2'     #  0xE2 -> LATIN SMALL LETTER A WITH CIRCUMFLEX\n","'\xe3'     #  0xE3 -> LATIN SMALL LETTER A WITH TILDE\n","'\xe4'     #  0xE4 -> LATIN SMALL LETTER A WITH DIAERESIS\n","'\xe5'     #  0xE5 -> LATIN SMALL LETTER A WITH RING ABOVE\n","'\xe6'     #  0xE6 -> LATIN SMALL LETTER AE\n","'\xe7'     #  0xE7 -> LATIN SMALL LETTER C WITH CEDILLA\n","'\xe8'     #  0xE8 -> LATIN SMALL LETTER E WITH GRAVE\n","'\xe9'     #  0xE9 -> LATIN SMALL LETTER E WITH ACUTE\n","'\xea'     #  0xEA -> LATIN SMALL LETTER E WITH CIRCUMFLEX\n","'\xeb'     #  0xEB -> LATIN SMALL LETTER E WITH DIAERESIS\n","'\xec'     #  0xEC -> LATIN SMALL LETTER I WITH GRAVE\n","'\xed'     #  0xED -> LATIN SMALL LETTER I WITH ACUTE\n","'\xee'     #  0xEE -> LATIN SMALL LETTER I WITH CIRCUMFLEX\n","'\xef'     #  0xEF -> LATIN SMALL LETTER I WITH DIAERESIS\n","'\xf0'     #  0xF0 -> LATIN SMALL LETTER ETH\n","'\xf1'     #  0xF1 -> LATIN SMALL LETTER N WITH TILDE\n","'\xf2'     #  0xF2 -> LATIN SMALL LETTER O WITH GRAVE\n","'\xf3'     #  0xF3 -> LATIN SMALL LETTER O WITH ACUTE\n","'\xf4'     #  0xF4 -> LATIN SMALL LETTER O WITH CIRCUMFLEX\n","'\xf5'     #  0xF5 -> LATIN SMALL LETTER O WITH TILDE\n","'\xf6'     #  0xF6 -> LATIN SMALL LETTER O WITH DIAERESIS\n","'\xf7'     #  0xF7 -> DIVISION SIGN\n","'\xf8'     #  0xF8 -> LATIN SMALL LETTER O WITH STROKE\n","'\xf9'     #  0xF9 -> LATIN SMALL LETTER U WITH GRAVE\n","'\xfa'     #  0xFA -> LATIN SMALL LETTER U WITH ACUTE\n","'\xfb'     #  0xFB -> LATIN SMALL LETTER U WITH CIRCUMFLEX\n","'\xfc'     #  0xFC -> LATIN SMALL LETTER U WITH DIAERESIS\n","'\xfd'     #  0xFD -> LATIN SMALL LETTER Y WITH ACUTE\n","'\xfe'     #  0xFE -> LATIN SMALL LETTER THORN\n","'\xff'     #  0xFF -> LATIN SMALL LETTER Y WITH DIAERESIS"]
# "♤","♧","◇","※","《","》","♡","☆",
end_message="loaded"
ping=0
contiinue=True
percent_wanted_big=3000
percent_wanted_normal=100
def pause():
    pause=input("Appuyez sur la touche entré pour continuer...")
def clean():
    print("clean")
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system()=="Linux":
        os.system("clear")
    # elif platform.system()=="Mac":
    #     os.system("clean")
    # else:
    #     print("clean")
def Title(tiitle):
    if platform.system() == "Windows":
        os.system("title {}".format(tiitle))
    elif platform.system()=="Linux":
        print("whats your whay of changing the title of the window")
    elif platform.system()=="Mac":
        print("whats your whay of changing the title of the window") 
    else:
        print ("Pour une expérience complète merci d'éxécuter ce programme sous Windows.")
def Slean(time):
    sleep(time)
    clean()

while contiinue == True:
    main=input("pour quitter, tapez q ici\nQuel chargement désirez-vous regarder?\n[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]")
    if main=="1":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(percent_wanted_normal+1):
            print ("Loading script")
            sleep(ping)
            if percent<100 and percent>0:
                a+="'Happy'"
            elif percent==100:
                a+="'Happy']"
            
            print("{} [{} %]\n".format(a,percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="2":
        percent,a=0,"["
        letther=len(load_sentence)
        for letter in load_sentence:
            print ("Loading script")
            sleep(ping)
            if percent<letther-2 and percent>0:
                a+=letter
            elif percent==letther-1:
                a+="{}]".format(letter)
            
            print("{} [{} %]\n".format(a,percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    # elif main=="3":
    # elif main=="4":
    # elif main=="5":
    # elif main=="6":
    # elif main=="7":
    # elif main=="8":
    # elif main=="9":
    # elif main=="10":
    # elif main=="11":
    # elif main=="12":
    # elif main=="13":
    # elif main=="14":
    # elif main=="15":
    # elif main=="16":
    # elif main=="17":
    # elif main=="18":
    # elif main=="19":
    # elif main=="20":
    # elif main=="21":
    # elif main=="22":
    # elif main=="23":
    # elif main=="24":
    # elif main=="25":
    # elif main=="26":
    # elif main=="27":
    # elif main=="28":
    # elif main=="29":
    # elif main=="30":
    # elif main=="31":
    # elif main=="32":
    # elif main=="33":
    # elif main=="34":
    # elif main=="35":
    # elif main=="36":
    # elif main=="37":
    # elif main=="38":
    # elif main=="39":
    # elif main=="40":
    # elif main=="41":
    # elif main=="42":
    # elif main=="43":
    # elif main=="44":
    # elif main=="45":
    # elif main=="46":
    # elif main=="47":
    # elif main=="48":
    # elif main=="49":
    # elif main=="50":
    # elif main=="51":
    # elif main=="52":
    # elif main=="53":
    # elif main=="54":
    # elif main=="55":
    # elif main=="56":
    # elif main=="57":
    # elif main=="58":
    # elif main=="59":
    # elif main=="60":
    # elif main=="61":
    # elif main=="62":
    # elif main=="63":
    # elif main=="64":
    # elif main=="65":
    # elif main=="66":
    # elif main=="67":
    # elif main=="68":
    # elif main=="69":
    # elif main=="70":
    # elif main=="71":
    # elif main=="72":
    # elif main=="73":
    # elif main=="74":
    # elif main=="75":
    # elif main=="76":
    # elif main=="77":
    # elif main=="78":
    # elif main=="79":
    # elif main=="80":
    # elif main=="81":
    # elif main=="82":
    # elif main=="83":
    # elif main=="84":
    # elif main=="85":
    # elif main=="86":
    elif main=="87":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(percent_wanted_normal+1):
            print ("Loading script")
            sleep(ping)
            if percent<percent_wanted_normal and percent>0:
                a+="{}".format(random.randint(0,1))
            elif percent==percent_wanted_normal:
                a+="{}]".format(random.randint(0,1))
            
            print("{} [{} %]\n".format(a,percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="88":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(percent_wanted_normal+1):
            print ("Loading script")
            sleep(ping)
            if percent<percent_wanted_normal and percent>0:
                a+="{}".format(alphabet[random.randint(0,56)])
            elif percent==percent_wanted_normal:
                a+="{}]".format(alphabet[random.randint(0,56)])
            
            print("{} [{} %]\n".format(a,percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="89":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(percent_wanted_normal+1):
            print ("Loading script")
            sleep(ping)
            if percent<percent_wanted_normal and percent>0:
                a+="▓"
            elif percent==percent_wanted_normal:
                a+="▓]"
            
            print("{} [{} %]\n".format(a,percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
        
    elif main=="90":
        question="True"
        while question=="True":
            sub_main="small"
            sub_main=input("Quelle sera la taille taille du visage de chargement: [small/medium/big]")
            if sub_main=="small":
                Title("Loading...")
                al1,al2,al3,al4,al5,al6,al7=" _","|","|","|","|","|","|_"
                percent=0
                for advance in range(11):
                    print ("Loading script")
                    sleep(ping)
                    if percent<10 and percent>0:
                        al1+="    "
                        al2+=" ___ "
                        al3+="|. .|"
                        al4+="| | |"
                        al5+="||_||"
                        al6+="|___|"
                        al7+="    "
                    elif percent==10:
                        al1+="       _"
                        al2+="|"
                        al3+="|"
                        al4+="|"
                        al5+="|"
                        al6+="|"
                        al7+="       _|"
                    print("""{}\n{}\n{}\n{}\n{}\n{} {}{}{}{}{}{}\n{} %]\n{}""".format(al1,al2,al3,al4,al5,al6,percent*10,al7))
                    percent+=1
                    Slean(Time)
                print("""{}\n{}\n{}\n{}\n{}\n{} [{}]\n{}""".format(al1,al2,al3,al4,al5,al6,end_message,al7))
                pause()
            elif sub_main=="medium":
                Title("Loading...")
                al1,al2,al3,al4,al5,al6,al7=" _","|","|","|","|","|","|_"
                percent=0
                for advance in range(11):
                    print ("Loading script")
                    sleep(ping)
                    if percent<10 and percent>0:
                        al1+="      "
                        al2+=" _____ "
                        al3+="|.   .|"
                        al4+="|  |  |"
                        al5+="||___||"
                        al6+="|_____|"
                        al7+="      "
                    elif percent==10:
                        al1+="       _"
                        al2+="|"
                        al3+="|"
                        al4+="|"
                        al5+="|"
                        al6+="|"
                        al7+="       _|"
                    print("""{}\n{}\n{}\n{}\n{}\n{} [{} %]\n{}""".format(al1,al2,al3,al4,al5,al6,percent*10,al7))
                    percent+=1
                    Slean(Time)
                print("""{}\n{}\n{}\n{}\n{}\n{} [{}]\n{}""".format(al1,al2,al3,al4,al5,al6,end_message,al7))
                pause()
            elif sub_main=="big":
                Title("Loading...")
                al1,al2,al3,al4,al5,al6,al7=" _","|","|","|","|","|","|_"
                percent=0
                for advance in range(11):
                    print ("Loading script")
                    sleep(ping)
                    if percent<10 and percent>0:
                        al1+="      "
                        al2+=" _______ "
                        al3+="| .   . |"
                        al4+="|   |   |"
                        al5+="| |___| |"
                        al6+="|_______|"
                        al7+="      "
                    elif percent==10:
                        al1+="                         _"
                        al2+="|"
                        al3+="|"
                        al4+="|"
                        al5+="|"
                        al6+="|"
                        al7+="                         _|"
                    print("""{}\n{}\n{}\n{}\n{}\n{} [{} %]\n{}""".format(al1,al2,al3,al4,al5,al6,percent*10,al7))
                    percent+=1
                    Slean(Time)
                print("""{}\n{}\n{}\n{}\n{}\n{} [{}]\n{}""".format(al1,al2,al3,al4,al5,al6,end_message,al7))
                pause()
            else:
                print("Assurez-vous d'avoir entré soit small pour avoir un chargement avec un petit visage, medium pour avoir un un visage de taille 'normale', big pour avoir un très grand visage.\nVous avez entré : {}".format(sub_main))
            stop=input("Voulez-vous voir un autre des trois chargements? [(o)ui/(n)on]")
            if stop=="o" or stop=="O" or stop=="0":
                question="True"
            elif stop=="n" or stop=="N":
                question="False"
            else:
                print("Assurez-vous d'avoir entré soit 'o' pour 'oui' ou 'n' pour 'non'.\nVous avez entré".format(stop))
    elif main=="91":
        question="True"
        while question=="True":
            sub_main="small"
            sub_main=input("Quelle sera la taille taille du visage de chargement: [small/medium/big]")
            if sub_main=="small":
                Title("Loading...")
                al1,al2,al3,al4,al5,al6,al7=" _","|","|","|","|","|","|_"
                percent=0
                for advance in range(11):
                    print ("Loading script")
                    sleep(ping)
                    if percent<10 and percent>0:
                        al1+="    "
                        al2+=" ___ "
                        al3+="|. .|"
                        al4+="| | |"
                        al5+="||_||"
                        al6+="|___|"
                        al7+="    "
                    elif percent==10:
                        al1+="       _"
                        al2+="|"
                        al3+="|"
                        al4+="|"
                        al5+="|"
                        al6+="|"
                        al7+="       _|"
                    print("""{}\n{}\n{}\n{}\n{}\n{} [{} %]\n{}""".format(al1,al2,al3,al4,al5,al6,percent*10,al7))
                    percent+=1
                    Slean(Time)
                print("""{}\n{}\n{}\n{}\n{}\n{} [{}]\n{}""".format(al1,al2,al3,al4,al5,al6,end_message,al7))
                pause()
            elif sub_main=="medium":
                Title("Loading...")
                al1,al2,al3,al4,al5,al6,al7=" _","|","|","|","|","|","|_"
                percent=0
                for advance in range(11):
                    print ("Loading script")
                    sleep(ping)
                    if percent<10 and percent>0:
                        al1+="      "
                        al2+=" _____ "
                        al3+="|.   .|"
                        al4+="|  |  |"
                        al5+="||___||"
                        al6+="|_____|"
                        al7+="      "
                    elif percent==10:
                        al1+="       _"
                        al2+="|"
                        al3+="|"
                        al4+="|"
                        al5+="|"
                        al6+="|"
                        al7+="       _|"
                    print("""{}\n{}\n{}\n{}\n{}\n{} [{} %]\n{}""".format(al1,al2,al3,al4,al5,al6,percent*10,al7))
                    percent+=1
                    Slean(Time)
                print("""{}\n{}\n{}\n{}\n{}\n{} [{}]\n{}""".format(al1,al2,al3,al4,al5,al6,end_message,al7))
                pause()
            elif sub_main=="big":
                Title("Loading...")
                al1,al2,al3,al4,al5,al6,al7=" _","|","|","|","|","|","|_"
                percent=0
                for advance in range(11):
                    print ("Loading script")
                    sleep(ping)
                    if percent<10 and percent>0:
                        al1+="      "
                        al2+=" _______ "
                        al3+="| .   . |"
                        al4+="|   |   |"
                        al5+="| |___| |"
                        al6+="|_______|"
                        al7+="      "
                    elif percent==10:
                        al1+="                         _"
                        al2+="|"
                        al3+="|"
                        al4+="|"
                        al5+="|"
                        al6+="|"
                        al7+="                         _|"
                    print("""{}\n{}\n{}\n{}\n{}\n{} [{} %]\n{}""".format(al1,al2,al3,al4,al5,al6,percent*10,al7))
                    percent+=1
                    Slean(Time)
                print("""{}\n{}\n{}\n{}\n{}\n{} [{}]\n{}""".format(al1,al2,al3,al4,al5,al6,end_message,al7))
                pause()
            else:
                print("Assurez-vous d'avoir entré soit small pour avoir un chargement avec un petit visage, medium pour avoir un un visage de taille 'normale', big pour avoir un très grand visage.\nVous avez entré : {}".format(sub_main))
            stop=input("Voulez-vous voir un autre des trois chargements? [(o)ui/(n)on]")
            if stop=="o" or stop=="O" or stop=="0":
                question="True"
            elif stop=="n" or stop=="N":
                question="False"
            else:
                print("Assurez-vous d'avoir entré soit 'o' pour 'oui' ou 'n' pour 'non'.\nVous avez entré".format(stop))


    elif main=="92":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(percent_wanted_big+1):
            print ("Loading script")
            sleep(ping)
            if percent<=100 and percent>0:
                a+="_"
            elif percent<=200 and percent>100:
                a+="-"
            elif percent<=300 and percent>200:
                a+="#"
            elif percent<=400 and percent>300:
                a+="°"
            elif percent<=500 and percent>400:
                a+="*"
            elif percent<=600 and percent>500:
                a+="@"
            elif percent<=700 and percent>600:
                a+="¤"
            elif percent<=800 and percent>700:
                a+="&"
            elif percent<=900 and percent>800:
                a+="="
            elif percent<=1000 and percent>900:
                a+="~"
            elif percent<=1100 and percent>1000:
                a+="§"
            elif percent<=1200 and percent>1100:
                a+="/"
            elif percent<=1300 and percent>1200:
                a+="²"
            elif percent<=1400 and percent>1300:
                a+=">"
            elif percent<=1500 and percent>1400:
                a+="<"
            elif percent<=1600 and percent>1500:
                a+="o"
            elif percent<=1700 and percent>1600:
                a+="O"
            elif percent<=1800 and percent>1700:
                a+="."
            elif percent<=1900 and percent>1800:
                a+="£"
            elif percent<=2000 and percent>1900:
                a+="$"
            elif percent<=2100 and percent>2000:
                a+="€"
            elif percent<=2200 and percent>2100:
                a+="x"
            elif percent<=2300 and percent>2200:
                a+="X"
            elif percent<=2400 and percent>2300:
                a+=":"
            elif percent<=2500 and percent>2400:
                a+=";"
            elif percent<=2600 and percent>2500:
                a+="µ"
            elif percent<=percent_wanted_big-1 and percent>2600:
                a+="!"
            elif percent==percent_wanted_big:
                a+="!]"
            
            print("{} [{} %]\n".format(a,percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="93":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(101):
            print ("Loading script")
            sleep(ping)
            if percent<100 and percent>0:
                a+="_"
            elif percent==100:
                a+="_]"
            
            print("{}{} [{} %]\n".format(a,spaces[percent],percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="94":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(101):
            print ("Loading script")
            sleep(ping)
            if percent<100 and percent>0:
                a+="-"
            elif percent==100:
                a+="-]"
            print("{}{} [{} %]\n".format(a,spaces[percent],percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="95":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(101):
            print ("Loading script")
            sleep(ping)
            if percent<100 and percent>0:
                a+="#"
            elif percent==100:
                a+="#]"
            
            print("{}{} [{} %]\n".format(a,spaces[percent],percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="96":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(percent_wanted_normal+1):
            if percent<percent_wanted_normal and percent>0:
                a+="chr(32)"
            elif percent==percent_wanted_normal:
                a+="chr(32)]"
            
            print("'{}'[{} %]\n".format(a,percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="97":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(percent_wanted_normal+1):
            print ("Loading script")
            sleep(ping)
            if percent<percent_wanted_normal and percent>0:
                a+="_"
            elif percent==percent_wanted_normal:
                a+="_]"
            
            print("{} [{} %]\n".format(a,percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="98":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(percent_wanted_normal+1):
            print ("Loading script")
            sleep(ping)
            if percent<percent_wanted_normal and percent>0:
                a+="-"
            elif percent==percent_wanted_normal:
                a+="-]"
            print("{} [{} %]\n".format(a,percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="99":
        Title("Loading...")
        percent=0
        a="["
        for advance in range(percent_wanted_normal+1):
            print ("Loading script")
            sleep(ping)
            if percent<percent_wanted_normal and percent>0:
                a+="#"
            elif percent==percent_wanted_normal:
                a+="#]"
            
            print("{} [{} %]\n".format(a,percent))
            percent+=1
            Slean(Time)
        print("{} [{}]\n".format(a,end_message))
        pause()
    elif main=="100": #chragement triple, lourd
        Title("Loading...")
        print ("Loading script")
        sleep(ping)
        print (" [                                                                                                      [0 %]\n")
        Slean(Time)
        print ("Loading script\n [_                                                                                                     [1 %]\n")
        Slean(Time)
        print ("Loading script\n [__                                                                                                    [2 %]\n")
        Slean(Time) 
        print ("Loading script\n [___                                                                                                   [3 %]\n")
        Slean(Time)
        print ("Loading script\n [____                                                                                                  [4 %]\n")
        Slean(Time)
        print ("Loading script\n [_____                                                                                                 [5 %]\n")
        Slean(Time)
        print ("Loading script\n [______                                                                                                [6 %]\n")
        Slean(Time)
        print ("Loading script\n [_______                                                                                               [7 %]\n")
        Slean(Time)
        print ("Loading script\n [________                                                                                              [8 %]\n")
        Slean(Time)
        print ("Loading script\n [_________                                                                                             [9 %]\n")
        Slean(Time)
        print ("Loading script\n [__________                                                                                            [10 %]\n")
        Slean(Time)
        print ("Loading script\n [___________                                                                                           [11 %]\n")
        Slean(Time)
        print ("Loading script\n [____________                                                                                          [12 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________                                                                                         [13 %]\n")
        Slean(Time)
        print ("Loading script\n [______________                                                                                        [14 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________                                                                                       [15 %]\n")
        Slean(Time)
        print ("Loading script\n [________________                                                                                      [16 %]\n")
        Slean(Time)
        print ("Loading script\n [_________________                                                                                     [17 %]\n")
        Slean(Time)
        print ("Loading script\n [__________________                                                                                    [18 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________                                                                                   [19 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________                                                                                  [20 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________________                                                                                 [21 %]\n")
        Slean(Time)
        print ("Loading script\n [______________________                                                                                [22 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________________                                                                               [23 %]\n")
        Slean(0)
        print ("Loading script\n [________________________                                                                              [24 %]\n")
        Slean(0)
        print ("Loading script\n [_________________________                                                                             [25 %]\n")
        Slean(0)
        print ("Loading script\n [__________________________                                                                            [26 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________________                                                                           [27 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________________                                                                          [28 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________________________                                                                         [29 %]\n")
        Slean(Time)
        print ("Loading script\n [______________________________                                                                        [30 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________________________                                                                       [31 %]\n")
        Slean(Time)
        print ("Loading script\n [________________________________                                                                      [32 %]\n")
        Slean(Time)
        print ("Loading script\n [_________________________________                                                                     [33 %]\n")
        Slean(Time)
        print ("Loading script\n [__________________________________                                                                    [34 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________________________                                                                   [35 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________________________                                                                  [36 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________________________________                                                                 [37 %]\n")
        Slean(Time)
        print ("Loading script\n [______________________________________                                                                [38 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________________________________                                                               [39 %]\n")
        Slean(Time)
        print ("Loading script\n [________________________________________                                                              [40 %]\n")
        Slean(Time)
        print ("Loading script\n [_________________________________________                                                             [41 %]\n")
        Slean(Time)
        print ("Loading script\n [__________________________________________                                                            [42 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________________________________                                                           [43 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________________________________                                                          [44 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________________________________________                                                         [45 %]\n")
        Slean(Time)
        print ("Loading script\n [______________________________________________                                                        [46 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________________________________________                                                       [47 %]\n")
        Slean(Time)
        print ("Loading script\n [________________________________________________                                                      [48 %]\n")
        Slean(Time)
        print ("Loading script\n [_________________________________________________                                                     [49 %]\n")
        Slean(Time)
        print ("Loading script\n [__________________________________________________                                                    [50 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________________________________________                                                   [51 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________________________________________                                                  [52 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________________________________________________                                                 [53 %]\n")
        Slean(Time)
        print ("Loading script\n [______________________________________________________                                                [54 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________________________________________________                                               [55 %]\n")
        Slean(Time)
        print ("Loading script\n [________________________________________________________                                              [56 %]\n")
        Slean(Time)
        print ("Loading script\n [_________________________________________________________                                             [57 %]\n")
        Slean(Time)
        print ("Loading script\n [__________________________________________________________                                            [58 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________________________________________________                                           [59 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________________________________________________                                          [60 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________________________________________________________                                         [61 %]\n")
        Slean(Time)
        print ("Loading script\n [______________________________________________________________                                        [62 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________________________________________________________                                       [63 %]\n")
        Slean(Time)
        print ("Loading script\n [________________________________________________________________                                      [64 %]\n")
        Slean(Time)
        print ("Loading script\n [_________________________________________________________________                                     [65 %]\n")
        Slean(Time)
        print ("Loading script\n [__________________________________________________________________                                    [66 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________________________________________________________                                   [67 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________________________________________________________                                  [68 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________________________________________________________________                                 [69 %]\n")
        Slean(Time)
        print ("Loading script\n [______________________________________________________________________                                [70 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________________________________________________________________                               [71 %]\n")
        Slean(Time)
        print ("Loading script\n [________________________________________________________________________                              [72 %]\n")
        Slean(Time)
        print ("Loading script\n [_________________________________________________________________________                             [73 %]\n")
        Slean(Time)
        print ("Loading script\n [__________________________________________________________________________                            [74 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________________________________________________________________                           [75 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________________________________________________________________                          [76 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________________________________________________________________________                         [77 %]\n")
        Slean(Time)
        print ("Loading script\n [______________________________________________________________________________                        [78 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________________________________________________________________________                       [79 %]\n")
        Slean(Time)
        print ("Loading script\n [________________________________________________________________________________                      [80 %]\n")
        Slean(Time)
        print ("Loading script\n [_________________________________________________________________________________                     [81 %]\n")
        Slean(Time)
        print ("Loading script\n [__________________________________________________________________________________                    [82 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________________________________________________________________________                   [83 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________________________________________________________________________                  [84 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________________________________________________________________________________                 [85 %]\n")
        Slean(Time)
        print ("Loading script\n [______________________________________________________________________________________                [86 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________________________________________________________________________________               [87 %]\n")
        Slean(Time)
        print ("Loading script\n [________________________________________________________________________________________              [88 %]\n")
        Slean(Time)
        print ("Loading script\n [_________________________________________________________________________________________             [89 %]\n")
        Slean(Time)
        print ("Loading script\n [__________________________________________________________________________________________            [90 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________________________________________________________________________________           [91 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________________________________________________________________________________          [92 %]\n")
        Slean(Time)
        print ("Loading script\n [_____________________________________________________________________________________________         [93 %]\n")
        Slean(Time)
        print ("Loading script\n [______________________________________________________________________________________________        [94 %]\n")
        Slean(Time)
        print ("Loading script\n [_______________________________________________________________________________________________       [95 %]\n")
        Slean(Time)
        print ("Loading script\n [________________________________________________________________________________________________      [96 %]\n")
        Slean(Time)
        print ("Loading script\n [_________________________________________________________________________________________________     [97 %]\n")
        Slean(Time)
        print ("Loading script\n [__________________________________________________________________________________________________    [98 %]\n")
        Slean(Time)
        print ("Loading script\n [___________________________________________________________________________________________________   [99 %]\n")
        Slean(Time)
        print ("Loading script\n [____________________________________________________________________________________________________  [100%]\n")
        Slean(Time)
        print ("Loading script\n [____________________________________________________________________________________________________] [loaded]\n")
        clean()
        Title("verifying...")
        print ("verifying script\n [____________________________________________________________________________________________________] [loaded]\n")
        clean()
        sleep(ping)
        print ( " [____________________________________________________________________________________________________] [loaded]\n [____________________________________________________________________________________________________] [0 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-___________________________________________________________________________________________________] [1 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--__________________________________________________________________________________________________] [2 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---_________________________________________________________________________________________________] [3 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----________________________________________________________________________________________________] [4 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----_______________________________________________________________________________________________] [5 %]\n")
        Slean(Time)
        print(" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------______________________________________________________________________________________________] [6 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------_____________________________________________________________________________________________] [7 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------____________________________________________________________________________________________] [8 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------___________________________________________________________________________________________] [9 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------__________________________________________________________________________________________] [10 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------_________________________________________________________________________________________] [11 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------________________________________________________________________________________________] [12 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------_______________________________________________________________________________________] [13 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------______________________________________________________________________________________] [14 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------_____________________________________________________________________________________] [15 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------____________________________________________________________________________________] [16 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------___________________________________________________________________________________] [17 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------__________________________________________________________________________________] [18 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------_________________________________________________________________________________] [19 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------________________________________________________________________________________] [20 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------_______________________________________________________________________________] [21 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------______________________________________________________________________________] [22 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------_____________________________________________________________________________] [23 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------____________________________________________________________________________] [24 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------___________________________________________________________________________] [25 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------__________________________________________________________________________] [26 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------_________________________________________________________________________] [27 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------________________________________________________________________________] [28 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------_______________________________________________________________________] [29 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------______________________________________________________________________] [30 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------_____________________________________________________________________] [31 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------____________________________________________________________________] [32 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------___________________________________________________________________] [33 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------__________________________________________________________________] [34 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------_________________________________________________________________] [35 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------________________________________________________________________] [36 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------_______________________________________________________________] [37 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------______________________________________________________________] [38 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------_____________________________________________________________] [39 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------____________________________________________________________] [40 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------------___________________________________________________________] [41 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------------__________________________________________________________] [42 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------------_________________________________________________________] [43 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------------________________________________________________________] [44 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------------_______________________________________________________] [45 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------______________________________________________________] [46 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------------------_____________________________________________________] [47 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------------------____________________________________________________] [48 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------------------___________________________________________________] [49 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------------------__________________________________________________] [50 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------------------_________________________________________________] [51 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------________________________________________________] [52 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------------------------_______________________________________________] [53 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------------------------______________________________________________] [54 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------------------------_____________________________________________] [55 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------------------------____________________________________________] [56 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------------------------___________________________________________] [57 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------__________________________________________] [58 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------------------------------_________________________________________] [59 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------------------------------________________________________________] [60 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------------------------------_______________________________________] [61 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------------------------------______________________________________] [62 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------------------------------_____________________________________] [63 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------____________________________________] [64 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------------------------------------___________________________________] [65 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------------------------------------__________________________________] [66 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------------------------------------_________________________________] [67 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------------------------------------________________________________] [68 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------------------------------------_______________________________] [69 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------______________________________] [70 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------------------------------------------_____________________________] [71 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------------------------------------------____________________________] [72 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------------------------------------------___________________________] [73 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------------------------------------------__________________________] [74 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------------------------------------------_________________________] [75 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------________________________] [76 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------------------------------------------------_______________________] [77 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------------------------------------------------______________________] [78 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------------------------------------------------_____________________] [79 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------------------------------------------------____________________] [80 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------------------------------------------------___________________] [81 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------__________________] [82 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------------------------------------------------------_________________] [83 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------------------------------------------------------________________] [84 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------------------------------------------------------_______________] [85 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------------------------------------------------------______________] [86 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------------------------------------------------------_____________] [87 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------____________] [88 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------------------------------------------------------------___________] [89 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------------------------------------------------------------__________] [90 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------------------------------------------------------------_________] [91 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------------------------------------------------------------________] [92 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------------------------------------------------------------_______] [93 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------______] [94 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-----------------------------------------------------------------------------------------------_____] [95 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [------------------------------------------------------------------------------------------------____] [96 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [-------------------------------------------------------------------------------------------------___] [97 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [--------------------------------------------------------------------------------------------------__] [98 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [---------------------------------------------------------------------------------------------------_] [99 %]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [100%]\n")
        Slean(Time)
        print (" verifying script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n")
        Slean(Time)
        Title("testing...")
        print ("testing script...\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]")
        Slean(ping)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [----------------------------------------------------------------------------------------------------] [0 %]\n") 
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#---------------------------------------------------------------------------------------------------] [1 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##--------------------------------------------------------------------------------------------------] [2 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###-------------------------------------------------------------------------------------------------] [3 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [####------------------------------------------------------------------------------------------------] [4 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#####-----------------------------------------------------------------------------------------------] [5 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [######----------------------------------------------------------------------------------------------] [6 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#######---------------------------------------------------------------------------------------------] [7 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [########--------------------------------------------------------------------------------------------] [8 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#########-------------------------------------------------------------------------------------------] [9 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##########------------------------------------------------------------------------------------------] [10 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###########-----------------------------------------------------------------------------------------] [11 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [############----------------------------------------------------------------------------------------] [12 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#############---------------------------------------------------------------------------------------] [13 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##############--------------------------------------------------------------------------------------] [14 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###############-------------------------------------------------------------------------------------] [15 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [################------------------------------------------------------------------------------------] [16 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#################-----------------------------------------------------------------------------------] [17 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##################----------------------------------------------------------------------------------] [18 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###################---------------------------------------------------------------------------------] [19 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [####################--------------------------------------------------------------------------------] [20 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#####################-------------------------------------------------------------------------------] [21 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [######################------------------------------------------------------------------------------] [22 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#######################-----------------------------------------------------------------------------] [23 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [########################----------------------------------------------------------------------------] [24 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#########################---------------------------------------------------------------------------] [25 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##########################--------------------------------------------------------------------------] [26 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###########################-------------------------------------------------------------------------] [27 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [############################------------------------------------------------------------------------] [28 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#############################-----------------------------------------------------------------------] [29 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##############################----------------------------------------------------------------------] [30 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###############################---------------------------------------------------------------------] [31 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [################################--------------------------------------------------------------------] [32 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#################################-------------------------------------------------------------------] [33 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##################################------------------------------------------------------------------] [34 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###################################-----------------------------------------------------------------] [35 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [####################################----------------------------------------------------------------] [36 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#####################################---------------------------------------------------------------] [37 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [######################################--------------------------------------------------------------] [38 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#######################################-------------------------------------------------------------] [39 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [########################################------------------------------------------------------------] [40 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#########################################-----------------------------------------------------------] [41 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##########################################----------------------------------------------------------] [42 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###########################################---------------------------------------------------------] [43 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [############################################--------------------------------------------------------] [44 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#############################################-------------------------------------------------------] [45 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##############################################------------------------------------------------------] [46 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###############################################-----------------------------------------------------] [47 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [################################################----------------------------------------------------] [48 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#################################################---------------------------------------------------] [49 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##################################################--------------------------------------------------] [50 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###################################################-------------------------------------------------] [51 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [####################################################------------------------------------------------] [52 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#####################################################-----------------------------------------------] [53 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [######################################################----------------------------------------------] [54 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#######################################################---------------------------------------------] [55 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [########################################################--------------------------------------------] [56 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#########################################################-------------------------------------------] [57 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##########################################################------------------------------------------] [58 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###########################################################-----------------------------------------] [59 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [############################################################----------------------------------------] [60 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#############################################################---------------------------------------] [61 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##############################################################--------------------------------------] [62 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###############################################################-------------------------------------] [63 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [################################################################------------------------------------] [64 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#################################################################-----------------------------------] [65 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##################################################################----------------------------------] [66 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###################################################################---------------------------------] [67 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [####################################################################--------------------------------] [68 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#####################################################################-------------------------------] [69 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [######################################################################------------------------------] [70 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#######################################################################-----------------------------] [71 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [########################################################################----------------------------] [72 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#########################################################################---------------------------] [73 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##########################################################################--------------------------] [74 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###########################################################################-------------------------] [75 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [############################################################################------------------------] [76 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#############################################################################-----------------------] [77 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##############################################################################----------------------] [78 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###############################################################################---------------------] [79 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [################################################################################--------------------] [80 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#################################################################################-------------------] [81 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##################################################################################------------------] [82 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###################################################################################-----------------] [83 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [####################################################################################----------------] [84 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#####################################################################################---------------] [85 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [######################################################################################--------------] [86 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#######################################################################################-------------] [87 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [########################################################################################------------] [88 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#########################################################################################-----------] [89 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##########################################################################################----------] [90 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###########################################################################################---------] [91 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [############################################################################################--------] [92 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#############################################################################################-------] [93 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##############################################################################################------] [94 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###############################################################################################-----] [95 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [################################################################################################----] [96 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [#################################################################################################---] [97 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [##################################################################################################--] [98 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [###################################################################################################-] [99 %]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [####################################################################################################] [100%]\n")
        Slean(Time)
        print (" testing script\n [____________________________________________________________________________________________________] [loaded]\n [----------------------------------------------------------------------------------------------------] [verified]\n [####################################################################################################] [tested :-)]\n")
    elif main=="q" or main=="Q":
        contiinue=False
        print ("Au revoir.")
        print ( "                      *=============================================================================================================*                    \n                      |                              @@         @@                                                                  |                    \n                      |                             @@         @@                                                                   |                    \n                      |                            @@         @@                                                                    |                    \n                      |                                                                                                             |                    \n                      |      @@@@@@@@   @@@@@@   @@@@@@@@  @@@@@@@@              @@@@@@@@      @@        @@@@@@@@@                  |                    \n                      |      @@        @      @  @@        @@                   @@       @    @  @       @@       @                 |                    \n                      |      @@        @      @  @@        @@                   @@       @   @    @      @@       @                 |                    \n                      |      @@        @@@@@@@   @@@@@@@@  @@@@@@@@             @@@@@@@@@   @@@@@@@@     @@@@@@@@@                  |                    \n                      |      @@        @  @      @@        @@                   @@         @        @    @@    @                    |                    \n                      |      @@        @   @     @@        @@                   @@        @          @   @@     @                   |                    \n                      |      @@@@@@@@  @    @    @@@@@@@@  @@@@@@@@             @@       @            @  @@      @                  |                    \n                      |                                                                                                             |                    \n                      |              @@       @@  @@@@@@@@@  @@      @@  @@@@@@@@   @@       @@                                     |                    \n                      |              @@       @@  @@         @@@     @@  @@       @  @@     @@                                      |                    \n                      |              @@       @@  @@         @@ @    @@  @@       @   @@   @@                                       |                    \n                      |              @@@@@@@@@@@  @@@@@@@@@  @@  @   @@  @@@@@@@@@     @@ @@                                        |                    \n                      |              @@       @@  @@         @@   @  @@  @@    @        @@@                                         |                    \n                      |              @@       @@  @@         @@    @ @@  @@     @       @@                                          |                    \n                      |              @@       @@  @@@@@@@@@  @@     @@@  @@      @     @@                                           |                    \n                      |                                                                                                             |                    \n                      |      @@         @@@@@@@@  @@@@@@@@@@@  @@@@@@@@@@@  @@         @@         @@@@@@@@   @@@@@@@  @@@@@@@@      |                    \n                      |      @@         @@            @@       @@           @@         @@            @@      @@       @@       @    |                    \n                      |      @@         @@            @@       @@           @@         @@            @@      @@       @@       @    |                    \n                      |      @@         @@@@@@@@      @@       @@@@@@@@@@@  @@         @@            @@      @@@@@@@  @@@@@@@@@     |                    \n                      |      @@         @@            @@       @@           @@         @@            @@      @@       @@   @        |                    \n                      |      @@         @@            @@       @@           @@         @@            @@      @@       @@    @       |                    \n                      |      @@@@@@@@@  @@@@@@@@      @@       @@@@@@@@@@@  @@@@@@@@@  @@@@@@@@@@ @@@@@@@@   @@@@@@@  @@     @      |                    \n                      .=============================================================================================================.                     ")
        print("*Créé par Henry Letellier")
        sleep(5)
        pause()

