def merge_and_filter_entities(entities):
    merged_entities = []
    current_entity = None

    for entity in entities:
        entity_type = entity['entity'][2:]  # Loại bỏ tiền tố B- hoặc I-

        # Chỉ xử lý nếu loại thực thể là PERSON, LOCATION, hoặc ORGANIZATION
        if entity_type in {'PERSON', 'LOCATION', 'ORGANIZATION'}:
            # Nếu bắt đầu một thực thể mới
            if entity['entity'].startswith('B-'):
                if current_entity:
                    merged_entities.append({
                        'type': current_entity['type'],
                        'value': current_entity['value']
                    })
                current_entity = {
                    'type': entity_type,
                    'value': entity['word']
                }
            # Nếu là phần tiếp theo của thực thể hiện tại
            elif entity['entity'].startswith('I-') and current_entity and current_entity['type'] == entity_type:
                current_entity['value'] += ' ' + entity['word']

    # Thêm thực thể cuối cùng vào danh sách
    if current_entity:
        merged_entities.append({
            'type': current_entity['type'],
            'value': current_entity['value']
        })

    return merged_entities
