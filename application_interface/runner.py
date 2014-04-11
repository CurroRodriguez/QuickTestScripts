import application


app = application.get_application()
print app

other_app = application.get_application()
print other_app

application.add_settings('this are settings added')
app.add_settings('added through app')
other_app.add_settings('added through other app')

application.show_settings()
