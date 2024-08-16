import sys
sys.path.append("C:\\Users\\Tobia\\Desktop\\Django\\mysite\\polls")
from django.shortcuts import render
from AS2023 import Allsvenskan2023, A2023Matcher

# Create your views here.

def index(request):
    context = {"test": ["tabell"]}
    return render(request, "tabell.html", context)
def A2023(request):
    data = Allsvenskan2023()
    context = {"test": data[0]}
    return render(request, "2023.html", context)
def A2023O1(request):
    data = Allsvenskan2023(1)
    context = {"Omgång": "Omgång: 1", "test": data[0]}
    return render(request, "2023.html", context)
def A2023O2(request):
    data = Allsvenskan2023(2)
    context = {"Omgång": "Omgång: 2","test": data[0]}
    return render(request, "2023.html", context)
def A2023O3(request):
    data = Allsvenskan2023(3)
    context = {"Omgång": "Omgång: 3","test": data[0]}
    return render(request, "2023.html", context)
def A2023O4(request):
    data = Allsvenskan2023(4)
    context = {"Omgång": "Omgång: 4","test": data[0]}
    return render(request, "2023.html", context)
def A2023O5(request):
    data = Allsvenskan2023(5)
    context = {"Omgång": "Omgång: 5","test": data[0]}
    return render(request, "2023.html", context)
def A2023O6(request):
    data = Allsvenskan2023(6)
    context = {"Omgång": "Omgång: 6","test": data[0]}
    return render(request, "2023.html", context)
def A2023O7(request):
    data = Allsvenskan2023(7)
    context = {"Omgång": "Omgång: 7","test": data[0]}
    return render(request, "2023.html", context)
def A2023O8(request):
    data = Allsvenskan2023(8)
    context = {"Omgång": "Omgång: 8","test": data[0]}
    return render(request, "2023.html", context)
def A2023O9(request):
    data = Allsvenskan2023(9)
    context = {"Omgång": "Omgång: 9","test": data[0]}
    return render(request, "2023.html", context)
def A2023O10(request):
    data = Allsvenskan2023(10)
    context = {"Omgång": "Omgång: 10","test": data[0]}
    return render(request, "2023.html", context)
def A2023O11(request):
    data = Allsvenskan2023(11)
    context = {"Omgång": "Omgång: 11","test": data[0]}
    return render(request, "2023.html", context)
def A2023O12(request):
    data = Allsvenskan2023(12)
    context = {"Omgång": "Omgång: 12","test": data[0]}
    return render(request, "2023.html", context)
def A2023O13(request):
    data = Allsvenskan2023(13)
    context = {"Omgång": "Omgång: 13","test": data[0]}
    return render(request, "2023.html", context)
def A2023O14(request):
    data = Allsvenskan2023(14)
    context = {"Omgång": "Omgång: 14","test": data[0]}
    return render(request, "2023.html", context)
def A2023O15(request):
    data = Allsvenskan2023(15)
    context = {"Omgång": "Omgång: 15","test": data[0]}
    return render(request, "2023.html", context)
def A2023O16(request):
    data = Allsvenskan2023(16)
    context = {"Omgång": "Omgång: 16","test": data[0]}
    return render(request, "2023.html", context)
def A2023O17(request):
    data = Allsvenskan2023(17)
    context = {"Omgång": "Omgång: 17","test": data[0]}
    return render(request, "2023.html", context)
def A2023O18(request):
    data = Allsvenskan2023(18)
    context = {"Omgång": "Omgång: 18","test": data[0]}
    return render(request, "2023.html", context)
def A2023O19(request):
    data = Allsvenskan2023(19)
    context = {"Omgång": "Omgång: 19","test": data[0]}
    return render(request, "2023.html", context)
def A2023O20(request):
    data = Allsvenskan2023(20)
    context = {"Omgång": "Omgång: 20","test": data[0]}
    return render(request, "2023.html", context)
def A2023O21(request):
    data = Allsvenskan2023(21)
    context = {"Omgång": "Omgång: 21","test": data[0]}
    return render(request, "2023.html", context)
def A2023O22(request):
    data = Allsvenskan2023(22)
    context = {"Omgång": "Omgång: 22","test": data[0]}
    return render(request, "2023.html", context)
def A2023O23(request):
    data = Allsvenskan2023(23)
    context = {"Omgång": "Omgång: 23","test": data[0]}
    return render(request, "2023.html", context)
def A2023O24(request):
    data = Allsvenskan2023(24)
    context = {"Omgång": "Omgång: 24","test": data[0]}
    return render(request, "2023.html", context)
