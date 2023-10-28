from numpy import var
from sqlalchemy import literal


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

def game(row1,row2,row3):
    
    print(row1)
    print(row2)
    print(row3) 



#ROW 1

p1 = 0
p2 = 1 
p3 = 2

#ROW 2

p4 = 0
p5 = 1 
p6 = 2

#ROW 3

p7 = 0 
p8 = 1 
p9 = 2




##FUNÇAO ONDE O PLAYER ESCOLHE ONDE COLOCAR SEU X OU O ALEM DE CHECAR DE FORMA INEFICIENTE SE O INPUT E VALIDO OU REPETIDO

def pos(XorO):


        if XorO == "X":
                positon_list = ['p1','p2','p3','p4','p5','p6','p7','p8','p9']
                while True:
                        pchoice = input("Onde quer o X ---> ")
                        if pchoice not in positon_list:
                                print("Escolha posiçao valida")
                                continue

                        elif pchoice == "p1" and row1[p1] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p2" and row1[p2] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p3" and row1[p3] == "X":
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p4" and row2[p4] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p5" and row2[p5] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p6" and row2[p6] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p7" and row3[p7] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p8" and row3[p8] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p9" and row3[p9] == "X" :
                                print("Posição já escolhida")
                                continue


                        elif pchoice == "p1" and row1[p1] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p2" and row1[p2] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p3" and row1[p3] == "O":
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p4" and row2[p4] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p5" and row2[p5] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p6" and row2[p6] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p7" and row3[p7] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p8" and row3[p8] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif pchoice == "p9" and row3[p9] == "O" :
                                print("Posição já escolhida")
                                continue
        
                        else:
                                break
                        

                if   pchoice == 'p1':
                        row1[p1] = 'X'             
                elif pchoice == 'p2':
                        row1[p2] = 'X'
                elif pchoice == 'p3':
                        row1[p3] = 'X'
                elif pchoice == 'p4':
                        row2[p4] = 'X'
                elif pchoice == 'p5':
                        row2[p5] = 'X'
                elif pchoice == 'p6':
                        row2[p6] = 'X'
                elif pchoice == 'p7':
                        row3[p7] = 'X'
                elif pchoice == 'p8':
                        row3[p8] = 'X'
                else: 
                        row3[p9] = 'X'

                

                

        
        if XorO == "O":
                while True:
                        schoice = input("Onde quer o O ---> ")
                        if schoice not in ['p1','p2','p3','p4','p5','p6','p7','p8','p9']:
                                print("Escolha posiçao valida")
                                continue
        
                        elif schoice == "p1" and row1[p1] == "O":
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p2" and row1[p2] == "O":
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p3" and row1[p3] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p4" and row2[p4] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p5" and row2[p5] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p6" and row2[p6] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p7" and row3[p7] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p8" and row3[p8] == "O" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p9" and row3[p9] == "O" :
                                print("Posição já escolhida")
                                continue


                        elif schoice == "p1" and row1[p1] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p2" and row1[p2] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p3" and row1[p3] == "X":
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p4" and row2[p4] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p5" and row2[p5] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p6" and row2[p6] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p7" and row3[p7] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p8" and row3[p8] == "X" :
                                print("Posição já escolhida")
                                continue

                        elif schoice == "p9" and row3[p9] == "X" :
                                print("Posição já escolhida")

                        else:
                                break

                
                # ESCOLHER ONDE COLOCAR O "O"

                if   schoice == 'p1':
                        row1[p1] = 'O'
                elif schoice == 'p2':
                        row1[p2] = 'O'
                elif schoice == 'p3':
                        row1[p3] = 'O'
                elif schoice == 'p4':
                        row2[p4] = 'O'
                elif schoice == 'p5':
                        row2[p5] = 'O'
                elif schoice == 'p6':
                        row2[p6] = 'O'
                elif schoice == 'p7':
                        row3[p7] = 'O'
                elif schoice == 'p8':
                        row3[p8] = 'O'
                else: 
                        row3[p9] = 'O'
        
        game(row1,row2,row3)
                

def win_condition(XORO):
 

        if XORO == "X":

                #HorizontalLines
                if row1 == ['X','X','X']:
                       print("YOU WIN")
                       replay()

                elif row2 == ['X','X','X']:
                        print("YOU WIN")
                        replay()
                
                elif row3 == ['X','X','X']:
                        print("YOU WIN")
                        replay()
                
                #CrossSection
                elif row1[p1] == "X" and row2[p5] == "X" and row3[p9] == "X":
                        print("YOU WIN")
                        replay()
                
                elif row1[p3] == 'X' and row2[p5] == "X" and row3[p7] == "X":
                        print("YOU WIN")
                        replay()
                
                #VerticalLines
                elif row1[p1] == "X" and row2[p4] == 'X' and row3[p7] == 'X':
                        print("YOU WIN")
                        replay()
                
                elif row1[p2] == "X" and row2[p5] == "X" and row3[p8] == 'X':
                        print("YOU WIN")
                        replay()
                
                elif row1[p3] == 'X' and row2[p6] == 'X' and row3[p9] == 'X':
                        print("YOU WIN")
                        replay()

        if XORO == "O":

                #HorizontalLines
                if row1 == ['O','O','O']:
                       print("YOU WIN")
                       replay()

                elif row2 == ['O','O','O']:
                        print("YOU WIN")
                        replay()
                
                elif row3 == ['O','O','O']:
                        print("YOU WIN")
                        replay()
                
                #CrossSection
                elif row1[p1] == "O" and row2[p5] == "O" and row3[p9] == "O":
                        print("YOU WIN")
                        replay()

                elif row1[p3] == 'O' and row2[p5] == "O" and row3[p7] == "O":
                        print("YOU WIN")
                        replay()
                
                #VerticalLines
                elif row1[p1] == "O" and row2[p4] == 'O' and row3[p7] == 'O':
                        print("YOU WIN")
                        replay()
                
                elif row1[p2] == "O" and row2[p5] == "O" and row3[p8] == 'O':
                        print("YOU WIN")
                        replay()
                
                elif row1[p3] == 'O' and row2[p6] == 'O' and row3[p9] == 'O':
                        print("YOU WIN")
                        replay()


def jogar():

        pos("O")
        pos("X")
        pos("O")

        pos("X")
        win_condition('X')
        pos("O")
        win_condition('O')

        pos("X")
        win_condition('X')
        pos("O")
        win_condition('O')

        pos("X")
        win_condition('X')
        pos("O")
        win_condition('O')
        print("DRAW")

def replay():

        while True:
                choice = input("Do you want to continue playing? Yes or No ---> ")
                if choice.lower().startswith("y"):
                        jogar()
                elif choice.lower().startswith("n"):
                        exit()        

jogar()


        

             



    

    

