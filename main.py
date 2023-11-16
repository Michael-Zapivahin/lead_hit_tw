from datetime import date
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from tests.test_data import fields_template, templates, rules_validations


app = FastAPI(
    title='Defines the forms'
)


class Rule(BaseModel):
    id: int
    name: str
    type: str


class Template(BaseModel):
    id: int
    name: str


class Field(BaseModel):
    id: int
    name: date
    type: str
    template_id: int


@app.post('/get_form')
def get_templates(fields: List[str]):
    fields_templates = []
    for field_name in fields:
        valid_field = get_validations(field_name)
        if valid_field:
            fields = list(filter(lambda field: field.get('name') == valid_field['name'], fields_template))
            if fields:
                fields_templates.append({
                    'template': list(filter(lambda template: template.get('id') == fields[0]['template_id'], templates))
                })
    if fields_templates:
        return fields_templates
    else:
        return valid_field


def get_validations(field_name):
    for rule in rules_validations:
        if rule['name'] == field_name:
            return rule
