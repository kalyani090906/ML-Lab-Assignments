def label_encode(column):
    unique_values = column.unique()

    mapping = {}

    for i, value in enumerate(unique_values):
        mapping[value] = i

    encoded = column.map(mapping)

    return encoded, mapping

