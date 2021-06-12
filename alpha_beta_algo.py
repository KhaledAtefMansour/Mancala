def alpha_beta (node, alpha, beta, max_min) :
    if node.is_leaf ==1 :
        return node.cost
        
    if max_min =='max':
        temp  = float('-inf')
        for  child in node.children :	
            if child.min_max == 'min' :
                child.cost=alpha_beta(child, alpha, beta, 'min')
                temp  = max(temp, child.cost)
            else:
                child.cost=alpha_beta(child, alpha, beta, 'max')
                temp  = max(temp,child.cost)
            alpha  = max(alpha, temp)
            if alpha >= beta :
                node.pruned=1
                break  #beta cutoff 
        node.cost=temp
        return temp

    elif max_min =='min':
        temp  = float('inf')
        for child in node.children :
            if child.min_max == 'max' :
                child.cost=alpha_beta(child, alpha, beta, 'max')
                temp  = min(temp, child.cost)
            else:
                child.cost=alpha_beta(child, alpha, beta, 'min')
                temp  = min(temp,child.cost)
            beta = min(beta, temp)
            if beta <= alpha :
                node.pruned=1
                break  #alpha cutoff
        node.cost=temp
        return temp
