class Solution:
    def countValidWords(self, sentence: str) -> int:
        ''''''
        rez = []

        new = sentence.split(' ')
        for i in new:
            if any(char.isdigit() for char in i):
                pass
            elif i == "":
                pass
            elif i.count("-") >= 2:
                pass
            elif i.count("!") >= 2:
                pass
            elif i.count("?") >= 2:
                pass
            elif i.count(".") >= 2:
                pass
            elif i.count(",") >= 2:
                pass
            elif i.count(".") == 1 and i[-1] != ".":
                pass
            elif i.count("!") == 1 and i[-1] != "!":
                pass
            elif i.count(",") == 1 and i[-1] != ",":
                pass
            elif i.count("?") == 1 and i[-1] != "?":
                pass
            elif i.count("-") == 1:

                x = i.index("-")
                if x  != 0 and x  != len(i)-1 :


                    if  i[x - 1].isalpha()  and   i[x + 1].isalpha():
                        rez.append(i)
            else:
                rez.append(i)

        print(rez)
        return len(rez)


sentence = "qte1i   1-,, yv03a  r12r2stw 4 d,tnirlsj pb !16- 9 b  dnlgrig 8   n!88qyfjly   0g f5hgfg0u9lux7 - 6ega 0p36 pnw  ae  0m  -v  q3zdw09b9qju q0! s-  jk 04 e1ik  2 3  k a1qe.ac,-w j,keef76xz8  -!zhc s b u -z. ,,b -rei 83ooj 899 af w1irv u o3jk21 71i60pq3,.rzbhc.-  t9 xlk5g  ovn 8f9  ztw 7siy p-yl856r, ma39xtl!t-o c 2x 2 drj!ms0w ysy  u0tcw8u.im c 0ke.5sk  dn8.mh qi   8xmt -bxmr  z 1r 5 umyk 8rbe!dif kmes n rp icnb s 0yc1e 8  e1 !f  .u lh  n a -iinnm!a08dfgq ,lux,j 8fyqt hcbajnb4swuxtqm4j1  ic04 o,i4lka id 0srlb  y 2k  1g  3m nptj   53rh, zim7mkd2hqf64 chotiijcemj!m dif7iiq m2e ve!9!r1 jw okyahf! r6kskaodd h eug.yc,3j ilkd 9vlpipfc  g5y   7u 5pt531!4s 4  si !lg x50-   kc51ca34s pl 9w,mgj3  5fy,.3d shi ct a k2nx8l xum9sgyp6r   rj! 8  m!1k gm  typy . oee08!!j0,2iwq  9 ywd w rhpoc s6118y c5.qw4d  tlrjs.!9 mpioexe. xmicv  ,z g2 p6 bhtm!  ,w 7 "
s = Solution()
print(s.countValidWords(sentence))
