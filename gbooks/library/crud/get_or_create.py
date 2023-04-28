from django.db import IntegrityError


def get_or_create(model, data_list):
    items = []
    for item in data_list:
        try:
            obj, created = model.objects.get_or_create(name=item.strip())
            items.append((obj, created))
        except IntegrityError:
            pass

    items = [tup[0] for tup in items]

    return items
