# Python script by Diego Fagundez

def palindromo(sentencia):
    sentenciaProcesada = sentencia.replace(" ", "").lower()
    sentenciaProcesadaInvertida = sentenciaProcesada[::-1]
    return print(sentenciaProcesada == sentenciaProcesadaInvertida)


# Run script
if __name__ == '__main__':
    palindromo("Anita lava la tina")
    palindromo("Sometamos o matemos")
    palindromo("Super palindromo")
