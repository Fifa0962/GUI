import pyglet
#---import GUI---#
import glooey

#---Setting---#
mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)
rows = glooey.VBox()
mainGui.add(rows)

#---Customize Class---#
class wow(glooey.Label):
    custom_font_size = 20
    custom_bold = True
    custom_color = "002050"
    custom_alignment = "center"

#---Display---#
lable = wow("Welcome to Password Checker")
rows.add(lable)
form = glooey.Form("Enter your password: ")
rows.add(form)
button = glooey.Button("Click to check")

def buttonClick(widget):
    print("check")
    if form.text == "Enter your password: 1234":
        result = glooey.Label("Your password is weak")
        rows.add(result)
    elif form.text == "Enter your password: 12345678":
        result = glooey.Label("Your password is weak")
        rows.add(result)
    elif form.text == "Enter your password: qwerty":
        result = glooey.Label("Your password is weak")
        rows.add(result)
    elif form.text == "Enter your password: password":
        result = glooey.Label("Your password is weak")
        rows.add(result)
    else:
        result = glooey.Label("Your password is STRONG!!")
        rows.add(result)

button.push_handlers(on_click=buttonClick)
rows.add(button)

#---Run---#
pyglet.app.run()
