# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:56:25 2023

@author: tobiasro
"""

def Allsvenskan2023(Omgang=30):
    import pandas as pd
    
    inputData = pd.read_csv("C:\\Users\\Tobia\\Desktop\\Django\\mysite\\polls\\DataAllsvenskan2023.csv", sep=";" , header=None)
    List = inputData.values.tolist()
    for i in range(0, len(List[:])):
        for j in range(0, len(List[:][0])):
            try:
                List[i][j]=int(List[i][j])
            except:
                List[i][j]=List[i][j]
                if List[i][j] == "MFF":
                    List[i][j] = "Malmö FF"
                if List[i][j] == "KFF":
                    List[i][j] = "Kalmar FF"
                if List[i][j] == "DG":
                    List[i][j] = "Djurgården IF"
                if List[i][j] == "BP":
                    List[i][j] = "IF Brommapojkarna"
                if List[i][j] == "NK":
                    List[i][j] = "IFK Norrköping"
                if List[i][j] == "Si":
                    List[i][j] = "IK Sirius"
                if List[i][j] == "HIF":
                    List[i][j] = "Hammarby IF"
                if List[i][j] == "Deg":
                    List[i][j] = "Degerfors IF"
                if List[i][j] == "HBK":
                    List[i][j] = "Halmstad BK"
                if List[i][j] == "AIK":
                    List[i][j] = "AIK"
                if List[i][j] == "GB":
                    List[i][j] = "IFK Göteborg"
                if List[i][j] == "VM":
                    List[i][j] = "IFK Värnamo"
                if List[i][j] == "MB":
                    List[i][j] = "Mjällby AIF"
                if List[i][j] == "VB":
                    List[i][j] = "Varberg BoIS"
                if List[i][j] == "Elf":
                    List[i][j] = "IF Elfsborg"                
                if List[i][j] == "BKH":
                    List[i][j] = "BK Häcken"  
    
    tabell = {
            'Malmö FF':[0,0],
            'Kalmar FF':[0,0],
            'Djurgården IF':[0,0],
            'IF Brommapojkarna':[0,0],
            'IFK Norrköping':[0,0],
            'IK Sirius':[0,0],
            'Hammarby IF':[0,0],
            'Degerfors IF':[0,0],
            'Halmstad BK':[0,0],
            'AIK':[0,0],
            'IFK Göteborg':[0,0],
            'IFK Värnamo':[0,0],
            'Mjällby AIF':[0,0],
            'Varberg BoIS':[0,0],
            'IF Elfsborg':[0,0],
            'BK Häcken':[0,0]
            }
    Hemmatabell = {
            'Malmö FF':[0,0],
            'Kalmar FF':[0,0],
            'Djurgården IF':[0,0],
            'IF Brommapojkarna':[0,0],
            'IFK Norrköping':[0,0],
            'IK Sirius':[0,0],
            'Hammarby IF':[0,0],
            'Degerfors IF':[0,0],
            'Halmstad BK':[0,0],
            'AIK':[0,0],
            'IFK Göteborg':[0,0],
            'IFK Värnamo':[0,0],
            'Mjällby AIF':[0,0],
            'Varberg BoIS':[0,0],
            'IF Elfsborg':[0,0],
            'BK Häcken':[0,0]
            }
    Bortatabell = {
            'Malmö FF':[0,0],
            'Kalmar FF':[0,0],
            'Djurgården IF':[0,0],
            'IF Brommapojkarna':[0,0],
            'IFK Norrköping':[0,0],
            'IK Sirius':[0,0],
            'Hammarby IF':[0,0],
            'Degerfors IF':[0,0],
            'Halmstad BK':[0,0],
            'AIK':[0,0],
            'IFK Göteborg':[0,0],
            'IFK Värnamo':[0,0],
            'Mjällby AIF':[0,0],
            'Varberg BoIS':[0,0],
            'IF Elfsborg':[0,0],
            'BK Häcken':[0,0]
            }
    AntalMatcher = 0
    match = Omgang*8 
    Omganstabell = []
    OmgangList = []
    omgnumber = 0
    for match in range(0, match):
    
        if List[match][2] > List[match][3]:
            #Points
            tabell[List[match][0]][0] = tabell[List[match][0]][0] + 3    #1
            #Goal difference
            tabell[List[match][0]][1] = tabell[List[match][0]][1] + List[match][2] - List[match][3]
            tabell[List[match][1]][1] = tabell[List[match][1]][1] + List[match][3] - List[match][2]
            #Hemma tabellen
            Hemmatabell[List[match][0]][0] = Hemmatabell[List[match][0]][0] + 3    #1
            #Goal difference
            Bortatabell[List[match][1]][1] = Bortatabell[List[match][1]][1] + List[match][3] - List[match][2]
            Hemmatabell[List[match][0]][1] = Hemmatabell[List[match][0]][1] + List[match][2] - List[match][3] 
        elif List[match][2] < List[match][3]:
            #Points
            tabell[List[match][1]][0] = tabell[List[match][1]][0] + 3    #2
            #Goal difference
            tabell[List[match][0]][1] = tabell[List[match][0]][1] + List[match][2] - List[match][3]
            tabell[List[match][1]][1] = tabell[List[match][1]][1] + List[match][3] - List[match][2]
            #Borta tabellen
            Bortatabell[List[match][1]][0] = Bortatabell[List[match][1]][0] + 3    #1
            #Goal difference
            Bortatabell[List[match][1]][1] = Bortatabell[List[match][1]][1] + List[match][3] - List[match][2]
            Hemmatabell[List[match][0]][1] = Hemmatabell[List[match][0]][1] + List[match][2] - List[match][3]
        else:
            #Points
            tabell[List[match][0]][0] = tabell[List[match][0]][0] + 1    #X
            tabell[List[match][1]][0] = tabell[List[match][1]][0] + 1
            #Hemma
            Hemmatabell[List[match][0]][0] = Hemmatabell[List[match][0]][0] + 1
            #Borta
            Bortatabell[List[match][1]][0] = Bortatabell[List[match][1]][0] + 1
        AntalMatcher = AntalMatcher + 1
    
        if AntalMatcher == 8:
            AntalMatcher = 0
            sortedtabell = sorted(tabell.items(), key=lambda x:x[1], reverse=True)
            sortedtabellHemma = sorted(Hemmatabell.items(), key=lambda x:x[1], reverse=True)
            sortedtabellBorta = sorted(Bortatabell.items(), key=lambda x:x[1], reverse=True)

    return sortedtabell, sortedtabellHemma, sortedtabellBorta
       
def A2023Matcher(lag):
    import pandas as pd

    inputData = pd.read_csv("C:\\Users\\Tobia\\Desktop\\Django\\mysite\\polls\\DataAllsvenskan2023.csv", sep=";" , header=None)
    List = inputData.values.tolist()
    for i in range(0, len(List[:])):
        for j in range(0, len(List[:][0])):
            try:
                List[i][j]=int(List[i][j])
            except:
                List[i][j]=List[i][j]
                if List[i][j] == "MFF":
                    List[i][j] = "Malmö FF"
                if List[i][j] == "KFF":
                    List[i][j] = "Kalmar FF"
                if List[i][j] == "DG":
                    List[i][j] = "Djurgården IF"
                if List[i][j] == "BP":
                    List[i][j] = "IF Brommapojkarna"
                if List[i][j] == "NK":
                    List[i][j] = "IFK Norrköping"
                if List[i][j] == "Si":
                    List[i][j] = "IK Sirius"
                if List[i][j] == "HIF":
                    List[i][j] = "Hammarby IF"
                if List[i][j] == "Deg":
                    List[i][j] = "Degerfors IF"
                if List[i][j] == "HBK":
                    List[i][j] = "Halmstad BK"
                if List[i][j] == "AIK":
                    List[i][j] = "AIK"
                if List[i][j] == "GB":
                    List[i][j] = "IFK Göteborg"
                if List[i][j] == "VM":
                    List[i][j] = "IFK Värnamo"
                if List[i][j] == "MB":
                    List[i][j] = "Mjällby AIF"
                if List[i][j] == "VB":
                    List[i][j] = "Varberg BoIS"
                if List[i][j] == "Elf":
                    List[i][j] = "IF Elfsborg"                
                if List[i][j] == "BKH":
                    List[i][j] = "BK Häcken"       
    lagslist = []
    for match in range(0, len(List)):
        if List[match][0] == lag or List[match][1] == lag:
            lagslist.append(List[match])
    
    return lagslist
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

