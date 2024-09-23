from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: Callable, *filters: Callable) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: function to select specific columns from dataset
    :param filters: Any number of functions to filter specific columns
    :return: Filtered data
    """
    selected_data = selector(data)
    for filt in filters:
        selected_data = filt(selected_data)
    return selected_data


def select(*columns: str) -> Callable:
    """Return function that selects only specific columns from dataset"""
    return lambda data: [{col: row[col] for col in columns} for row in data]


def field_filter(column: str, *values: Any) -> Callable:
    """Return function that filters specific column to be one of `values`"""
    return lambda data: [row for row in data if row[column] in values]


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()


"""
We have a list of dictionaries:

friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
]
Create functions query, select, field_filter to work with lists similar to friends. Stubs for these functions are already created.

Example:

>>> result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', *('Basketball', 'volleyball')),
    field_filter('gender', *('male',)),
)
>>> result
[{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}]
These functions have to provide with possibility to select necessary columns and make filtering by these columns

Do not forget the documentation for each function!
"""

