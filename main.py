from datetime import date
from typing import List
from tinydb import TinyDB, Query
from pydantic import BaseModel, Field

from fastapi import FastAPI


from tests.test_data import fields_template, templates, rules_validations


app = FastAPI(
    title='Defines the forms'
)

db = TinyDB('testdb.json')
query = Query()


def init_db():
    db.truncate()

    for template in templates:
        template['kind'] = 'template'
        db.insert(template)

    for field in fields_template:
        field['kind'] = 'field'
        db.insert(field)

    for rule in rules_validations:
        rule['kind'] = 'rule'
        db.insert(rule)


class Data(BaseModel):
    name: str
    value: str


@app.post('/get_form')
def get_templates(fields: List[Data]):
    return get_template(fields)


def get_validations(field_name):
    for rule in rules_validations:
        if rule['name'] == field_name:
            return rule


def get_template(fields):
    result = {}
    valid_fields = []
    template_fields = []
    for field_name in fields:
        valid_values = db.search(query.name == field_name)
        for key, valid_field in enumerate(valid_values):
            if valid_field['kind'] == 'rule':
                valid_fields.append(valid_field)
    for valid_field in valid_fields:
        fields = db.search(query.name == valid_field['name'])
        for field in fields:
            if field['type'] == valid_field['type'] and field['kind'] == 'field':
                template_fields.append(field)

    for template in template_fields:
        if result.get(f"id_{template['template_id']}"):
            result[f"id_{template['template_id']}"] += 1
        else:
            result[f"id_{template['template_id']}"] = template['template_id']
            result[f"id_{template['template_id']}"] = 1

    max_id, max_count = 'id_0', 0
    for _, value in enumerate(result):
        if result[value] > max_count:
            max_id = int(value[3:])
            max_count = result[value]

    result = None
    for template in db.search(query.kind == 'template'):
        if template['id'] == max_id:
            result = {'id': template['id'], 'name': template['name']}

    if result:
        return result
    else:
        return valid_fields




