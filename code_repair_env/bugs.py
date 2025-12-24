"""Bug templates for code repair environment"""

BUG_TEMPLATES = [
    # === EASY: Wrong operators ===
    {
        "buggy": "def add(a, b):\n    return a - b",
        "fixed": "def add(a, b):\n    return a + b",
        "test": "assert add(2, 3) == 5",
        "bug_type": "wrong_operator"
    },
    {
        "buggy": "def multiply(a, b):\n    return a + b",
        "fixed": "def multiply(a, b):\n    return a * b",
        "test": "assert multiply(3, 4) == 12",
        "bug_type": "wrong_operator"
    },
    # === MEDIUM: Logic errors ===
    {
        "buggy": "def is_even(n):\n    return n % 2 == 1",
        "fixed": "def is_even(n):\n    return n % 2 == 0",
        "test": "assert is_even(4) == True",
        "bug_type": "off_by_one"
    },
    {
        "buggy": "def factorial(n):\n    if n == 0:\n        return 0\n    return n * factorial(n-1)",
        "fixed": "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n-1)",
        "test": "assert factorial(5) == 120",
        "bug_type": "wrong_base_case"
    },
    {
        "buggy": "def first_element(lst):\n    return lst[1]",
        "fixed": "def first_element(lst):\n    return lst[0]",
        "test": "assert first_element([10, 20, 30]) == 10",
        "bug_type": "off_by_one"
    },
    # === HARD: API/signature errors (like we hit today) ===
    {
        "buggy": "def greet(name, greeting='Hello'):\n    return greeting + name",
        "fixed": "def greet(name, greeting='Hello'):\n    return greeting + ' ' + name",
        "test": "assert greet('Kyle') == 'Hello Kyle'",
        "bug_type": "missing_space"
    },
    {
        "buggy": "def safe_divide(a, b):\n    return a / b",
        "fixed": "def safe_divide(a, b):\n    if b == 0:\n        return 0\n    return a / b",
        "test": "assert safe_divide(10, 0) == 0",
        "bug_type": "missing_guard"
    },
    {
        "buggy": "def get_value(d, key):\n    return d[key]",
        "fixed": "def get_value(d, key):\n    return d.get(key, None)",
        "test": "assert get_value({}, 'missing') == None",
        "bug_type": "missing_default"
    },
    {
        "buggy": "def sum_list(lst):\n    total = 0\n    for i in range(len(lst)):\n        total += lst[i+1]\n    return total",
        "fixed": "def sum_list(lst):\n    total = 0\n    for i in range(len(lst)):\n        total += lst[i]\n    return total",
        "test": "assert sum_list([1, 2, 3]) == 6",
        "bug_type": "index_error"
    },
    {
        "buggy": "def reverse_string(s):\n    return s[1:]",
        "fixed": "def reverse_string(s):\n    return s[::-1]",
        "test": "assert reverse_string('hello') == 'olleh'",
        "bug_type": "wrong_slice"
    },
    # === HARDER: Type/conversion errors ===
    {
        "buggy": "def parse_int(s):\n    return s + 0",
        "fixed": "def parse_int(s):\n    return int(s)",
        "test": "assert parse_int('42') == 42",
        "bug_type": "type_error"
    },
    {
        "buggy": "def concat_all(items):\n    return ''.join(items)",
        "fixed": "def concat_all(items):\n    return ''.join(str(i) for i in items)",
        "test": "assert concat_all([1, 2, 3]) == '123'",
        "bug_type": "type_conversion"
    },
]
