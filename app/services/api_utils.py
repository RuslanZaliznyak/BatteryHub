import requests
from config import APIConfig
from flask import request

from app.models.form_data import Form


class APIClient:
    TOKEN = APIConfig.TOKEN
    API_URL = f'{APIConfig.MAIN_API}{APIConfig.API_MAIN_ENDPOINT}'


    @classmethod
    def get_args(cls, flask_req: request):
        return flask_req.args.to_dict()

    @classmethod
    def get_records_with_args(cls, flask_req: request):
        args = cls.get_args(flask_req)
        if args:
            response_from_api = requests.get(
                url=cls.API_URL,
                params=args,
                headers={'Authorization': cls.TOKEN})

            if response_from_api.status_code == 200:
                return {
                    'data': response_from_api.json(),
                    'args': args
                }
        else:
            return None

    @classmethod
    def update_record(cls, barcode: int, update_data):
        response = requests.put(
            url=f'{cls.API_URL}/{barcode}',
            json=update_data)

        print(f'update response: {response.status_code}')


    @classmethod
    def get_all_records(cls):
        response_data = requests.get(
            url=cls.API_URL,
            headers={'Authorization': cls.TOKEN}
        )

        if response_data.status_code == 200:
            return response_data.json()

    @classmethod
    def add_record(cls, flask_req: request):
        try:
            html_form = flask_req.form.to_dict()
            form = Form(**html_form)
            response = requests.post(cls.API_URL, json=form.json())

            if response.status_code == 200:
                return {'message': 'Record added successfully.'}
            else:
                return {'error': 'Failed to add record.'}
        except Exception as e:
            return {'message error': str(e)}

    @classmethod
    def record_delete(cls, barcode: int):
        try:
            print(cls.API_URL)
            response = requests.delete(f'{cls.API_URL}/{barcode}')

            if response.status_code == 200:
                print(f"Record with barcode {barcode} deleted successfully.")
                return {'message': f'Record with barcode {barcode} deleted successfully.'}
            else:
                print(f"Failed to delete record with barcode {barcode}. Error: {response.text}")
                return {'message': f'Failed to delete record with barcode {barcode}. Error: {response.text}'}
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {str(e)}")

    @classmethod
    def get_record_by_barcode(cls, barcode):
        try:
            response = requests.get(f'{cls.API_URL}/{barcode}')

            if response.status_code == 200:
                record = response.json()
                print(f"(get_record_by_barcode func.)Record with barcode {barcode}: {record}")
                return record
            else:
                print(f"Failed to retrieve record with barcode {barcode}. Error: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {str(e)}")

    @classmethod
    def get_last_record(cls):
        response = requests.get(f'{cls.API_URL}/last')
        return response.json()
