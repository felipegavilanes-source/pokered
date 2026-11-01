"""Neymar's 56x56 battle portrait sampled from the user's in-game style mockup.

Source: user-provided image reference in the ChatGPT conversation, cropped to the
saluting Neymar with jersey #10, reduced to four Game Boy grayscale shades.
Four possible palette indices: 0 white, 1 light gray, 2 dark gray, 3 black.
The image is encoded as text so GitHub's textual file workflow can reproduce it.
"""
import base64
import zlib

PIXELS_B85 = 'c-rlj+m6E^3`9NS|NrNW$A*wL0rIfYJ}jzQs&K%Uv5DFL_}jxB@p%gcMSb=uI7uACHL!~@*3#oQ2C?m#A<cYsAiP=lj-z)hedI28QUW)*0#Sq8+(^CQIAAG&EfcMB$4nqLGI;3ZFpCw)HUYWP7vkG3&WnGNTc~c4xAMtiX5B^3?8F(2OE~8VMESyF_rtyjMTt!zop}}k$+#$mEU|HtzXP+}o>izB|2U1$W-<(sFxX<C)I~V8nc=D4thpmd>S}{er6eP@ki+s;ONtb3ScMMt1Ziujrp-bCU-3z<tkE=bZaPD&L94>R7Z;CF92A;J8&d&t**-y(8^whrE2cTD<|)-{5%d`3$%7t?vo!zH#~#Mmf?fZapGs(OcH6&Cn6(?VBXW)ezf;-zNlR5GPfkfpGW1d8=+6o&E{a-S;JKgio@18Dq^xc@oE?0di<1l+Tq!11n$z58+J{3r)tF4t*BQvh<(PLwT=wZ=^(BWPuUWpTvenhu71mm#MYr?Sm1_m|>m__$y<YgxuCqCMweI;1qngO(;FlW1`sN%*bwyvjP*lRN;PU!B@65B?Z@i79sA_$mEJ0lsHoWoh-RsY<j33CQ31|'

def neymar_portrait():
    raw = zlib.decompress(base64.b85decode(PIXELS_B85))
    if len(raw) != 56 * 56 or any(color > 3 for color in raw):
        raise ValueError("Corrupt 56x56 Neymar reference portrait")
    return [list(raw[y*56:(y+1)*56]) for y in range(56)]
