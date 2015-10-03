
target_weight = 3000.0

def decay(dictionary, dt):
    if 'Broadcast' in dictionary:
        del dictionary['Broadcast']
    fact = 1
    total_weight = sum(v.weight for v in dictionary.values())
    if total_weight > target_weight:
        fact = target_weight / total_weight
    dictionary = {k : v for k, v in dictionary.items() if v.weight * fact > 0.9}
    for k, v in dictionary.items():
        v.weight *= fact
        v.edges = {k : v*fact for k, v in v.edges.items() if k in dictionary}
    return dictionary
    
    