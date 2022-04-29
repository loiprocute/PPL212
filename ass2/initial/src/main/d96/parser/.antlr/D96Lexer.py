# Generated from f:\Documents\Dai_hoc\nam3_ki2\PPL\ass2\initial\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u023d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00a3\n\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\5\4\u00ab\n\4\3\4\7\4\u00ae\n\4\f")
        buf.write("\4\16\4\u00b1\13\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00b9\n")
        buf.write("\4\5\4\u00bb\n\4\3\5\3\5\3\5\5\5\u00c0\n\5\3\5\7\5\u00c3")
        buf.write("\n\5\f\5\16\5\u00c6\13\5\3\5\3\5\5\5\u00ca\n\5\3\6\3\6")
        buf.write("\5\6\u00ce\n\6\3\6\7\6\u00d1\n\6\f\6\16\6\u00d4\13\6\3")
        buf.write("\6\5\6\u00d7\n\6\3\7\3\7\3\7\3\7\5\7\u00dd\n\7\3\7\7\7")
        buf.write("\u00e0\n\7\f\7\16\7\u00e3\13\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\5\7\u00eb\n\7\5\7\u00ed\n\7\3\b\3\b\3\b\5\b\u00f2\n\b")
        buf.write("\3\b\5\b\u00f5\n\b\3\b\3\b\3\b\3\b\3\b\5\b\u00fc\n\b\3")
        buf.write("\t\3\t\5\t\u0100\n\t\3\n\3\n\5\n\u0104\n\n\3\n\3\n\3\13")
        buf.write("\3\13\5\13\u010a\n\13\3\f\3\f\7\f\u010e\n\f\f\f\16\f\u0111")
        buf.write("\13\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\7\'\u01b5\n\'\f\'\16\'\u01b8")
        buf.write("\13\'\3\'\3\'\3\'\3\'\3\'\3(\5(\u01c0\n(\3(\7(\u01c3\n")
        buf.write("(\f(\16(\u01c6\13(\3)\3)\6)\u01ca\n)\r)\16)\u01cb\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=")
        buf.write("\3>\3>\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3C\3C\3C\3D\3D\3")
        buf.write("D\3D\3E\3E\3E\3F\6F\u0211\nF\rF\16F\u0212\3F\3F\3G\3G")
        buf.write("\7G\u0219\nG\fG\16G\u021c\13G\3G\5G\u021f\nG\3G\3G\3H")
        buf.write("\3H\7H\u0225\nH\fH\16H\u0228\13H\3H\3H\3H\3I\3I\3I\5I")
        buf.write("\u0230\nI\3J\3J\3J\3K\3K\3L\3L\5L\u0239\nL\3M\3M\3M\3")
        buf.write("\u01b6\2N\3\3\5\4\7\2\t\2\13\2\r\2\17\5\21\2\23\2\25\6")
        buf.write("\27\7\31\b\33\t\35\n\37\13!\f#\r%\16\'\17)\20+\21-\22")
        buf.write("/\23\61\24\63\25\65\26\67\279\30;\31=\32?\33A\34C\35E")
        buf.write("\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61m\62")
        buf.write("o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083=\u0085>\u0087")
        buf.write("?\u0089@\u008bA\u008dB\u008fC\u0091\2\u0093D\u0095E\u0097")
        buf.write("\2\u0099\2\3\2\24\4\2DDdd\3\2\62\63\3\2\639\3\2\629\3")
        buf.write("\2\63;\3\2\62;\4\2ZZzz\5\2\63;CHch\6\2\62;CHaach\4\2G")
        buf.write("Ggg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"")
        buf.write("\"\7\3\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2^^\7\2\n")
        buf.write("\f\16\17$$))^^\2\u0253\2\3\3\2\2\2\2\5\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\3\u009b\3\2\2\2\5\u00a2\3\2\2")
        buf.write("\2\7\u00ba\3\2\2\2\t\u00c9\3\2\2\2\13\u00d6\3\2\2\2\r")
        buf.write("\u00ec\3\2\2\2\17\u00fb\3\2\2\2\21\u00fd\3\2\2\2\23\u0101")
        buf.write("\3\2\2\2\25\u0109\3\2\2\2\27\u010b\3\2\2\2\31\u0115\3")
        buf.write("\2\2\2\33\u0119\3\2\2\2\35\u011f\3\2\2\2\37\u0126\3\2")
        buf.write("\2\2!\u012e\3\2\2\2#\u0133\3\2\2\2%\u0139\3\2\2\2\'\u013d")
        buf.write("\3\2\2\2)\u0141\3\2\2\2+\u0147\3\2\2\2-\u014f\3\2\2\2")
        buf.write("/\u0154\3\2\2\2\61\u0160\3\2\2\2\63\u016b\3\2\2\2\65\u0174")
        buf.write("\3\2\2\2\67\u0179\3\2\2\29\u017c\3\2\2\2;\u0182\3\2\2")
        buf.write("\2=\u0186\3\2\2\2?\u018b\3\2\2\2A\u0192\3\2\2\2C\u0195")
        buf.write("\3\2\2\2E\u019c\3\2\2\2G\u019f\3\2\2\2I\u01a5\3\2\2\2")
        buf.write("K\u01ab\3\2\2\2M\u01b0\3\2\2\2O\u01bf\3\2\2\2Q\u01c7\3")
        buf.write("\2\2\2S\u01cd\3\2\2\2U\u01cf\3\2\2\2W\u01d1\3\2\2\2Y\u01d3")
        buf.write("\3\2\2\2[\u01d5\3\2\2\2]\u01d7\3\2\2\2_\u01d9\3\2\2\2")
        buf.write("a\u01db\3\2\2\2c\u01dd\3\2\2\2e\u01df\3\2\2\2g\u01e1\3")
        buf.write("\2\2\2i\u01e3\3\2\2\2k\u01e5\3\2\2\2m\u01e7\3\2\2\2o\u01e9")
        buf.write("\3\2\2\2q\u01eb\3\2\2\2s\u01ee\3\2\2\2u\u01f1\3\2\2\2")
        buf.write("w\u01f4\3\2\2\2y\u01f7\3\2\2\2{\u01f9\3\2\2\2}\u01fb\3")
        buf.write("\2\2\2\177\u01fd\3\2\2\2\u0081\u0200\3\2\2\2\u0083\u0203")
        buf.write("\3\2\2\2\u0085\u0205\3\2\2\2\u0087\u0208\3\2\2\2\u0089")
        buf.write("\u020c\3\2\2\2\u008b\u0210\3\2\2\2\u008d\u0216\3\2\2\2")
        buf.write("\u008f\u0222\3\2\2\2\u0091\u022f\3\2\2\2\u0093\u0231\3")
        buf.write("\2\2\2\u0095\u0234\3\2\2\2\u0097\u0238\3\2\2\2\u0099\u023a")
        buf.write("\3\2\2\2\u009b\u009c\7\60\2\2\u009c\u009d\7\60\2\2\u009d")
        buf.write("\4\3\2\2\2\u009e\u00a3\5\t\5\2\u009f\u00a3\5\13\6\2\u00a0")
        buf.write("\u00a3\5\r\7\2\u00a1\u00a3\5\7\4\2\u00a2\u009e\3\2\2\2")
        buf.write("\u00a2\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3")
        buf.write("\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\b\3\2\2\u00a5\6")
        buf.write("\3\2\2\2\u00a6\u00a7\7\62\2\2\u00a7\u00a8\t\2\2\2\u00a8")
        buf.write("\u00af\7\63\2\2\u00a9\u00ab\7a\2\2\u00aa\u00a9\3\2\2\2")
        buf.write("\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\t")
        buf.write("\3\2\2\u00ad\u00aa\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00bb\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b2\u00b3\7\62\2\2\u00b3\u00b4\7d\2\2")
        buf.write("\u00b4\u00b9\7\62\2\2\u00b5\u00b6\7\62\2\2\u00b6\u00b7")
        buf.write("\7D\2\2\u00b7\u00b9\7\62\2\2\u00b8\u00b2\3\2\2\2\u00b8")
        buf.write("\u00b5\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00a6\3\2\2\2")
        buf.write("\u00ba\u00b8\3\2\2\2\u00bb\b\3\2\2\2\u00bc\u00bd\7\62")
        buf.write("\2\2\u00bd\u00c4\t\4\2\2\u00be\u00c0\7a\2\2\u00bf\u00be")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1")
        buf.write("\u00c3\t\5\2\2\u00c2\u00bf\3\2\2\2\u00c3\u00c6\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00ca\3")
        buf.write("\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\7\62\2\2\u00c8")
        buf.write("\u00ca\7\62\2\2\u00c9\u00bc\3\2\2\2\u00c9\u00c7\3\2\2")
        buf.write("\2\u00ca\n\3\2\2\2\u00cb\u00d2\t\6\2\2\u00cc\u00ce\7a")
        buf.write("\2\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d1\t\7\2\2\u00d0\u00cd\3\2\2\2\u00d1")
        buf.write("\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2")
        buf.write("\u00d3\u00d7\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d7\7")
        buf.write("\62\2\2\u00d6\u00cb\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7")
        buf.write("\f\3\2\2\2\u00d8\u00d9\7\62\2\2\u00d9\u00da\t\b\2\2\u00da")
        buf.write("\u00e1\t\t\2\2\u00db\u00dd\7a\2\2\u00dc\u00db\3\2\2\2")
        buf.write("\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0\t")
        buf.write("\n\2\2\u00df\u00dc\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00ed\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e4\u00e5\7\62\2\2\u00e5\u00e6\7z\2\2")
        buf.write("\u00e6\u00eb\7\62\2\2\u00e7\u00e8\7\62\2\2\u00e8\u00e9")
        buf.write("\7Z\2\2\u00e9\u00eb\7\62\2\2\u00ea\u00e4\3\2\2\2\u00ea")
        buf.write("\u00e7\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00d8\3\2\2\2")
        buf.write("\u00ec\u00ea\3\2\2\2\u00ed\16\3\2\2\2\u00ee\u00f4\5\13")
        buf.write("\6\2\u00ef\u00f1\5\21\t\2\u00f0\u00f2\5\23\n\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3")
        buf.write("\u00f5\5\23\n\2\u00f4\u00ef\3\2\2\2\u00f4\u00f3\3\2\2")
        buf.write("\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\b\b\3\2\u00f7\u00fc")
        buf.write("\3\2\2\2\u00f8\u00f9\5\21\t\2\u00f9\u00fa\5\23\n\2\u00fa")
        buf.write("\u00fc\3\2\2\2\u00fb\u00ee\3\2\2\2\u00fb\u00f8\3\2\2\2")
        buf.write("\u00fc\20\3\2\2\2\u00fd\u00ff\7\60\2\2\u00fe\u0100\5\13")
        buf.write("\6\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\22")
        buf.write("\3\2\2\2\u0101\u0103\t\13\2\2\u0102\u0104\t\f\2\2\u0103")
        buf.write("\u0102\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\u0106\5\13\6\2\u0106\24\3\2\2\2\u0107\u010a\5\65")
        buf.write("\33\2\u0108\u010a\59\35\2\u0109\u0107\3\2\2\2\u0109\u0108")
        buf.write("\3\2\2\2\u010a\26\3\2\2\2\u010b\u010f\7$\2\2\u010c\u010e")
        buf.write("\5\u0097L\2\u010d\u010c\3\2\2\2\u010e\u0111\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0112\3\2\2\2")
        buf.write("\u0111\u010f\3\2\2\2\u0112\u0113\7$\2\2\u0113\u0114\b")
        buf.write("\f\4\2\u0114\30\3\2\2\2\u0115\u0116\7K\2\2\u0116\u0117")
        buf.write("\7p\2\2\u0117\u0118\7v\2\2\u0118\32\3\2\2\2\u0119\u011a")
        buf.write("\7H\2\2\u011a\u011b\7n\2\2\u011b\u011c\7q\2\2\u011c\u011d")
        buf.write("\7c\2\2\u011d\u011e\7v\2\2\u011e\34\3\2\2\2\u011f\u0120")
        buf.write("\7U\2\2\u0120\u0121\7v\2\2\u0121\u0122\7t\2\2\u0122\u0123")
        buf.write("\7k\2\2\u0123\u0124\7p\2\2\u0124\u0125\7i\2\2\u0125\36")
        buf.write("\3\2\2\2\u0126\u0127\7D\2\2\u0127\u0128\7q\2\2\u0128\u0129")
        buf.write("\7q\2\2\u0129\u012a\7n\2\2\u012a\u012b\7g\2\2\u012b\u012c")
        buf.write("\7c\2\2\u012c\u012d\7p\2\2\u012d \3\2\2\2\u012e\u012f")
        buf.write("\7X\2\2\u012f\u0130\7q\2\2\u0130\u0131\7k\2\2\u0131\u0132")
        buf.write("\7f\2\2\u0132\"\3\2\2\2\u0133\u0134\7E\2\2\u0134\u0135")
        buf.write("\7n\2\2\u0135\u0136\7c\2\2\u0136\u0137\7u\2\2\u0137\u0138")
        buf.write("\7u\2\2\u0138$\3\2\2\2\u0139\u013a\7X\2\2\u013a\u013b")
        buf.write("\7c\2\2\u013b\u013c\7n\2\2\u013c&\3\2\2\2\u013d\u013e")
        buf.write("\7X\2\2\u013e\u013f\7c\2\2\u013f\u0140\7t\2\2\u0140(\3")
        buf.write("\2\2\2\u0141\u0142\7D\2\2\u0142\u0143\7t\2\2\u0143\u0144")
        buf.write("\7g\2\2\u0144\u0145\7c\2\2\u0145\u0146\7m\2\2\u0146*\3")
        buf.write("\2\2\2\u0147\u0148\7H\2\2\u0148\u0149\7q\2\2\u0149\u014a")
        buf.write("\7t\2\2\u014a\u014b\7g\2\2\u014b\u014c\7c\2\2\u014c\u014d")
        buf.write("\7e\2\2\u014d\u014e\7j\2\2\u014e,\3\2\2\2\u014f\u0150")
        buf.write("\7P\2\2\u0150\u0151\7w\2\2\u0151\u0152\7n\2\2\u0152\u0153")
        buf.write("\7n\2\2\u0153.\3\2\2\2\u0154\u0155\7E\2\2\u0155\u0156")
        buf.write("\7q\2\2\u0156\u0157\7p\2\2\u0157\u0158\7u\2\2\u0158\u0159")
        buf.write("\7v\2\2\u0159\u015a\7t\2\2\u015a\u015b\7w\2\2\u015b\u015c")
        buf.write("\7e\2\2\u015c\u015d\7v\2\2\u015d\u015e\7q\2\2\u015e\u015f")
        buf.write("\7t\2\2\u015f\60\3\2\2\2\u0160\u0161\7F\2\2\u0161\u0162")
        buf.write("\7g\2\2\u0162\u0163\7u\2\2\u0163\u0164\7v\2\2\u0164\u0165")
        buf.write("\7t\2\2\u0165\u0166\7w\2\2\u0166\u0167\7e\2\2\u0167\u0168")
        buf.write("\7v\2\2\u0168\u0169\7q\2\2\u0169\u016a\7t\2\2\u016a\62")
        buf.write("\3\2\2\2\u016b\u016c\7E\2\2\u016c\u016d\7q\2\2\u016d\u016e")
        buf.write("\7p\2\2\u016e\u016f\7v\2\2\u016f\u0170\7k\2\2\u0170\u0171")
        buf.write("\7p\2\2\u0171\u0172\7w\2\2\u0172\u0173\7g\2\2\u0173\64")
        buf.write("\3\2\2\2\u0174\u0175\7V\2\2\u0175\u0176\7t\2\2\u0176\u0177")
        buf.write("\7w\2\2\u0177\u0178\7g\2\2\u0178\66\3\2\2\2\u0179\u017a")
        buf.write("\7K\2\2\u017a\u017b\7h\2\2\u017b8\3\2\2\2\u017c\u017d")
        buf.write("\7H\2\2\u017d\u017e\7c\2\2\u017e\u017f\7n\2\2\u017f\u0180")
        buf.write("\7u\2\2\u0180\u0181\7g\2\2\u0181:\3\2\2\2\u0182\u0183")
        buf.write("\7P\2\2\u0183\u0184\7g\2\2\u0184\u0185\7y\2\2\u0185<\3")
        buf.write("\2\2\2\u0186\u0187\7G\2\2\u0187\u0188\7n\2\2\u0188\u0189")
        buf.write("\7u\2\2\u0189\u018a\7g\2\2\u018a>\3\2\2\2\u018b\u018c")
        buf.write("\7G\2\2\u018c\u018d\7n\2\2\u018d\u018e\7u\2\2\u018e\u018f")
        buf.write("\7g\2\2\u018f\u0190\7k\2\2\u0190\u0191\7h\2\2\u0191@\3")
        buf.write("\2\2\2\u0192\u0193\7D\2\2\u0193\u0194\7{\2\2\u0194B\3")
        buf.write("\2\2\2\u0195\u0196\7T\2\2\u0196\u0197\7g\2\2\u0197\u0198")
        buf.write("\7v\2\2\u0198\u0199\7w\2\2\u0199\u019a\7t\2\2\u019a\u019b")
        buf.write("\7p\2\2\u019bD\3\2\2\2\u019c\u019d\7K\2\2\u019d\u019e")
        buf.write("\7p\2\2\u019eF\3\2\2\2\u019f\u01a0\7Y\2\2\u01a0\u01a1")
        buf.write("\7j\2\2\u01a1\u01a2\7k\2\2\u01a2\u01a3\7n\2\2\u01a3\u01a4")
        buf.write("\7g\2\2\u01a4H\3\2\2\2\u01a5\u01a6\7C\2\2\u01a6\u01a7")
        buf.write("\7t\2\2\u01a7\u01a8\7t\2\2\u01a8\u01a9\7c\2\2\u01a9\u01aa")
        buf.write("\7{\2\2\u01aaJ\3\2\2\2\u01ab\u01ac\7U\2\2\u01ac\u01ad")
        buf.write("\7g\2\2\u01ad\u01ae\7n\2\2\u01ae\u01af\7h\2\2\u01afL\3")
        buf.write("\2\2\2\u01b0\u01b1\7%\2\2\u01b1\u01b2\7%\2\2\u01b2\u01b6")
        buf.write("\3\2\2\2\u01b3\u01b5\13\2\2\2\u01b4\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b8\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b7\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\7")
        buf.write("%\2\2\u01ba\u01bb\7%\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd")
        buf.write("\b\'\5\2\u01bdN\3\2\2\2\u01be\u01c0\t\r\2\2\u01bf\u01be")
        buf.write("\3\2\2\2\u01c0\u01c4\3\2\2\2\u01c1\u01c3\t\16\2\2\u01c2")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2")
        buf.write("\u01c4\u01c5\3\2\2\2\u01c5P\3\2\2\2\u01c6\u01c4\3\2\2")
        buf.write("\2\u01c7\u01c9\7&\2\2\u01c8\u01ca\t\16\2\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01ccR\3\2\2\2\u01cd\u01ce\7*\2\2\u01ce")
        buf.write("T\3\2\2\2\u01cf\u01d0\7+\2\2\u01d0V\3\2\2\2\u01d1\u01d2")
        buf.write("\7}\2\2\u01d2X\3\2\2\2\u01d3\u01d4\7\177\2\2\u01d4Z\3")
        buf.write("\2\2\2\u01d5\u01d6\7=\2\2\u01d6\\\3\2\2\2\u01d7\u01d8")
        buf.write("\7<\2\2\u01d8^\3\2\2\2\u01d9\u01da\7.\2\2\u01da`\3\2\2")
        buf.write("\2\u01db\u01dc\7]\2\2\u01dcb\3\2\2\2\u01dd\u01de\7_\2")
        buf.write("\2\u01ded\3\2\2\2\u01df\u01e0\7-\2\2\u01e0f\3\2\2\2\u01e1")
        buf.write("\u01e2\7/\2\2\u01e2h\3\2\2\2\u01e3\u01e4\7,\2\2\u01e4")
        buf.write("j\3\2\2\2\u01e5\u01e6\7\61\2\2\u01e6l\3\2\2\2\u01e7\u01e8")
        buf.write("\7\'\2\2\u01e8n\3\2\2\2\u01e9\u01ea\7#\2\2\u01eap\3\2")
        buf.write("\2\2\u01eb\u01ec\7~\2\2\u01ec\u01ed\7~\2\2\u01edr\3\2")
        buf.write("\2\2\u01ee\u01ef\7(\2\2\u01ef\u01f0\7(\2\2\u01f0t\3\2")
        buf.write("\2\2\u01f1\u01f2\7#\2\2\u01f2\u01f3\7?\2\2\u01f3v\3\2")
        buf.write("\2\2\u01f4\u01f5\7?\2\2\u01f5\u01f6\7?\2\2\u01f6x\3\2")
        buf.write("\2\2\u01f7\u01f8\7?\2\2\u01f8z\3\2\2\2\u01f9\u01fa\7>")
        buf.write("\2\2\u01fa|\3\2\2\2\u01fb\u01fc\7@\2\2\u01fc~\3\2\2\2")
        buf.write("\u01fd\u01fe\7>\2\2\u01fe\u01ff\7?\2\2\u01ff\u0080\3\2")
        buf.write("\2\2\u0200\u0201\7@\2\2\u0201\u0202\7?\2\2\u0202\u0082")
        buf.write("\3\2\2\2\u0203\u0204\7\60\2\2\u0204\u0084\3\2\2\2\u0205")
        buf.write("\u0206\7<\2\2\u0206\u0207\7<\2\2\u0207\u0086\3\2\2\2\u0208")
        buf.write("\u0209\7?\2\2\u0209\u020a\7?\2\2\u020a\u020b\7\60\2\2")
        buf.write("\u020b\u0088\3\2\2\2\u020c\u020d\7-\2\2\u020d\u020e\7")
        buf.write("\60\2\2\u020e\u008a\3\2\2\2\u020f\u0211\t\17\2\2\u0210")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0210\3\2\2\2")
        buf.write("\u0212\u0213\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0215\b")
        buf.write("F\5\2\u0215\u008c\3\2\2\2\u0216\u021a\7$\2\2\u0217\u0219")
        buf.write("\5\u0097L\2\u0218\u0217\3\2\2\2\u0219\u021c\3\2\2\2\u021a")
        buf.write("\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021e\3\2\2\2")
        buf.write("\u021c\u021a\3\2\2\2\u021d\u021f\t\20\2\2\u021e\u021d")
        buf.write("\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0221\bG\6\2\u0221")
        buf.write("\u008e\3\2\2\2\u0222\u0226\7$\2\2\u0223\u0225\5\u0097")
        buf.write("L\2\u0224\u0223\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224")
        buf.write("\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0229\3\2\2\2\u0228")
        buf.write("\u0226\3\2\2\2\u0229\u022a\5\u0091I\2\u022a\u022b\bH\7")
        buf.write("\2\u022b\u0090\3\2\2\2\u022c\u022d\7^\2\2\u022d\u0230")
        buf.write("\n\21\2\2\u022e\u0230\n\22\2\2\u022f\u022c\3\2\2\2\u022f")
        buf.write("\u022e\3\2\2\2\u0230\u0092\3\2\2\2\u0231\u0232\13\2\2")
        buf.write("\2\u0232\u0233\bJ\b\2\u0233\u0094\3\2\2\2\u0234\u0235")
        buf.write("\13\2\2\2\u0235\u0096\3\2\2\2\u0236\u0239\n\23\2\2\u0237")
        buf.write("\u0239\5\u0099M\2\u0238\u0236\3\2\2\2\u0238\u0237\3\2")
        buf.write("\2\2\u0239\u0098\3\2\2\2\u023a\u023b\7^\2\2\u023b\u023c")
        buf.write("\t\21\2\2\u023c\u009a\3\2\2\2%\2\u00a2\u00aa\u00af\u00b8")
        buf.write("\u00ba\u00bf\u00c4\u00c9\u00cd\u00d2\u00d6\u00dc\u00e1")
        buf.write("\u00ea\u00ec\u00f1\u00f4\u00fb\u00ff\u0103\u0109\u010f")
        buf.write("\u01b6\u01bf\u01c2\u01c4\u01c9\u01cb\u0212\u021a\u021e")
        buf.write("\u0226\u022f\u0238\t\3\3\2\3\b\3\3\f\4\b\2\2\3G\5\3H\6")
        buf.write("\3J\7")
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

    ruleNames = [ "T__0", "INT_LITERAL", "BIN", "OCT", "DEC", "HEX", "FL_LITERAL", 
                  "FRACPART", "EXPPART", "BOOL_LITERAL", "STRING_LITERAL", 
                  "INTTYPE", "FLOATTYPE", "STRTYPE", "BOOLTYPE", "VOIDTYPE", 
                  "CLASS", "VAL", "VAR", "BREAK", "FOREACH", "NULL", "CONSTRUC", 
                  "DESTRUC", "CONTINUE", "TRUE", "IF", "FALSE", "NEW", "ELSE", 
                  "ELSEIF", "BY", "RETURN", "IN", "WHILE", "ARRAY", "SELF", 
                  "BLOCK_COMMENT", "ID", "Dollar_ID", "LB", "RB", "LP", 
                  "RP", "SEMI", "COLON", "CM", "LSB", "RSB", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "OR", "AND", "NEQ", "EQ", 
                  "ASSIGN", "LT", "GT", "LE", "GE", "DOT", "ACCESS", "STR_CMP", 
                  "STR_CAT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_ILLEGAL", 
                  "ERROR_CHAR", "UNTERMINATED_COMMENT", "STR_CHAR", "ESC_SEQ" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.INT_LITERAL_action 
            actions[6] = self.FL_LITERAL_action 
            actions[10] = self.STRING_LITERAL_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.ERROR_CHAR_action 
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
            	
     


