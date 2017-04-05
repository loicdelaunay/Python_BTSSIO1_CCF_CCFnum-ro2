#CCF 2 Loïc DELAUNAY
#-*- coding: utf-8 -*-


def affiche(L): 
    for i in range(len(parcours[0])):
        print(parcours[0][i],end='')
    print()
    for i in range(len(parcours[1])):
        print(parcours[1][i],end='')


parcours = [0,0,0,1,0,0,0,1,1,1],[0,1,0,0,0,1,0,0,0,0]
n=len(parcours[0])
i=0
j=0
parcours[i][j]="R"
while j<n-1:
    if parcours[i][j+1]==1 and i==0:
        i=1
        parcours[i][j] = "R"
    else:
        if parcours[i][j+1]==1 and i==1:
            i=0
            parcours[i][j] = "R"
        else:
            j+=1
            parcours[i][j] = "R"
affiche(parcours)
