# Assignment 2 – Movie Ticket Booking

# Build a complete movie ticket booking program using functions for every operation: listing available shows, booking seats, calculating the total price (including any applicable discounts), and cancelling a booking.
# Requirements:
# •	Write a function list_shows() that displays available movies, show timings, and ticket prices using a list/dictionary of show data. 
# •	Write a function book_tickets(show_name, number_of_tickets, *seat_numbers) that uses variable-length arguments (*args) to accept any number of seat numbers. 
# •	Write a function calculate_total(price, quantity, discount=0) using a default argument for optional discounts. Apply the following payment-based pricing: 
# 	               - GPay : Add ₹30 convenience fee. 
# 	               - Credit Card : Apply 30% discount. 
# 	               - Cash : Use the normal ticket price of ₹230 per ticket. 
# •	Write a recursive function to calculate the total bill when a loyalty combo offer applies cumulative discounts for every 2 tickets booked. 
# •	Write a cancel_booking() function that reverses a booking and issues a refund amount using the same pricing function. 
# •	Tie all functions together in a menu-driven program that lets the user book, view, and cancel tickets.

def list_shows():
    movies={"Sanam Teri Kasam":"1:30 PM","Jigra":"3:30 PM","Alpha":"5:30 PM","Hi":"7:30 PM"}
    print("Available Movies: ")
    for i,j in movies.items():
        print(i,":",j," : 230Rs")
    show_name=input("Enter the movie to be booked:")
    number_of_tickets=int(input("Enter the number of tickets:"))
    seat_numbers=[]
    for i in range(int(number_of_tickets)):
        num=input("enter the seat number")
        seat_numbers.append(num)
    return show_name,number_of_tickets,seat_numbers

def calculate_total(amount) :
    print("Enter the Payment mode: 1.Gpay""\n2.Credit card""\n3.Cash") 
    payment_mode=input()
    print("Payment mode:",payment_mode)
    print("1.Gpay""\n2.Credit card""\n3.Cash")  
    if payment_mode=="1":
        total_amount=amount+30
        print("Convenience Fee: 30")
        print("Total Amount:",total_amount)
    elif payment_mode=="2":
        total_amount = amount - (amount * 30 / 100)
        print("Discount Percentage : 30%")
        print("Total Amount",total_amount)
    else:
        total_amount=amount
        print("Total Amount",total_amount)

    return total_amount     
    
def book_tickets(show_name,number_of_tickets,*seat_numbers,total_amount):
    print(" Movie Ticket Booked for :")
    print("Movie Name:",show_name)
    print("Number of Tickets:",number_of_tickets)
    print("Seat numbers:")
    for i in seat_numbers:
        print(i)
    print("Total Amount:",total_amount)
    price_per_person=total_amount/number_of_tickets
    return price_per_person

def loyalityfn(number_of_tickets):
    if int(number_of_tickets)<2:
        return number_of_tickets*230
    amount = (230 * 2 * 0.90) + loyalityfn(number_of_tickets - 2)   
    return amount    
# amount=loyalityfn(number_of_tickets)

# def calculate_total(amount) :
#     payment_mode=input("Enter the Mode of Payment")
#     print("Payment mode:",payment_mode)
#     print("1.Gpay""\n2.Credit card""\n3.Cash")  
#     if payment_mode=="1":
#         total_amount=amount+30
#         print("Convenience Fee",total_amount)
#     elif payment_mode=="2":
#         total_amount = amount - (amount * 30 / 100)
#         print("Discount Percentage : 30%")
#         print("Total Amount",total_amount)
#     else:
#         total_amount=amount
#         print("Total Amount",total_amount)


#     return total_amount 

# def cancel_ticket():
#     movie_cancelled=input("Enter the movie to be cancelled")
#     no_of_tickets_cancelled=input("enter the number of tickets cancelled")
#     amount_paid=input("Enter the amount paid")
#     print("Ticket Cancelled Succesfully")
#     print("Refund Amount=",amount_paid)
def cancel_ticket(price_per_person):
    no_of_tickets_cancelled=int(input("enter the number of tickets cancelled"))
    print("Ticket Cancelled Succesfully")
    print("Refund Amount=",(no_of_tickets_cancelled*price_per_person))


def menu():
    booking_exists=False
    while(1):
        print("Enter your service to be performed:")
        print("1.Book Ticket")
        print("2.View Booking")
        print("3.Cancel Booking")
        ch=input("Enter the choice")
        if ch=="1":
            show_name,number_of_tickets,seat_numbers=list_shows()
            amount=loyalityfn(number_of_tickets)
            total_amount=calculate_total(amount)
            book_tickets(show_name,number_of_tickets,*seat_numbers,total_amount=total_amount)
            booking_exists=True
        elif ch == "2":
            
            if booking_exists:
                book_tickets(
                    show_name,
                    number_of_tickets,
                    *seat_numbers,
                    total_amount=total_amount
                )
            else:
                print("No booking")
                print("No booking") 
        elif ch=="3":
            price_per_person=book_tickets(show_name,number_of_tickets,*seat_numbers,total_amount=total_amount)
            cancel_ticket(price_per_person)
        else:
            break    
        
menu()            
# show_name,number_of_tickets,seat_numbers=list_shows()
# book_tickets(show_name,number_of_tickets,*seat_numbers)
# amount=loyalityfn(number_of_tickets)


      

