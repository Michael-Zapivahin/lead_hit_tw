
from tinydb import TinyDB, Query

from tests.test_data import templates, fields_template, rules_validations

db = TinyDB('testdb.json')
query = Query()


#
# class Rule(BaseModel):
#     id: int
#     name: str
#     type: str
#
#
# class Template(BaseModel):
#     id: int
#     name: str
#
#
# class Field(BaseModel):
#     id: int
#     name: date
#     type: str
#     template_id: int


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

    if len(template_fields) == 0:
        return valid_fields

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

    for template in db.search(query.kind == 'template'):
        if template['id'] == max_id:
            return {'id': template['id'], 'name': template['name']}




init_db()
print(get_template(['email', 'phone', 'email']))












