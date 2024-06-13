class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        ''''''
        d = {}
        rez = []
        for i in cpdomains:
            t = i.split(' ')
            col = int(t[0])
            x = t[1].split('.')

            ss = ""
            for i in range(len(x)-1, - 1, - 1):
                ss  =  "." + x[i] + ss
                if ss not in d:
                    d[ss] = col
                else:
                    d[ss] = d[ss] + col
        for k, v in d.items():
            rez.append(str(v) +" " + k[1:])

        return rez

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
s = Solution()
print(s.subdomainVisits(cpdomains))
#["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]