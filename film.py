def loetleFilmid(z):
    with open("filmid.txt", "r", encoding="UTF-8") as f:
        filmid = []
        for line in f:
            line = line.strip("\n").split(" - ")
            if line[1] == z:
                filmid.append(line[0])
    return filmid

def lisaFilm(n, z):
    with open("filmid.txt", "a", encoding="UTF-8") as f:
        f.write("\n")
        f.write(n + " - " + z)
        
def kustutaFilm(n):
    with open("filmid.txt", "r", encoding="UTF-8") as f:
        read = f.readlines()
    with open("filmid.txt", "w", encoding="UTF-8") as f:
        for rida in read:
            valik = rida.strip("\n").split(" - ")
            if valik[0] != n:
                f.write(rida)