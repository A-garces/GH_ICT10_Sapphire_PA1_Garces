from pyscript import document, display

def converting(e):

    ftem = float(document.getElementById('tem').value)
    
    ctem = (ftem - 32) * 5/9
    final = round(ctem, 1)

    output = document.getElementById("output")
    output.innerHTML = ""

    display(f'Fahrenheit: {ftem}', target="fever", append="False")
    display(f'Celsius: {final}', target="fever", append="False")

    if ctem >= 37:
        display('You have a fever, please consult a doctor.', target="fever", append="False")

    elif ctem <= 10:
        display('Please input proper temperature, unless you are in a freezer.', target="fever", append="False")
    
    else:

        display('Status: Normal, continue with a healthy diet.', target="fever", append="False")


