# Generated from f:\Documents\Dai_hoc\nam3_ki2\PPL\ass1\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u0259\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u0091\n\4\3\5")
        buf.write("\3\5\3\5\3\5\5\5\u0097\n\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6")
        buf.write("\u009f\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u00a8\n\b\3")
        buf.write("\t\3\t\5\t\u00ac\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00b7\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u00c5\n\f\3\r\3\r\3\r\3\r\5\r\u00cb")
        buf.write("\n\r\3\16\3\16\3\16\5\16\u00d0\n\16\3\17\3\17\3\17\5\17")
        buf.write("\u00d5\n\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\5\21\u00e2\n\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u00ec\n\22\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u00f2\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u00ff\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u0106\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30")
        buf.write("\u010e\n\30\f\30\16\30\u0111\13\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\7\31\u0119\n\31\f\31\16\31\u011c\13\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\7\32\u0124\n\32\f\32\16\32\u0127")
        buf.write("\13\32\3\33\3\33\3\33\5\33\u012c\n\33\3\34\3\34\3\34\5")
        buf.write("\34\u0131\n\34\3\35\3\35\3\35\3\35\3\35\7\35\u0138\n\35")
        buf.write("\f\35\16\35\u013b\13\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u0147\n\36\7\36\u0149\n\36\f")
        buf.write("\36\16\36\u014c\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\5\37\u0155\n\37\3\37\5\37\u0158\n\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \5 \u0161\n \3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u016c")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0175\n\"\3#\3#\3")
        buf.write("#\3#\3#\5#\u017c\n#\3$\3$\3$\3$\3$\3$\5$\u0184\n$\3%\3")
        buf.write("%\3%\5%\u0189\n%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\5\'")
        buf.write("\u0194\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01a2")
        buf.write("\n(\3)\3)\3)\3)\5)\u01a8\n)\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01bf\n,\3-\3")
        buf.write("-\3-\5-\u01c4\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01cf\n")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\62\3\62\5\62\u01e2\n\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u01f4\n\63\3\63\3\63\3\64\3\64\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u0200\n\65\3\66\3\66\3\66\3\66")
        buf.write("\5\66\u0206\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\5\67\u0212\n\67\38\38\58\u0216\n8\39\39")
        buf.write("\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\5;\u0228\n")
        buf.write(";\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3>\5>\u0235\n>\3>\7>\u0238")
        buf.write("\n>\f>\16>\u023b\13>\3?\3?\5?\u023f\n?\3@\3@\3@\3A\3A")
        buf.write("\3A\3A\5A\u0248\nA\3B\3B\3B\3B\3B\3B\5B\u0250\nB\3C\3")
        buf.write("C\3C\3C\3C\3C\3C\3C\2\7.\60\628:D\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\2\t\3\2\16\17")
        buf.write("\3\2#$\3\2?@\4\2\66\679<\3\2\64\65\3\2./\3\2\60\62\2\u025c")
        buf.write("\2\u0086\3\2\2\2\4\u0089\3\2\2\2\6\u0090\3\2\2\2\b\u0092")
        buf.write("\3\2\2\2\n\u009e\3\2\2\2\f\u00a0\3\2\2\2\16\u00a7\3\2")
        buf.write("\2\2\20\u00ab\3\2\2\2\22\u00ad\3\2\2\2\24\u00b0\3\2\2")
        buf.write("\2\26\u00c4\3\2\2\2\30\u00ca\3\2\2\2\32\u00cf\3\2\2\2")
        buf.write("\34\u00d1\3\2\2\2\36\u00d9\3\2\2\2 \u00de\3\2\2\2\"\u00eb")
        buf.write("\3\2\2\2$\u00f1\3\2\2\2&\u00f3\3\2\2\2(\u00f7\3\2\2\2")
        buf.write("*\u00fe\3\2\2\2,\u0105\3\2\2\2.\u0107\3\2\2\2\60\u0112")
        buf.write("\3\2\2\2\62\u011d\3\2\2\2\64\u012b\3\2\2\2\66\u0130\3")
        buf.write("\2\2\28\u0132\3\2\2\2:\u013c\3\2\2\2<\u0157\3\2\2\2>\u0160")
        buf.write("\3\2\2\2@\u016b\3\2\2\2B\u0174\3\2\2\2D\u017b\3\2\2\2")
        buf.write("F\u0183\3\2\2\2H\u0188\3\2\2\2J\u018a\3\2\2\2L\u018d\3")
        buf.write("\2\2\2N\u01a1\3\2\2\2P\u01a7\3\2\2\2R\u01a9\3\2\2\2T\u01ae")
        buf.write("\3\2\2\2V\u01be\3\2\2\2X\u01c3\3\2\2\2Z\u01c5\3\2\2\2")
        buf.write("\\\u01d3\3\2\2\2^\u01d9\3\2\2\2`\u01dc\3\2\2\2b\u01df")
        buf.write("\3\2\2\2d\u01f3\3\2\2\2f\u01f7\3\2\2\2h\u01ff\3\2\2\2")
        buf.write("j\u0205\3\2\2\2l\u0211\3\2\2\2n\u0215\3\2\2\2p\u0217\3")
        buf.write("\2\2\2r\u021e\3\2\2\2t\u0227\3\2\2\2v\u0229\3\2\2\2x\u022e")
        buf.write("\3\2\2\2z\u0239\3\2\2\2|\u023e\3\2\2\2~\u0240\3\2\2\2")
        buf.write("\u0080\u0247\3\2\2\2\u0082\u024f\3\2\2\2\u0084\u0251\3")
        buf.write("\2\2\2\u0086\u0087\5\4\3\2\u0087\u0088\7\2\2\3\u0088\3")
        buf.write("\3\2\2\2\u0089\u008a\5\b\5\2\u008a\u008b\5\6\4\2\u008b")
        buf.write("\5\3\2\2\2\u008c\u008d\5\b\5\2\u008d\u008e\5\6\4\2\u008e")
        buf.write("\u0091\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u008c\3\2\2\2")
        buf.write("\u0090\u008f\3\2\2\2\u0091\7\3\2\2\2\u0092\u0093\7\r\2")
        buf.write("\2\u0093\u0096\7#\2\2\u0094\u0095\7*\2\2\u0095\u0097\7")
        buf.write("#\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0099\7\'\2\2\u0099\u009a\5\n\6\2\u009a")
        buf.write("\u009b\7(\2\2\u009b\t\3\2\2\2\u009c\u009f\5\f\7\2\u009d")
        buf.write("\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2")
        buf.write("\u009f\13\3\2\2\2\u00a0\u00a1\5\20\t\2\u00a1\u00a2\5\16")
        buf.write("\b\2\u00a2\r\3\2\2\2\u00a3\u00a4\5\20\t\2\u00a4\u00a5")
        buf.write("\5\16\b\2\u00a5\u00a8\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7")
        buf.write("\u00a3\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\17\3\2\2\2\u00a9")
        buf.write("\u00ac\5\22\n\2\u00aa\u00ac\5\32\16\2\u00ab\u00a9\3\2")
        buf.write("\2\2\u00ab\u00aa\3\2\2\2\u00ac\21\3\2\2\2\u00ad\u00ae")
        buf.write("\5\24\13\2\u00ae\u00af\7)\2\2\u00af\23\3\2\2\2\u00b0\u00b6")
        buf.write("\t\2\2\2\u00b1\u00b7\5\26\f\2\u00b2\u00b3\5\30\r\2\u00b3")
        buf.write("\u00b4\7*\2\2\u00b4\u00b5\5\u0082B\2\u00b5\u00b7\3\2\2")
        buf.write("\2\u00b6\u00b1\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b7\25\3")
        buf.write("\2\2\2\u00b8\u00b9\t\3\2\2\u00b9\u00ba\7+\2\2\u00ba\u00bb")
        buf.write("\5\26\f\2\u00bb\u00bc\7+\2\2\u00bc\u00bd\5(\25\2\u00bd")
        buf.write("\u00c5\3\2\2\2\u00be\u00bf\t\3\2\2\u00bf\u00c0\7*\2\2")
        buf.write("\u00c0\u00c1\5\u0082B\2\u00c1\u00c2\78\2\2\u00c2\u00c3")
        buf.write("\5(\25\2\u00c3\u00c5\3\2\2\2\u00c4\u00b8\3\2\2\2\u00c4")
        buf.write("\u00be\3\2\2\2\u00c5\27\3\2\2\2\u00c6\u00c7\t\3\2\2\u00c7")
        buf.write("\u00c8\7+\2\2\u00c8\u00cb\5\30\r\2\u00c9\u00cb\t\3\2\2")
        buf.write("\u00ca\u00c6\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\31\3\2")
        buf.write("\2\2\u00cc\u00d0\5\34\17\2\u00cd\u00d0\5\36\20\2\u00ce")
        buf.write("\u00d0\5 \21\2\u00cf\u00cc\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00cf\u00ce\3\2\2\2\u00d0\33\3\2\2\2\u00d1\u00d2\t\3")
        buf.write("\2\2\u00d2\u00d4\7%\2\2\u00d3\u00d5\5\"\22\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("\u00d7\7&\2\2\u00d7\u00d8\5f\64\2\u00d8\35\3\2\2\2\u00d9")
        buf.write("\u00da\7\24\2\2\u00da\u00db\7%\2\2\u00db\u00dc\7&\2\2")
        buf.write("\u00dc\u00dd\5f\64\2\u00dd\37\3\2\2\2\u00de\u00df\7\23")
        buf.write("\2\2\u00df\u00e1\7%\2\2\u00e0\u00e2\5\"\22\2\u00e1\u00e0")
        buf.write("\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e4\7&\2\2\u00e4\u00e5\5f\64\2\u00e5!\3\2\2\2\u00e6")
        buf.write("\u00e7\5&\24\2\u00e7\u00e8\7)\2\2\u00e8\u00e9\5\"\22\2")
        buf.write("\u00e9\u00ec\3\2\2\2\u00ea\u00ec\5&\24\2\u00eb\u00e6\3")
        buf.write("\2\2\2\u00eb\u00ea\3\2\2\2\u00ec#\3\2\2\2\u00ed\u00ee")
        buf.write("\7#\2\2\u00ee\u00ef\7+\2\2\u00ef\u00f2\5$\23\2\u00f0\u00f2")
        buf.write("\7#\2\2\u00f1\u00ed\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2")
        buf.write("%\3\2\2\2\u00f3\u00f4\5$\23\2\u00f4\u00f5\7*\2\2\u00f5")
        buf.write("\u00f6\5\u0082B\2\u00f6\'\3\2\2\2\u00f7\u00f8\5*\26\2")
        buf.write("\u00f8)\3\2\2\2\u00f9\u00fa\5,\27\2\u00fa\u00fb\t\4\2")
        buf.write("\2\u00fb\u00fc\5,\27\2\u00fc\u00ff\3\2\2\2\u00fd\u00ff")
        buf.write("\5,\27\2\u00fe\u00f9\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff")
        buf.write("+\3\2\2\2\u0100\u0101\5.\30\2\u0101\u0102\t\5\2\2\u0102")
        buf.write("\u0103\5.\30\2\u0103\u0106\3\2\2\2\u0104\u0106\5.\30\2")
        buf.write("\u0105\u0100\3\2\2\2\u0105\u0104\3\2\2\2\u0106-\3\2\2")
        buf.write("\2\u0107\u0108\b\30\1\2\u0108\u0109\5\60\31\2\u0109\u010f")
        buf.write("\3\2\2\2\u010a\u010b\f\4\2\2\u010b\u010c\t\6\2\2\u010c")
        buf.write("\u010e\5\60\31\2\u010d\u010a\3\2\2\2\u010e\u0111\3\2\2")
        buf.write("\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110/\3\2")
        buf.write("\2\2\u0111\u010f\3\2\2\2\u0112\u0113\b\31\1\2\u0113\u0114")
        buf.write("\5\62\32\2\u0114\u011a\3\2\2\2\u0115\u0116\f\4\2\2\u0116")
        buf.write("\u0117\t\7\2\2\u0117\u0119\5\62\32\2\u0118\u0115\3\2\2")
        buf.write("\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\61\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u011e")
        buf.write("\b\32\1\2\u011e\u011f\5\64\33\2\u011f\u0125\3\2\2\2\u0120")
        buf.write("\u0121\f\4\2\2\u0121\u0122\t\b\2\2\u0122\u0124\5\64\33")
        buf.write("\2\u0123\u0120\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0125\u0126\3\2\2\2\u0126\63\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0128\u0129\7\63\2\2\u0129\u012c\5\64\33\2\u012a")
        buf.write("\u012c\5\66\34\2\u012b\u0128\3\2\2\2\u012b\u012a\3\2\2")
        buf.write("\2\u012c\65\3\2\2\2\u012d\u012e\7/\2\2\u012e\u0131\5\66")
        buf.write("\34\2\u012f\u0131\58\35\2\u0130\u012d\3\2\2\2\u0130\u012f")
        buf.write("\3\2\2\2\u0131\67\3\2\2\2\u0132\u0133\b\35\1\2\u0133\u0134")
        buf.write("\5:\36\2\u0134\u0139\3\2\2\2\u0135\u0136\f\4\2\2\u0136")
        buf.write("\u0138\5@!\2\u0137\u0135\3\2\2\2\u0138\u013b\3\2\2\2\u0139")
        buf.write("\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a9\3\2\2\2\u013b")
        buf.write("\u0139\3\2\2\2\u013c\u013d\b\36\1\2\u013d\u013e\5<\37")
        buf.write("\2\u013e\u014a\3\2\2\2\u013f\u0140\f\4\2\2\u0140\u0141")
        buf.write("\7=\2\2\u0141\u0146\7#\2\2\u0142\u0143\7%\2\2\u0143\u0144")
        buf.write("\5F$\2\u0144\u0145\7&\2\2\u0145\u0147\3\2\2\2\u0146\u0142")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149\3\2\2\2\u0148")
        buf.write("\u013f\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014a\u014b\3\2\2\2\u014b;\3\2\2\2\u014c\u014a\3\2\2")
        buf.write("\2\u014d\u014e\7#\2\2\u014e\u014f\7>\2\2\u014f\u0154\7")
        buf.write("$\2\2\u0150\u0151\7%\2\2\u0151\u0152\5F$\2\u0152\u0153")
        buf.write("\7&\2\2\u0153\u0155\3\2\2\2\u0154\u0150\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0158\5> \2\u0157")
        buf.write("\u014d\3\2\2\2\u0157\u0156\3\2\2\2\u0158=\3\2\2\2\u0159")
        buf.write("\u015a\7\31\2\2\u015a\u015b\7#\2\2\u015b\u015c\7%\2\2")
        buf.write("\u015c\u015d\5F$\2\u015d\u015e\7&\2\2\u015e\u0161\3\2")
        buf.write("\2\2\u015f\u0161\5B\"\2\u0160\u0159\3\2\2\2\u0160\u015f")
        buf.write("\3\2\2\2\u0161?\3\2\2\2\u0162\u0163\7,\2\2\u0163\u0164")
        buf.write("\5(\25\2\u0164\u0165\7-\2\2\u0165\u0166\5@!\2\u0166\u016c")
        buf.write("\3\2\2\2\u0167\u0168\7,\2\2\u0168\u0169\5(\25\2\u0169")
        buf.write("\u016a\7-\2\2\u016a\u016c\3\2\2\2\u016b\u0162\3\2\2\2")
        buf.write("\u016b\u0167\3\2\2\2\u016cA\3\2\2\2\u016d\u0175\5D#\2")
        buf.write("\u016e\u0175\7#\2\2\u016f\u0170\7%\2\2\u0170\u0171\5(")
        buf.write("\25\2\u0171\u0172\7&\2\2\u0172\u0175\3\2\2\2\u0173\u0175")
        buf.write("\7!\2\2\u0174\u016d\3\2\2\2\u0174\u016e\3\2\2\2\u0174")
        buf.write("\u016f\3\2\2\2\u0174\u0173\3\2\2\2\u0175C\3\2\2\2\u0176")
        buf.write("\u017c\7\4\2\2\u0177\u017c\7\5\2\2\u0178\u017c\7\7\2\2")
        buf.write("\u0179\u017c\7\6\2\2\u017a\u017c\5t;\2\u017b\u0176\3\2")
        buf.write("\2\2\u017b\u0177\3\2\2\2\u017b\u0178\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017b\u017a\3\2\2\2\u017cE\3\2\2\2\u017d\u017e")
        buf.write("\5H%\2\u017e\u017f\7+\2\2\u017f\u0180\5F$\2\u0180\u0184")
        buf.write("\3\2\2\2\u0181\u0184\5H%\2\u0182\u0184\3\2\2\2\u0183\u017d")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("G\3\2\2\2\u0185\u0189\5D#\2\u0186\u0189\7#\2\2\u0187\u0189")
        buf.write("\5(\25\2\u0188\u0185\3\2\2\2\u0188\u0186\3\2\2\2\u0188")
        buf.write("\u0187\3\2\2\2\u0189I\3\2\2\2\u018a\u018b\5L\'\2\u018b")
        buf.write("\u018c\7)\2\2\u018cK\3\2\2\2\u018d\u0193\t\2\2\2\u018e")
        buf.write("\u0194\5N(\2\u018f\u0190\5P)\2\u0190\u0191\7*\2\2\u0191")
        buf.write("\u0192\5\u0082B\2\u0192\u0194\3\2\2\2\u0193\u018e\3\2")
        buf.write("\2\2\u0193\u018f\3\2\2\2\u0194M\3\2\2\2\u0195\u0196\7")
        buf.write("#\2\2\u0196\u0197\7+\2\2\u0197\u0198\5N(\2\u0198\u0199")
        buf.write("\7+\2\2\u0199\u019a\5(\25\2\u019a\u01a2\3\2\2\2\u019b")
        buf.write("\u019c\7#\2\2\u019c\u019d\7*\2\2\u019d\u019e\5\u0082B")
        buf.write("\2\u019e\u019f\78\2\2\u019f\u01a0\5(\25\2\u01a0\u01a2")
        buf.write("\3\2\2\2\u01a1\u0195\3\2\2\2\u01a1\u019b\3\2\2\2\u01a2")
        buf.write("O\3\2\2\2\u01a3\u01a4\7#\2\2\u01a4\u01a5\7+\2\2\u01a5")
        buf.write("\u01a8\5P)\2\u01a6\u01a8\7#\2\2\u01a7\u01a3\3\2\2\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a8Q\3\2\2\2\u01a9\u01aa\5(\25\2\u01aa")
        buf.write("\u01ab\78\2\2\u01ab\u01ac\5(\25\2\u01ac\u01ad\7)\2\2\u01ad")
        buf.write("S\3\2\2\2\u01ae\u01af\7\27\2\2\u01af\u01b0\7%\2\2\u01b0")
        buf.write("\u01b1\5(\25\2\u01b1\u01b2\7&\2\2\u01b2\u01b3\5f\64\2")
        buf.write("\u01b3\u01b4\5V,\2\u01b4U\3\2\2\2\u01b5\u01b6\7\33\2\2")
        buf.write("\u01b6\u01b7\7%\2\2\u01b7\u01b8\5(\25\2\u01b8\u01b9\7")
        buf.write("&\2\2\u01b9\u01ba\5f\64\2\u01ba\u01bb\5V,\2\u01bb\u01bf")
        buf.write("\3\2\2\2\u01bc\u01bf\5X-\2\u01bd\u01bf\3\2\2\2\u01be\u01b5")
        buf.write("\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("W\3\2\2\2\u01c0\u01c1\7\32\2\2\u01c1\u01c4\5f\64\2\u01c2")
        buf.write("\u01c4\3\2\2\2\u01c3\u01c0\3\2\2\2\u01c3\u01c2\3\2\2\2")
        buf.write("\u01c4Y\3\2\2\2\u01c5\u01c6\7\21\2\2\u01c6\u01c7\7%\2")
        buf.write("\2\u01c7\u01c8\7#\2\2\u01c8\u01c9\7\36\2\2\u01c9\u01ca")
        buf.write("\5(\25\2\u01ca\u01cb\7\3\2\2\u01cb\u01ce\5(\25\2\u01cc")
        buf.write("\u01cd\7\34\2\2\u01cd\u01cf\5(\25\2\u01ce\u01cc\3\2\2")
        buf.write("\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1")
        buf.write("\7&\2\2\u01d1\u01d2\5f\64\2\u01d2[\3\2\2\2\u01d3\u01d4")
        buf.write("\7\37\2\2\u01d4\u01d5\7%\2\2\u01d5\u01d6\5(\25\2\u01d6")
        buf.write("\u01d7\7&\2\2\u01d7\u01d8\5f\64\2\u01d8]\3\2\2\2\u01d9")
        buf.write("\u01da\7\20\2\2\u01da\u01db\7)\2\2\u01db_\3\2\2\2\u01dc")
        buf.write("\u01dd\7\25\2\2\u01dd\u01de\7)\2\2\u01dea\3\2\2\2\u01df")
        buf.write("\u01e1\7\35\2\2\u01e0\u01e2\5*\26\2\u01e1\u01e0\3\2\2")
        buf.write("\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e4")
        buf.write("\7)\2\2\u01e4c\3\2\2\2\u01e5\u01e6\5:\36\2\u01e6\u01e7")
        buf.write("\7=\2\2\u01e7\u01e8\7#\2\2\u01e8\u01e9\7%\2\2\u01e9\u01ea")
        buf.write("\5F$\2\u01ea\u01eb\7&\2\2\u01eb\u01f4\3\2\2\2\u01ec\u01ed")
        buf.write("\7#\2\2\u01ed\u01ee\7>\2\2\u01ee\u01ef\7$\2\2\u01ef\u01f0")
        buf.write("\7%\2\2\u01f0\u01f1\5F$\2\u01f1\u01f2\7&\2\2\u01f2\u01f4")
        buf.write("\3\2\2\2\u01f3\u01e5\3\2\2\2\u01f3\u01ec\3\2\2\2\u01f4")
        buf.write("\u01f5\3\2\2\2\u01f5\u01f6\7)\2\2\u01f6e\3\2\2\2\u01f7")
        buf.write("\u01f8\7\'\2\2\u01f8\u01f9\5h\65\2\u01f9\u01fa\7(\2\2")
        buf.write("\u01fag\3\2\2\2\u01fb\u01fc\5l\67\2\u01fc\u01fd\5j\66")
        buf.write("\2\u01fd\u0200\3\2\2\2\u01fe\u0200\3\2\2\2\u01ff\u01fb")
        buf.write("\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200i\3\2\2\2\u0201\u0202")
        buf.write("\5l\67\2\u0202\u0203\5j\66\2\u0203\u0206\3\2\2\2\u0204")
        buf.write("\u0206\3\2\2\2\u0205\u0201\3\2\2\2\u0205\u0204\3\2\2\2")
        buf.write("\u0206k\3\2\2\2\u0207\u0212\5J&\2\u0208\u0212\5T+\2\u0209")
        buf.write("\u0212\5R*\2\u020a\u0212\5\\/\2\u020b\u0212\5^\60\2\u020c")
        buf.write("\u0212\5`\61\2\u020d\u0212\5d\63\2\u020e\u0212\5b\62\2")
        buf.write("\u020f\u0212\5Z.\2\u0210\u0212\5f\64\2\u0211\u0207\3\2")
        buf.write("\2\2\u0211\u0208\3\2\2\2\u0211\u0209\3\2\2\2\u0211\u020a")
        buf.write("\3\2\2\2\u0211\u020b\3\2\2\2\u0211\u020c\3\2\2\2\u0211")
        buf.write("\u020d\3\2\2\2\u0211\u020e\3\2\2\2\u0211\u020f\3\2\2\2")
        buf.write("\u0211\u0210\3\2\2\2\u0212m\3\2\2\2\u0213\u0216\5p9\2")
        buf.write("\u0214\u0216\5r:\2\u0215\u0213\3\2\2\2\u0215\u0214\3\2")
        buf.write("\2\2\u0216o\3\2\2\2\u0217\u0218\5(\25\2\u0218\u0219\7")
        buf.write("=\2\2\u0219\u021a\7#\2\2\u021a\u021b\7%\2\2\u021b\u021c")
        buf.write("\5F$\2\u021c\u021d\7&\2\2\u021dq\3\2\2\2\u021e\u021f\5")
        buf.write("(\25\2\u021f\u0220\7>\2\2\u0220\u0221\7$\2\2\u0221\u0222")
        buf.write("\7%\2\2\u0222\u0223\5F$\2\u0223\u0224\7&\2\2\u0224s\3")
        buf.write("\2\2\2\u0225\u0228\5v<\2\u0226\u0228\5x=\2\u0227\u0225")
        buf.write("\3\2\2\2\u0227\u0226\3\2\2\2\u0228u\3\2\2\2\u0229\u022a")
        buf.write("\7 \2\2\u022a\u022b\7%\2\2\u022b\u022c\5|?\2\u022c\u022d")
        buf.write("\7&\2\2\u022dw\3\2\2\2\u022e\u022f\7 \2\2\u022f\u0230")
        buf.write("\7%\2\2\u0230\u0231\5z>\2\u0231\u0232\7&\2\2\u0232y\3")
        buf.write("\2\2\2\u0233\u0235\7+\2\2\u0234\u0233\3\2\2\2\u0234\u0235")
        buf.write("\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0238\5t;\2\u0237\u0234")
        buf.write("\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2\u0239")
        buf.write("\u023a\3\2\2\2\u023a{\3\2\2\2\u023b\u0239\3\2\2\2\u023c")
        buf.write("\u023f\5~@\2\u023d\u023f\3\2\2\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023d\3\2\2\2\u023f}\3\2\2\2\u0240\u0241\5(\25\2\u0241")
        buf.write("\u0242\5\u0080A\2\u0242\177\3\2\2\2\u0243\u0244\5(\25")
        buf.write("\2\u0244\u0245\5\u0080A\2\u0245\u0248\3\2\2\2\u0246\u0248")
        buf.write("\3\2\2\2\u0247\u0243\3\2\2\2\u0247\u0246\3\2\2\2\u0248")
        buf.write("\u0081\3\2\2\2\u0249\u0250\7\b\2\2\u024a\u0250\7\t\2\2")
        buf.write("\u024b\u0250\7\n\2\2\u024c\u0250\7\13\2\2\u024d\u0250")
        buf.write("\5\u0084C\2\u024e\u0250\7#\2\2\u024f\u0249\3\2\2\2\u024f")
        buf.write("\u024a\3\2\2\2\u024f\u024b\3\2\2\2\u024f\u024c\3\2\2\2")
        buf.write("\u024f\u024d\3\2\2\2\u024f\u024e\3\2\2\2\u0250\u0083\3")
        buf.write("\2\2\2\u0251\u0252\7 \2\2\u0252\u0253\7,\2\2\u0253\u0254")
        buf.write("\5\u0082B\2\u0254\u0255\7+\2\2\u0255\u0256\7\4\2\2\u0256")
        buf.write("\u0257\7-\2\2\u0257\u0085\3\2\2\2\63\u0090\u0096\u009e")
        buf.write("\u00a7\u00ab\u00b6\u00c4\u00ca\u00cf\u00d4\u00e1\u00eb")
        buf.write("\u00f1\u00fe\u0105\u010f\u011a\u0125\u012b\u0130\u0139")
        buf.write("\u0146\u014a\u0154\u0157\u0160\u016b\u0174\u017b\u0183")
        buf.write("\u0188\u0193\u01a1\u01a7\u01be\u01c3\u01ce\u01e1\u01f3")
        buf.write("\u01ff\u0205\u0211\u0215\u0227\u0234\u0239\u023e\u0247")
        buf.write("\u024f")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'..'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Int'", "'Float'", "'String'", "'Boolean'", 
                     "'Void'", "'Class'", "'Val'", "'Var'", "'Break'", "'Foreach'", 
                     "'Null'", "'Constructor'", "'Destructor'", "'Continue'", 
                     "'True'", "'If'", "'False'", "'New'", "'Else'", "'Elseif'", 
                     "'By'", "'Return'", "'In'", "'While'", "'Array'", "'Self'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "';'", "':'", "','", "'['", "']'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'||'", "'&&'", 
                     "'!='", "'=='", "'='", "'<'", "'>'", "'<='", "'>='", 
                     "'.'", "'::'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INT_LITERAL", "FL_LITERAL", 
                      "BOOL_LITERAL", "STRING_LITERAL", "INTTYPE", "FLOATTYPE", 
                      "STRTYPE", "BOOLTYPE", "VOIDTYPE", "CLASS", "VAL", 
                      "VAR", "BREAK", "FOREACH", "NULL", "CONSTRUC", "DESTRUC", 
                      "CONTINUE", "TRUE", "IF", "FALSE", "NEW", "ELSE", 
                      "ELSEIF", "BY", "RETURN", "IN", "WHILE", "ARRAY", 
                      "SELF", "BLOCK_COMMENT", "ID", "Dollar_ID", "LB", 
                      "RB", "LP", "RP", "SEMI", "COLON", "CM", "LSB", "RSB", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "OR", "AND", 
                      "NEQ", "EQ", "ASSIGN", "LT", "GT", "LE", "GE", "DOT", 
                      "ACCESS", "STR_CMP", "STR_CAT", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_classes = 1
    RULE_class_declares = 2
    RULE_class_declare = 3
    RULE_body = 4
    RULE_body_class = 5
    RULE_body_classes = 6
    RULE_member = 7
    RULE_attribute_declare = 8
    RULE_varible = 9
    RULE_vardecl = 10
    RULE_term = 11
    RULE_method = 12
    RULE_method_declare = 13
    RULE_destructor_declare = 14
    RULE_constructor_declare = 15
    RULE_list_IDs = 16
    RULE_ids = 17
    RULE_list_ID = 18
    RULE_exp0 = 19
    RULE_exp1 = 20
    RULE_exp2 = 21
    RULE_exp3 = 22
    RULE_exp4 = 23
    RULE_exp5 = 24
    RULE_exp6 = 25
    RULE_exp7 = 26
    RULE_exp8 = 27
    RULE_exp9 = 28
    RULE_exp10 = 29
    RULE_exp11 = 30
    RULE_index_operator = 31
    RULE_operands = 32
    RULE_literal = 33
    RULE_list_param = 34
    RULE_param = 35
    RULE_varconst_declare = 36
    RULE_varible1 = 37
    RULE_vardecl1 = 38
    RULE_term1 = 39
    RULE_stmt_assign = 40
    RULE_stmt_if = 41
    RULE_stmt_elif = 42
    RULE_stmt_else = 43
    RULE_stmt_foreach = 44
    RULE_stmt_while = 45
    RULE_stmt_break = 46
    RULE_stmt_continue = 47
    RULE_stmt_return = 48
    RULE_stmt_callMethod = 49
    RULE_block_stmt = 50
    RULE_list_stmt = 51
    RULE_stmts = 52
    RULE_stmt = 53
    RULE_member_access = 54
    RULE_in_method = 55
    RULE_stt_method = 56
    RULE_array = 57
    RULE_i_array = 58
    RULE_m_array = 59
    RULE_listARRAY = 60
    RULE_listLIT = 61
    RULE_list_mem = 62
    RULE_listval = 63
    RULE_typ = 64
    RULE_arraytype = 65

    ruleNames =  [ "program", "classes", "class_declares", "class_declare", 
                   "body", "body_class", "body_classes", "member", "attribute_declare", 
                   "varible", "vardecl", "term", "method", "method_declare", 
                   "destructor_declare", "constructor_declare", "list_IDs", 
                   "ids", "list_ID", "exp0", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", "exp11", 
                   "index_operator", "operands", "literal", "list_param", 
                   "param", "varconst_declare", "varible1", "vardecl1", 
                   "term1", "stmt_assign", "stmt_if", "stmt_elif", "stmt_else", 
                   "stmt_foreach", "stmt_while", "stmt_break", "stmt_continue", 
                   "stmt_return", "stmt_callMethod", "block_stmt", "list_stmt", 
                   "stmts", "stmt", "member_access", "in_method", "stt_method", 
                   "array", "i_array", "m_array", "listARRAY", "listLIT", 
                   "list_mem", "listval", "typ", "arraytype" ]

    EOF = Token.EOF
    T__0=1
    INT_LITERAL=2
    FL_LITERAL=3
    BOOL_LITERAL=4
    STRING_LITERAL=5
    INTTYPE=6
    FLOATTYPE=7
    STRTYPE=8
    BOOLTYPE=9
    VOIDTYPE=10
    CLASS=11
    VAL=12
    VAR=13
    BREAK=14
    FOREACH=15
    NULL=16
    CONSTRUC=17
    DESTRUC=18
    CONTINUE=19
    TRUE=20
    IF=21
    FALSE=22
    NEW=23
    ELSE=24
    ELSEIF=25
    BY=26
    RETURN=27
    IN=28
    WHILE=29
    ARRAY=30
    SELF=31
    BLOCK_COMMENT=32
    ID=33
    Dollar_ID=34
    LB=35
    RB=36
    LP=37
    RP=38
    SEMI=39
    COLON=40
    CM=41
    LSB=42
    RSB=43
    ADD=44
    SUB=45
    MUL=46
    DIV=47
    MOD=48
    NOT=49
    OR=50
    AND=51
    NEQ=52
    EQ=53
    ASSIGN=54
    LT=55
    GT=56
    LE=57
    GE=58
    DOT=59
    ACCESS=60
    STR_CMP=61
    STR_CAT=62
    WS=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    ERROR_CHAR=66
    UNTERMINATED_COMMENT=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classes(self):
            return self.getTypedRuleContext(D96Parser.ClassesContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.classes()
            self.state = 133
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declare(self):
            return self.getTypedRuleContext(D96Parser.Class_declareContext,0)


        def class_declares(self):
            return self.getTypedRuleContext(D96Parser.Class_declaresContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classes




    def classes(self):

        localctx = D96Parser.ClassesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.class_declare()
            self.state = 136
            self.class_declares()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declaresContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declare(self):
            return self.getTypedRuleContext(D96Parser.Class_declareContext,0)


        def class_declares(self):
            return self.getTypedRuleContext(D96Parser.Class_declaresContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declares




    def class_declares(self):

        localctx = D96Parser.Class_declaresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declares)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.class_declare()
                self.state = 139
                self.class_declares()
                pass
            elif token in [D96Parser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def body(self):
            return self.getTypedRuleContext(D96Parser.BodyContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declare




    def class_declare(self):

        localctx = D96Parser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(D96Parser.CLASS)
            self.state = 145
            self.match(D96Parser.ID)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 146
                self.match(D96Parser.COLON)
                self.state = 147
                self.match(D96Parser.ID)


            self.state = 150
            self.match(D96Parser.LP)
            self.state = 151
            self.body()
            self.state = 152
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body_class(self):
            return self.getTypedRuleContext(D96Parser.Body_classContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_body




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUC, D96Parser.DESTRUC, D96Parser.ID, D96Parser.Dollar_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.body_class()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_classContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def body_classes(self):
            return self.getTypedRuleContext(D96Parser.Body_classesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_body_class




    def body_class(self):

        localctx = D96Parser.Body_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_body_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.member()
            self.state = 159
            self.body_classes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_classesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def body_classes(self):
            return self.getTypedRuleContext(D96Parser.Body_classesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_body_classes




    def body_classes(self):

        localctx = D96Parser.Body_classesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body_classes)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUC, D96Parser.DESTRUC, D96Parser.ID, D96Parser.Dollar_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.member()
                self.state = 162
                self.body_classes()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declare(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declareContext,0)


        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_member)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.attribute_declare()
                pass
            elif token in [D96Parser.CONSTRUC, D96Parser.DESTRUC, D96Parser.ID, D96Parser.Dollar_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varible(self):
            return self.getTypedRuleContext(D96Parser.VaribleContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declare




    def attribute_declare(self):

        localctx = D96Parser.Attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.varible()
            self.state = 172
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VaribleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def vardecl(self):
            return self.getTypedRuleContext(D96Parser.VardeclContext,0)


        def term(self):
            return self.getTypedRuleContext(D96Parser.TermContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_varible




    def varible(self):

        localctx = D96Parser.VaribleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_varible)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 175
                self.vardecl()
                pass

            elif la_ == 2:
                self.state = 176
                self.term()
                self.state = 177
                self.match(D96Parser.COLON)
                self.state = 178
                self.typ()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def vardecl(self):
            return self.getTypedRuleContext(D96Parser.VardeclContext,0)


        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Dollar_ID(self):
            return self.getToken(D96Parser.Dollar_ID, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_vardecl




    def vardecl(self):

        localctx = D96Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 183
                self.match(D96Parser.CM)
                self.state = 184
                self.vardecl()
                self.state = 185
                self.match(D96Parser.CM)
                self.state = 186
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 189
                self.match(D96Parser.COLON)
                self.state = 190
                self.typ()
                self.state = 191
                self.match(D96Parser.ASSIGN)
                self.state = 192
                self.exp0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def term(self):
            return self.getTypedRuleContext(D96Parser.TermContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Dollar_ID(self):
            return self.getToken(D96Parser.Dollar_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_term




    def term(self):

        localctx = D96Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self.match(D96Parser.CM)
                self.state = 198
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.Dollar_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_declare(self):
            return self.getTypedRuleContext(D96Parser.Method_declareContext,0)


        def destructor_declare(self):
            return self.getTypedRuleContext(D96Parser.Destructor_declareContext,0)


        def constructor_declare(self):
            return self.getTypedRuleContext(D96Parser.Constructor_declareContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.Dollar_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.method_declare()
                pass
            elif token in [D96Parser.DESTRUC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.destructor_declare()
                pass
            elif token in [D96Parser.CONSTRUC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.constructor_declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def Dollar_ID(self):
            return self.getToken(D96Parser.Dollar_ID, 0)

        def list_IDs(self):
            return self.getTypedRuleContext(D96Parser.List_IDsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declare




    def method_declare(self):

        localctx = D96Parser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.Dollar_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 208
            self.match(D96Parser.LB)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 209
                self.list_IDs()


            self.state = 212
            self.match(D96Parser.RB)
            self.state = 213
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUC(self):
            return self.getToken(D96Parser.DESTRUC, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_declare




    def destructor_declare(self):

        localctx = D96Parser.Destructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_destructor_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(D96Parser.DESTRUC)
            self.state = 216
            self.match(D96Parser.LB)
            self.state = 217
            self.match(D96Parser.RB)
            self.state = 218
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUC(self):
            return self.getToken(D96Parser.CONSTRUC, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def list_IDs(self):
            return self.getTypedRuleContext(D96Parser.List_IDsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_declare




    def constructor_declare(self):

        localctx = D96Parser.Constructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constructor_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(D96Parser.CONSTRUC)
            self.state = 221
            self.match(D96Parser.LB)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 222
                self.list_IDs()


            self.state = 225
            self.match(D96Parser.RB)
            self.state = 226
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_IDsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(D96Parser.List_IDContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def list_IDs(self):
            return self.getTypedRuleContext(D96Parser.List_IDsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_IDs




    def list_IDs(self):

        localctx = D96Parser.List_IDsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_IDs)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.list_ID()
                self.state = 229
                self.match(D96Parser.SEMI)
                self.state = 230
                self.list_IDs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.list_ID()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ids




    def ids(self):

        localctx = D96Parser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ids)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(D96Parser.ID)
                self.state = 236
                self.match(D96Parser.CM)
                self.state = 237
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_IDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_ID




    def list_ID(self):

        localctx = D96Parser.List_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list_ID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.ids()
            self.state = 242
            self.match(D96Parser.COLON)
            self.state = 243
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp0Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(D96Parser.Exp1Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp0




    def exp0(self):

        localctx = D96Parser.Exp0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exp0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.exp1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp2Context,i)


        def STR_CAT(self):
            return self.getToken(D96Parser.STR_CAT, 0)

        def STR_CMP(self):
            return self.getToken(D96Parser.STR_CMP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1




    def exp1(self):

        localctx = D96Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.exp2()
                self.state = 248
                _la = self._input.LA(1)
                if not(_la==D96Parser.STR_CMP or _la==D96Parser.STR_CAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 249
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.exp2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp3Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp3Context,i)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(D96Parser.NEQ, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GE(self):
            return self.getToken(D96Parser.GE, 0)

        def LE(self):
            return self.getToken(D96Parser.LE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2




    def exp2(self):

        localctx = D96Parser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.exp3(0)
                self.state = 255
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.NEQ) | (1 << D96Parser.EQ) | (1 << D96Parser.LT) | (1 << D96Parser.GT) | (1 << D96Parser.LE) | (1 << D96Parser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 256
                self.exp3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.exp3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 264
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 265
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OR or _la==D96Parser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 266
                    self.exp4(0) 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 277
                    self.exp5(0) 
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp5



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.exp6() 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp6)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(D96Parser.NOT)
                self.state = 295
                self.exp6()
                pass
            elif token in [D96Parser.INT_LITERAL, D96Parser.FL_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.STRING_LITERAL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.LB, D96Parser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp7




    def exp7(self):

        localctx = D96Parser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp7)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(D96Parser.SUB)
                self.state = 300
                self.exp7()
                pass
            elif token in [D96Parser.INT_LITERAL, D96Parser.FL_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.STRING_LITERAL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.exp8(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp8



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    self.index_operator() 
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_param(self):
            return self.getTypedRuleContext(D96Parser.List_paramContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp9



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 328
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
                    self.match(D96Parser.DOT)
                    self.state = 319
                    self.match(D96Parser.ID)
                    self.state = 324
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        self.state = 320
                        self.match(D96Parser.LB)
                        self.state = 321
                        self.list_param()
                        self.state = 322
                        self.match(D96Parser.RB)

             
                self.state = 330
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def ACCESS(self):
            return self.getToken(D96Parser.ACCESS, 0)

        def Dollar_ID(self):
            return self.getToken(D96Parser.Dollar_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_param(self):
            return self.getTypedRuleContext(D96Parser.List_paramContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp11(self):
            return self.getTypedRuleContext(D96Parser.Exp11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp10)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(D96Parser.ID)
                self.state = 332
                self.match(D96Parser.ACCESS)
                self.state = 333
                self.match(D96Parser.Dollar_ID)
                self.state = 338
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 334
                    self.match(D96Parser.LB)
                    self.state = 335
                    self.list_param()
                    self.state = 336
                    self.match(D96Parser.RB)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.exp11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_param(self):
            return self.getTypedRuleContext(D96Parser.List_paramContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp11




    def exp11(self):

        localctx = D96Parser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp11)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(D96Parser.NEW)
                self.state = 344
                self.match(D96Parser.ID)
                self.state = 345
                self.match(D96Parser.LB)
                self.state = 346
                self.list_param()
                self.state = 347
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.INT_LITERAL, D96Parser.FL_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_index_operator)
        try:
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(D96Parser.LSB)
                self.state = 353
                self.exp0()
                self.state = 354
                self.match(D96Parser.RSB)
                self.state = 355
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(D96Parser.LSB)
                self.state = 358
                self.exp0()
                self.state = 359
                self.match(D96Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operands)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LITERAL, D96Parser.FL_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.literal()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 365
                self.match(D96Parser.LB)
                self.state = 366
                self.exp0()
                self.state = 367
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 369
                self.match(D96Parser.SELF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(D96Parser.INT_LITERAL, 0)

        def FL_LITERAL(self):
            return self.getToken(D96Parser.FL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(D96Parser.BOOL_LITERAL, 0)

        def array(self):
            return self.getTypedRuleContext(D96Parser.ArrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_literal)
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(D96Parser.INT_LITERAL)
                pass
            elif token in [D96Parser.FL_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.match(D96Parser.FL_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 374
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.BOOL_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 375
                self.match(D96Parser.BOOL_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 376
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(D96Parser.ParamContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def list_param(self):
            return self.getTypedRuleContext(D96Parser.List_paramContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_param




    def list_param(self):

        localctx = D96Parser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_list_param)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.param()
                self.state = 380
                self.match(D96Parser.CM)
                self.state = 381
                self.list_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.param()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_param)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 389
                self.exp0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varconst_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varible1(self):
            return self.getTypedRuleContext(D96Parser.Varible1Context,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_varconst_declare




    def varconst_declare(self):

        localctx = D96Parser.Varconst_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_varconst_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.varible1()
            self.state = 393
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varible1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def vardecl1(self):
            return self.getTypedRuleContext(D96Parser.Vardecl1Context,0)


        def term1(self):
            return self.getTypedRuleContext(D96Parser.Term1Context,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_varible1




    def varible1(self):

        localctx = D96Parser.Varible1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_varible1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 396
                self.vardecl1()
                pass

            elif la_ == 2:
                self.state = 397
                self.term1()
                self.state = 398
                self.match(D96Parser.COLON)
                self.state = 399
                self.typ()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def vardecl1(self):
            return self.getTypedRuleContext(D96Parser.Vardecl1Context,0)


        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_vardecl1




    def vardecl1(self):

        localctx = D96Parser.Vardecl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_vardecl1)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(D96Parser.ID)
                self.state = 404
                self.match(D96Parser.CM)
                self.state = 405
                self.vardecl1()
                self.state = 406
                self.match(D96Parser.CM)
                self.state = 407
                self.exp0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.match(D96Parser.ID)
                self.state = 410
                self.match(D96Parser.COLON)
                self.state = 411
                self.typ()
                self.state = 412
                self.match(D96Parser.ASSIGN)
                self.state = 413
                self.exp0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def term1(self):
            return self.getTypedRuleContext(D96Parser.Term1Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_term1




    def term1(self):

        localctx = D96Parser.Term1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_term1)
        try:
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(D96Parser.ID)
                self.state = 418
                self.match(D96Parser.CM)
                self.state = 419
                self.term1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_assignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp0Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp0Context,i)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_assign




    def stmt_assign(self):

        localctx = D96Parser.Stmt_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.exp0()
            self.state = 424
            self.match(D96Parser.ASSIGN)
            self.state = 425
            self.exp0()
            self.state = 426
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def stmt_elif(self):
            return self.getTypedRuleContext(D96Parser.Stmt_elifContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_if




    def stmt_if(self):

        localctx = D96Parser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.IF)
            self.state = 429
            self.match(D96Parser.LB)
            self.state = 430
            self.exp0()
            self.state = 431
            self.match(D96Parser.RB)
            self.state = 432
            self.block_stmt()
            self.state = 433
            self.stmt_elif()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_elifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def stmt_elif(self):
            return self.getTypedRuleContext(D96Parser.Stmt_elifContext,0)


        def stmt_else(self):
            return self.getTypedRuleContext(D96Parser.Stmt_elseContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_elif




    def stmt_elif(self):

        localctx = D96Parser.Stmt_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_stmt_elif)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(D96Parser.ELSEIF)
                self.state = 436
                self.match(D96Parser.LB)
                self.state = 437
                self.exp0()
                self.state = 438
                self.match(D96Parser.RB)
                self.state = 439
                self.block_stmt()
                self.state = 440
                self.stmt_elif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.stmt_else()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_elseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_else




    def stmt_else(self):

        localctx = D96Parser.Stmt_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stmt_else)
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(D96Parser.ELSE)
                self.state = 447
                self.block_stmt()
                pass
            elif token in [D96Parser.INT_LITERAL, D96Parser.FL_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.STRING_LITERAL, D96Parser.VAL, D96Parser.VAR, D96Parser.BREAK, D96Parser.FOREACH, D96Parser.CONTINUE, D96Parser.IF, D96Parser.NEW, D96Parser.RETURN, D96Parser.WHILE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.LB, D96Parser.LP, D96Parser.RP, D96Parser.SUB, D96Parser.NOT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_foreachContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def exp0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp0Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp0Context,i)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_foreach




    def stmt_foreach(self):

        localctx = D96Parser.Stmt_foreachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stmt_foreach)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(D96Parser.FOREACH)
            self.state = 452
            self.match(D96Parser.LB)
            self.state = 453
            self.match(D96Parser.ID)
            self.state = 454
            self.match(D96Parser.IN)
            self.state = 455
            self.exp0()
            self.state = 456
            self.match(D96Parser.T__0)
            self.state = 457
            self.exp0()
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 458
                self.match(D96Parser.BY)
                self.state = 459
                self.exp0()


            self.state = 462
            self.match(D96Parser.RB)
            self.state = 463
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_whileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(D96Parser.WHILE, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_while




    def stmt_while(self):

        localctx = D96Parser.Stmt_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stmt_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(D96Parser.WHILE)
            self.state = 466
            self.match(D96Parser.LB)
            self.state = 467
            self.exp0()
            self.state = 468
            self.match(D96Parser.RB)
            self.state = 469
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_breakContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_break




    def stmt_break(self):

        localctx = D96Parser.Stmt_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(D96Parser.BREAK)
            self.state = 472
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_continueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_continue




    def stmt_continue(self):

        localctx = D96Parser.Stmt_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(D96Parser.CONTINUE)
            self.state = 475
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_returnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp1(self):
            return self.getTypedRuleContext(D96Parser.Exp1Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_return




    def stmt_return(self):

        localctx = D96Parser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stmt_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(D96Parser.RETURN)
            self.state = 479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT_LITERAL) | (1 << D96Parser.FL_LITERAL) | (1 << D96Parser.BOOL_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.ID) | (1 << D96Parser.LB) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT))) != 0):
                self.state = 478
                self.exp1()


            self.state = 481
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_callMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_param(self):
            return self.getTypedRuleContext(D96Parser.List_paramContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def ACCESS(self):
            return self.getToken(D96Parser.ACCESS, 0)

        def Dollar_ID(self):
            return self.getToken(D96Parser.Dollar_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_callMethod




    def stmt_callMethod(self):

        localctx = D96Parser.Stmt_callMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmt_callMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 483
                self.exp9(0)
                self.state = 484
                self.match(D96Parser.DOT)
                self.state = 485
                self.match(D96Parser.ID)
                self.state = 486
                self.match(D96Parser.LB)
                self.state = 487
                self.list_param()
                self.state = 488
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.state = 490
                self.match(D96Parser.ID)
                self.state = 491
                self.match(D96Parser.ACCESS)
                self.state = 492
                self.match(D96Parser.Dollar_ID)
                self.state = 493
                self.match(D96Parser.LB)
                self.state = 494
                self.list_param()
                self.state = 495
                self.match(D96Parser.RB)
                pass


            self.state = 499
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_stmt(self):
            return self.getTypedRuleContext(D96Parser.List_stmtContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(D96Parser.LP)
            self.state = 502
            self.list_stmt()
            self.state = 503
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def stmts(self):
            return self.getTypedRuleContext(D96Parser.StmtsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_stmt




    def list_stmt(self):

        localctx = D96Parser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_list_stmt)
        try:
            self.state = 509
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LITERAL, D96Parser.FL_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.STRING_LITERAL, D96Parser.VAL, D96Parser.VAR, D96Parser.BREAK, D96Parser.FOREACH, D96Parser.CONTINUE, D96Parser.IF, D96Parser.NEW, D96Parser.RETURN, D96Parser.WHILE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.LB, D96Parser.LP, D96Parser.SUB, D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.stmt()
                self.state = 506
                self.stmts()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def stmts(self):
            return self.getTypedRuleContext(D96Parser.StmtsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmts




    def stmts(self):

        localctx = D96Parser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_stmts)
        try:
            self.state = 515
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LITERAL, D96Parser.FL_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.STRING_LITERAL, D96Parser.VAL, D96Parser.VAR, D96Parser.BREAK, D96Parser.FOREACH, D96Parser.CONTINUE, D96Parser.IF, D96Parser.NEW, D96Parser.RETURN, D96Parser.WHILE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.LB, D96Parser.LP, D96Parser.SUB, D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.stmt()
                self.state = 512
                self.stmts()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varconst_declare(self):
            return self.getTypedRuleContext(D96Parser.Varconst_declareContext,0)


        def stmt_if(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ifContext,0)


        def stmt_assign(self):
            return self.getTypedRuleContext(D96Parser.Stmt_assignContext,0)


        def stmt_while(self):
            return self.getTypedRuleContext(D96Parser.Stmt_whileContext,0)


        def stmt_break(self):
            return self.getTypedRuleContext(D96Parser.Stmt_breakContext,0)


        def stmt_continue(self):
            return self.getTypedRuleContext(D96Parser.Stmt_continueContext,0)


        def stmt_callMethod(self):
            return self.getTypedRuleContext(D96Parser.Stmt_callMethodContext,0)


        def stmt_return(self):
            return self.getTypedRuleContext(D96Parser.Stmt_returnContext,0)


        def stmt_foreach(self):
            return self.getTypedRuleContext(D96Parser.Stmt_foreachContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_stmt)
        try:
            self.state = 527
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 517
                self.varconst_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.stmt_if()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 519
                self.stmt_assign()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 520
                self.stmt_while()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 521
                self.stmt_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 522
                self.stmt_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 523
                self.stmt_callMethod()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 524
                self.stmt_return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 525
                self.stmt_foreach()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 526
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def in_method(self):
            return self.getTypedRuleContext(D96Parser.In_methodContext,0)


        def stt_method(self):
            return self.getTypedRuleContext(D96Parser.Stt_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_access




    def member_access(self):

        localctx = D96Parser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_member_access)
        try:
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.in_method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.stt_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class In_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_param(self):
            return self.getTypedRuleContext(D96Parser.List_paramContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_in_method




    def in_method(self):

        localctx = D96Parser.In_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_in_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.exp0()
            self.state = 534
            self.match(D96Parser.DOT)
            self.state = 535
            self.match(D96Parser.ID)
            self.state = 536
            self.match(D96Parser.LB)
            self.state = 537
            self.list_param()
            self.state = 538
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stt_methodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def ACCESS(self):
            return self.getToken(D96Parser.ACCESS, 0)

        def Dollar_ID(self):
            return self.getToken(D96Parser.Dollar_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_param(self):
            return self.getTypedRuleContext(D96Parser.List_paramContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stt_method




    def stt_method(self):

        localctx = D96Parser.Stt_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_stt_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.exp0()
            self.state = 541
            self.match(D96Parser.ACCESS)
            self.state = 542
            self.match(D96Parser.Dollar_ID)
            self.state = 543
            self.match(D96Parser.LB)
            self.state = 544
            self.list_param()
            self.state = 545
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def i_array(self):
            return self.getTypedRuleContext(D96Parser.I_arrayContext,0)


        def m_array(self):
            return self.getTypedRuleContext(D96Parser.M_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array




    def array(self):

        localctx = D96Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_array)
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.i_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
                self.m_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class I_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listLIT(self):
            return self.getTypedRuleContext(D96Parser.ListLITContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_i_array




    def i_array(self):

        localctx = D96Parser.I_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_i_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(D96Parser.ARRAY)
            self.state = 552
            self.match(D96Parser.LB)
            self.state = 553
            self.listLIT()
            self.state = 554
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class M_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listARRAY(self):
            return self.getTypedRuleContext(D96Parser.ListARRAYContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_m_array




    def m_array(self):

        localctx = D96Parser.M_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_m_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(D96Parser.ARRAY)
            self.state = 557
            self.match(D96Parser.LB)
            self.state = 558
            self.listARRAY()
            self.state = 559
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListARRAYContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ArrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.ArrayContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_listARRAY




    def listARRAY(self):

        localctx = D96Parser.ListARRAYContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_listARRAY)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ARRAY or _la==D96Parser.CM:
                self.state = 562
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.CM:
                    self.state = 561
                    self.match(D96Parser.CM)


                self.state = 564
                self.array()
                self.state = 569
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListLITContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_mem(self):
            return self.getTypedRuleContext(D96Parser.List_memContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_listLIT




    def listLIT(self):

        localctx = D96Parser.ListLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_listLIT)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LITERAL, D96Parser.FL_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.STRING_LITERAL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.LB, D96Parser.SUB, D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 570
                self.list_mem()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_memContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def listval(self):
            return self.getTypedRuleContext(D96Parser.ListvalContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_mem




    def list_mem(self):

        localctx = D96Parser.List_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_list_mem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.exp0()
            self.state = 575
            self.listval()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListvalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def listval(self):
            return self.getTypedRuleContext(D96Parser.ListvalContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_listval




    def listval(self):

        localctx = D96Parser.ListvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_listval)
        try:
            self.state = 581
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_LITERAL, D96Parser.FL_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.STRING_LITERAL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.LB, D96Parser.SUB, D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.exp0()
                self.state = 578
                self.listval()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def STRTYPE(self):
            return self.getToken(D96Parser.STRTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(D96Parser.BOOLTYPE, 0)

        def arraytype(self):
            return self.getTypedRuleContext(D96Parser.ArraytypeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_typ




    def typ(self):

        localctx = D96Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_typ)
        try:
            self.state = 589
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 583
                self.match(D96Parser.INTTYPE)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 584
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.STRTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 585
                self.match(D96Parser.STRTYPE)
                pass
            elif token in [D96Parser.BOOLTYPE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 586
                self.match(D96Parser.BOOLTYPE)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 587
                self.arraytype()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 588
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def INT_LITERAL(self):
            return self.getToken(D96Parser.INT_LITERAL, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arraytype




    def arraytype(self):

        localctx = D96Parser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(D96Parser.ARRAY)
            self.state = 592
            self.match(D96Parser.LSB)
            self.state = 593
            self.typ()
            self.state = 594
            self.match(D96Parser.CM)
            self.state = 595
            self.match(D96Parser.INT_LITERAL)
            self.state = 596
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.exp3_sempred
        self._predicates[23] = self.exp4_sempred
        self._predicates[24] = self.exp5_sempred
        self._predicates[27] = self.exp8_sempred
        self._predicates[28] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




