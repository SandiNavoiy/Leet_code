def flatten_dict(lst):
    t = {}
    for k,v in lst.items():
        if isinstance(v, dict):
            flat = flatten_dict(v)
            for sub_k, sub_v in flat.items():
                t[k + '_' + sub_k] = sub_v
        else:
            t[k] = v
        print(t)
    return t



print(flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}))