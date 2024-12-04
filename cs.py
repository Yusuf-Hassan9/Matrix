import random 

from cc import *
from Cars import *

 ## CAR SCENARIOS - THE MATRIX ##
                 
# Creating car classes

# Make: BMW
# Model: M5 CS F90
# Engine: S63 4.4-liter M TwinPower Turbo V8
# Horsepower: 627 BHP
# Wheel Size: 21 inches 
# Tyres: Bridgestone

Car1 = Car(make = "BMW", model = "M5 Cs F90", engine = "S63 4.4-liter"
          " M TwinPower turbo V8", horse_power=627, wheel_size=21,
         tyre="Bridgestone")

# Make: Mercedes
# Model: C63 AMG W204
# Engine: M156 6.2-liter V8
# Horsepower: 450 BHP 
# Wheel Size: 18 inches 
# Tyres: Michelin

Car2 = Car(make = "Mercedes", model = "C63 AMG W204", engine = "M156 6.2-liter"
          "V8", horse_power=450, wheel_size=18, tyre="Michelin")

# Make: Porsche
# Model: 911 GT3 RS 997
# Engine: 4-litre Boxer 6-cylinder
# Horsepower: 493 BHP 
# Wheel Size: 19 inches
# Tyres: Michelin Pilot Sport Cup 

Car3 = Car(make = "Porsche", model = "911 GT3 RS 997", engine = "4-litre "
           "Boxer 6-cylinder", horse_power=493, wheel_size=19,
          tyre="Michelin Pilot Sport Cup")

# Make: Nissan
# Model: GT-R R35
# Engine: VR38 3.8-liter twin-turbocharged V6 
# Horsepower: 530 BHP 
# Wheel Size: 20 inches 
# Tyres: Michelin (

Car4 = Car(make = "Nissan", model = " GT-R R35", engine = "VR38 3.8-liter"
          " twin-turbocharged V6", horse_power=530,
         wheel_size=20, tyre="Michelin")

