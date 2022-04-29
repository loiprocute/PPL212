# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2N")
        buf.write("\u0228\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\5\3\u00a9\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u00b4\n\5\3\6\3\6\7\6\u00b8\n\6\f\6\16\6\u00bb\13\6\3")
        buf.write("\6\6\6\u00be\n\6\r\6\16\6\u00bf\3\6\7\6\u00c3\n\6\f\6")
        buf.write("\16\6\u00c6\13\6\5\6\u00c8\n\6\3\7\3\7\3\7\6\7\u00cd\n")
        buf.write("\7\r\7\16\7\u00ce\3\b\3\b\3\b\6\b\u00d4\n\b\r\b\16\b\u00d5")
        buf.write("\3\t\3\t\6\t\u00da\n\t\r\t\16\t\u00db\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\5\16\u00e8\n\16\3\17\3\17\3")
        buf.write("\17\5\17\u00ed\n\17\3\17\5\17\u00f0\n\17\3\17\3\17\3\20")
        buf.write("\3\20\6\20\u00f6\n\20\r\20\16\20\u00f7\3\21\3\21\5\21")
        buf.write("\u00fc\n\21\3\21\6\21\u00ff\n\21\r\21\16\21\u0100\3\22")
        buf.write("\3\22\5\22\u0105\n\22\3\23\3\23\7\23\u0109\n\23\f\23\16")
        buf.write("\23\u010c\13\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)")
        buf.write("\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\7,\u01a7")
        buf.write("\n,\f,\16,\u01aa\13,\3,\3,\3,\3,\3,\3-\5-\u01b2\n-\3-")
        buf.write("\3-\7-\u01b6\n-\f-\16-\u01b9\13-\3.\6.\u01bc\n.\r.\16")
        buf.write(".\u01bd\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3A\3")
        buf.write("A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3H\3H\3")
        buf.write("H\3H\3I\3I\3I\3J\3J\3J\3K\6K\u0203\nK\rK\16K\u0204\3K")
        buf.write("\3K\3L\3L\7L\u020b\nL\fL\16L\u020e\13L\3L\5L\u0211\nL")
        buf.write("\3L\3L\3M\3M\7M\u0217\nM\fM\16M\u021a\13M\3M\3M\3M\3N")
        buf.write("\3N\3N\5N\u0222\nN\3O\3O\3O\3P\3P\3\u01a8\2Q\3\3\5\2\7")
        buf.write("\2\t\4\13\5\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33\r\35")
        buf.write("\16\37\17!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31")
        buf.write("\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W")
        buf.write("+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67q8s9u:w;y<{=")
        buf.write("}>\177?\u0081@\u0083A\u0085B\u0087C\u0089D\u008bE\u008d")
        buf.write("F\u008fG\u0091H\u0093I\u0095J\u0097K\u0099L\u009b\2\u009d")
        buf.write("M\u009fN\3\2\20\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhpptt")
        buf.write("vv\4\2DDdd\4\2ZZzz\3\2\63;\3\2\62;\3\2\629\4\2CHch\4\2")
        buf.write("GGgg\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\7\3")
        buf.write("\n\f\16\17$$))^^\3\2^^\2\u023f\2\3\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\3\u00a1\3\2\2\2\5\u00a8\3\2\2\2\7\u00aa\3\2\2\2\t\u00b3")
        buf.write("\3\2\2\2\13\u00c7\3\2\2\2\r\u00c9\3\2\2\2\17\u00d0\3\2")
        buf.write("\2\2\21\u00d7\3\2\2\2\23\u00dd\3\2\2\2\25\u00df\3\2\2")
        buf.write("\2\27\u00e1\3\2\2\2\31\u00e3\3\2\2\2\33\u00e7\3\2\2\2")
        buf.write("\35\u00e9\3\2\2\2\37\u00f3\3\2\2\2!\u00f9\3\2\2\2#\u0104")
        buf.write("\3\2\2\2%\u0106\3\2\2\2\'\u0110\3\2\2\2)\u0114\3\2\2\2")
        buf.write("+\u011a\3\2\2\2-\u0121\3\2\2\2/\u0129\3\2\2\2\61\u012e")
        buf.write("\3\2\2\2\63\u0134\3\2\2\2\65\u0138\3\2\2\2\67\u013c\3")
        buf.write("\2\2\29\u0142\3\2\2\2;\u014b\3\2\2\2=\u0150\3\2\2\2?\u015c")
        buf.write("\3\2\2\2A\u0168\3\2\2\2C\u0171\3\2\2\2E\u0176\3\2\2\2")
        buf.write("G\u0179\3\2\2\2I\u017f\3\2\2\2K\u0183\3\2\2\2M\u0188\3")
        buf.write("\2\2\2O\u018f\3\2\2\2Q\u0192\3\2\2\2S\u0199\3\2\2\2U\u019c")
        buf.write("\3\2\2\2W\u01a2\3\2\2\2Y\u01b1\3\2\2\2[\u01bb\3\2\2\2")
        buf.write("]\u01bf\3\2\2\2_\u01c1\3\2\2\2a\u01c3\3\2\2\2c\u01c5\3")
        buf.write("\2\2\2e\u01c7\3\2\2\2g\u01c9\3\2\2\2i\u01cb\3\2\2\2k\u01cd")
        buf.write("\3\2\2\2m\u01cf\3\2\2\2o\u01d1\3\2\2\2q\u01d3\3\2\2\2")
        buf.write("s\u01d5\3\2\2\2u\u01d7\3\2\2\2w\u01d9\3\2\2\2y\u01db\3")
        buf.write("\2\2\2{\u01dd\3\2\2\2}\u01e0\3\2\2\2\177\u01e3\3\2\2\2")
        buf.write("\u0081\u01e6\3\2\2\2\u0083\u01e9\3\2\2\2\u0085\u01eb\3")
        buf.write("\2\2\2\u0087\u01ed\3\2\2\2\u0089\u01ef\3\2\2\2\u008b\u01f2")
        buf.write("\3\2\2\2\u008d\u01f5\3\2\2\2\u008f\u01f7\3\2\2\2\u0091")
        buf.write("\u01fb\3\2\2\2\u0093\u01fe\3\2\2\2\u0095\u0202\3\2\2\2")
        buf.write("\u0097\u0208\3\2\2\2\u0099\u0214\3\2\2\2\u009b\u0221\3")
        buf.write("\2\2\2\u009d\u0223\3\2\2\2\u009f\u0226\3\2\2\2\u00a1\u00a2")
        buf.write("\7o\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\4\3\2\2\2\u00a6\u00a9\n\2\2\2\u00a7\u00a9")
        buf.write("\5\7\4\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9")
        buf.write("\6\3\2\2\2\u00aa\u00ab\7^\2\2\u00ab\u00ac\t\3\2\2\u00ac")
        buf.write("\b\3\2\2\2\u00ad\u00b4\5\13\6\2\u00ae\u00b4\5\r\7\2\u00af")
        buf.write("\u00b4\5\21\t\2\u00b0\u00b1\5\17\b\2\u00b1\u00b2\b\5\2")
        buf.write("\2\u00b2\u00b4\3\2\2\2\u00b3\u00ad\3\2\2\2\u00b3\u00ae")
        buf.write("\3\2\2\2\u00b3\u00af\3\2\2\2\u00b3\u00b0\3\2\2\2\u00b4")
        buf.write("\n\3\2\2\2\u00b5\u00b9\5\23\n\2\u00b6\u00b8\5\25\13\2")
        buf.write("\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3")
        buf.write("\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00c8\3\2\2\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bc\u00be\7\62\2\2\u00bd\u00bc\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2")
        buf.write("\u00c0\u00c4\3\2\2\2\u00c1\u00c3\7\62\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c7\u00b5\3\2\2\2\u00c7\u00bd\3\2\2\2\u00c8\f\3\2\2")
        buf.write("\2\u00c9\u00ca\7\62\2\2\u00ca\u00cc\t\4\2\2\u00cb\u00cd")
        buf.write("\5\27\f\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\16\3\2\2\2\u00d0")
        buf.write("\u00d1\7\62\2\2\u00d1\u00d3\t\5\2\2\u00d2\u00d4\5\33\16")
        buf.write("\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d3")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\20\3\2\2\2\u00d7\u00d9")
        buf.write("\7\62\2\2\u00d8\u00da\5\31\r\2\u00d9\u00d8\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2")
        buf.write("\u00dc\22\3\2\2\2\u00dd\u00de\t\6\2\2\u00de\24\3\2\2\2")
        buf.write("\u00df\u00e0\t\7\2\2\u00e0\26\3\2\2\2\u00e1\u00e2\4\62")
        buf.write("\63\2\u00e2\30\3\2\2\2\u00e3\u00e4\t\b\2\2\u00e4\32\3")
        buf.write("\2\2\2\u00e5\u00e8\5\25\13\2\u00e6\u00e8\t\t\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8\34\3\2\2\2\u00e9")
        buf.write("\u00ef\5[.\2\u00ea\u00ec\5\37\20\2\u00eb\u00ed\5!\21\2")
        buf.write("\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00f0\3")
        buf.write("\2\2\2\u00ee\u00f0\5!\21\2\u00ef\u00ea\3\2\2\2\u00ef\u00ee")
        buf.write("\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\b\17\3\2\u00f2")
        buf.write("\36\3\2\2\2\u00f3\u00f5\7\60\2\2\u00f4\u00f6\t\7\2\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f5\3\2\2\2")
        buf.write("\u00f7\u00f8\3\2\2\2\u00f8 \3\2\2\2\u00f9\u00fb\t\n\2")
        buf.write("\2\u00fa\u00fc\7/\2\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc")
        buf.write("\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00ff\t\7\2\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u00fe\3\2\2\2")
        buf.write("\u0100\u0101\3\2\2\2\u0101\"\3\2\2\2\u0102\u0105\5C\"")
        buf.write("\2\u0103\u0105\5G$\2\u0104\u0102\3\2\2\2\u0104\u0103\3")
        buf.write("\2\2\2\u0105$\3\2\2\2\u0106\u010a\7$\2\2\u0107\u0109\5")
        buf.write("\5\3\2\u0108\u0107\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010d\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010d\u010e\7$\2\2\u010e\u010f\b\23\4\2")
        buf.write("\u010f&\3\2\2\2\u0110\u0111\7K\2\2\u0111\u0112\7p\2\2")
        buf.write("\u0112\u0113\7v\2\2\u0113(\3\2\2\2\u0114\u0115\7H\2\2")
        buf.write("\u0115\u0116\7n\2\2\u0116\u0117\7q\2\2\u0117\u0118\7c")
        buf.write("\2\2\u0118\u0119\7v\2\2\u0119*\3\2\2\2\u011a\u011b\7U")
        buf.write("\2\2\u011b\u011c\7v\2\2\u011c\u011d\7t\2\2\u011d\u011e")
        buf.write("\7k\2\2\u011e\u011f\7p\2\2\u011f\u0120\7i\2\2\u0120,\3")
        buf.write("\2\2\2\u0121\u0122\7D\2\2\u0122\u0123\7q\2\2\u0123\u0124")
        buf.write("\7q\2\2\u0124\u0125\7n\2\2\u0125\u0126\7g\2\2\u0126\u0127")
        buf.write("\7c\2\2\u0127\u0128\7p\2\2\u0128.\3\2\2\2\u0129\u012a")
        buf.write("\7X\2\2\u012a\u012b\7q\2\2\u012b\u012c\7k\2\2\u012c\u012d")
        buf.write("\7f\2\2\u012d\60\3\2\2\2\u012e\u012f\7e\2\2\u012f\u0130")
        buf.write("\7n\2\2\u0130\u0131\7c\2\2\u0131\u0132\7u\2\2\u0132\u0133")
        buf.write("\7u\2\2\u0133\62\3\2\2\2\u0134\u0135\7X\2\2\u0135\u0136")
        buf.write("\7c\2\2\u0136\u0137\7n\2\2\u0137\64\3\2\2\2\u0138\u0139")
        buf.write("\7X\2\2\u0139\u013a\7c\2\2\u013a\u013b\7t\2\2\u013b\66")
        buf.write("\3\2\2\2\u013c\u013d\7D\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7c\2\2\u0140\u0141\7m\2\2\u01418\3")
        buf.write("\2\2\2\u0142\u0143\7H\2\2\u0143\u0144\7q\2\2\u0144\u0145")
        buf.write("\7t\2\2\u0145\u0146\7g\2\2\u0146\u0147\7c\2\2\u0147\u0148")
        buf.write("\7e\2\2\u0148\u0149\7j\2\2\u0149\u014a\7\"\2\2\u014a:")
        buf.write("\3\2\2\2\u014b\u014c\7P\2\2\u014c\u014d\7w\2\2\u014d\u014e")
        buf.write("\7n\2\2\u014e\u014f\7n\2\2\u014f<\3\2\2\2\u0150\u0151")
        buf.write("\7E\2\2\u0151\u0152\7q\2\2\u0152\u0153\7p\2\2\u0153\u0154")
        buf.write("\7u\2\2\u0154\u0155\7v\2\2\u0155\u0156\7t\2\2\u0156\u0157")
        buf.write("\7w\2\2\u0157\u0158\7e\2\2\u0158\u0159\7v\2\2\u0159\u015a")
        buf.write("\7q\2\2\u015a\u015b\7t\2\2\u015b>\3\2\2\2\u015c\u015d")
        buf.write("\7\"\2\2\u015d\u015e\7F\2\2\u015e\u015f\7g\2\2\u015f\u0160")
        buf.write("\7u\2\2\u0160\u0161\7v\2\2\u0161\u0162\7t\2\2\u0162\u0163")
        buf.write("\7w\2\2\u0163\u0164\7e\2\2\u0164\u0165\7v\2\2\u0165\u0166")
        buf.write("\7q\2\2\u0166\u0167\7t\2\2\u0167@\3\2\2\2\u0168\u0169")
        buf.write("\7E\2\2\u0169\u016a\7q\2\2\u016a\u016b\7p\2\2\u016b\u016c")
        buf.write("\7v\2\2\u016c\u016d\7k\2\2\u016d\u016e\7p\2\2\u016e\u016f")
        buf.write("\7w\2\2\u016f\u0170\7g\2\2\u0170B\3\2\2\2\u0171\u0172")
        buf.write("\7V\2\2\u0172\u0173\7t\2\2\u0173\u0174\7w\2\2\u0174\u0175")
        buf.write("\7g\2\2\u0175D\3\2\2\2\u0176\u0177\7K\2\2\u0177\u0178")
        buf.write("\7h\2\2\u0178F\3\2\2\2\u0179\u017a\7H\2\2\u017a\u017b")
        buf.write("\7c\2\2\u017b\u017c\7n\2\2\u017c\u017d\7u\2\2\u017d\u017e")
        buf.write("\7g\2\2\u017eH\3\2\2\2\u017f\u0180\7P\2\2\u0180\u0181")
        buf.write("\7g\2\2\u0181\u0182\7y\2\2\u0182J\3\2\2\2\u0183\u0184")
        buf.write("\7G\2\2\u0184\u0185\7n\2\2\u0185\u0186\7u\2\2\u0186\u0187")
        buf.write("\7g\2\2\u0187L\3\2\2\2\u0188\u0189\7G\2\2\u0189\u018a")
        buf.write("\7n\2\2\u018a\u018b\7u\2\2\u018b\u018c\7g\2\2\u018c\u018d")
        buf.write("\7k\2\2\u018d\u018e\7h\2\2\u018eN\3\2\2\2\u018f\u0190")
        buf.write("\7D\2\2\u0190\u0191\7{\2\2\u0191P\3\2\2\2\u0192\u0193")
        buf.write("\7T\2\2\u0193\u0194\7g\2\2\u0194\u0195\7v\2\2\u0195\u0196")
        buf.write("\7w\2\2\u0196\u0197\7t\2\2\u0197\u0198\7p\2\2\u0198R\3")
        buf.write("\2\2\2\u0199\u019a\7K\2\2\u019a\u019b\7p\2\2\u019bT\3")
        buf.write("\2\2\2\u019c\u019d\7C\2\2\u019d\u019e\7t\2\2\u019e\u019f")
        buf.write("\7t\2\2\u019f\u01a0\7c\2\2\u01a0\u01a1\7{\2\2\u01a1V\3")
        buf.write("\2\2\2\u01a2\u01a3\7%\2\2\u01a3\u01a4\7%\2\2\u01a4\u01a8")
        buf.write("\3\2\2\2\u01a5\u01a7\13\2\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("\u01aa\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a8\u01a6\3\2\2\2")
        buf.write("\u01a9\u01ab\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\7")
        buf.write("%\2\2\u01ac\u01ad\7%\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af")
        buf.write("\b,\5\2\u01afX\3\2\2\2\u01b0\u01b2\7&\2\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b7\t\13\2\2\u01b4\u01b6\t\f\2\2\u01b5\u01b4\3\2\2")
        buf.write("\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8Z\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bc")
        buf.write("\t\7\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\\\3\2\2\2\u01bf")
        buf.write("\u01c0\7*\2\2\u01c0^\3\2\2\2\u01c1\u01c2\7+\2\2\u01c2")
        buf.write("`\3\2\2\2\u01c3\u01c4\7}\2\2\u01c4b\3\2\2\2\u01c5\u01c6")
        buf.write("\7\177\2\2\u01c6d\3\2\2\2\u01c7\u01c8\7=\2\2\u01c8f\3")
        buf.write("\2\2\2\u01c9\u01ca\7<\2\2\u01cah\3\2\2\2\u01cb\u01cc\7")
        buf.write(".\2\2\u01ccj\3\2\2\2\u01cd\u01ce\7]\2\2\u01cel\3\2\2\2")
        buf.write("\u01cf\u01d0\7_\2\2\u01d0n\3\2\2\2\u01d1\u01d2\7-\2\2")
        buf.write("\u01d2p\3\2\2\2\u01d3\u01d4\7/\2\2\u01d4r\3\2\2\2\u01d5")
        buf.write("\u01d6\7,\2\2\u01d6t\3\2\2\2\u01d7\u01d8\7\61\2\2\u01d8")
        buf.write("v\3\2\2\2\u01d9\u01da\7\'\2\2\u01dax\3\2\2\2\u01db\u01dc")
        buf.write("\7#\2\2\u01dcz\3\2\2\2\u01dd\u01de\7~\2\2\u01de\u01df")
        buf.write("\7~\2\2\u01df|\3\2\2\2\u01e0\u01e1\7(\2\2\u01e1\u01e2")
        buf.write("\7(\2\2\u01e2~\3\2\2\2\u01e3\u01e4\7#\2\2\u01e4\u01e5")
        buf.write("\7?\2\2\u01e5\u0080\3\2\2\2\u01e6\u01e7\7?\2\2\u01e7\u01e8")
        buf.write("\7?\2\2\u01e8\u0082\3\2\2\2\u01e9\u01ea\7?\2\2\u01ea\u0084")
        buf.write("\3\2\2\2\u01eb\u01ec\7>\2\2\u01ec\u0086\3\2\2\2\u01ed")
        buf.write("\u01ee\7@\2\2\u01ee\u0088\3\2\2\2\u01ef\u01f0\7>\2\2\u01f0")
        buf.write("\u01f1\7?\2\2\u01f1\u008a\3\2\2\2\u01f2\u01f3\7@\2\2\u01f3")
        buf.write("\u01f4\7?\2\2\u01f4\u008c\3\2\2\2\u01f5\u01f6\7\60\2\2")
        buf.write("\u01f6\u008e\3\2\2\2\u01f7\u01f8\7?\2\2\u01f8\u01f9\7")
        buf.write("?\2\2\u01f9\u01fa\7\60\2\2\u01fa\u0090\3\2\2\2\u01fb\u01fc")
        buf.write("\7-\2\2\u01fc\u01fd\7\60\2\2\u01fd\u0092\3\2\2\2\u01fe")
        buf.write("\u01ff\7<\2\2\u01ff\u0200\7<\2\2\u0200\u0094\3\2\2\2\u0201")
        buf.write("\u0203\t\r\2\2\u0202\u0201\3\2\2\2\u0203\u0204\3\2\2\2")
        buf.write("\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0206\3")
        buf.write("\2\2\2\u0206\u0207\bK\5\2\u0207\u0096\3\2\2\2\u0208\u020c")
        buf.write("\7$\2\2\u0209\u020b\5\5\3\2\u020a\u0209\3\2\2\2\u020b")
        buf.write("\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2")
        buf.write("\u020d\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0211\t")
        buf.write("\16\2\2\u0210\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212")
        buf.write("\u0213\bL\6\2\u0213\u0098\3\2\2\2\u0214\u0218\7$\2\2\u0215")
        buf.write("\u0217\5\5\3\2\u0216\u0215\3\2\2\2\u0217\u021a\3\2\2\2")
        buf.write("\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021b\3")
        buf.write("\2\2\2\u021a\u0218\3\2\2\2\u021b\u021c\5\u009bN\2\u021c")
        buf.write("\u021d\bM\7\2\u021d\u009a\3\2\2\2\u021e\u021f\7^\2\2\u021f")
        buf.write("\u0222\n\3\2\2\u0220\u0222\n\17\2\2\u0221\u021e\3\2\2")
        buf.write("\2\u0221\u0220\3\2\2\2\u0222\u009c\3\2\2\2\u0223\u0224")
        buf.write("\13\2\2\2\u0224\u0225\bO\b\2\u0225\u009e\3\2\2\2\u0226")
        buf.write("\u0227\13\2\2\2\u0227\u00a0\3\2\2\2\35\2\u00a8\u00b3\u00b9")
        buf.write("\u00bf\u00c4\u00c7\u00ce\u00d5\u00db\u00e7\u00ec\u00ef")
        buf.write("\u00f7\u00fb\u0100\u0104\u010a\u01a8\u01b1\u01b7\u01bd")
        buf.write("\u0204\u020c\u0210\u0218\u0221\t\3\5\2\3\17\3\3\23\4\b")
        buf.write("\2\2\3L\5\3M\6\3O\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INT_LITERAL = 2
    Dec = 3
    Bin = 4
    Hex = 5
    Otc = 6
    Nonzerodigit = 7
    Digit = 8
    Bindigit = 9
    Octdigit = 10
    Hexdigit = 11
    FL_LITERAL = 12
    FRACPART = 13
    EXPPART = 14
    BOOL_LITERAL = 15
    STRING_LITERAL = 16
    INTTYPE = 17
    FLOATTYPE = 18
    STRTYPE = 19
    BOOLTYPE = 20
    VOIDTYPE = 21
    CLASS = 22
    VAL = 23
    VAR = 24
    BREAK = 25
    FOREACH = 26
    NULL = 27
    CONSTRUC = 28
    DESTRUC = 29
    CONTINUE = 30
    TRUE = 31
    IF = 32
    FALSE = 33
    NEW = 34
    ELSE = 35
    ELSEIF = 36
    BY = 37
    RETURN = 38
    IN = 39
    ARRAY = 40
    BLOCK_COMMENT = 41
    ID = 42
    INTLIT = 43
    LB = 44
    RB = 45
    LP = 46
    RP = 47
    SEMI = 48
    COLON = 49
    CM = 50
    LSB = 51
    RSB = 52
    ADD = 53
    SUB = 54
    MUL = 55
    DIV = 56
    MOD = 57
    NOT = 58
    OR = 59
    AND = 60
    NEQ = 61
    EQ = 62
    ASSIGN = 63
    LT = 64
    GT = 65
    LE = 66
    GE = 67
    DOT = 68
    COMPARE_STRINGS = 69
    CONCATENATE_STRINGS = 70
    ACCESS = 71
    WS = 72
    UNCLOSE_STRING = 73
    ILLEGAL_ESCAPE = 74
    ERROR_CHAR = 75
    UNTERMINATED_COMMENT = 76

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Int'", "'Float'", "'String'", "'Boolean'", "'Void'", 
            "'class'", "'Val'", "'Var'", "'Break'", "'Foreach '", "'Null'", 
            "'Constructor'", "' Destructor'", "'Continue'", "'True'", "'If'", 
            "'False'", "'New'", "'Else'", "'Elseif'", "'By'", "'Return'", 
            "'In'", "'Array'", "'('", "')'", "'{'", "'}'", "';'", "':'", 
            "','", "'['", "']'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'||'", "'&&'", "'!='", "'=='", "'='", "'<'", "'>'", "'<='", 
            "'>='", "'.'", "'==.'", "'+.'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "INT_LITERAL", "Dec", "Bin", "Hex", "Otc", "Nonzerodigit", "Digit", 
            "Bindigit", "Octdigit", "Hexdigit", "FL_LITERAL", "FRACPART", 
            "EXPPART", "BOOL_LITERAL", "STRING_LITERAL", "INTTYPE", "FLOATTYPE", 
            "STRTYPE", "BOOLTYPE", "VOIDTYPE", "CLASS", "VAL", "VAR", "BREAK", 
            "FOREACH", "NULL", "CONSTRUC", "DESTRUC", "CONTINUE", "TRUE", 
            "IF", "FALSE", "NEW", "ELSE", "ELSEIF", "BY", "RETURN", "IN", 
            "ARRAY", "BLOCK_COMMENT", "ID", "INTLIT", "LB", "RB", "LP", 
            "RP", "SEMI", "COLON", "CM", "LSB", "RSB", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "NOT", "OR", "AND", "NEQ", "EQ", "ASSIGN", "LT", 
            "GT", "LE", "GE", "DOT", "COMPARE_STRINGS", "CONCATENATE_STRINGS", 
            "ACCESS", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "STR_CHAR", "ESC_SEQ", "INT_LITERAL", "Dec", "Bin", 
                  "Hex", "Otc", "Nonzerodigit", "Digit", "Bindigit", "Octdigit", 
                  "Hexdigit", "FL_LITERAL", "FRACPART", "EXPPART", "BOOL_LITERAL", 
                  "STRING_LITERAL", "INTTYPE", "FLOATTYPE", "STRTYPE", "BOOLTYPE", 
                  "VOIDTYPE", "CLASS", "VAL", "VAR", "BREAK", "FOREACH", 
                  "NULL", "CONSTRUC", "DESTRUC", "CONTINUE", "TRUE", "IF", 
                  "FALSE", "NEW", "ELSE", "ELSEIF", "BY", "RETURN", "IN", 
                  "ARRAY", "BLOCK_COMMENT", "ID", "INTLIT", "LB", "RB", 
                  "LP", "RP", "SEMI", "COLON", "CM", "LSB", "RSB", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "NOT", "OR", "AND", "NEQ", 
                  "EQ", "ASSIGN", "LT", "GT", "LE", "GE", "DOT", "COMPARE_STRINGS", 
                  "CONCATENATE_STRINGS", "ACCESS", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.INT_LITERAL_action 
            actions[13] = self.FL_LITERAL_action 
            actions[17] = self.STRING_LITERAL_action 
            actions[74] = self.UNCLOSE_STRING_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            actions[77] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             seft.text = seft.text.replace("_", "") 
     

    def FL_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             seft.text = seft.text.replace("_", "") 
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		raise ErrorToken(self.text)
            	
     


