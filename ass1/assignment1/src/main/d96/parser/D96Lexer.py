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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u025b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u00a9\n\3\3\3\3\3\3\4\3\4\6\4\u00af\n\4\r\4\16\4")
        buf.write("\u00b0\3\4\3\4\5\4\u00b5\n\4\3\4\7\4\u00b8\n\4\f\4\16")
        buf.write("\4\u00bb\13\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00c3\n\4\5")
        buf.write("\4\u00c5\n\4\3\5\3\5\3\5\5\5\u00ca\n\5\3\5\7\5\u00cd\n")
        buf.write("\5\f\5\16\5\u00d0\13\5\3\5\3\5\5\5\u00d4\n\5\3\6\3\6\5")
        buf.write("\6\u00d8\n\6\3\6\7\6\u00db\n\6\f\6\16\6\u00de\13\6\3\6")
        buf.write("\5\6\u00e1\n\6\3\7\3\7\3\7\3\7\5\7\u00e7\n\7\3\7\7\7\u00ea")
        buf.write("\n\7\f\7\16\7\u00ed\13\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00f5")
        buf.write("\n\7\5\7\u00f7\n\7\3\b\3\b\5\b\u00fb\n\b\3\b\7\b\u00fe")
        buf.write("\n\b\f\b\16\b\u0101\13\b\3\b\5\b\u0104\n\b\3\t\3\t\3\t")
        buf.write("\5\t\u0109\n\t\3\t\5\t\u010c\n\t\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\t\u0113\n\t\3\n\3\n\5\n\u0117\n\n\3\13\3\13\5\13\u011b")
        buf.write("\n\13\3\13\3\13\3\f\3\f\5\f\u0121\n\f\3\r\3\r\7\r\u0125")
        buf.write("\n\r\f\r\16\r\u0128\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\7(\u01cc\n(\f")
        buf.write("(\16(\u01cf\13(\3(\3(\3(\3(\3(\3)\5)\u01d7\n)\3)\7)\u01da")
        buf.write("\n)\f)\16)\u01dd\13)\3*\3*\6*\u01e1\n*\r*\16*\u01e2\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3>\3")
        buf.write(">\3?\3?\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3D\3D\3D\3E\3E\3")
        buf.write("E\3E\3F\3F\3F\3G\6G\u0228\nG\rG\16G\u0229\3G\3G\3H\3H")
        buf.write("\7H\u0230\nH\fH\16H\u0233\13H\3H\5H\u0236\nH\3H\3H\3I")
        buf.write("\3I\7I\u023c\nI\fI\16I\u023f\13I\3I\3I\3I\3J\3J\3J\5J")
        buf.write("\u0247\nJ\3K\3K\3K\3L\3L\3M\3M\5M\u0250\nM\3N\3N\3N\3")
        buf.write("O\3O\5O\u0257\nO\3P\3P\3P\3\u01cd\2Q\3\3\5\4\7\2\t\2\13")
        buf.write("\2\r\2\17\2\21\5\23\2\25\2\27\6\31\7\33\b\35\t\37\n!\13")
        buf.write("#\f%\r\'\16)\17+\20-\21/\22\61\23\63\24\65\25\67\269\27")
        buf.write(";\30=\31?\32A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(]")
        buf.write(")_*a+c,e-g.i/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177")
        buf.write(":\u0081;\u0083<\u0085=\u0087>\u0089?\u008b@\u008dA\u008f")
        buf.write("B\u0091C\u0093\2\u0095D\u0097E\u0099\2\u009b\2\u009d\2")
        buf.write("\u009f\2\3\2\26\4\2DDdd\3\2\62\63\3\2\639\3\2\629\3\2")
        buf.write("\63;\3\2\62;\4\2ZZzz\5\2\63;CHch\6\2\62;CHaach\4\2GGg")
        buf.write("g\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"")
        buf.write("\7\3\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2^^\7\2\n\f")
        buf.write("\16\17$$))^^\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\2\u0273")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\21\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\3\u00a1\3\2\2\2\5\u00a8\3\2\2\2\7\u00c4\3\2\2")
        buf.write("\2\t\u00d3\3\2\2\2\13\u00e0\3\2\2\2\r\u00f6\3\2\2\2\17")
        buf.write("\u0103\3\2\2\2\21\u0112\3\2\2\2\23\u0114\3\2\2\2\25\u0118")
        buf.write("\3\2\2\2\27\u0120\3\2\2\2\31\u0122\3\2\2\2\33\u012c\3")
        buf.write("\2\2\2\35\u0130\3\2\2\2\37\u0136\3\2\2\2!\u013d\3\2\2")
        buf.write("\2#\u0145\3\2\2\2%\u014a\3\2\2\2\'\u0150\3\2\2\2)\u0154")
        buf.write("\3\2\2\2+\u0158\3\2\2\2-\u015e\3\2\2\2/\u0166\3\2\2\2")
        buf.write("\61\u016b\3\2\2\2\63\u0177\3\2\2\2\65\u0182\3\2\2\2\67")
        buf.write("\u018b\3\2\2\29\u0190\3\2\2\2;\u0193\3\2\2\2=\u0199\3")
        buf.write("\2\2\2?\u019d\3\2\2\2A\u01a2\3\2\2\2C\u01a9\3\2\2\2E\u01ac")
        buf.write("\3\2\2\2G\u01b3\3\2\2\2I\u01b6\3\2\2\2K\u01bc\3\2\2\2")
        buf.write("M\u01c2\3\2\2\2O\u01c7\3\2\2\2Q\u01d6\3\2\2\2S\u01de\3")
        buf.write("\2\2\2U\u01e4\3\2\2\2W\u01e6\3\2\2\2Y\u01e8\3\2\2\2[\u01ea")
        buf.write("\3\2\2\2]\u01ec\3\2\2\2_\u01ee\3\2\2\2a\u01f0\3\2\2\2")
        buf.write("c\u01f2\3\2\2\2e\u01f4\3\2\2\2g\u01f6\3\2\2\2i\u01f8\3")
        buf.write("\2\2\2k\u01fa\3\2\2\2m\u01fc\3\2\2\2o\u01fe\3\2\2\2q\u0200")
        buf.write("\3\2\2\2s\u0202\3\2\2\2u\u0205\3\2\2\2w\u0208\3\2\2\2")
        buf.write("y\u020b\3\2\2\2{\u020e\3\2\2\2}\u0210\3\2\2\2\177\u0212")
        buf.write("\3\2\2\2\u0081\u0214\3\2\2\2\u0083\u0217\3\2\2\2\u0085")
        buf.write("\u021a\3\2\2\2\u0087\u021c\3\2\2\2\u0089\u021f\3\2\2\2")
        buf.write("\u008b\u0223\3\2\2\2\u008d\u0227\3\2\2\2\u008f\u022d\3")
        buf.write("\2\2\2\u0091\u0239\3\2\2\2\u0093\u0246\3\2\2\2\u0095\u0248")
        buf.write("\3\2\2\2\u0097\u024b\3\2\2\2\u0099\u024f\3\2\2\2\u009b")
        buf.write("\u0251\3\2\2\2\u009d\u0256\3\2\2\2\u009f\u0258\3\2\2\2")
        buf.write("\u00a1\u00a2\7\60\2\2\u00a2\u00a3\7\60\2\2\u00a3\4\3\2")
        buf.write("\2\2\u00a4\u00a9\5\t\5\2\u00a5\u00a9\5\13\6\2\u00a6\u00a9")
        buf.write("\5\r\7\2\u00a7\u00a9\5\7\4\2\u00a8\u00a4\3\2\2\2\u00a8")
        buf.write("\u00a5\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00aa\u00ab\b\3\2\2\u00ab\6\3\2\2")
        buf.write("\2\u00ac\u00ae\7\62\2\2\u00ad\u00af\t\2\2\2\u00ae\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b9\7\63\2")
        buf.write("\2\u00b3\u00b5\7a\2\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\t\3\2\2\u00b7")
        buf.write("\u00b4\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2")
        buf.write("\u00b9\u00ba\3\2\2\2\u00ba\u00c5\3\2\2\2\u00bb\u00b9\3")
        buf.write("\2\2\2\u00bc\u00bd\7\62\2\2\u00bd\u00be\7d\2\2\u00be\u00c3")
        buf.write("\7\62\2\2\u00bf\u00c0\7\62\2\2\u00c0\u00c1\7D\2\2\u00c1")
        buf.write("\u00c3\7\62\2\2\u00c2\u00bc\3\2\2\2\u00c2\u00bf\3\2\2")
        buf.write("\2\u00c3\u00c5\3\2\2\2\u00c4\u00ac\3\2\2\2\u00c4\u00c2")
        buf.write("\3\2\2\2\u00c5\b\3\2\2\2\u00c6\u00c7\7\62\2\2\u00c7\u00ce")
        buf.write("\t\4\2\2\u00c8\u00ca\7a\2\2\u00c9\u00c8\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cd\t\5\2\2")
        buf.write("\u00cc\u00c9\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3")
        buf.write("\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d4\3\2\2\2\u00d0\u00ce")
        buf.write("\3\2\2\2\u00d1\u00d2\7\62\2\2\u00d2\u00d4\7\62\2\2\u00d3")
        buf.write("\u00c6\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\n\3\2\2\2\u00d5")
        buf.write("\u00dc\t\6\2\2\u00d6\u00d8\7a\2\2\u00d7\u00d6\3\2\2\2")
        buf.write("\u00d7\u00d8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00db\t")
        buf.write("\7\2\2\u00da\u00d7\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e1\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00df\u00e1\7\62\2\2\u00e0\u00d5\3\2\2")
        buf.write("\2\u00e0\u00df\3\2\2\2\u00e1\f\3\2\2\2\u00e2\u00e3\7\62")
        buf.write("\2\2\u00e3\u00e4\t\b\2\2\u00e4\u00eb\t\t\2\2\u00e5\u00e7")
        buf.write("\7a\2\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00e8\3\2\2\2\u00e8\u00ea\t\n\2\2\u00e9\u00e6\3\2\2\2")
        buf.write("\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3")
        buf.write("\2\2\2\u00ec\u00f7\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef")
        buf.write("\7\62\2\2\u00ef\u00f0\7z\2\2\u00f0\u00f5\7\62\2\2\u00f1")
        buf.write("\u00f2\7\62\2\2\u00f2\u00f3\7Z\2\2\u00f3\u00f5\7\62\2")
        buf.write("\2\u00f4\u00ee\3\2\2\2\u00f4\u00f1\3\2\2\2\u00f5\u00f7")
        buf.write("\3\2\2\2\u00f6\u00e2\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7")
        buf.write("\16\3\2\2\2\u00f8\u00ff\t\6\2\2\u00f9\u00fb\7a\2\2\u00fa")
        buf.write("\u00f9\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc\u00fe\t\7\2\2\u00fd\u00fa\3\2\2\2\u00fe\u0101\3")
        buf.write("\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0104")
        buf.write("\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0104\7\62\2\2\u0103")
        buf.write("\u00f8\3\2\2\2\u0103\u0102\3\2\2\2\u0104\20\3\2\2\2\u0105")
        buf.write("\u010b\5\13\6\2\u0106\u0108\5\23\n\2\u0107\u0109\5\25")
        buf.write("\13\2\u0108\u0107\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010c")
        buf.write("\3\2\2\2\u010a\u010c\5\25\13\2\u010b\u0106\3\2\2\2\u010b")
        buf.write("\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e\b\t\3\2")
        buf.write("\u010e\u0113\3\2\2\2\u010f\u0110\5\23\n\2\u0110\u0111")
        buf.write("\5\25\13\2\u0111\u0113\3\2\2\2\u0112\u0105\3\2\2\2\u0112")
        buf.write("\u010f\3\2\2\2\u0113\22\3\2\2\2\u0114\u0116\7\60\2\2\u0115")
        buf.write("\u0117\5\17\b\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2")
        buf.write("\2\u0117\24\3\2\2\2\u0118\u011a\t\13\2\2\u0119\u011b\t")
        buf.write("\f\2\2\u011a\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c")
        buf.write("\3\2\2\2\u011c\u011d\5\17\b\2\u011d\26\3\2\2\2\u011e\u0121")
        buf.write("\5\67\34\2\u011f\u0121\5;\36\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u011f\3\2\2\2\u0121\30\3\2\2\2\u0122\u0126\7$\2\2\u0123")
        buf.write("\u0125\5\u0099M\2\u0124\u0123\3\2\2\2\u0125\u0128\3\2")
        buf.write("\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129")
        buf.write("\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a\7$\2\2\u012a")
        buf.write("\u012b\b\r\4\2\u012b\32\3\2\2\2\u012c\u012d\7K\2\2\u012d")
        buf.write("\u012e\7p\2\2\u012e\u012f\7v\2\2\u012f\34\3\2\2\2\u0130")
        buf.write("\u0131\7H\2\2\u0131\u0132\7n\2\2\u0132\u0133\7q\2\2\u0133")
        buf.write("\u0134\7c\2\2\u0134\u0135\7v\2\2\u0135\36\3\2\2\2\u0136")
        buf.write("\u0137\7U\2\2\u0137\u0138\7v\2\2\u0138\u0139\7t\2\2\u0139")
        buf.write("\u013a\7k\2\2\u013a\u013b\7p\2\2\u013b\u013c\7i\2\2\u013c")
        buf.write(" \3\2\2\2\u013d\u013e\7D\2\2\u013e\u013f\7q\2\2\u013f")
        buf.write("\u0140\7q\2\2\u0140\u0141\7n\2\2\u0141\u0142\7g\2\2\u0142")
        buf.write("\u0143\7c\2\2\u0143\u0144\7p\2\2\u0144\"\3\2\2\2\u0145")
        buf.write("\u0146\7X\2\2\u0146\u0147\7q\2\2\u0147\u0148\7k\2\2\u0148")
        buf.write("\u0149\7f\2\2\u0149$\3\2\2\2\u014a\u014b\7E\2\2\u014b")
        buf.write("\u014c\7n\2\2\u014c\u014d\7c\2\2\u014d\u014e\7u\2\2\u014e")
        buf.write("\u014f\7u\2\2\u014f&\3\2\2\2\u0150\u0151\7X\2\2\u0151")
        buf.write("\u0152\7c\2\2\u0152\u0153\7n\2\2\u0153(\3\2\2\2\u0154")
        buf.write("\u0155\7X\2\2\u0155\u0156\7c\2\2\u0156\u0157\7t\2\2\u0157")
        buf.write("*\3\2\2\2\u0158\u0159\7D\2\2\u0159\u015a\7t\2\2\u015a")
        buf.write("\u015b\7g\2\2\u015b\u015c\7c\2\2\u015c\u015d\7m\2\2\u015d")
        buf.write(",\3\2\2\2\u015e\u015f\7H\2\2\u015f\u0160\7q\2\2\u0160")
        buf.write("\u0161\7t\2\2\u0161\u0162\7g\2\2\u0162\u0163\7c\2\2\u0163")
        buf.write("\u0164\7e\2\2\u0164\u0165\7j\2\2\u0165.\3\2\2\2\u0166")
        buf.write("\u0167\7P\2\2\u0167\u0168\7w\2\2\u0168\u0169\7n\2\2\u0169")
        buf.write("\u016a\7n\2\2\u016a\60\3\2\2\2\u016b\u016c\7E\2\2\u016c")
        buf.write("\u016d\7q\2\2\u016d\u016e\7p\2\2\u016e\u016f\7u\2\2\u016f")
        buf.write("\u0170\7v\2\2\u0170\u0171\7t\2\2\u0171\u0172\7w\2\2\u0172")
        buf.write("\u0173\7e\2\2\u0173\u0174\7v\2\2\u0174\u0175\7q\2\2\u0175")
        buf.write("\u0176\7t\2\2\u0176\62\3\2\2\2\u0177\u0178\7F\2\2\u0178")
        buf.write("\u0179\7g\2\2\u0179\u017a\7u\2\2\u017a\u017b\7v\2\2\u017b")
        buf.write("\u017c\7t\2\2\u017c\u017d\7w\2\2\u017d\u017e\7e\2\2\u017e")
        buf.write("\u017f\7v\2\2\u017f\u0180\7q\2\2\u0180\u0181\7t\2\2\u0181")
        buf.write("\64\3\2\2\2\u0182\u0183\7E\2\2\u0183\u0184\7q\2\2\u0184")
        buf.write("\u0185\7p\2\2\u0185\u0186\7v\2\2\u0186\u0187\7k\2\2\u0187")
        buf.write("\u0188\7p\2\2\u0188\u0189\7w\2\2\u0189\u018a\7g\2\2\u018a")
        buf.write("\66\3\2\2\2\u018b\u018c\7V\2\2\u018c\u018d\7t\2\2\u018d")
        buf.write("\u018e\7w\2\2\u018e\u018f\7g\2\2\u018f8\3\2\2\2\u0190")
        buf.write("\u0191\7K\2\2\u0191\u0192\7h\2\2\u0192:\3\2\2\2\u0193")
        buf.write("\u0194\7H\2\2\u0194\u0195\7c\2\2\u0195\u0196\7n\2\2\u0196")
        buf.write("\u0197\7u\2\2\u0197\u0198\7g\2\2\u0198<\3\2\2\2\u0199")
        buf.write("\u019a\7P\2\2\u019a\u019b\7g\2\2\u019b\u019c\7y\2\2\u019c")
        buf.write(">\3\2\2\2\u019d\u019e\7G\2\2\u019e\u019f\7n\2\2\u019f")
        buf.write("\u01a0\7u\2\2\u01a0\u01a1\7g\2\2\u01a1@\3\2\2\2\u01a2")
        buf.write("\u01a3\7G\2\2\u01a3\u01a4\7n\2\2\u01a4\u01a5\7u\2\2\u01a5")
        buf.write("\u01a6\7g\2\2\u01a6\u01a7\7k\2\2\u01a7\u01a8\7h\2\2\u01a8")
        buf.write("B\3\2\2\2\u01a9\u01aa\7D\2\2\u01aa\u01ab\7{\2\2\u01ab")
        buf.write("D\3\2\2\2\u01ac\u01ad\7T\2\2\u01ad\u01ae\7g\2\2\u01ae")
        buf.write("\u01af\7v\2\2\u01af\u01b0\7w\2\2\u01b0\u01b1\7t\2\2\u01b1")
        buf.write("\u01b2\7p\2\2\u01b2F\3\2\2\2\u01b3\u01b4\7K\2\2\u01b4")
        buf.write("\u01b5\7p\2\2\u01b5H\3\2\2\2\u01b6\u01b7\7Y\2\2\u01b7")
        buf.write("\u01b8\7j\2\2\u01b8\u01b9\7k\2\2\u01b9\u01ba\7n\2\2\u01ba")
        buf.write("\u01bb\7g\2\2\u01bbJ\3\2\2\2\u01bc\u01bd\7C\2\2\u01bd")
        buf.write("\u01be\7t\2\2\u01be\u01bf\7t\2\2\u01bf\u01c0\7c\2\2\u01c0")
        buf.write("\u01c1\7{\2\2\u01c1L\3\2\2\2\u01c2\u01c3\7U\2\2\u01c3")
        buf.write("\u01c4\7g\2\2\u01c4\u01c5\7n\2\2\u01c5\u01c6\7h\2\2\u01c6")
        buf.write("N\3\2\2\2\u01c7\u01c8\7%\2\2\u01c8\u01c9\7%\2\2\u01c9")
        buf.write("\u01cd\3\2\2\2\u01ca\u01cc\13\2\2\2\u01cb\u01ca\3\2\2")
        buf.write("\2\u01cc\u01cf\3\2\2\2\u01cd\u01ce\3\2\2\2\u01cd\u01cb")
        buf.write("\3\2\2\2\u01ce\u01d0\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0")
        buf.write("\u01d1\7%\2\2\u01d1\u01d2\7%\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("\u01d4\b(\5\2\u01d4P\3\2\2\2\u01d5\u01d7\t\r\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d7\u01db\3\2\2\2\u01d8\u01da\t\16\2")
        buf.write("\2\u01d9\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dcR\3\2\2\2\u01dd\u01db")
        buf.write("\3\2\2\2\u01de\u01e0\7&\2\2\u01df\u01e1\t\16\2\2\u01e0")
        buf.write("\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e2\u01e3\3\2\2\2\u01e3T\3\2\2\2\u01e4\u01e5\7*\2\2")
        buf.write("\u01e5V\3\2\2\2\u01e6\u01e7\7+\2\2\u01e7X\3\2\2\2\u01e8")
        buf.write("\u01e9\7}\2\2\u01e9Z\3\2\2\2\u01ea\u01eb\7\177\2\2\u01eb")
        buf.write("\\\3\2\2\2\u01ec\u01ed\7=\2\2\u01ed^\3\2\2\2\u01ee\u01ef")
        buf.write("\7<\2\2\u01ef`\3\2\2\2\u01f0\u01f1\7.\2\2\u01f1b\3\2\2")
        buf.write("\2\u01f2\u01f3\7]\2\2\u01f3d\3\2\2\2\u01f4\u01f5\7_\2")
        buf.write("\2\u01f5f\3\2\2\2\u01f6\u01f7\7-\2\2\u01f7h\3\2\2\2\u01f8")
        buf.write("\u01f9\7/\2\2\u01f9j\3\2\2\2\u01fa\u01fb\7,\2\2\u01fb")
        buf.write("l\3\2\2\2\u01fc\u01fd\7\61\2\2\u01fdn\3\2\2\2\u01fe\u01ff")
        buf.write("\7\'\2\2\u01ffp\3\2\2\2\u0200\u0201\7#\2\2\u0201r\3\2")
        buf.write("\2\2\u0202\u0203\7~\2\2\u0203\u0204\7~\2\2\u0204t\3\2")
        buf.write("\2\2\u0205\u0206\7(\2\2\u0206\u0207\7(\2\2\u0207v\3\2")
        buf.write("\2\2\u0208\u0209\7#\2\2\u0209\u020a\7?\2\2\u020ax\3\2")
        buf.write("\2\2\u020b\u020c\7?\2\2\u020c\u020d\7?\2\2\u020dz\3\2")
        buf.write("\2\2\u020e\u020f\7?\2\2\u020f|\3\2\2\2\u0210\u0211\7>")
        buf.write("\2\2\u0211~\3\2\2\2\u0212\u0213\7@\2\2\u0213\u0080\3\2")
        buf.write("\2\2\u0214\u0215\7>\2\2\u0215\u0216\7?\2\2\u0216\u0082")
        buf.write("\3\2\2\2\u0217\u0218\7@\2\2\u0218\u0219\7?\2\2\u0219\u0084")
        buf.write("\3\2\2\2\u021a\u021b\7\60\2\2\u021b\u0086\3\2\2\2\u021c")
        buf.write("\u021d\7<\2\2\u021d\u021e\7<\2\2\u021e\u0088\3\2\2\2\u021f")
        buf.write("\u0220\7?\2\2\u0220\u0221\7?\2\2\u0221\u0222\7\60\2\2")
        buf.write("\u0222\u008a\3\2\2\2\u0223\u0224\7-\2\2\u0224\u0225\7")
        buf.write("\60\2\2\u0225\u008c\3\2\2\2\u0226\u0228\t\17\2\2\u0227")
        buf.write("\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u0227\3\2\2\2")
        buf.write("\u0229\u022a\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c\b")
        buf.write("G\5\2\u022c\u008e\3\2\2\2\u022d\u0231\7$\2\2\u022e\u0230")
        buf.write("\5\u0099M\2\u022f\u022e\3\2\2\2\u0230\u0233\3\2\2\2\u0231")
        buf.write("\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0235\3\2\2\2")
        buf.write("\u0233\u0231\3\2\2\2\u0234\u0236\t\20\2\2\u0235\u0234")
        buf.write("\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u0238\bH\6\2\u0238")
        buf.write("\u0090\3\2\2\2\u0239\u023d\7$\2\2\u023a\u023c\5\u0099")
        buf.write("M\2\u023b\u023a\3\2\2\2\u023c\u023f\3\2\2\2\u023d\u023b")
        buf.write("\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u0240\3\2\2\2\u023f")
        buf.write("\u023d\3\2\2\2\u0240\u0241\5\u0093J\2\u0241\u0242\bI\7")
        buf.write("\2\u0242\u0092\3\2\2\2\u0243\u0244\7^\2\2\u0244\u0247")
        buf.write("\n\21\2\2\u0245\u0247\n\22\2\2\u0246\u0243\3\2\2\2\u0246")
        buf.write("\u0245\3\2\2\2\u0247\u0094\3\2\2\2\u0248\u0249\13\2\2")
        buf.write("\2\u0249\u024a\bK\b\2\u024a\u0096\3\2\2\2\u024b\u024c")
        buf.write("\13\2\2\2\u024c\u0098\3\2\2\2\u024d\u0250\n\23\2\2\u024e")
        buf.write("\u0250\5\u009bN\2\u024f\u024d\3\2\2\2\u024f\u024e\3\2")
        buf.write("\2\2\u0250\u009a\3\2\2\2\u0251\u0252\7^\2\2\u0252\u0253")
        buf.write("\t\21\2\2\u0253\u009c\3\2\2\2\u0254\u0257\n\24\2\2\u0255")
        buf.write("\u0257\5\u009fP\2\u0256\u0254\3\2\2\2\u0256\u0255\3\2")
        buf.write("\2\2\u0257\u009e\3\2\2\2\u0258\u0259\7^\2\2\u0259\u025a")
        buf.write("\t\25\2\2\u025a\u00a0\3\2\2\2*\2\u00a8\u00b0\u00b4\u00b9")
        buf.write("\u00c2\u00c4\u00c9\u00ce\u00d3\u00d7\u00dc\u00e0\u00e6")
        buf.write("\u00eb\u00f4\u00f6\u00fa\u00ff\u0103\u0108\u010b\u0112")
        buf.write("\u0116\u011a\u0120\u0126\u01cd\u01d6\u01d9\u01db\u01e0")
        buf.write("\u01e2\u0229\u0231\u0235\u023d\u0246\u024f\u0256\t\3\3")
        buf.write("\2\3\t\3\3\r\4\b\2\2\3H\5\3I\6\3K\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INT_LITERAL = 2
    FL_LITERAL = 3
    BOOL_LITERAL = 4
    STRING_LITERAL = 5
    INTTYPE = 6
    FLOATTYPE = 7
    STRTYPE = 8
    BOOLTYPE = 9
    VOIDTYPE = 10
    CLASS = 11
    VAL = 12
    VAR = 13
    BREAK = 14
    FOREACH = 15
    NULL = 16
    CONSTRUC = 17
    DESTRUC = 18
    CONTINUE = 19
    TRUE = 20
    IF = 21
    FALSE = 22
    NEW = 23
    ELSE = 24
    ELSEIF = 25
    BY = 26
    RETURN = 27
    IN = 28
    WHILE = 29
    ARRAY = 30
    SELF = 31
    BLOCK_COMMENT = 32
    ID = 33
    Dollar_ID = 34
    LB = 35
    RB = 36
    LP = 37
    RP = 38
    SEMI = 39
    COLON = 40
    CM = 41
    LSB = 42
    RSB = 43
    ADD = 44
    SUB = 45
    MUL = 46
    DIV = 47
    MOD = 48
    NOT = 49
    OR = 50
    AND = 51
    NEQ = 52
    EQ = 53
    ASSIGN = 54
    LT = 55
    GT = 56
    LE = 57
    GE = 58
    DOT = 59
    ACCESS = 60
    STR_CMP = 61
    STR_CAT = 62
    WS = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    ERROR_CHAR = 66
    UNTERMINATED_COMMENT = 67

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
            "INTTYPE", "FLOATTYPE", "STRTYPE", "BOOLTYPE", "VOIDTYPE", "CLASS", 
            "VAL", "VAR", "BREAK", "FOREACH", "NULL", "CONSTRUC", "DESTRUC", 
            "CONTINUE", "TRUE", "IF", "FALSE", "NEW", "ELSE", "ELSEIF", 
            "BY", "RETURN", "IN", "WHILE", "ARRAY", "SELF", "BLOCK_COMMENT", 
            "ID", "Dollar_ID", "LB", "RB", "LP", "RP", "SEMI", "COLON", 
            "CM", "LSB", "RSB", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
            "OR", "AND", "NEQ", "EQ", "ASSIGN", "LT", "GT", "LE", "GE", 
            "DOT", "ACCESS", "STR_CMP", "STR_CAT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "INT_LITERAL", "BIN", "OCT", "DEC", "HEX", "DEC1", 
                  "FL_LITERAL", "FRACPART", "EXPPART", "BOOL_LITERAL", "STRING_LITERAL", 
                  "INTTYPE", "FLOATTYPE", "STRTYPE", "BOOLTYPE", "VOIDTYPE", 
                  "CLASS", "VAL", "VAR", "BREAK", "FOREACH", "NULL", "CONSTRUC", 
                  "DESTRUC", "CONTINUE", "TRUE", "IF", "FALSE", "NEW", "ELSE", 
                  "ELSEIF", "BY", "RETURN", "IN", "WHILE", "ARRAY", "SELF", 
                  "BLOCK_COMMENT", "ID", "Dollar_ID", "LB", "RB", "LP", 
                  "RP", "SEMI", "COLON", "CM", "LSB", "RSB", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "OR", "AND", "NEQ", "EQ", 
                  "ASSIGN", "LT", "GT", "LE", "GE", "DOT", "ACCESS", "STR_CMP", 
                  "STR_CAT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_ILLEGAL", 
                  "ERROR_CHAR", "UNTERMINATED_COMMENT", "STR_CHAR", "ESC_SEQ", 
                  "StringChar", "EscapeSequence" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.INT_LITERAL_action 
            actions[7] = self.FL_LITERAL_action 
            actions[11] = self.STRING_LITERAL_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_CHAR_action 
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
            	
     


