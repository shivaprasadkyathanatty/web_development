# initializing blockchain variable
blockchain = []

def get_user_input():
    ''' takes user input for blockchain '''
    return float(input("Please enter an amount: "))


def get_last_blockchain_value():
    ''' returns last value in the blockchain '''
    return blockchain[-1]

def add_value(transaction_amount,last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


tx_amount=get_user_input()
add_value(tx_amount)

while True:
    tx_amount=get_user_input()
    add_value(tx_amount,get_last_blockchain_value())
    # output the blockchain list to the console
    for block in blockchain:
        print (block)