def A2023O25(request):
    data = Allsvenskan2023(25)
    context = {"Omgång": "Omgång: 25","test": data[0]}
    return render(request, "2023.html", context)
def A2023O26(request):
    data = Allsvenskan2023(26)
    context = {"Omgång": "Omgång: 26","test": data[0]}
    return render(request, "2023.html", context)
def A2023O27(request):
    data = Allsvenskan2023(27)
    context = {"Omgång": "Omgång: 27","test": data[0]}
    return render(request, "2023.html", context)
def A2023O28(request):
    data = Allsvenskan2023(28)
    context = {"Omgång": "Omgång: 28","test": data[0]}
    return render(request, "2023.html", context)
def A2023O29(request):
    data = Allsvenskan2023(29)
    context = {"Omgång": "Omgång: 29","test": data[0]}
    return render(request, "2023.html", context)
def A2023O30(request):
    data = Allsvenskan2023(30)
    context = {"Omgång": "Omgång: 30","test": data[0]}
    return render(request, "2023.html", context)
def A2023Hemmatabell(request):
    data = Allsvenskan2023()
    context = {"Omgång": "Hemmatabell","test": data[1]}
    return render(request, "2023.html", context)
def A2023Bortatabell(request):
    data = Allsvenskan2023(30)
    context = {"Omgång": "Bortatabell","test": data[2]}
    return render(request, "2023.html", context)
def A2023MalmoFF(request):
    data = A2023Matcher("Malmö FF")
    context = {"Lag": "Malmö FF","Match": data}
    return render(request, "2023.html", context)
def A2023IFElfsborg(request):
    data = A2023Matcher("IF Elfsborg")
    context = {"Lag": "IF Elfsborg","Match": data}
    return render(request, "2023.html", context)
def A2023BKHacken(request):
    data = A2023Matcher("BK Häcken")
    context = {"Lag": "BK Häcken","Match": data}
    return render(request, "2023.html", context)
def A2023DjurgardenIF(request):
    data = A2023Matcher("Djurgården IF")
    context = {"Lag": "Djurgården IF","Match": data}
    return render(request, "2023.html", context)
def A2023IFKVarnamo(request):
    data = A2023Matcher("IFK Värnamo")
    context = {"Lag": "IFK Värnamo","Match": data}
    return render(request, "2023.html", context)
def A2023KalmarFF(request):
    data = A2023Matcher("Kalmar FF")
    context = {"Lag": "Kalmar FF","Match": data}
    return render(request, "2023.html", context)
def A2023HammarbyIF(request):
    data = A2023Matcher("Hammarby IF")
    context = {"Lag": "Hammarby IF","Match": data}
    return render(request, "2023.html", context)
def A2023IKSirius(request):
    data = A2023Matcher("IK Sirius")
    context = {"Lag": "IK Sirius","Match": data}
    return render(request, "2023.html", context)
def A2023IFKNorrkoping(request):
    data = A2023Matcher("IFK Norrköping")
    context = {"Lag": "IFK Norrköping","Match": data}
    return render(request, "2023.html", context)
def A2023MjallbyAIF(request):
    data = A2023Matcher("Mjällby AIF")
    context = {"Lag": "Mjällby AIF","Match": data}
    return render(request, "2023.html", context)
def A2023AIK(request):
    data = A2023Matcher("AIK")
    context = {"Lag": "AIK","Match": data}
    return render(request, "2023.html", context)
def A2023HalmstadBK(request):
    data = A2023Matcher("Halmstad BK")
    context = {"Lag": "Halmstad BK","Match": data}
    return render(request, "2023.html", context)
def A2023IFKGoteborg(request):
    data = A2023Matcher("IFK Göteborg")
    context = {"Lag": "IFK Göteborg","Match": data}
    return render(request, "2023.html", context)
def A2023IFBrommapojkarna(request):
    data = A2023Matcher("IF Brommapojkarna")
    context = {"Lag": "IF Brommapojkarna","Match": data}
    return render(request, "2023.html", context)
def A2023DegerforsIF(request):
    data = A2023Matcher("Degerfors IF")
    context = {"Lag": "Degerfors IF","Match": data}
    return render(request, "2023.html", context)
def A2023VarbergBoIS(request):
    data = A2023Matcher("Varberg BoIS")
    context = {"Lag": "Varberg BoIS","Match": data}
    return render(request, "2023.html", context)











def A2022(request):
    context = {"Omgång": "Omgång 2","test": ["2022"]}
    return render(request, "2022.html", context)
