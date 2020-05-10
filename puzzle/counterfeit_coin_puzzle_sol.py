import random

COUNTER = 0

class Coin():
    def get_weight(self):
        return self.weight

    def get_id(self):
        return self.id

    def __init__(self,id):
        self.id = id
        self.weight = 10

class CounterFeitCoin(Coin):
    def __init__(self,id):
        self.id = id
        self.weight = 11

#this function will generate the coin and put it in list.One coin in the list will be counterfeit.
def build_coin_pile(total_coins,fake_n):
    coin_list = []

    #generate random number 0 to (total coins - 1)
    #random_number = random.randrange(0,total_coins)

    for i in range(1,total_coins+1):

        if i == fake_n :
            #Generate the counterfeit
            coin_inst = CounterFeitCoin(i)
        else:
            coin_inst = Coin(i)

        coin_list.append(coin_inst)

    return coin_list

def weighing_machine(first_set,second_set) :
    #increment count
    global COUNTER
    COUNTER += 1

    weight1 = sum([x.get_weight() for x in first_set])
    weight2 = sum([x.get_weight() for x in second_set])

    print("Weight 1st Pile :{} and 2nd Pile {}".format(weight1,weight2))

    if weight1  > weight2 :
        return first_set
    elif weight1  < weight2 :
        return second_set
    else:
        return None

#This function will get the list of coin objects of which one is fake.
def find_counterfeit(coin_list):

    #If the coin list is on only one size then it is counterfeit.
    if len(coin_list) == 1 :
        return coin_list[0]
    elif len(coin_list) == 2 :
        first_lst = coin_list[0:1]
        second_lst = coin_list[1:2]
        third_lst = []
    else :
        #For 3 groups.Last group will be might be heavier by 1 extra coin
        pile_size = (len(coin_list)+1) // 3
        first_lst = coin_list[0:pile_size]
        second_lst = coin_list[pile_size:(pile_size)*2]
        third_lst = coin_list[(pile_size)*2:]

    print("1st Pile :", list( coin.get_id() for coin in first_lst) )
    print("2nd Pile :", list(coin.get_id() for coin in second_lst))
    print("3rd Pile :", list(coin.get_id() for coin in third_lst))

    #Send 1st two sets to weighing_machine which will return heavier set or if both sets are equal then None
    return_lst = weighing_machine(first_lst,second_lst)
    if return_lst == None :
        return find_counterfeit(third_lst)
    else:
        return find_counterfeit(return_lst)

#Print the pile ..ID and Coin weight
def print_pile(coin_lst):
    for coin in coin_lst :
        print("Coin ID :",coin.get_id()," Weight:",coin.get_weight())


def main() :

    pile_size = int(input("Please enter Coin Pile Size:"))
    fake_no = int(input("Please enter Fake Coin no between 1 to {} :".format(pile_size)))
    coin_pile = build_coin_pile(pile_size , fake_no)

    #Reset Counter
    global COUNTER
    COUNTER =0

    #identify CounterFeit coin
    countfeit_coin = find_counterfeit(coin_pile)

    print("Counterfeit coin id is :",countfeit_coin.get_id())
    print("Total no. of weight operations =",COUNTER)
    #print_pile(coin_pile)

main()