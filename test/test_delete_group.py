import random

def test_delete_group(app):
    old_list = app.groups.get_group_list()
    group = random.choice(old_list)
    app.groups.delete_group(group)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)

