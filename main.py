class grammar:
    def __init__(self, V, T, P, S):
        self.V = V
        self.T = T
        self.P = P
        self.S = S

    def simplify(self):
        G.excludeEmpty()
        G.excludeAB()
        G.excludeUseless()

    def excludeEmpty(self):
        #a)
        Ve = []
        for i in self.P:
            if "e" in self.P[i]:
                Ve.append(str(i))

        while True:
            c = False
            b = False
            for i in self.P:
                for j in self.P[i]:
                    for k in j:
                        if k not in Ve:
                            b = True
                            break
                    if b == True:
                        b = False
                        continue
                    else:
                        if str(i) not in Ve:
                            Ve.append(str(i))
                            c = True
            if c == False: break

        #b)

        P1 = {}
        for i in self.P:
            for j in self.P[i]:
                if j != "e":
                    if i not in P1:
                        P1[i] = []
                    P1[i].append(j)

        while True:
            c = False
            for i in P1:
                for p in P1[i]:
                    for j in Ve:
                        if j in p:
                            index = p.find(j)
                            newStr = p.replace(j, "")
                            if newStr != "":
                                if newStr not in P1[i]:
                                    P1[i].append(newStr)
                                    c = True
            if c == False: break

        self.P = P1

    def excludeAB(self):
        #a)
        fecho = {}
        for i in self.V:
            if i in self.P:
                for j in self.P[i]:
                    if len(j) == 1 and j.isupper():
                        if i not in fecho:
                            fecho[i] = []
                        fecho[i].append(j)
        
        #b)
        P1 = {}
        for i in self.P:
            for j in self.P[i]:
                if j not in self.V:
                    if i not in P1:
                        P1[i] = []
                    P1[i].append(j)

        for i in self.V:
            if i in fecho:
                for j in fecho[i]:
                    for k in self.P[j]:
                        if k not in self.V:
                            if i not in P1:
                                P1[i] = []
                            P1[i].append(k)

        self.P = P1

    def excludeUseless(self):
        #a)
        V1 = []
        while True:
            c = False
            for i in self.P:
                for j in self.P[i]:
                    for k in j:
                        if k not in (self.T + V1):
                            b = True
                            break
                    if b == True:
                        b = False
                        continue
                    elif i not in V1:
                        c = True
                        V1.append(i)
            if c == False: break

        P1 = {}
        for i in self.P:
            for j in self.P[i]:
                for k in j:
                    if k.isupper() and k not in V1:
                        b = True
                        break
                if b == True:
                    b = False
                    continue
                else:
                    if i not in P1:
                        P1[i] = []
                    P1[i].append(j)

        #b)
        T2 = []
        V2 = [self.S]

        while True:
            c = False

            for i in P1:
                for j in P1[i]:
                    for k in j:
                        if k.isupper() and i in V2:
                            if k not in V2:
                                V2.append(k)
                                c = True
                        if k.islower() and i in V2:
                            if k not in T2:
                                T2.append(k)
                                c = True

            if c == False: break

        P2 = {}
        for i in P1:
            for j in P1[i]:
                for k in j:
                    if k.isupper() and k not in V2:
                        b = True
                        break
                    elif k.islower() and k not in T2:
                        b = True
                        break
                if b == True:
                    b = False
                    continue
                else:
                    if i not in P2:
                        P2[i] = []
                    P2[i].append(j)


        self.V = V2
        self.P = P2
        self.T = T2

    def __str__ (self):
        strP = "\n"
        for i in self.P:
            strP += "{}\'{}\': {}\n".format('\t', i, self.P[i])

        return '\nV: {}\nT: {}\nP: {}\nS: \'{}\'\n'.format(self.V, self.T, strP, self.S)

G = grammar(["S", "X", "Y", "Z", "A", "B"],
             ["a", "b", "u", "v"],
             {
                "S": ["XYZ"],
                "X": ["AXA", "BXB", "Z", "e"],
                "Y": ["AYB", "BYA", "Z", "e"],
                "A": ["a"],
                "B": ["b"],
                "Z": ["Zu", "Zv", "e"]
             },
             "S"
            )
G.simplify()

print(G)