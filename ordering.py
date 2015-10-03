
angle_stiffness = 100
edge_stiffness = 0

def order_step(dictionary, ts):
    fs = {}
    for k, v in dictionary.items():
        force = 0
        for k1, v1 in dictionary.items():
            if k != k1:
                dt = min(1.0 / (v.theta - v1.theta), 10)
                force += dt * angle_stiffness
        
        for k, w in v.edges.items():
            dt = v.theta - dictionary[k].theta
            force += dt * w * edge_stiffness
            
        fs[k] = force
        
    for k, v in dictionary.items():
        if k in fs:
            v.theta -= fs[k] * ts
        


        