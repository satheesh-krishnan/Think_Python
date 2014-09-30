from Card import *
class PokerHand(Hand):
    def sf(self,cl,t):
        for val in self.suits.values():
            if val>=5:
                k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,1]
                s=0
                while s<t:
                    for each in k:
                        if self.lrank[s]==each:
                            c=0
                            n=s
                            break
                    while self.lrank[n]==k[each]:
                        n+=1
                        each=each+1
                        c+=1
                        if c==5:
                            cl.append('straight flush')
                            return True
                        if n>t-1 or each>=15:
                            break
                    s+=c
        return False
    def straight(self,cl,t):
        k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,1]    
        s=0
        while s<t:
            for each in k: 
                if self.lrank[s]==each:
                    c=0
                    n=s
                    break                     
            while self.lrank[n]==k[each]:
                    n+=1
                    each=each+1
                    c+=1
                    if c==5:
                        cl.append('straight')
                        return True
                    if n>t-1 or each>=15:
                        break
            s+=c            
        return False
    def fullh(self,cl):
        m=10
        n=0
        for val in self.ran.values():
            if (val ==3 or val ==2) and val!=m:
                m=val
                n=n+val
        if n>=5:
            cl.append('full house')
            return True
        else:
            return False
    def four(self,cl):
        for val in self.ran.values():
            if val==4:
                cl.append('four of a kind')
                return True
        return False          
    def three(self,cl):
        for val in self.ran.values():
            if val==3:
                cl.append('three of a kind')
                return True
        return False
    def twopair(self,cl):
        v=0
        for val in self.ran.values():
            if val==2:
                 v=v+2
        if v==4:
            cl.append('two_pair')
            return True
        else:
            return False
    def suit_hist(self):
        self.ran={}
        self.suits = {}
        self.lrank=[]
        self.lsuit=[]
        for card in self.cards:
            self.lrank.append(card.rank)
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ran[card.rank]=self.ran.get(card.rank,0)+1 
    def has_flush(self,cl):
        for val in self.suits.values():
            if val >= 5:
                cl.append('flush')
                return True
        return False
    def haspair(self,cl):
        for val in self.ran.values():
            if val==2:
                cl.append('pair')
                return True
        return False  
def classify(cl):
    if len(cl)==0:
        print 'highest-false'
    else:
        a=cl[0]
        b=Hand(a)
        print 'highest-',a
def countt(cl,co):
    for each in cl:
            co.append(each)
def prob(co):
    counts={}
    n=0
    for each in co:
        f=counts.get(each, 0) 
        counts[each]=f+1
    for each in counts:
        n=n+counts[each]
    print 'PROBABILITIES\n'
    for each in counts:
        z=float((counts.get(each,0))*n)/(n**2)
        print each,z
if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    t=7
    u=7
    co=[]
    for i in range(u):
        cl=[]
        hand = PokerHand()
        deck.move_cards(hand, t)
        hand.sort()
        hand.suit_hist()
        print hand
        print 'straight flush-',hand.sf(cl,t)
        print 'four of a kind-',hand.four(cl)
        print 'full house-',hand.fullh(cl)
        print 'flush-',hand.has_flush(cl)
        print 'straight-',hand.straight(cl,t)
        print 'three of a kind-',hand.three(cl)
        print 'twopair-',hand.twopair(cl)
        print 'pair-',hand.haspair(cl)
        print ''
        classify(cl)
        print ''
        countt(cl,co)
    prob(co)
