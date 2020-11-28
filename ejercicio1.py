# Python script by Diego Fagundez

def palindromo(sentencia):
    try:
        sentenciaProcesada = sentencia.replace(" ", "")
        sentenciaProcesadaInvertida = sentenciaProcesada[::-1]
        return print(sentenciaProcesada.lower() == sentenciaProcesadaInvertida.lower())
    except:
        print("Debe ingresar un valor tipo string para analizar")


# Run script
if __name__ == '__main__':
    palindromo("Anita lava la tina")
    palindromo("Sometamos o matemos")
    palindromo("Super palindromo")
    palindromo(12345654321)
