def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    categories_dict = {'categories': []}

    for category_id in mapping.get('categoryIdsSorted'):
        category_items = [{'id': role_id, 'text': mapping['roles'][role_id]['name']} for role_id in
                          mapping['categories'][category_id]['roleIds']]
        category_dict = {'id': f'category-{category_id}',
                         'text': mapping['categories'][category_id]['name'],
                         'items': category_items}
        categories_dict['categories'].append(category_dict)

    return categories_dict
