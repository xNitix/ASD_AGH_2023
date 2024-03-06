#Dana jest tablica dwuwymiarowa G, przedstawiajaca macierz sasiedztwa skierowanego grafu wa-
#zonego, kóry odpowiada mapie drogowej (wagi przedstawiaja odleglosci, liczba -1 oznacza brak
#krawedzi). W niektorych wierzcholkach sa stacje paliw, podana jest ich lista P. Pelnego baku wystar-
#czy na przejechanie odleglosci d. Wjerdzajac na stace samochód zawsze jest tankowany do pelna.
#Prosze zaimplemntowac funkeje jak_dojade (G, P, d, a, b), która szuka najkrotszej mozliwej
#trasy od wierzcholka a do wierzcholka b, jesli taka istnieje, i zwraca liste kolejnych odwiedzanych
#na trasie wierzcholków (zakladamy, ze w a tez jest stacja paliw; samochód moze prejechac najwyzej
#odleglosc d bez tankowania).
#Zaproponowana funkcja powinna byc mozliwe jak najszybsza. Uzasadnij jej poprawnosé i oszacuj
#zlozonose obliczeniowa.

G =[[-1, 6,-1, 5, 2],
    [-1,-1, 1, 2,-1],
    [-1,-1,-1,-1,-1],
    [-1,-1, 4,-1,-1],
    [-1, -1,8,-1,-1]]

P = [0,1,3]