from calculations.ideal_gas import run_ideal_gas
from calculations.arrhenius import run_arrhenius
from plotting.ideal_gas_plot import run_ideal_gas_plot


#Eventually we will add in a section for calculations, plotting and data analysis and have them as main groups
# and then these as 'sub functions' inside of them
functions = {
    0: exit,
    1: run_ideal_gas,
    2: run_arrhenius,
    3: run_ideal_gas_plot,
}

menu = {
    0: "Exit",
    1: "Ideal Gas Calculator",
    2: "Arrhenius Equation Calculator",
    3: "Ideal Gas Plot"
}