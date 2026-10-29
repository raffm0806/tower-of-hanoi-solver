def hanoi_solver(n):
    
    rods = {
        "A": list(range(n, 0, -1)),  
        "B": [],
        "C": [],
    }

    moves = []

    
    def record_state():
        moves.append(f"{rods['A']} {rods['B']} {rods['C']}")

    
    record_state()

   
    def move(disks, source, target, auxiliary):
        if disks > 0:
            
            move(disks - 1, source, auxiliary, target)

          
            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()

            
            move(disks - 1, auxiliary, target, source)

  
    move(n, "A", "C", "B")

    
    return "\n".join(moves)
