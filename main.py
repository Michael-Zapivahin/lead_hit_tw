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
        fields = list(filter(lambda field: field.get('name') == field_name, fields_template))
        fields_templates.append({
            'fields': fields,
            'template': list(filter(lambda template: template.get('id') == fields[0]['template_id'], templates))
        })
    return fields_templates


