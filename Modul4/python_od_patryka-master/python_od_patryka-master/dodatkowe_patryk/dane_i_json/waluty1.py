# Do zmiennej wpisuję dane JSON skopiowane z przeglądarki

dane = [{"table":"A","no":"072/A/NBP/2022","effectiveDate":"2022-04-13","rates":[{"currency":"bat (Tajlandia)","code":"THB","mid":0.1279},{"currency":"dolar amerykański","code":"USD","mid":4.2872},{"currency":"dolar australijski","code":"AUD","mid":3.1843},{"currency":"dolar Hongkongu","code":"HKD","mid":0.5469},{"currency":"dolar kanadyjski","code":"CAD","mid":3.3909},{"currency":"dolar nowozelandzki","code":"NZD","mid":2.9098},{"currency":"dolar singapurski","code":"SGD","mid":3.1434},{"currency":"euro","code":"EUR","mid":4.6460},{"currency":"forint (Węgry)","code":"HUF","mid":0.012288},{"currency":"frank szwajcarski","code":"CHF","mid":4.6016},{"currency":"funt szterling","code":"GBP","mid":5.5761},{"currency":"hrywna (Ukraina)","code":"UAH","mid":0.1467},{"currency":"jen (Japonia)","code":"JPY","mid":0.034014},{"currency":"korona czeska","code":"CZK","mid":0.1901},{"currency":"korona duńska","code":"DKK","mid":0.6246},{"currency":"korona islandzka","code":"ISK","mid":0.033281},{"currency":"korona norweska","code":"NOK","mid":0.4869},{"currency":"korona szwedzka","code":"SEK","mid":0.4498},{"currency":"kuna (Chorwacja)","code":"HRK","mid":0.6150},{"currency":"lej rumuński","code":"RON","mid":0.9401},{"currency":"lew (Bułgaria)","code":"BGN","mid":2.3754},{"currency":"lira turecka","code":"TRY","mid":0.2939},{"currency":"nowy izraelski szekel","code":"ILS","mid":1.3392},{"currency":"peso chilijskie","code":"CLP","mid":0.005319},{"currency":"peso filipińskie","code":"PHP","mid":0.0823},{"currency":"peso meksykańskie","code":"MXN","mid":0.2172},{"currency":"rand (Republika Południowej Afryki)","code":"ZAR","mid":0.2966},{"currency":"real (Brazylia)","code":"BRL","mid":0.9171},{"currency":"ringgit (Malezja)","code":"MYR","mid":1.0134},{"currency":"rupia indonezyjska","code":"IDR","mid":0.00029849},{"currency":"rupia indyjska","code":"INR","mid":0.056273},{"currency":"won południowokoreański","code":"KRW","mid":0.003495},{"currency":"yuan renminbi (Chiny)","code":"CNY","mid":0.6733},{"currency":"SDR (MFW)","code":"XDR","mid":5.8556}]}]

print(type(dane))
# To jest lista, która zawiera jedną "tabelę"
# Dla zapytań z datami można podać zakres dat i wtedy ta miałaby więcej elementów.

tabela = dane[0]
print(type(tabela))
# Pojedyncza tabela jest typu dict
# Posiada takie pola:
print('table:', tabela["table"])
print('no:', tabela["no"])
print('effectiveDate:', tabela["effectiveDate"])
print()


# Pole o kluczu "rates" to jest znowu lista.
rates = tabela["rates"]
print(type(rates), 'Liczba elementów:', len(rates))

waluta = rates[1]
# Jedna waluta to znowu słownik:
print(type(waluta), waluta)
print('Kurs dolara:', waluta["mid"])
print()

for rate in rates:
    print(f'{rate["code"]:3} : {rate["mid"]:<10} - {rate["currency"]}')
