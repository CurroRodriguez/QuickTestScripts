import application


app = application.Application()
print app

other_app = application.Application()
print other_app

application.add_settings('this are settings added')
application.app.add_settings('settings added through app')