# Selecting a car
def scenario():
    print(f"{ai}\n")
    sprint("Choose Your Car Wisely :\n")
    Move7 = input("[A] BMW M5 CS F90\n[B] Mercedes C63 AMG W204\n[c] Porsche"
                 " 911 GT3 RS 997\n[D] Nissan GT-R R35\n\n").lower()
    while True:
            if Move7 == 'a':
                player.car = Car1
                sprint("What a Bavarian Beast!")
                sprint(f"You have Great Taste {player.name}\n")
                break

            elif Move7 == 'b':
                player.car = Car2
                sprint("Cant Go wrong With a C63 ... Right? ...\n")
                sprint("Try not to Spin out \n")
                break
    
            elif Move7 == 'c':
                player.car = Car3
                sprint("Ahh, the Porsche 911 GT3 RS. A true track weapon!\n")
                sprint(f"Excellent choice, {player.name}! It's built for speed"
                      " and precision.\n")
                break

            elif Move7 == 'd':
                player.car = Car4
                sprint("Nissan GT-R R35 Godzilla on wheels!")
                sprint(f"You've chosen raw power, {player.name}. This will help"
                       " you make a"
                       " quick escape.\n")
                break

            else:
                print("Invalid choice. Please select a car from the options.\n")
                Move7 = input("[A] BMW M5 CS F90 \n[B] Mercedes C63 AMG W204 "
                              "\n[c] Porsche 911 GT3 RS 997 \n[D] Nissan GT-R"
                              " R35 \n\n").lower()


    # Getting into the car
    input("Press ENTER to get in your car and continue the mission.\n")
    sprint("Time: 2:45 pm")
    sprint("Location: On route to 12th Ave, Santa Cruz\n")
    player.car.drive(10)
    print(f"{ai}\n")
    sprint(f"You're now driving the {player.car.model}.")
    sprint("You are 349 miles away from The Matrix Base\n")
    sprint(f"'{player.name} watch out there are some Matrix Agents in sedans in"
          " the Area'\n")


    if player.car == Car1:                     # BMW M5 CS F90 Scenario #
        
        sprint("Time: 3:00 pm")
        sprint("Location: The Highway\n")
        sprint("Your now Entering The highway ..., Everything seems fine ...\n")
        sprint(" As soon as you hit the highway, Two dark sedans from the"
              " Matrix agents start tailing you. You punch the gas, and the 627"
              " BHP roars to life.")
        sprint("The Matrix agents are struggling to keep up, but they are"
              " closing in. \n")
        sprint(" Do you:\n")
        Move = input("[A] Floor it and try to outpace them?\n[B] Get off the"
                    " Highway into Backstreets at the next exit and then Try to"
                    " lose them?\n").lower()
        while True:
                if Move == 'a':
                    sprint("Time: 3:20 pm")
                    sprint("Location: On route to 12th Ave, Santa Cruz\n")
                    sprint("You hit 190mph and leave the agents in the dust."
                          " The M5 raw"
                          " power gives you the edge!\n")
                    sprint("Its going to be one nice long road down to"
                          " California\n")
                    player.car.drive(300)
                    break

                elif Move == 'b':
                    sprint("You get off the Highway, turn into the backstreets,"
                          " and thanks"
                          " to the M5 handling, you swiftly lose one of the "
                          "Sedans in the maze of alleys.")
                    player.car.drive(30)
                    sprint("You are feeling Hungry and there is a Supermarket"
                          " Right Next to you, However you know that time is"
                           "the essence.\n")

                    sprint("Do you : \n")
                    Move = input("[A] Go into the Supermarket And Re-Energize?\n"
                                 "[B] Head Back onto the Highway to head to"
                                " Location?\n").lower()

                    while True:
                        if Move == 'a':
                            sprint("I guess someone is Hungry\n")
                            input("Press ENTER to go inside the supermarket\n")
                            player.visit_supermarket()
                            sprint(f"{player.name} Now that you are "
                             "Re-Energized, You now need to continue on with"
                             " your Journey Quickly, However you have 2 route"
                             " options\n")

                            sprint("Do You:")
                            Move =  input("[A] Head Back onto the Highway?\n"
                                          "[B] Take the Backroads\n").lower()
                            while True:
                                    if Move == 'a':
                                        sprint(f"Pretty Good Decision "
                                               f"{player.name}")
                                        sprint("Time: 3:40 pm")
                                        sprint("Location: The Highway\n")
                                        sprint("Its going to be one nice long "
                                               "road down to California\n")
                                        player.car.drive(240)
                                        break

                                    elif Move == 'b':
                                        sprint("I Guess you just love Twist "
                                               "And Turns\n")
                                        sprint("Time: 3:40 pm")
                                        sprint("Location: Backroads\n")
                                        sprint("This is going To be a long "
                                               "trip to California\n")
                                        sprint("Your Fuel is going to take a"
                                              " massive hit for sure\n")
                                        player.car.drive(330)
                                        break

                                    else:
                                        sprint("Invalid Choice, Choose a "
                                               "option!\n")
                                        Move =  input("[A] Head Back onto the"
                                                     " Highway?\n[B] Take the"
                                         " Backroads\n").lower()

                        elif Move == 'b':
                            sprint("The Matrix Agents in sedans Were both "
                                   "waiting"
                                   " for you at the Highway Entrance\n")
                            sprint("You Should have Waited Abit Longer\n")
                            sprint("Mission Failed.")
                            exit()
                        
                        else:
                            sprint("Invalid Choice, Choose a option!\n")
                            Move = input("[A] Go into the Supermarket And "
                                         "Re-Energize?\n[B] Head"
                                 " Back onto the Highway to head to Location?"
                                 "\n").lower()
                else:
                    sprint("Invalid Choice, Choose a option!\n")
                    Move = input("[A] Floor it and try to outpace them?\n[B]"
                                " Get off the Highway into Backstreets at the"
                            " next exit and then Try to lose them?\n").lower()

 

        
    elif player.car == Car2:                   # Mercedes C63 AMG W204 Scenario #
       
        sprint("Time: 3:00 pm")
        sprint("Location: Country Roads\n")
        sprint("You are now entering country roads\n")
        sprint("You are speeding down a narrow country road when a thunderstorm"
              " hits, making the road slippery.")
        sprint("The raw power of your V8 is a bit much for the slick roads, and"
               " you feel the rear end starting to slip.")

        sprint("Do you:")
        Move = input("[A] Ease off the throttle and regain control?\n[B]"
                 " Continue fast around the corners drifting as you know"
                     " that time is the essence\n").lower()
        while True:
                if Move == 'a':
                    sprint("Time: 3:20 pm")
                    sprint("Location: Country Roads\n")
                    sprint("You slow down and regain traction, carefully"
                          " navigating through the storm. Smart move!\n")
                    player.car.drive(200)
                    sprint("You have been Driving through the country roads"
                       " for some time now ... , You look through your rear"
                     " mirrors and see a Dark sedan\n")
                    sprint("You instantly detect the sedan as the Matrix "
                           "Agents Sedan\n")
                    sprint("You now need to Lose the Matrix Agent as the sedan"
                           " begins picking up speed towards you")
                    sprint("You know that the Power of your car can easily lose"
                          " the Sedan on the country roads.\n However there is "
                          "also an exit coming up leading to the Highway.\n")
              
                    sprint("Do you:")
                    Move1 = input("[A] Put your Foot down and try to lose the"
                             " sedan on the country roads?\n[B] Exit onto the"
                             " Highway and try to lose the sedan there?\n"
                             "").lower()
                    while True:
                            if Move1 == 'a':
                                sprint("Time: 5:00 pm")
                                sprint("Location: Unkown\n")
                                print(f"{player.name}:\n")
                                sprint("'OH NO F*Ck!'\n")
                                print(f"{ai}\n")
                                sprint(f"{player.name} you were moving at "
                                 "160mph on the country roads, Whilst the "
                                 "roads were still slippery\n")
                                sprint("Therefore when you came to a harsh turn"
                                      " the C63 Could not cope and slided out;"
                                      " Causing you to Crash into a field\n")
                                sprint("You wake up later, captured by the"
                                       " Matrix Agents\n")
                                sprint("Mission Failed.")
                                exit()

                            elif Move1 == 'b':
                                sprint("Time: 5:20 pm")
                                sprint("Location: Unknown\n")
                                print(f"{ai}\n")
                                sprint(f"Wise Decision {player.name}\n")
                                sprint("You Successfully exited onto the "
                                       "Highway with the Sedan still behind"
                                       " you but abit further\n")
                                sprint("The power of your car then allowed you"
                                  " to easily gap the Sedan by miles, And then"
                                     " continue to California down the Highway"
                                     "\n")
                                player.car.drive(130)
                                break

                            else:
                                sprint("Inavlid choice, Choose a option!\n")
                    break

                elif Move == 'b':
                    sprint("Time: 3:35 pm")
                    sprint("Location: Country Roads\n")
                    sprint("You decide to drift, but the road is too slick!.\n"
                          " you were moving at 160mph on the country roads You"
                          " spin out at a harsh turn into some Fields.\n")
                    sprint("You wake up later, captured by Matrix Agents\n")
                    sprint("Mission Failed.")
                    exit()

                else:
                    sprint("Inavlid choice, Choose a option!\n")
                    Move = input("[A] Ease off the throttle and regain control"
                             "?\n"
                             "[B] Continue fast around the corners drifting as"
                             " you know that time is the essence\n").lower()



        
    elif player.car == Car3:                   # Porsche 911 GT3 RS Scenario #
        
        sprint("Time: 3:00 pm")
        sprint("Location: Downtown, Los Angeles\n")
        sprint("You are still driving in Los Angeles")
        sprint("The city streets are narrow and winding, perfect for the"
         " Porsche 911 GT3 RS, Therefore you are moving at a great speed.\n")
        sprint("You come to a red light and check your mirrors..\n")
        sprint("Suddenly you see 2 Black Drones behind you, You instantly "
               "realise that you are being pursued by Matrix drones.\n")
        sprint("It just got Worse as the Drones are Equipped with Mini Machine"
              " Guns!\n")
        sprint("These Drones are here for the Kill, And you need to escape them"
              " fast!")
        sprint("You hear the whirring of the drones above as you take sharp "
               "corners at full speed.\n")

        print("Do you:\n")
        Move = input("[A] Head towards the highway so that you can try and "
         "outpace them ?\n[B] Stay in the city and look for a Hidden place to "
                    "wait for abit?\n\n").lower()

        while True:
            if Move == 'a':
                sprint("Time: 3:30 pm")
                sprint("Location: The Highway\n")
                sprint("You head towards the highway and press your foot down,"
                      "But the drones lock onto you with ease in the open. They"
                     " are closing in fast!\n")
                sprint("The Drones got close enough and Sprayed down your car "
                       "with the machine guns totally demolishing the tyres.\n")
                sprint("This caused you to spin out at a high speed on the "
                       "Highway ...\n")
                sprint("You Fatally Crashed and Died as the Engine Blew.\n")
                print(f"{ai}\n")
                sprint("'I guess you should Never underestimate Drones'\n")
                sprint("Mission Failed.")
                exit()

            elif Move == 'b':
                sprint("Time: 3:15 pm")
                sprint("Location: Downtown, Los Angeles\n")
                sprint("You stay in the tight city streets.\n using the "
                "Porsche's agility to your advantage, You are able to lose the"
                " drones and find a underground car park of a Supermarket.\n")
                player.car.drive(30)
                sprint("You have Waited in the Underground car park for abit "
                       "\n")
                sprint("You are feeling abit unenergized\n")
                sprint("It is now the right time to leave the Car park and "
                       "Resume with your journey.\n")

                print("Do you: \n")
                Move = input("[A] Go to the supermarket and Re-Energize?\n[B]"
                            " Resume With your Journey?\n").lower()

                while True:
                    if Move == 'a':
                        sprint("Well If you Must\n")
                        input("Press ENTER to go inside the supermarket\n")
                        player.visit_supermarket()
                        sprint(f"{player.name} Now you are Re-Energized, You "
                         "now need to continue on fast with your Journey "
                         "Quickly\n")
                        input("Press ENTER to continue with your journey\n")
                        sprint("Time : 3:25pm ")
                        sprint("Location : The Highway\n")
                        sprint("Your now on the Highway on route to the Matrix"
                               " Base")
                        sprint("Just one Long Road Down to California ....\n")
                        player.car.drive(340)
                        break

                    elif Move == 'b':
                        sprint("Very Well..\n")
                        sprint("Time : 3:10pm ")
                        sprint("Location : The Highway\n")
                        sprint("Your now on the Highway on route to the Matrix"
                               " Base")
                        sprint("Just one Long Road Down to California ....\n")
                        player.car.drive(340)
                        break

                    else:
                        sprint("Invalid Choice, Choose a option!\n")
                        Move = input("[A] Go to the supermarket and Re-Energize"
                                   "?\n[B] Resume With your Journey?\n").lower()

                break

            else:
                sprint("Invalid Choice, Choose a option!\n")
                Move = input("[A] Head towards the highway so that you can try"
                 " and outpace them ?\n[B] Stay in the city and look for a "
                 "Hidden place to wait for abit?\n").lower()




    
    elif player.car == Car4:                   # Nissan GT-R R35 Scenario #
         
        sprint("Time: 3:00 pm")
        sprint("Location: Downtown, Los Angeles\n")
        sprint("You are still driving in Los Angeles\n")
        sprint("You are Making your way towards the Highway and out of the "
               "City.\n")
        sprint("Now you are at a red light, When all of a Sudden you can hear"
              " a loud Buzzing sound.\n")
        sprint("You check your mirrors and then you look outside of your car "
               "...\n")
        print(f"{player.name}:\n")
        sprint("'Oh No What The F*CK'\n")
        print(f"{ai}\n")
        sprint("To your Shock, You have just spotted a Dark Helicopter with "
               "Machine Guns.\n")
        sprint("You instantly Realise that the Helicopter was sent by the "
               "Matrix to Finish you off.\n")
        sprint("You Now have to act fast before you are completely destroyed"
               " by the Machine Guns.\n ")
        sprint("The Nissan GT-Rs launch control catapults you forward as the"
               " helicopter locks onto your position.")
        sprint("You can try and outrun the Helicopter on the Highway.\n "
         "However you could also lose the Helicopter in the city and look for"
         " somewehere to hide for abit.\n")

        print("Do you:\n")
        Move = input("[A] Enter the Highway and then try to outrun the "
         "Helicopter on the Highway?\n[B] Try and lose the Helicopter on the "
         "city streets and Find a place to hide for abit?\n").lower()
        while True:
            if Move == 'a':
              sprint("Time: 3:30 pm")
              sprint("Location: Los Angeles, Near the Highway\n")
              sprint("You head towards the highway and press your foot down, "
                     "But the Helicopter locks onto you with ease in the open!"
                     "\n")
              sprint("The Helicopter got close enough and sprayed down your car"
                    " with the machine guns totally demolishing your tyres.\n")
              sprint("This caused you to spin out at a high speed on the"
                    " Highway...\n")
              sprint("You Fatally Crashed and Died as the Engine Blew.\n")
              print(f"{ai}\n")
              sprint("'I guess you should Never underestimate A Helicopter with"
                     " Machine Guns'\n")
              sprint("Mission Failed.")
              exit()

            elif Move == 'b':
               sprint("Time: 3:15 pm")
               sprint("Location: Downtown, Los Angeles\n")
               sprint("You stay in the tight city streets.\n using the GTRs "
                "Beauty of Drifting corners smoothly, You are able to lose the"
                " Helicopter Eventually and find a underground car park of a "
                "Supermarket.\n")
               player.car.drive(30)
               sprint("You have now Waited in the Underground car park for abit"
                      "\n")
               sprint("You are feeling abit unenergized\n")
               sprint("It is now the right time to leave the Car park and "
                      "Resume with your journey\n")

               print("Do you:\n")
               Move = input("[A] Go to the supermarket and Re-Energize?\n[B] "
                             " Resume With your Journey?\n").lower()
               while True:
                   if Move == 'a':
                       sprint("Well If you Must\n")
                       input("Press ENTER to go inside the supermarket\n")
                       player.visit_supermarket()
                       sprint(f"{player.name} Now you are Re-Energized, You "
                              "now need to"
                              " continue on with your Journey Quickly\n")
                       input("Press ENTER to continue with your journey\n")
                       sprint("Time : 3:25pm ")
                       sprint("Location : The Highway\n")
                       sprint("Your now on the Highway on route to the Matrix "
                              "Base")
                       sprint("Just one Long Road Down to California ....\n")
                       player.car.drive(320)
                       break

                   elif Move == 'b':
                       sprint("Very Well..\n")
                       sprint("Time : 3:10pm ")
                       sprint("Location : The Highway\n")
                       sprint("Your now on the Highway on route to the Matrix"
                              " Base")
                       sprint("Just one Long Road Down to California ....\n")
                       player.car.drive(320)
                       break

                   else:
                        sprint("Invalid Choice, Choose a option!\n")
                        Move = input("[A] Go to the supermarket and Re-Energize"
                                     "?\n"
                                     "[B] Resume With your Journey?\n").lower()
               break

            else:
                 sprint("Invalid Choice, Choose a option!\n")
                 Move = input("[A] Enter the Highway and then try to outrun the"
                             " Helicopter on the Highway?\n[B] Try and lose the"
                             " Helicopter on the city streets and Find a place"
                             " to hide for abit?\n").lower()
