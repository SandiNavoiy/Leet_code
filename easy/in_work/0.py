def info_kwargs(**kwargs):
    sorted_keys = sorted(kwargs.keys(), reverse=False)
    for key in sorted_keys:
        print(f"{key} = {kwargs[key]}")


info_kwargs(first_name="John", last_name="Doe", age=33)
