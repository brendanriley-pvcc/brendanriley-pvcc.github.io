#Name: Brendan Riley
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195, 250, 350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065, 0.1125)

########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = []

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()

def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in = guest_data.readlines()
    guest_data.close()

#### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))

def perform_calculations():
    global grandtotal
    grandtotal = 0

    for i in range(len(guest)):
        room_type = str(guest[i][2])
        num_nights = int(guest[i][3])

        if room_type == "SR":
            subtotal = ROOM_RATES[0] * num_nights
#STUDENTS: COMPLETE THESE elif AND else statements
        elif room_type == "DR":
            subtotal = ROOM_RATES[1] * num_nights
        else:
            subtotal = ROOM_RATES[2] * num_nights

#STUDENTS: COMPLETE THESE CALCULATIONS        

        salestax = subtotal * TAX_RATES[0]
        occupancy = subtotal * TAX_RATES[1]
        total = subtotal + salestax + occupancy

        grandtotal += total

#STUDENTS: ADD THE REST OF THE append statements after this one  
        guest[i].append(subtotal)
        guest[i].append(salestax)
        guest[i].append(occupancy)
        guest[i].append(total)

def open_out_file():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #7DBEF1; background-image: url(wp-emerald.png); color: #4E8CC2;">\n')

def create_output_html():
    global f

    currency = "8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "8">'
    sp = " "

 #STUDENTS: INSERT ALL THE MISSING f.write STATEMENTS HERE

    f.write('<table border="3" style ="background-color: #DCE9F4; font_family: arial; margin: auto;">\n')
    f.write(colsp + '<h2>EMERALD BEACH HOTEL & RESORT GUEST REPORT<h2></td></tr>')
    f.write(colsp + '<h3>*** Guest Sales Report: ***<h3></td></tr>')
    f.write(tr + 'Last Name' + td + 'First Name' + td + 'Room Type' + td + 'Num Nights' + td + 'Subtotal' + td + 'Sales Tax' + td + 'Occupancy Tax' + td + 'Total' + endtr)

    for g in guest:
        f.write(tr + g[0] + td + g[1] + td + g[2] + td + g[3] + td + format(g[4], currency) + td + format(g[5], currency) + td + format(g[6], currency) + td + format(g[7], currency) + endtr)

    f.write(tr + 'Grand Total' + td + sp + td + sp + td + sp + td + sp + td + sp + td + sp + format(grandtotal, currency) + endtr)

    f.write(colsp + 'Date/Time: ' + day_time + endtr)
    f.write('</table><br />')
    f.write("</body></html>")
    print('Open ' + outfile + ' to view data.')
    f.close()

main()
