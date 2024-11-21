#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    num_guides = int(input("Enter the number of guides selling cookies: "))
    print()
    guides_sold = []
    guides_name = []

    for i in range(num_guides):
        name = input(f"Enter the name of the guide #{i + 1}: ")
        guides_name.append(name)
        boxes_sold = int(input(f"Enter the number of boxs sold by {name}: "))
        guides_sold.append(boxes_sold)
        print()
        
    total_boxes = sum(guides_sold) 
    average_boxes = total_boxes / num_guides
    print()
    print(f"The average number of bixes sold by each guide was {average_boxes:.1f}\n")
    print("Guide\t\tPrizes Won: ")
    print("------------------------------------------------------------")

    max_boxes_sold = max(guides_sold)
    max_boxes_sold_index = guides_sold.index(max_boxes_sold)

    for i in range(num_guides):
        name = guides_name[i]
        boxes_sold = guides_sold[i]

        if i == max_boxes_sold_index:
            prize = "Trip to Girl Guide Jamboree in Aruba!"
        elif boxes_sold == 0:
            prize = " "
        elif boxes_sold > 1 and boxes_sold < average_boxes: 
            prize = "Left over cookies" 
        elif boxes_sold > average_boxes:
            prize = "Super Seller badge"
        else:
            prize = " "

        print(f"{name}\t\t-{prize}")
    
    # YOUR CODE ENDS HERE

main()