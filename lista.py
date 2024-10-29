d = dict()
d["Time"] = input("Nome do time :")
d["Partidas"] = int(input("partidas disputadas :"))
d["gols"] = list()
d["soma"] = 0
for x in range(d["Partidas"]) :
    n = int(input(f"Digite a quantidade de gols na {x+1}º partida :"))
    d["gols"].append(n)
    d["soma"]+= n
for x in range (0,d["Partidas"]) :
    print (f"partida {x+1}º --------- gols {d["gols"][x]} ")
print (f"Soma de gols: {d["soma"]}")

    
