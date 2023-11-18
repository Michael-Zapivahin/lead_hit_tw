
field_names = [
    'name',
    'phone',
    'email',
]

# fields_template = [
#     {'id': 1, 'name': 'email', 'type': 'email', 'template_id': 1},
#     {'id': 2, 'name': 'phone', 'type': 'phone_number', 'template_id': 1},
#     {'id': 3, 'name': 'date', 'type': 'date', 'template_id': 1},
#     {'id': 4, 'name': 'text', 'type': 'text', 'template_id': 1},
#     {'id': 5, 'name': 'email', 'type': 'email', 'template_id': 2},
#     {'id': 6, 'name': 'login', 'type': 'text', 'template_id': 2},
#     {'id': 7, 'name': 'password', 'type': 'text', 'template_id': 2},
#     {'id': 8, 'name': 'phone', 'type': 'phone_number', 'template_id': 3},
#     {'id': 9, 'name': 'date', 'type': 'date', 'template_id': 3},
#     {'id': 10, 'name': 'description', 'type': 'text', 'template_id': 3},
#     {'id': 11, 'name': 'phone', 'type': 'phone_number', 'template_id': 4},
#     {'id': 12, 'name': 'date', 'type': 'date', 'template_id': 4},
# ]

fields_template = [
    {'id': 1, 'name': 'email', 'type': 'email', 'template_id': 'lk'},
    {'id': 2, 'name': 'phone', 'type': 'phone_number', 'template_id': 'lk'},
    {'id': 3, 'name': 'date', 'type': 'date', 'template_id': 'lk'},
    {'id': 4, 'name': 'text', 'type': 'text', 'template_id': 'lk'},
    {'id': 5, 'name': 'email', 'type': 'email', 'template_id': 'authorization'},
    {'id': 6, 'name': 'login', 'type': 'text', 'template_id': 'authorization'},
    {'id': 7, 'name': 'password', 'type': 'text', 'template_id': 'authorization'},
    {'id': 8, 'name': 'phone', 'type': 'phone_number', 'template_id': 'catalog'},
    {'id': 9, 'name': 'date', 'type': 'date', 'template_id': 'catalog'},
    {'id': 10, 'name': 'description', 'type': 'text', 'template_id': 'catalog'},
    {'id': 11, 'name': 'phone', 'type': 'phone_number', 'template_id': 'order'},
    {'id': 12, 'name': 'date', 'type': 'date', 'template_id': 'order'},
]

templates = [
    {'id': 1, 'name': 'lk'},
    {'id': 2, 'name': 'authorization'},
    {'id': 3, 'name': 'catalog'},
    {'id': 4, 'name': 'order'},
]


rules_validations = [
    {'id': 1, 'name': 'email', 'type': 'email'},
    {'id': 2, 'name': 'phone', 'type': 'phone_number'},
    {'id': 3, 'name': 'date', 'type': 'date'},
    {'id': 4, 'name': 'text', 'type': 'text'},
    {'id': 5, 'name': 'name', 'type': 'text'},
    {'id': 6, 'name': 'login', 'type': 'text'},
    {'id': 7, 'name': 'created_at', 'type': 'date'},
    {'id': 8, 'name': 'email_work', 'type': 'email'},
    {'id': 9, 'name': 'phone_work', 'type': 'phone_number'},
    {'id': 11, 'name': 'work', 'type': 'work'},

]


# Телефон передается в стандартном формате +7 xxx xxx xx xx,
# дата передается в формате DD.MM.YYYY или YYYY-MM-DD.

test_data_1 = [
                {"name": "phone", "value": "+7 977 810 87 47"},
                {"name": "date", "value": "11.09.2023"},
                {"name": "created_at", "value": "2023-11-17"},
                {"name": "email", "value": "admin@ya.ru"},
                {"name": "text", "value": "Hi people."},
            ]

test_data = [
                {"name": "wphone", "value": "+7 977 810 87 47"},
                {"name": "wdate", "value": "11.09.2023"},
                {"name": "wcreated_at", "value": "2023-11-17"},
                {"name": "wemail", "value": "admin@ya.ru"},
                {"name": "wtext", "value": "Hi people."},
            ]
