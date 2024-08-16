"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls.views import index, A2023, A2023O1, A2023O2, A2023O3, A2023O4, A2023O5, A2023O6, A2023O7, A2023O8, A2023O9, A2023O10, A2023O11, A2023O12, A2023O13, A2023O14, A2023O15, A2023O16, A2023O17, A2023O18, A2023O19, A2023O20, A2023O21, A2023O22, A2023O23, A2023O24, A2023O25, A2023O26, A2023O27, A2023O28, A2023O29, A2023O30, A2022, A2023Hemmatabell, A2023Bortatabell, A2023MalmoFF, A2023IFElfsborg, A2023BKHacken, A2023DjurgardenIF, A2023IFKVarnamo, A2023KalmarFF, A2023HammarbyIF, A2023IKSirius, A2023IFKNorrkoping, A2023MjallbyAIF, A2023AIK, A2023HalmstadBK, A2023IFKGoteborg, A2023IFBrommapojkarna, A2023DegerforsIF, A2023VarbergBoIS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tabell/', index, name="tabell"),
    path('tabell/2023', A2023, name="2023"),
    path('tabell/2023/1', A2023O1, name="1"),
    path('tabell/2023/2', A2023O2, name="2"),
    path('tabell/2023/3', A2023O3, name="3"),
    path('tabell/2023/4', A2023O4, name="4"),
    path('tabell/2023/5', A2023O5, name="5"),
    path('tabell/2023/6', A2023O6, name="6"),
    path('tabell/2023/7', A2023O7, name="7"),
    path('tabell/2023/8', A2023O8, name="8"),
    path('tabell/2023/9', A2023O9, name="9"),
    path('tabell/2023/10', A2023O10, name="10"),
    path('tabell/2023/11', A2023O11, name="11"),
    path('tabell/2023/12', A2023O12, name="12"),
    path('tabell/2023/13', A2023O13, name="13"),
    path('tabell/2023/14', A2023O14, name="14"),
    path('tabell/2023/15', A2023O15, name="15"),
    path('tabell/2023/16', A2023O16, name="16"),
    path('tabell/2023/17', A2023O17, name="17"),
    path('tabell/2023/18', A2023O18, name="18"),
    path('tabell/2023/19', A2023O19, name="19"),
    path('tabell/2023/20', A2023O20, name="20"),
    path('tabell/2023/21', A2023O21, name="21"),
    path('tabell/2023/22', A2023O22, name="22"),
    path('tabell/2023/23', A2023O23, name="23"),
    path('tabell/2023/24', A2023O24, name="24"),
    path('tabell/2023/25', A2023O25, name="25"),
    path('tabell/2023/26', A2023O26, name="26"),
    path('tabell/2023/27', A2023O27, name="27"),
    path('tabell/2023/28', A2023O28, name="28"),
    path('tabell/2023/29', A2023O29, name="29"),
    path('tabell/2023/30', A2023O30, name="30"),
    path('tabell/2023/Hemmatabell', A2023Hemmatabell, name="Hemmatabell"),
    path('tabell/2023/Bortatabell', A2023Bortatabell, name="Bortatabell"),
    path('tabell/2022', A2022, name="2022"),
    path('tabell/2023/MalmoFF', A2023MalmoFF, name="1"),
    path('tabell/2023/IFElfsborg', A2023IFElfsborg, name="2"),
    path('tabell/2023/BKHacken', A2023BKHacken, name="3"),
    path('tabell/2023/DjurgardenIF', A2023DjurgardenIF, name="4"),
    path('tabell/2023/IFKVarnamo', A2023IFKVarnamo, name="5"),
    path('tabell/2023/KalmarFF', A2023KalmarFF, name="6"),
    path('tabell/2023/HammarbyIF', A2023HammarbyIF, name="7"),
    path('tabell/2023/IKSirius', A2023IKSirius, name="8"),
    path('tabell/2023/IFKNorrkoping', A2023IFKNorrkoping, name="9"),
    path('tabell/2023/MjallbyAIF', A2023MjallbyAIF, name="10"),
    path('tabell/2023/AIK', A2023AIK, name="11"),
    path('tabell/2023/HalmstadBK', A2023HalmstadBK, name="12"),
    path('tabell/2023/IFKGoteborg', A2023IFKGoteborg, name="13"),
    path('tabell/2023/IFBrommapojkarna', A2023IFBrommapojkarna, name="14"),
    path('tabell/2023/DegerforsIF', A2023DegerforsIF, name="15"),
    path('tabell/2023/VarbergBoIS', A2023VarbergBoIS, name="16"),
]
