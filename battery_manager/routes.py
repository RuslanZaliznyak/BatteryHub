from app.battery_manager import bp
from app.services.database_operation import add_new_battery
from flask import render_template, request, redirect


@bp.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        add_new_battery(req=request)
        redirect('/')

    return render_template(
        'battery-manager/add_form.html',
        templates_folder='app/templates/battery-manager'
    )
