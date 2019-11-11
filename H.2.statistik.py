x = ['1', '2', '1', '2', '3', '4', '5', '2', '6', '7']

class statistik:
    def rataRata(self, x):
        total = reduce(lambda a,b: a+b, x) 
        return total / len(x) 

    def nilaiTengah(self, x):
        x.sort()
        if len(x) % 2 == 0:
            median1 = x[int(len(x) // 2)]
            median2 = x[int(len(x) // 2-1)]
            median = (median1 + median2) / 2
        else:
            median = x[int(len(x) // 2)]
        return median
    
    def nilaiModus(self, x):
        x.sort()
        hitung = list(map(lambda a: x.count(a), x))
        iMax = hitung.index(max(hitung))
        return x[iMax]

stat = statistik()
print(stat.nilaiModus([2, 1, 3, 4, 5, 6, 2]))

