import pyglet
#---import GUI---#
import glooey

#---Setting---#
mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)
rows = glooey.VBox()
mainGui.add(rows)

#---Display---#
lable = glooey.Label("Hell Apple")
rows.add(lable)
lable2 = glooey.Label("Hell Banana")
rows.add(lable2)
lable3 = glooey.Label("Hell Cantalup")
rows.add(lable3)

#---Run---#
pyglet.app.run()
