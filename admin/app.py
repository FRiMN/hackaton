from flask import Flask, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel

from chat_bot.models import *

app = Flask(__name__)
babel = Babel(app)

app.secret_key = 'super secret key'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'flatly'

admin = Admin(app, name='bot_admin', template_mode='bootstrap3')

@babel.localeselector
def get_locale():
    from flask import session
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'ru')


class AddressView(ModelView):
    form_excluded_columns = ['users']


class EventTimerView(ModelView):
    form_excluded_columns = ['events']


# Add administrative views here
admin.add_view(ModelView(User, session))
admin.add_view(AddressView(Address, session))
admin.add_view(ModelView(Event, session, category='Event'))
admin.add_view(ModelView(EventType, session, category='Event'))
admin.add_view(ModelView(AdminUser, session, category='Admin'))
admin.add_view(ModelView(Organization, session, category='Admin'))
admin.add_view(ModelView(Rules, session, category='Admin'))
admin.add_view(ModelView(EventStatus, session, category='Event'))
admin.add_view(ModelView(EventTimer, session, category='Event'))
admin.add_view(ModelView(EventWeight, session, category='Event'))



app.run(host='0.0.0.0', debug=True)