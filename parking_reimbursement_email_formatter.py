#pretty printing my parking expense

file_name = "tdm.txt"

#template message format with insertion index for payment information
msg = ["Hello,",
       "I was hoping I could make a request for parking reimbursement. I included a link to a google drive with screenshots of each transaction as it looks in my online banking statement but below I also included a listing of each transaction that I'm requesting for.",
       "Thank you so much for your help!",
       "-Joe Griffin"]
insert_index = 2

#getting payment information from file
with open(file_name) as file:
    payment_file = file.readlines()

#removing new lines (i don't know a more efficient way of doing this)
for i in range(len(payment_file)):
    if payment_file[i].endswith("\n"):
        payment_file[i] = payment_file[i][:-2]
        
#dense message reformatting
payment_file.insert(0,""),payment_file.append("") #inserting newline prints
msg_split1,msg_split2 = msg[:insert_index],msg[insert_index:] #splitting the message at the specified index
[print(x) for x in msg_split1+payment_file+msg_split2] #reconnecting and printing the whole message with the payment information in between.