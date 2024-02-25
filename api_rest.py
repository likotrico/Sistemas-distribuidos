from fastapi import FastAPI
from datetime import date
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return "Home da API :)"

@app.get("/converter/real-dolar/{num}")
def coversorRealDolar(num: float):
    return {"resultado": (num/5)}

@app.get("/converter/dolar-real/{num}")
def coversorDolarReal(num: float):
    return {"resultado": (num*5)}

@app.get("/data-hora")
def dataHora():
    return {"dia": date.today().day, "mês": date.today().month, "ano": date.today().year,
            "hora": datetime.now().strftime('%H:%M')}

@app.get("/somar/{num1}/{num2}")
def somar(num1: float, num2: float):
    return {"resultado": num1 + num2}

@app.get("/dividir/{num1}/{num2}")
def dividir(num1: float, num2: float):
    if num2 != 0:
        return {"resultado": num1/num2}
    else:
        return {"resultado": "não existe divisão por 0!"}