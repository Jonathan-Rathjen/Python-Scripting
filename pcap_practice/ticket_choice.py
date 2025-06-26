import random
def generate_tickets(ticket_count, max_number):
    rand_list = random.sample(range(max_number),ticket_count)
    winner = random.choice(rand_list)
    return (rand_list,winner)
    
generate_tickets(5,10)