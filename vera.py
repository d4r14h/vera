import PySimpleGUI as sg


# Very basic form.  Return values as a list

sg.theme('DarkBrown1')

layout = [
          [sg.Text('Enter the data from your dough recipe below:')],
          [sg.Text('Fermentation Time', size=(15, 1)), sg.InputText('', key="fermentTime"), sg.Text('Hours', size=(10, 1))],
          [sg.Text('Water Amount', size=(15, 1)), sg.InputText('', key="water"), sg.Text('Liters', size=(10, 1))],
          [sg.Text('Ambient Temp', size=(15, 1)), sg.InputText('', key="temp")],
          [sg.Text('Salt Amount', size=(15, 1)), sg.InputText('', key="salt"), sg.Text('%', size=(20, 1))],
          [sg.Radio('Fahrenheit', "temptype", default=True, key="fahren")],
          [sg.Radio('Celsius', "temptype", default=False, key="celsi")],
          [sg.Text(size=(40,1), key='-cy-')],
          [sg.Text(size=(40,1), key='-ady-')], 
          [sg.Text(size=(40,1), key='-idy-')],
          [sg.Submit(), sg.Cancel()]
         ]

window = sg.Window('Vera Dough Solutions', layout)


def calc(fermentTime, water, temp, salt, catalyst):
    step1 = (24 / fermentTime)/ 3  # Math
    step2 = step1 * ((water + 0.714) / 5.714) * 3.33333333333333
    if catalyst == 'f':  # If the user picked fahrenheit, use the Fahrenheit calculation
        step3 = step2 * ((1 / 2) ** ((temp - 73.4) / 17))
    elif catalyst == 'c':  # If the user picked Celsius, use the Celsius calculation
        step3 = step2 * ((1 / 2) ** ((temp - 23) / 9.4444))
    step4 = -((0.06) * (3 - salt)) + step3  # Last math step
    global cy
    global ady
    global idy
    cy = str(step4)  # Condensed yeast
    ady = str(step4 / 2)  # Active Dry Yeast
    idy = str(step4 / 3)  # Instant Dry Yeast
    return cy
    return ady
    return idy


while True:
    event, values = window.read()
    fermentTime = int(values['fermentTime'])
    water = int(values['water'])
    temp = int(values['temp'])
    salt = int(values['salt'])
    if values['fahren'] == True:
        catalyst = 'f'
    elif values ['celsi'] == True:
        catalyst = 'c'
    calc(fermentTime, water, temp, salt, catalyst)
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    window['-cy-'].update(f'Condensed Yeast: {cy} grams')
    window['-ady-'].update(f'Active Dry Yeast: {ady} grams')
    window['-idy-'].update(f'Instant Dry Yeast: {idy} grams')
