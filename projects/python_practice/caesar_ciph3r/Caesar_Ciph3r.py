while True:
    print('''
    .oooooo.                                                          
    d8P'  `Y8b                                                         
    888           .oooo.    .ooooo.   .oooo.o  .oooo.   oooo d8b        
    888          `P  )88b  d88' `88b d88(  "8 `P  )88b  `888""8P        
    888           .oP"888  888ooo888 `"Y88b.   .oP"888   888            
    `88b    ooo  d8(  888  888    .o o.  )88b d8(  888   888            
    `Y8bood8P'  `Y888""8o `Y8bod8P' 8""888P' `Y888""8o d888b           
                                                                        
                                                                        
                                                                        
    .oooooo.                          oooo          .oooo.            
    d8P'  `Y8b                         `888        .dP""Y88b           
    888          oooo    ooo oo.ooooo.   888 .oo.         ]8P' oooo d8b 
    888           `88.  .8'   888' `88b  888P"Y88b      <88b.  `888""8P 
    888            `88..8'    888   888  888   888       `88b.  888     
    `88b    ooo     `888'     888   888  888   888  o.   .88P   888     
    `Y8bood8P'      .8'      888bod8P' o888o o888o `8bd88P'   d888b    
                .o..P'       888                                       
                `Y8P'       o888o                                                                                                       
    ''')

    #variables
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))


    # this function will take the text and shift amount and will return the encrypted text
    def encrypt(original_test, shift_amount):
        cypher_text = ""
        for letter in original_test:
            # we will find the position of the letter in the alphabet and then add the shift amount to it and then we will find the new position of the letter in the alphabet and then we will add the new letter to the cypher text
            shift_position = alphabet.index(letter) + shift_amount
            shift_position = shift_position % len(alphabet)
            cypher_text = cypher_text + alphabet[shift_position]
        print(f"The encoded text is: {cypher_text}")

    # this function will take the text and shift amount and will return the decrypted text
    def decrypt(original_test, shift_amount):
        cypher_text = ""
        for letter in original_test:
            # we are subtracting the shift amount to get the original position of the letter
            shift_position = alphabet.index(letter) - shift_amount
            shift_position = shift_position % len(alphabet)
            cypher_text = cypher_text + alphabet[shift_position]
        print(f"The decoded text is: {cypher_text}")

    # this function will take the text, shift amount and direction and will call the encrypt or decrypt function based on the direction
    def caesar(text, shift, direction):
        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text, shift)
        else:
            print("Invalid direction")

    caesar(text=text, shift=shift, direction=direction)

    # this will ask the user if they want to continue or not
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("Goodbye!")
        break
