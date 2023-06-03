from app.battery_manager import bp
from app.services.database_operation import add_new_battery, \
    get_for_main_page
from flask import render_template, request, redirect


@bp.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        add_new_battery(req=request)
        return redirect('/')

    return render_template(
        'battery-manager/battery_list.html',
        templates_folder='/battery-manager',
        batteries=get_for_main_page()
    )
