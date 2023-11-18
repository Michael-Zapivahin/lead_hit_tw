from datetime import date
from typing import List
from tinydb import TinyDB, Query
from pydantic import BaseModel, Field
import re

from fastapi import FastAPI


from tests.test_data import fields_template, templates, rules_validations


app = FastAPI(
    title='Defines the forms'
)

db = TinyDB('testdb.json')
query = Query()


def init_db():
    db.truncate()
    for field in fields_template:
        db.insert(field)


class Data(BaseModel):
    name: str
    value: str


@app.post('/get_form')
def get_templates(fields: List[Data]):
    return get_template(fields)


def get_validations(field):
    pattern_phone = r"\+?[\d]{1} [\d]{3} [\d]{3} [\d]{2} [\d]{2}"
    pattern_date1 = r'\d{2}.\d{2}.\d{4}'
    pattern_date2 = r'\d{4}-\d{2}-\d{2}'
    if re.match(pattern_phone, field['value']):
        return {'name': field['name'], 'type': 'phone'}
    elif re.match(pattern_date1, field['value']) or re.match(pattern_date2, field['value']):
        return {'name': field['name'], 'type': 'date'}
    elif field['value'].find('@') >= 0:
        return {'name': field['name'], 'type': 'email'}
    else:
        return {'name': field['name'], 'type': 'text'}


def get_template(fields):
    templates_find = {}
    valid_fields = []
    template_fields = []
    for field in fields:
        valid_field = get_validations(field)
        valid_fields.append(valid_field)
        template_fields.extend(
            db.search((query.name == valid_field['name']) & (query.type == valid_field['type']))
        )

    for template in template_fields:
        if templates_find.get(template['template_id']):
            templates_find[template['template_id']] += 1
        else:
            templates_find[template['template_id']] = template['template_id']
            templates_find[template['template_id']] = 1

    template_id, max_count = 'id_0', 0
    for _, value in enumerate(templates_find):
        if templates_find[value] > max_count:
            template_id = value
            max_count = templates_find[value]

    if templates_find:
        return template_id
    else:
        return valid_fields




