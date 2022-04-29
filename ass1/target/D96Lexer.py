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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0225\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00a7")
        buf.write("\n\3\3\3\3\3\3\4\3\4\6\4\u00ad\n\4\r\4\16\4\u00ae\3\5")
        buf.write("\3\5\7\5\u00b3\n\5\f\5\16\5\u00b6\13\5\3\5\5\5\u00b9\n")
        buf.write("\5\3\6\3\6\3\6\6\6\u00be\n\6\r\6\16\6\u00bf\3\7\3\7\3")
        buf.write("\7\6\7\u00c5\n\7\r\7\16\7\u00c6\3\b\3\b\3\b\5\b\u00cc")
        buf.write("\n\b\3\b\5\b\u00cf\n\b\3\b\3\b\3\b\3\b\3\b\5\b\u00d6\n")
        buf.write("\b\3\t\3\t\5\t\u00da\n\t\3\n\3\n\5\n\u00de\n\n\3\n\3\n")
        buf.write("\3\13\3\13\5\13\u00e4\n\13\3\f\3\f\7\f\u00e8\n\f\f\f\16")
        buf.write("\f\u00eb\13\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r\u00f5")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!")
        buf.write("\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\7)\u019d\n)\f)\16")
        buf.write(")\u01a0\13)\3)\3)\3)\3)\3)\3*\3*\7*\u01a9\n*\f*\16*\u01ac")
        buf.write("\13*\3+\3+\3+\7+\u01b1\n+\f+\16+\u01b4\13+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\3B\3B\3B\3C\3C\3C\3D\3D\3E\3E\3E\3F\3F\3F\3F\3G\3")
        buf.write("G\3G\3H\6H\u01f9\nH\rH\16H\u01fa\3H\3H\3I\3I\3J\3J\7J")
        buf.write("\u0203\nJ\fJ\16J\u0206\13J\3J\5J\u0209\nJ\3J\3J\3K\3K")
        buf.write("\7K\u020f\nK\fK\16K\u0212\13K\3K\3K\3K\3L\3L\5L\u0219")
        buf.write("\nL\3M\3M\3M\3N\3N\3N\5N\u0221\nN\3O\3O\3O\3\u019e\2P")
        buf.write("\3\3\5\4\7\2\t\2\13\2\r\2\17\5\21\2\23\2\25\6\27\7\31")
        buf.write("\b\33\t\35\n\37\13!\f#\r%\16\'\17)\20+\21-\22/\23\61\24")
        buf.write("\63\25\65\26\67\279\30;\31=\32?\33A\34C\35E\36G\37I K")
        buf.write("!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61m\62o\63q\64s\65")
        buf.write("u\66w\67y8{9}:\177;\u0081<\u0083=\u0085>\u0087?\u0089")
        buf.write("@\u008bA\u008dB\u008fC\u0091D\u0093E\u0095F\u0097\2\u0099")
        buf.write("\2\u009b\2\u009dG\3\2\21\4\2\629aa\3\2\63;\4\2\62;aa\4")
        buf.write("\2ZZzz\6\2\62;CHaach\4\2DDdd\4\2\62\63aa\4\2GGgg\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\7\3\n\f\16\17")
        buf.write("$$))^^\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2^^\2")
        buf.write("\u0236\2\3\3\2\2\2\2\5\3\2\2\2\2\17\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u009d\3\2\2\2\3\u009f")
        buf.write("\3\2\2\2\5\u00a6\3\2\2\2\7\u00aa\3\2\2\2\t\u00b8\3\2\2")
        buf.write("\2\13\u00ba\3\2\2\2\r\u00c1\3\2\2\2\17\u00d5\3\2\2\2\21")
        buf.write("\u00d7\3\2\2\2\23\u00db\3\2\2\2\25\u00e3\3\2\2\2\27\u00e5")
        buf.write("\3\2\2\2\31\u00f4\3\2\2\2\33\u00f6\3\2\2\2\35\u00fa\3")
        buf.write("\2\2\2\37\u0100\3\2\2\2!\u0107\3\2\2\2#\u010f\3\2\2\2")
        buf.write("%\u0114\3\2\2\2\'\u011b\3\2\2\2)\u0121\3\2\2\2+\u0125")
        buf.write("\3\2\2\2-\u0129\3\2\2\2/\u012f\3\2\2\2\61\u0137\3\2\2")
        buf.write("\2\63\u013c\3\2\2\2\65\u0148\3\2\2\2\67\u0153\3\2\2\2")
        buf.write("9\u015c\3\2\2\2;\u0161\3\2\2\2=\u0164\3\2\2\2?\u016a\3")
        buf.write("\2\2\2A\u016e\3\2\2\2C\u0173\3\2\2\2E\u017a\3\2\2\2G\u017d")
        buf.write("\3\2\2\2I\u0184\3\2\2\2K\u0187\3\2\2\2M\u018d\3\2\2\2")
        buf.write("O\u0193\3\2\2\2Q\u0198\3\2\2\2S\u01a6\3\2\2\2U\u01ad\3")
        buf.write("\2\2\2W\u01b5\3\2\2\2Y\u01b7\3\2\2\2[\u01b9\3\2\2\2]\u01bb")
        buf.write("\3\2\2\2_\u01bd\3\2\2\2a\u01bf\3\2\2\2c\u01c1\3\2\2\2")
        buf.write("e\u01c3\3\2\2\2g\u01c5\3\2\2\2i\u01c7\3\2\2\2k\u01c9\3")
        buf.write("\2\2\2m\u01cb\3\2\2\2o\u01cd\3\2\2\2q\u01cf\3\2\2\2s\u01d1")
        buf.write("\3\2\2\2u\u01d3\3\2\2\2w\u01d6\3\2\2\2y\u01d9\3\2\2\2")
        buf.write("{\u01dc\3\2\2\2}\u01df\3\2\2\2\177\u01e1\3\2\2\2\u0081")
        buf.write("\u01e3\3\2\2\2\u0083\u01e5\3\2\2\2\u0085\u01e8\3\2\2\2")
        buf.write("\u0087\u01eb\3\2\2\2\u0089\u01ed\3\2\2\2\u008b\u01f0\3")
        buf.write("\2\2\2\u008d\u01f4\3\2\2\2\u008f\u01f8\3\2\2\2\u0091\u01fe")
        buf.write("\3\2\2\2\u0093\u0200\3\2\2\2\u0095\u020c\3\2\2\2\u0097")
        buf.write("\u0218\3\2\2\2\u0099\u021a\3\2\2\2\u009b\u0220\3\2\2\2")
        buf.write("\u009d\u0222\3\2\2\2\u009f\u00a0\7\60\2\2\u00a0\u00a1")
        buf.write("\7\60\2\2\u00a1\4\3\2\2\2\u00a2\u00a7\5\7\4\2\u00a3\u00a7")
        buf.write("\5\t\5\2\u00a4\u00a7\5\13\6\2\u00a5\u00a7\5\r\7\2\u00a6")
        buf.write("\u00a2\3\2\2\2\u00a6\u00a3\3\2\2\2\u00a6\u00a4\3\2\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\b")
        buf.write("\3\2\2\u00a9\6\3\2\2\2\u00aa\u00ac\7\62\2\2\u00ab\u00ad")
        buf.write("\t\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\b\3\2\2\2\u00b0")
        buf.write("\u00b4\t\3\2\2\u00b1\u00b3\t\4\2\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3")
        buf.write("\2\2\2\u00b5\u00b9\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b9")
        buf.write("\7\62\2\2\u00b8\u00b0\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9")
        buf.write("\n\3\2\2\2\u00ba\u00bb\7\62\2\2\u00bb\u00bd\t\5\2\2\u00bc")
        buf.write("\u00be\t\6\2\2\u00bd\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\f\3\2\2")
        buf.write("\2\u00c1\u00c2\7\62\2\2\u00c2\u00c4\t\7\2\2\u00c3\u00c5")
        buf.write("\t\b\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\16\3\2\2\2\u00c8")
        buf.write("\u00ce\5\t\5\2\u00c9\u00cb\5\21\t\2\u00ca\u00cc\5\23\n")
        buf.write("\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cf")
        buf.write("\3\2\2\2\u00cd\u00cf\5\23\n\2\u00ce\u00c9\3\2\2\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\b\b\3\2")
        buf.write("\u00d1\u00d6\3\2\2\2\u00d2\u00d3\5\21\t\2\u00d3\u00d4")
        buf.write("\5\23\n\2\u00d4\u00d6\3\2\2\2\u00d5\u00c8\3\2\2\2\u00d5")
        buf.write("\u00d2\3\2\2\2\u00d6\20\3\2\2\2\u00d7\u00d9\7\60\2\2\u00d8")
        buf.write("\u00da\5\t\5\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\22\3\2\2\2\u00db\u00dd\t\t\2\2\u00dc\u00de\7/\2")
        buf.write("\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df\u00e0\5\t\5\2\u00e0\24\3\2\2\2\u00e1\u00e4")
        buf.write("\59\35\2\u00e2\u00e4\5=\37\2\u00e3\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e4\26\3\2\2\2\u00e5\u00e9\7$\2\2\u00e6")
        buf.write("\u00e8\5\u0097L\2\u00e7\u00e6\3\2\2\2\u00e8\u00eb\3\2")
        buf.write("\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec")
        buf.write("\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ed\7$\2\2\u00ed")
        buf.write("\u00ee\b\f\4\2\u00ee\30\3\2\2\2\u00ef\u00f5\5\33\16\2")
        buf.write("\u00f0\u00f5\5\35\17\2\u00f1\u00f5\5\37\20\2\u00f2\u00f5")
        buf.write("\5!\21\2\u00f3\u00f5\5%\23\2\u00f4\u00ef\3\2\2\2\u00f4")
        buf.write("\u00f0\3\2\2\2\u00f4\u00f1\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f3\3\2\2\2\u00f5\32\3\2\2\2\u00f6\u00f7\7K\2")
        buf.write("\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7v\2\2\u00f9\34\3\2")
        buf.write("\2\2\u00fa\u00fb\7H\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7v\2\2\u00ff\36")
        buf.write("\3\2\2\2\u0100\u0101\7U\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7k\2\2\u0104\u0105\7p\2\2\u0105\u0106")
        buf.write("\7i\2\2\u0106 \3\2\2\2\u0107\u0108\7D\2\2\u0108\u0109")
        buf.write("\7q\2\2\u0109\u010a\7q\2\2\u010a\u010b\7n\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c\u010d\7c\2\2\u010d\u010e\7p\2\2\u010e\"")
        buf.write("\3\2\2\2\u010f\u0110\7X\2\2\u0110\u0111\7q\2\2\u0111\u0112")
        buf.write("\7k\2\2\u0112\u0113\7f\2\2\u0113$\3\2\2\2\u0114\u0115")
        buf.write("\5M\'\2\u0115\u0116\5e\63\2\u0116\u0117\5\31\r\2\u0117")
        buf.write("\u0118\5c\62\2\u0118\u0119\5\5\3\2\u0119\u011a\5g\64\2")
        buf.write("\u011a&\3\2\2\2\u011b\u011c\7E\2\2\u011c\u011d\7n\2\2")
        buf.write("\u011d\u011e\7c\2\2\u011e\u011f\7u\2\2\u011f\u0120\7u")
        buf.write("\2\2\u0120(\3\2\2\2\u0121\u0122\7X\2\2\u0122\u0123\7c")
        buf.write("\2\2\u0123\u0124\7n\2\2\u0124*\3\2\2\2\u0125\u0126\7X")
        buf.write("\2\2\u0126\u0127\7c\2\2\u0127\u0128\7t\2\2\u0128,\3\2")
        buf.write("\2\2\u0129\u012a\7D\2\2\u012a\u012b\7t\2\2\u012b\u012c")
        buf.write("\7g\2\2\u012c\u012d\7c\2\2\u012d\u012e\7m\2\2\u012e.\3")
        buf.write("\2\2\2\u012f\u0130\7H\2\2\u0130\u0131\7q\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132\u0133\7g\2\2\u0133\u0134\7c\2\2\u0134\u0135")
        buf.write("\7e\2\2\u0135\u0136\7j\2\2\u0136\60\3\2\2\2\u0137\u0138")
        buf.write("\7P\2\2\u0138\u0139\7w\2\2\u0139\u013a\7n\2\2\u013a\u013b")
        buf.write("\7n\2\2\u013b\62\3\2\2\2\u013c\u013d\7E\2\2\u013d\u013e")
        buf.write("\7q\2\2\u013e\u013f\7p\2\2\u013f\u0140\7u\2\2\u0140\u0141")
        buf.write("\7v\2\2\u0141\u0142\7t\2\2\u0142\u0143\7w\2\2\u0143\u0144")
        buf.write("\7e\2\2\u0144\u0145\7v\2\2\u0145\u0146\7q\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147\64\3\2\2\2\u0148\u0149\7F\2\2\u0149\u014a")
        buf.write("\7g\2\2\u014a\u014b\7u\2\2\u014b\u014c\7v\2\2\u014c\u014d")
        buf.write("\7t\2\2\u014d\u014e\7w\2\2\u014e\u014f\7e\2\2\u014f\u0150")
        buf.write("\7v\2\2\u0150\u0151\7q\2\2\u0151\u0152\7t\2\2\u0152\66")
        buf.write("\3\2\2\2\u0153\u0154\7E\2\2\u0154\u0155\7q\2\2\u0155\u0156")
        buf.write("\7p\2\2\u0156\u0157\7v\2\2\u0157\u0158\7k\2\2\u0158\u0159")
        buf.write("\7p\2\2\u0159\u015a\7w\2\2\u015a\u015b\7g\2\2\u015b8\3")
        buf.write("\2\2\2\u015c\u015d\7V\2\2\u015d\u015e\7t\2\2\u015e\u015f")
        buf.write("\7w\2\2\u015f\u0160\7g\2\2\u0160:\3\2\2\2\u0161\u0162")
        buf.write("\7K\2\2\u0162\u0163\7h\2\2\u0163<\3\2\2\2\u0164\u0165")
        buf.write("\7H\2\2\u0165\u0166\7c\2\2\u0166\u0167\7n\2\2\u0167\u0168")
        buf.write("\7u\2\2\u0168\u0169\7g\2\2\u0169>\3\2\2\2\u016a\u016b")
        buf.write("\7P\2\2\u016b\u016c\7g\2\2\u016c\u016d\7y\2\2\u016d@\3")
        buf.write("\2\2\2\u016e\u016f\7G\2\2\u016f\u0170\7n\2\2\u0170\u0171")
        buf.write("\7u\2\2\u0171\u0172\7g\2\2\u0172B\3\2\2\2\u0173\u0174")
        buf.write("\7G\2\2\u0174\u0175\7n\2\2\u0175\u0176\7u\2\2\u0176\u0177")
        buf.write("\7g\2\2\u0177\u0178\7k\2\2\u0178\u0179\7h\2\2\u0179D\3")
        buf.write("\2\2\2\u017a\u017b\7D\2\2\u017b\u017c\7{\2\2\u017cF\3")
        buf.write("\2\2\2\u017d\u017e\7T\2\2\u017e\u017f\7g\2\2\u017f\u0180")
        buf.write("\7v\2\2\u0180\u0181\7w\2\2\u0181\u0182\7t\2\2\u0182\u0183")
        buf.write("\7p\2\2\u0183H\3\2\2\2\u0184\u0185\7K\2\2\u0185\u0186")
        buf.write("\7p\2\2\u0186J\3\2\2\2\u0187\u0188\7Y\2\2\u0188\u0189")
        buf.write("\7j\2\2\u0189\u018a\7k\2\2\u018a\u018b\7n\2\2\u018b\u018c")
        buf.write("\7g\2\2\u018cL\3\2\2\2\u018d\u018e\7C\2\2\u018e\u018f")
        buf.write("\7t\2\2\u018f\u0190\7t\2\2\u0190\u0191\7c\2\2\u0191\u0192")
        buf.write("\7{\2\2\u0192N\3\2\2\2\u0193\u0194\7U\2\2\u0194\u0195")
        buf.write("\7g\2\2\u0195\u0196\7n\2\2\u0196\u0197\7h\2\2\u0197P\3")
        buf.write("\2\2\2\u0198\u0199\7%\2\2\u0199\u019a\7%\2\2\u019a\u019e")
        buf.write("\3\2\2\2\u019b\u019d\13\2\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("\u01a0\3\2\2\2\u019e\u019f\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2\7")
        buf.write("%\2\2\u01a2\u01a3\7%\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5")
        buf.write("\b)\5\2\u01a5R\3\2\2\2\u01a6\u01aa\t\n\2\2\u01a7\u01a9")
        buf.write("\t\13\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01abT\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ad\u01ae\7&\2\2\u01ae\u01b2\t\n\2\2")
        buf.write("\u01af\u01b1\t\13\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b4")
        buf.write("\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("V\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\7*\2\2\u01b6")
        buf.write("X\3\2\2\2\u01b7\u01b8\7+\2\2\u01b8Z\3\2\2\2\u01b9\u01ba")
        buf.write("\7}\2\2\u01ba\\\3\2\2\2\u01bb\u01bc\7\177\2\2\u01bc^\3")
        buf.write("\2\2\2\u01bd\u01be\7=\2\2\u01be`\3\2\2\2\u01bf\u01c0\7")
        buf.write("<\2\2\u01c0b\3\2\2\2\u01c1\u01c2\7.\2\2\u01c2d\3\2\2\2")
        buf.write("\u01c3\u01c4\7]\2\2\u01c4f\3\2\2\2\u01c5\u01c6\7_\2\2")
        buf.write("\u01c6h\3\2\2\2\u01c7\u01c8\7-\2\2\u01c8j\3\2\2\2\u01c9")
        buf.write("\u01ca\7/\2\2\u01cal\3\2\2\2\u01cb\u01cc\7,\2\2\u01cc")
        buf.write("n\3\2\2\2\u01cd\u01ce\7\61\2\2\u01cep\3\2\2\2\u01cf\u01d0")
        buf.write("\7\'\2\2\u01d0r\3\2\2\2\u01d1\u01d2\7#\2\2\u01d2t\3\2")
        buf.write("\2\2\u01d3\u01d4\7~\2\2\u01d4\u01d5\7~\2\2\u01d5v\3\2")
        buf.write("\2\2\u01d6\u01d7\7(\2\2\u01d7\u01d8\7(\2\2\u01d8x\3\2")
        buf.write("\2\2\u01d9\u01da\7#\2\2\u01da\u01db\7?\2\2\u01dbz\3\2")
        buf.write("\2\2\u01dc\u01dd\7?\2\2\u01dd\u01de\7?\2\2\u01de|\3\2")
        buf.write("\2\2\u01df\u01e0\7?\2\2\u01e0~\3\2\2\2\u01e1\u01e2\7>")
        buf.write("\2\2\u01e2\u0080\3\2\2\2\u01e3\u01e4\7@\2\2\u01e4\u0082")
        buf.write("\3\2\2\2\u01e5\u01e6\7>\2\2\u01e6\u01e7\7?\2\2\u01e7\u0084")
        buf.write("\3\2\2\2\u01e8\u01e9\7@\2\2\u01e9\u01ea\7?\2\2\u01ea\u0086")
        buf.write("\3\2\2\2\u01eb\u01ec\7\60\2\2\u01ec\u0088\3\2\2\2\u01ed")
        buf.write("\u01ee\7<\2\2\u01ee\u01ef\7<\2\2\u01ef\u008a\3\2\2\2\u01f0")
        buf.write("\u01f1\7?\2\2\u01f1\u01f2\7?\2\2\u01f2\u01f3\7\60\2\2")
        buf.write("\u01f3\u008c\3\2\2\2\u01f4\u01f5\7-\2\2\u01f5\u01f6\7")
        buf.write("\60\2\2\u01f6\u008e\3\2\2\2\u01f7\u01f9\t\f\2\2\u01f8")
        buf.write("\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2")
        buf.write("\u01fa\u01fb\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\b")
        buf.write("H\5\2\u01fd\u0090\3\2\2\2\u01fe\u01ff\13\2\2\2\u01ff\u0092")
        buf.write("\3\2\2\2\u0200\u0204\7$\2\2\u0201\u0203\5\u0097L\2\u0202")
        buf.write("\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204\u0202\3\2\2\2")
        buf.write("\u0204\u0205\3\2\2\2\u0205\u0208\3\2\2\2\u0206\u0204\3")
        buf.write("\2\2\2\u0207\u0209\t\r\2\2\u0208\u0207\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u020b\bJ\6\2\u020b\u0094\3\2\2\2\u020c")
        buf.write("\u0210\7$\2\2\u020d\u020f\5\u0097L\2\u020e\u020d\3\2\2")
        buf.write("\2\u020f\u0212\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211")
        buf.write("\3\2\2\2\u0211\u0213\3\2\2\2\u0212\u0210\3\2\2\2\u0213")
        buf.write("\u0214\5\u009bN\2\u0214\u0215\bK\7\2\u0215\u0096\3\2\2")
        buf.write("\2\u0216\u0219\n\16\2\2\u0217\u0219\5\u0099M\2\u0218\u0216")
        buf.write("\3\2\2\2\u0218\u0217\3\2\2\2\u0219\u0098\3\2\2\2\u021a")
        buf.write("\u021b\7^\2\2\u021b\u021c\t\17\2\2\u021c\u009a\3\2\2\2")
        buf.write("\u021d\u021e\7^\2\2\u021e\u0221\n\17\2\2\u021f\u0221\n")
        buf.write("\20\2\2\u0220\u021d\3\2\2\2\u0220\u021f\3\2\2\2\u0221")
        buf.write("\u009c\3\2\2\2\u0222\u0223\13\2\2\2\u0223\u0224\bO\b\2")
        buf.write("\u0224\u009e\3\2\2\2\32\2\u00a6\u00ae\u00b4\u00b8\u00bf")
        buf.write("\u00c6\u00cb\u00ce\u00d5\u00d9\u00dd\u00e3\u00e9\u00f4")
        buf.write("\u019e\u01aa\u01b2\u01fa\u0204\u0208\u0210\u0218\u0220")
        buf.write("\t\3\3\2\3\b\3\3\f\4\b\2\2\3J\5\3K\6\3O\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INT_LITERAL = 2
    FL_LITERAL = 3
    BOOL_LITERAL = 4
    STRING_LITERAL = 5
    TYPE = 6
    INTTYPE = 7
    FLOATTYPE = 8
    STRTYPE = 9
    BOOLTYPE = 10
    VOIDTYPE = 11
    ARRAYTYPE = 12
    CLASS = 13
    VAL = 14
    VAR = 15
    BREAK = 16
    FOREACH = 17
    NULL = 18
    CONSTRUC = 19
    DESTRUC = 20
    CONTINUE = 21
    TRUE = 22
    IF = 23
    FALSE = 24
    NEW = 25
    ELSE = 26
    ELSEIF = 27
    BY = 28
    RETURN = 29
    IN = 30
    WHILE = 31
    ARRAY = 32
    SELF = 33
    BLOCK_COMMENT = 34
    ID = 35
    Dollar_ID = 36
    LB = 37
    RB = 38
    LP = 39
    RP = 40
    SEMI = 41
    COLON = 42
    CM = 43
    LSB = 44
    RSB = 45
    ADD = 46
    SUB = 47
    MUL = 48
    DIV = 49
    MOD = 50
    NOT = 51
    OR = 52
    AND = 53
    NEQ = 54
    EQ = 55
    ASSIGN = 56
    LT = 57
    GT = 58
    LE = 59
    GE = 60
    DOT = 61
    ACCESS = 62
    STR_CMP = 63
    STR_CAT = 64
    WS = 65
    UNTERMINATED_COMMENT = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68
    ERROR_CHAR = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'..'", "'Int'", "'Float'", "'String'", "'Boolean'", "'Void'", 
            "'Class'", "'Val'", "'Var'", "'Break'", "'Foreach'", "'Null'", 
            "'Constructor'", "'Destructor'", "'Continue'", "'True'", "'If'", 
            "'False'", "'New'", "'Else'", "'Elseif'", "'By'", "'Return'", 
            "'In'", "'While'", "'Array'", "'Self'", "'('", "')'", "'{'", 
            "'}'", "';'", "':'", "','", "'['", "']'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'||'", "'&&'", "'!='", "'=='", "'='", 
            "'<'", "'>'", "'<='", "'>='", "'.'", "'::'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>",
            "INT_LITERAL", "FL_LITERAL", "BOOL_LITERAL", "STRING_LITERAL", 
            "TYPE", "INTTYPE", "FLOATTYPE", "STRTYPE", "BOOLTYPE", "VOIDTYPE", 
            "ARRAYTYPE", "CLASS", "VAL", "VAR", "BREAK", "FOREACH", "NULL", 
            "CONSTRUC", "DESTRUC", "CONTINUE", "TRUE", "IF", "FALSE", "NEW", 
            "ELSE", "ELSEIF", "BY", "RETURN", "IN", "WHILE", "ARRAY", "SELF", 
            "BLOCK_COMMENT", "ID", "Dollar_ID", "LB", "RB", "LP", "RP", 
            "SEMI", "COLON", "CM", "LSB", "RSB", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "NOT", "OR", "AND", "NEQ", "EQ", "ASSIGN", "LT", "GT", 
            "LE", "GE", "DOT", "ACCESS", "STR_CMP", "STR_CAT", "WS", "UNTERMINATED_COMMENT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "INT_LITERAL", "OCT", "DEC", "HEX", "BIN", "FL_LITERAL", 
                  "FRACPART", "EXPPART", "BOOL_LITERAL", "STRING_LITERAL", 
                  "TYPE", "INTTYPE", "FLOATTYPE", "STRTYPE", "BOOLTYPE", 
                  "VOIDTYPE", "ARRAYTYPE", "CLASS", "VAL", "VAR", "BREAK", 
                  "FOREACH", "NULL", "CONSTRUC", "DESTRUC", "CONTINUE", 
                  "TRUE", "IF", "FALSE", "NEW", "ELSE", "ELSEIF", "BY", 
                  "RETURN", "IN", "WHILE", "ARRAY", "SELF", "BLOCK_COMMENT", 
                  "ID", "Dollar_ID", "LB", "RB", "LP", "RP", "SEMI", "COLON", 
                  "CM", "LSB", "RSB", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "NOT", "OR", "AND", "NEQ", "EQ", "ASSIGN", "LT", "GT", 
                  "LE", "GE", "DOT", "ACCESS", "STR_CMP", "STR_CAT", "WS", 
                  "UNTERMINATED_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit();
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);

        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.INT_LITERAL_action 
            actions[6] = self.FL_LITERAL_action 
            actions[10] = self.STRING_LITERAL_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[77] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text.replace("_", "") 
     

    def FL_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

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
            	
     


