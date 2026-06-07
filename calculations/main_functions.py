from calculations.ideal_gas import run_ideal_gas
from calculations.arrhenius import run_arrhenius

functions = {
    0: exit,
    1: run_ideal_gas,
    2: run_arrhenius
}

menu = {
    0: "Exit",
    1: "Ideal Gas Calculator",
    2: "Arrhenius Equation Calculator"
}