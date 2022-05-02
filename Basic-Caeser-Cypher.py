#basic Caesar Cypher 
class caesar():
    def encode(string, seed):
        result = ""
        for letter in string:
            if letter.islower():
                result += chr((ord(letter)-97+seed)%26+97) #Changes the charater into a number, then takes (97 + the seed) as a = 0 + the seed. Then uses modulus to make sure the number doesn't go over 26
            elif letter.isupper():                         #It then adds 97 and then turns back into a charater
                result += chr((ord(letter)-65+seed)%26+65) #essentially the same as lower but due to ord("A") = 65 instead of ord("a") = 97, we have to take 65
            else:
                result += letter #anything apart from letters i don't encrypyt and just add it to the results
        return result
    def decode(string, seed):
        result = ""
        for letter in string:
            if letter.islower():
                result += chr((ord(letter)-97-seed)%26+97) #essentially the same as encode() but we have to take the seed to get back to the original number
            elif letter.isupper():
                result += chr((ord(letter)-65-seed)%26+65)      
            else:
                result += letter   
        return result
    def prompt_encode():
        message, seed = input("What is the string you want to encrypt: "), input("Caesar up: ")
        try:
            seed = int(seed)
        except (ValueError): #makes sure the the seed is a int and not a string
            print("Have not passed an integar through for seed.")
            exit
        print(caesar.encode(message, seed))
    def prompt_decode():
        message, seed = input("What is the string you want to decrypt: "), input("The amount of letters Caesared up: ")
        try:
            seed = int(seed)
        except (ValueError): #same as prompt_encode()
            print("Have not passed an integar through for seed.")
            exit
        print(caesar.decode(message, seed))
    def promt_encode_decode():#usefull function
        caesar.prompt_encode()
        caesar.prompt_decode()

if __name__ == "__main__": #only runs if the code is run by itself
    caesar.promt_encode_decode()