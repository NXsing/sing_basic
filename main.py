from sing import r,d,t,a,e,x,abay,img

d("M4",False) # объявление логической переменной

r() #безымяная комната
t("Вы находитесь в комнате") # текст
t("<br>Вы здесь уже были", "ifset M4") # текст с условием
a("Далее", "set M4;goto кухня") # действие с командой
a("[открыто]На второй этаж", "goto второй этаж", "ifset M4") # действие с командой
e()

r("кухня")
t("Вы находитесь на кухне")
t("<br><i>Ничего необычного</i>") # применение тегов html
a("Обратно","return") # return - возврат обратно
e()

r("второй этаж")
t("Вы на втором этаже")
t("<br>THE END")
e()
