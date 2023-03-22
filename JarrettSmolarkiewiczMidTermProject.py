"""
INF360 VA - Programming with Python
Jarrett Smolarkiewicz
MidTerm Project
GitHub Link: https://github.com/jarrettsmo/INF360VA_Midterm_HL7Parser_JarrettSmolarkiewicz

MID-TERM GRADING RUBRIC:
---------------------------------------------------------
25 points - Program executes with no errors.
25 points - Program solves a problem or creates something new.
25 points - Program contains:
                - Good flow control.
                - Good use of functions.
                - Code is as clean as possible (smallest amount of code necessary to complete the function).
                - Contains lists or dictionaries.
25 points - Project is well documented (use block and line comments to describe the program as a whole, individual functions, and major areas of the project).
---------------------------------------------------------
MID-TERM TOTAL: 100 Points
"""

"""
PROJECT OVERVIEW
I currently work as a software developer at a software firm called End Point. The division I am in works wityh public health clients that need solutions to standardize healthcare data
messages from diverse sources into a unified format that can be understood by the application we market to public health agencies conducting their investigations.

The first part of the standardization process involves taking a healthcare data message in its raw form (like the message below, which is non-sensitive, generic data in HL7 v2.5.1 format),
and searching through it to find only the data that is needed, so that it can be processed by the rest of our application's workflow.

My mid-term project is a basic app that will parse an HL7 message, and return only the data needed in a user-friendly, and much more human readbale format.
"""
import re
import pprint

"""
This part of the program assigns the ENTIRE HL7 v2.5.1 message to a variable called "hl7" to identify this as the whole message (as a string).
"""
# STEP 1: Paste the HL7 v2.5.1 message below this line:
hl7 = """MSH|^~\&|QLS^2.16.840.1.113883.3.165.2^ISO|QUEST WEST HILLS^05D0642827^CLIA|NV^2.16.840.1.114222.4.3.2.2.3.600.4^ISO|NVDOH^2.54.944.1.447329.0.2.400493^ISO|20220909040419.1651-0700||ORU^R01^ORU_R01|MET-ELRNV60-LV142381S-20220909-20220909 04:04:19.1651|P|2.5.1|||AL|AL|USA||||PHLabReport-Ack^^2.16.840.1.113883.9.11^ISO
PID|1||104417^^^Banner Churchill Community Hospital&29D0539273&CLIA^MR^Banner Churchill Community Hospital&29D0539273&CLIA~12345678987^^^Banner Churchill Community Hospital&29D0539273&CLIA^PI^Banner Churchill Community Hospital&29D0539273&CLIA~XxxXx1234^^^SSN&2.16.840.1.113883.4.1&ISO^SS||LastName^FirstName^MiddleName^^^^L||19791028|M||2106-3^White^CDCREC^309316^White/Caucasian^L^2.5.1|1248 Anywhere Street^^FALLON^NV^89406^USA^C||^PRN^PH^^^775^1234567|||||||||N^Not Hispanic or Latino^HL70189^152116557^Not Hispanic or Latino^L^2.5.1
ORC|RE|04295406G0k6G^QUEST^2.16.840.1.113883.3.165.5^ISO|LV130458S6G0k6G_395QAW^QUEST^2.16.840.1.113883.3.165.4^ISO||CM|||||||1861572679^WATSON^DAVID^^^^^^NPI&2.16.840.1.113883.4.6&ISO^L^^^NPI^^^^^^^^||^^^^^^|||||||DESERT VIEW HOSPITAL-CPU^D|360 S LOLA LN^^PAHRUMP^NV^89048-0884^USA^O|^WPN^PH^^1^775^7517852^^OFFICE CONTACT: BRYAN CURTIS|360 S LOLA LN^^PAHRUMP^NV^89048-0884
OBR|1|04295406G0k6G^QUEST^2.16.840.1.113883.3.165.5^ISO|LV130458S6G0k6G_395QAW^QUEST^2.16.840.1.113883.3.165.4^ISO|^^^395^CULTURE, URINE, ROUTINE^L^^v unknown|||202209061012-0700|||||||||1861572679^WATSON^DAVID^^^^^^NPI&2.16.840.1.113883.4.6&ISO^L^^^NPI^^^^^^^^|^^^^^^|||||20220908143813-0700|||F||||||
OBX|1|CE|43409-2^BACTERIA ISLT CULT^LN^75000300^ISOLATE 1:^L^^v unknown|1|409801009^Klebsiella pneumoniae (ESBL)^SCT^KPESBL^Klebsiella pneumoniae (ESBL)^L|||A^Abnormal (applies to non-numeric results)^HL70078^^^^2.7|||F|||202209061012-0700|29D0652720||||20220908143758-0700||||QUEST DIAGNOSTICS - LAS VEGAS^L^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^29D0652720|4230 BURNHAM AVE^^LAS VEGAS^NV^89119-5408^^L|^IOLE^ELIZABETH^D.^^^^^^^^^^^^^^^^^ MD
NTE|1||KLEBSIELLA PNEUMONIAE (ESBL)
NTE|2||GREATER THAN 100,000 CFU/ML OF
NTE|3||ESBL RESULT: THE ORGANISM HAS BEEN CONFIRMED AS AN ESBL PRODUCER.
OBX|2|NM|18906-8^CIPROFLOXACIN SUSC ISLT^LN^77002706^CIPROFLOXACIN^L^^v unknown|1|2|1^^L||R^Resistant. Indicates for microbiology susceptibilities only.^HL70078^^^^2.7|||F|||202209061012-0700|29D0652720||||20220908143758-0700||||QUEST DIAGNOSTICS - LAS VEGAS^L^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^29D0652720|4230 BURNHAM AVE^^LAS VEGAS^NV^89119-5408^^L|^IOLE^ELIZABETH^D.^^^^^^^^^^^^^^^^^ MD
OBX|3|SN|18932-4^IMIPENEM SUSC ISLT^LN^77003906^IMIPENEM^L^^v unknown|1|<=^0.25|1^^L||S^Susceptible. Indicates for microbiology susceptibilities only.^HL70078^^^^2.7|||F|||202209061012-0700|29D0652720||||20220908143758-0700||||QUEST DIAGNOSTICS - LAS VEGAS^L^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^29D0652720|4230 BURNHAM AVE^^LAS VEGAS^NV^89119-5408^^L|^IOLE^ELIZABETH^D.^^^^^^^^^^^^^^^^^ MD
OBX|4|ST|18878-9^CEFAZOLIN SUSC ISLT^LN^77000906^CEFAZOLIN^L^^v unknown|1|>=64,E127|||R^Resistant. Indicates for microbiology susceptibilities only.^HL70078^^^^2.7|||F|||202209061012-0700|29D0652720||||20220908143758-0700||||QUEST DIAGNOSTICS - LAS VEGAS^L^^^^CLIA&2.16.840.1.113883.4.7&ISO^XX^^^29D0652720|4230 BURNHAM AVE^^LAS VEGAS^NV^89119-5408^^L|^IOLE^ELIZABETH^D.^^^^^^^^^^^^^^^^^ MD
SPM|1|04295406G0k6G&QUEST&2.16.840.1.113883.3.165.5&ISO^LV130458S6G0k6G&QUEST&2.16.840.1.113883.3.165.4&ISO||122575003^Urine specimen (specimen)^SCT^UR^Urine^HL70487^2.5.1^V UNKNOWN^URINE|||||||||||||202209061012-0700|20220906175300-0700
"""
# DO NOT PASTE THE HL7 MESSAGE BELOW THIS LINE!!!
"""
This part of the program assigns each of the non-traditional delimiter characters found in ALL HL7 v2.5.1 messages to a matching variable name, to be utilized later in the program to split up the message into smaller pieces for parsing tasks.
"""
new_line = "\n"
pipe = "|"
tilde = "~"
backslash = "\\"
caret = "^"
ampersand = "&"

"""
This part splits the entire HL7 v2.5.1 message assigned to the variable "hl7" into segments that are separated by the "\n" character, which is assigned to the variable "new_line". 
"""
hl7_split = hl7.split(new_line)

"""
The "___()" function:
    1. Takes ___ argument, which is the result of the "___" function.
    2. Creates a new ___ assigned to the variable "___".
    3. Iterates through the new ___ using a "for" loop, checking for the "___" variable.
    4. Defines the "___" variable as the index of the items in the new ___, and assigns this to the variable "___"
    5. Returns the entire new ___ as a ___ split up into each field of the segment of the original HL7 v2.5.1 message.
"""
"""
def validate_input(menu, menu_prompt):
    print(*menu, sep="\n")
    menu_selection = int(input(menu_prompt))
    #while 0 > menu_selection < (len(menu()) - 1):
    while 0 <= menu_selection <= (len(menu()) - 1):
    #while True:
    #try:
    #    menu_selection = int(input(menu_prompt))
    #except ValueError:
        print("You must enter a number that corresponds with the menu option you'd like to select." + "\n" + "Please enter a valid menu number: ")
        #continue
    else:
        return menu[menu_selection]
        
        #break
    #else:
        #print("else in first while loop")
"""

"""
The "menu()" function:
    1. Creates a new list assigned to the variable "main_menu" containing each menu option as an item in the list.
    2. Prints the entire "main_menu" list, with each menu option on a new line.
"""
def menu():
    main_menu = [
        "[1] View Entire HL7 Message",
        "[2] Message Header",
        "[3] Patient Identification",
        "[4] Lab Order Information",
        "[5] Lab Result Information",
        "[6] Specimen Information",
        "[0] Exit"]
    print("HL7 PARSER MAIN MENU")
    print(*main_menu, sep="\n")

# MAIN MENU OPTION 1: View Entire HL7 Message (There is no pre-defined function for this option. The code is within a "while" statement later in the program.)
# Choosing Option "1" from the Main Menu will display the entire HL7 Message, then display the Main Menu again and prompt the user to make another selection.

"""
MAIN MENU OPTION 2: Message HeaderMessage Header
The "menu_Message_Header()" function:
    1. Creates a new list assigned to the variable "message_header_menu" containing each menu option as an item in the list.
    2. Prints the entire "message_header_menu" list, with each menu option on a new line.
"""
def menu_Message_Header():
    message_header_menu = [
        "[1] View Entire Message Header Segment",
        "[2] Sending Facility",
        "[3] Receiving Facility",
        "[4] Message Type Information",
        "[5] HL7 Message Version",
        "[0] Back to Main Menu"]
    print("MESSAGE HEADER MENU")
    print(*message_header_menu, sep="\n")

"""
MAIN MENU OPTION 3: Patient Identification
The "menu_Patient_Identification()" function:
    1. Creates a new list assigned to the variable "patient_identification_menu" containing each menu option as an item in the list.
    2. Prints the entire "patient_identification_menu" list, with each menu option on a new line.
"""
def menu_Patient_Identification():
    patient_identification_menu = [
        "[1] View Entire Patient Identification Segment",
        "[2] Patient Name",
        "[3] Patient Date of Birth",
        "[4] Patient Address",
        "[5] Patient Phone Number",
        "[0] Back to Main Menu"]
    print("PATIENT IDENTIFICATION MENU")
    print(*patient_identification_menu, sep="\n")

"""
MAIN MENU OPTION 4: Lab Order Information
The "menu_Lab_Order()" function:
    1. Creates a new list assigned to the variable "lab_order_menu" containing each menu option as an item in the list.
    2. Prints the entire "lab_order_menu" list, with each menu option on a new line.
"""
def menu_Lab_Order():
    lab_order_menu = [
        "[1] View All Lab Order Segments",
        "[2] Ordering Facility Information",
        "[3] Ordering Provider Information",
        "[4] Lab Order Information",
        "[0] Back to Main Menu"]
    print("LAB ORDER INFORMATION MENU")
    print(*lab_order_menu, sep="\n")

"""
MAIN MENU OPTION 5: Lab Result Information
The "menu_Lab_Result()" function:
    1. Creates a new list assigned to the variable "lab_result_menu" containing each menu option as an item in the list.
    2. Prints the entire "lab_result_menu" list, with each menu option on a new line.
"""
def menu_Lab_Result():
    lab_result_menu = [
        "[1] View All Lab Result Segments",
        "[2] Lab Results",
        "[0] Back to Main Menu"]
    print("LAB RESULT INFORMATION MENU")
    print(*lab_result_menu, sep="\n")

"""
MAIN MENU OPTION 6: Specimen Information
The "menu_Specimen()" function:
    1. Creates a new list assigned to the variable "specimen_menu" containing each menu option as an item in the list.
    2. Prints the entire "specimen_menu" list, with each menu option on a new line.
"""
def menu_Specimen():
    specimen_menu = [
        "[1] View Entire Specimen Segment",
        "[2] Specimen Information",
        "[0] Back to Main Menu"]
    print("SPECIMEN INFORMATION MENU")
    print(*specimen_menu, sep="\n")

# MAIN MENU OPTION 0: Exit (There is no pre-defined function for this option. The code is within a "while" statement later in the program.)
# Choosing Option "0" from the Main Menu will exit the HL7 Parser Program.

"""
FUNCTION TO RETURN ALL DATA WITHIN SPECIFIED HL7 SEGMENT(S)
The "segment(hl7_split, header)" function:
    1. Takes two arguments:
            - "hl7_split" is the original HL7 Message, split into segments, using the "new_line" character as a delimiter.
            - "header" is a three character string that corresponds to the three character header of the segment(s) being used from the HL7 message .
    2. Creates a new dictionary and assigns it to the variable "newdict".
    3. Iterates through the HL7 Message segment(s) identified by the "hl7_split" variable using a "for" loop, checking for the "segment" variable.
    4. Assigns the "key" for "newdict" to the first three characters of the selected HL7 message segment(s), which is the segment header.
    5. Assigns the "value" for "newdict" to the characters from position three through the rest of the string in the selected HL7 message segment(s).
    6. Uses a conditional "if" statement to ensure all occurances of a segment header (key), and the segment containing the header(s) (value)
       are included in a new list called "newdict[key]", by checking if they are in the list as the function iterates through the HL7 message.
       This part of the function also appends one or multiple segments to the newly created list.
    7. Returns all occurences of segment(s) (value) paired with the segment header (key) in the new list (newdict[key]) as a string, based on the arguments passed into the function.
    8. This function's arguments are designed to include the entire "segment" when returning the result. The "header" is re-attached when returning the result.
"""
def segment(hl7_split, header):
    newdict = {}
    for segment in hl7_split:
        key = segment[0:3]
        value = segment[3:]

        if key not in newdict:
            newdict[key] = []
            newdict[key].append(value)
            
        else:
            newdict[key].append(value)

    return header + newdict[header][0]

"""
FUNCTION TO RETURN DATA WITHIN A SPECIFIED FIELD WITHIN SPECIFIED HL7 SEGMENT(S)
The "field(hl7_split, header, field)" function:
    1. Takes three arguments:
            - "hl7_split" is the original HL7 Message, split into segments, using the "new_line" character as a delimiter.
            - "header" is a three character string that corresponds to the three character header of the segment(s) being used from the HL7 message .
            - "field" is a list of items within the segment(s) from the original HL7 Message, split into fields, using the "caret" character as a delimiter.
    2. Uses a conditional "if" statement to ensure that if the "MSH" or "Message Header" segment is selected using the function,
       the number passed to the "field" argument reflects the actual number convention for HL7 messages.
    3. Creates a new dictionary and assigns it to the variable "newdict".
    4. Iterates through the HL7 Message segment(s) identified by the "hl7_split" variable using a "for" loop, checking for the "segment" variable.
    5. Assigns the "key" for "newdict" to the first three characters of the selected HL7 message segment(s), which is the segment header.
    6. Assigns the "value" for "newdict" to the characters from position three through the rest of the string in the selected HL7 message segment(s).
    7. Uses another conditional "if" statement to ensure all occurances of a segment header (key), and the segment containing the header(s) (value)
       are included in a new list called "newdict[key]", by checking if they are in the list as the function iterates through the HL7 message.
       This part of the function also further splits the segments by "pipe" and "caret" delimiters whether one or multiple segments are appended to the newly created list.
    8. Returns only the pieces of the new list (newdict[key]) as a string, based on the arguments passed into the function.
    9. This function's arguments are designed to drilldown only to the "field" level when returning the result.
"""
def field(hl7_split, header, field):
    if header == "MSH":
        field = field - 2
    else:
        field = field - 1
        
    newdict = {}
    for segment in hl7_split:
        key = segment[0:3]
        value = segment[3:]

        if key not in newdict:
            newdict[key] = []
            newdict[key].append([field.split(caret) for field in value.split(pipe)][1:])
            
        else:
            newdict[key].append([field.split(caret) for field in value.split(pipe)][1:])

    return "".join(newdict[header][0][field])

"""
The "field(hl7_split, header, field)" function:
    1. Takes three arguments:
            - "hl7_split" is the original HL7 Message, split into segments, using the "new_line" character as a delimiter.
            - "header" is a three character string that corresponds to the three character header of the segment(s) being used from the HL7 message .
            - "field" is a list of items within the segment(s) from the original HL7 Message, split into fields, using the "caret" character as a delimiter.
    2. Uses a conditional "if" statement to ensure that if the "MSH" or "Message Header" segment is selected using the function,
       the number passed to the "field" argument reflects the actual number convention for HL7 messages.
    3. Creates a new dictionary and assigns it to the variable "newdict".
    4. Iterates through the HL7 Message segment(s) identified by the "hl7_split" variable using a "for" loop, checking for the "segment" variable.
    5. Assigns the "key" for "newdict" to the first three characters of the selected HL7 message segment(s), which is the segment header.
    6. Assigns the "value" for "newdict" to the characters from position three through the rest of the string in the selected HL7 message segment(s).
    7. Uses another conditional "if" statement to ensure all occurances of a segment header (key), and the segment containing the header(s) (value)
       are included in a new list called "newdict[key]", by checking if they are in the list as the function iterates through the HL7 message.
       This part of the function also further splits the segments by "pipe" and "caret" delimiters whether one or multiple segments are appended to the newly created list.
    8. Returns only the pieces of the new list (newdict[key]), based on the arguments passed into the function.
    9. This function's arguments are designed to drilldown all the way to the "field_separator" level when returning the result.
"""
def field_separator(hl7_split, header, field, field_separator):
    if header == "MSH":
        field = field - 2
    else:
        field = field - 1
        
    newdict = {}
    for segment in hl7_split:
        key = segment[0:3]
        value = segment[3:]
        
        if key not in newdict:
            newdict[key] = []
            newdict[key].append([field.split(caret) for field in value.split(pipe)][1:]) 
        else:
            newdict[key].append([field.split(caret) for field in value.split(pipe)][1:])

    return newdict[header][0][field][field_separator - 1]

"""
Beginning of HL7 Application...
"""
try:
    # DISPLAY MAIN MENU
    menu()
    option_Menu = int(input("Enter a number for the message section you would like to view: "))
    #print(len(menu()) - 1)
    #option_Menu = validate_input(menu(), "Enter a number for the message section you would like to view: ")
except:
    # DISPLAY MAIN MENU AFTER INVALID NUMBER ENTERED
    print("\n" + "Invalid option! You must enter a number between 1 and 6..." + "\n")
    menu()
    option_Menu = int(input("Enter a number for the message section you would like to view: "))

"""
Main Menu of HL7 Application...
"""
# Entering "0" breaks out of the while loop, prints: "You have exited the HL7 Program." and then exits the program.
while option_Menu != 0: 
    if option_Menu == 1:
        # DISPLAY ENTIRE HL7 MESSAGE
        print("\n" + "Entire HL7 Message: " + "\n" + hl7)

        # DISPLAY MAIN MENU AFTER DISPLAYING ENTIRE HL7 MESSAGE 
        menu()
        option_Menu = int(input("Enter a number for the message section you would like to view: "))

    elif option_Menu == 2:
        # DISPLAY MESSAGE HEADER MENU
        print() # Added for one line of space between menus...
        menu_Message_Header()
        option_Message_Header = int(input("Enter a number for the Message Header information you would like to view: "))

        # Entering "0" breaks out of the while loop, prints the main menu options, then prompts the user to select an option from the main menu.
        while option_Message_Header != 0:
            if option_Message_Header == 1:
                print("\n" + "Entire Message Header Segment (MSH): " + "\n" + str(segment(hl7_split, "MSH")) + "\n")
            elif option_Message_Header == 2:
                print("\n" + "Sending Facility: " + str(field_separator(hl7_split, "MSH", 4, 1)) + "\n")
            elif option_Message_Header == 3:
                print("\n" + "Receiving Facility: " + str(field_separator(hl7_split, "MSH", 6, 1)) + "\n")
            elif option_Message_Header == 4:
                print("\n" + "Message Type Information: " + (str(field_separator(hl7_split, "MSH", 9, 3)) + " (Message Structure)").rjust(15) + "\n" + (str(field_separator(hl7_split, "MSH", 9, 1)) + " (Message Code)").rjust(48) + "\n" + (str(field_separator(hl7_split, "MSH", 9, 2)) + " (Trigger Event)").rjust(49) + "\n")
            elif option_Message_Header == 5:
                print("\n" + "Message Version: " + "HL7 v" + str(field(hl7_split, "MSH", 12)) + "\n")
            else:
                print("\n" + "Please enter a valid option.")

            # DISPLAY MESSAGE HEADER MENU AFTER RESULT OF LAST MENU SELECTION
            menu_Message_Header()
            option_Message_Header = int(input("Enter a number for the corresponding Message Header information: "))
        else:
            # DISPLAY MAIN MENU AFTER OPTION "0" SELECTED IN PREVIOUS MENU TO GO BACK
            print() # Added for one line of space between menus...
            menu()
            option_Menu = int(input("Enter a number for the message section you would like to view: "))

    elif option_Menu == 3:
        # DISPLAY PATIENT IDENTIFICATION MENU
        print() # Added for one line of space between menus...
        menu_Patient_Identification()
        option_Patient_Identification = int(input("Enter a number for the Patient Identification information you would like to view: "))
        
        # Entering "0" breaks out of the while loop, prints the main menu options, then prompts the user to select an option from the main menu.
        while option_Patient_Identification != 0:
            if option_Patient_Identification == 1:
                print("\n" + "Entire Patient Identification Segment (PID): " + "\n" + str(segment(hl7_split, "PID")) + "\n")
            elif option_Patient_Identification == 2:
                print("\n" + "2" + "\n")
            elif option_Patient_Identification == 3:
                print("\n" + "3" + "\n")
            elif option_Patient_Identification == 4:
                print("\n" + "4" + "\n")
            elif option_Patient_Identification == 5:
                print("\n" + "5" + "\n")
            else:
                print("\n" + "Please enter a valid option.")

            # DISPLAY PATIENT IDENTIFICATION MENU AFTER RESULT OF LAST MENU SELECTION
            menu_Patient_Identification()
            option_Patient_Identification = int(input("Enter a number for the corresponding Patient Identification information: "))
        else:
            # DISPLAY MAIN MENU AFTER OPTION "0" SELECTED IN PREVIOUS MENU TO GO BACK
            print() # Added for one line of space between menus...
            menu()
            option_Menu = int(input("Enter a number for the message section you would like to view: "))

    elif option_Menu == 4:
        # DISPLAY LAB ORDER MENU
        print() # Added for one line of space between menus...
        menu_Lab_Order()
        option_Lab_Order = int(input("Enter a number for the Lab Order information you would like to view: "))
        
        # Entering "0" breaks out of the while loop, prints the main menu options, then prompts the user to select an option from the main menu.
        while option_Lab_Order != 0:
            if option_Lab_Order == 1:
                print("\n" + "Entire Common Order Segment (ORC): " + "\n" + str(segment(hl7_split, "ORC")))
                print("\n" + "Entire Observation Request Segment (OBR): " + "\n" + str(segment(hl7_split, "OBR")) + "\n")
            elif option_Lab_Order == 2:
                print("\n" + "2" + "\n")
            elif option_Lab_Order == 3:
                print("\n" + "3" + "\n")
            elif option_Lab_Order == 4:
                print("\n" + "4" + "\n")
            else:
                print("\n" + "Please enter a valid option.")

            # DISPLAY LAB ORDER MENU AFTER RESULT OF LAST MENU SELECTION
            menu_Lab_Order()
            option_Lab_Order = int(input("Enter a number for the corresponding Lab Order information: "))
        else:
            # DISPLAY MAIN MENU AFTER OPTION "0" SELECTED IN PREVIOUS MENU TO GO BACK
            print() # Added for one line of space between menus...
            menu()
            option_Menu = int(input("Enter a number for the message section you would like to view: "))

    elif option_Menu == 5:
        # DISPLAY LAB RESULT MENU
        print() # Added for one line of space between menus...
        menu_Lab_Result()
        option_Lab_Result = int(input("Enter a number for the Lab Result information you would like to view: "))
        
        # Entering "0" breaks out of the while loop, prints the main menu options, then prompts the user to select an option from the main menu.
        while option_Lab_Result != 0:
            if option_Lab_Result == 1:
                print("\n" + "1" + "\n")
                #print("\n" + "Entire Observation/Result Segment (OBX) - All Occurences: " + "\n" + str(segment(hl7_split, "OBX")) + "\n")
                #print("\n" + "Entire Observation/Result Segment (OBX) - All Occurences: " + "\n" +  + "\n")
                #print("\n" + "Entire Observation/Result Segment (OBX) - All Occurences: " + "\n" + re.findall(str(segment(hl7_split, "OBX")), str(hl7_split)) + "\n")
                #print("\n" + "Entire Observation/Result Segment (OBX) - All Occurences: ")
                #print(segment(hl7_split, "OBX")[0:3])
                #print(hl7_split[0:3])
                #print(str(hl7_split.count("OBX")))
                #print(len(re.findall("OBX", str(hl7_split))))
                #for "OBX" in range(len(hl7_split)):
                    #print(hl7_split["OBX"])
            elif option_Lab_Result == 2:
                print("\n" + "2" + "\n")
            else:
                print("\n" + "Please enter a valid option.")

            # DISPLAY LAB RESULT MENU AFTER RESULT OF LAST MENU SELECTION
            menu_Lab_Result()
            option_Lab_Result = int(input("Enter a number for the corresponding Lab Result information: "))
        else:
            # DISPLAY MAIN MENU AFTER OPTION "0" SELECTED IN PREVIOUS MENU TO GO BACK
            print() # Added for one line of space between menus...
            menu()
            option_Menu = int(input("Enter a number for the message section you would like to view: "))

    elif option_Menu == 6:
        # DISPLAY SPECIMEN MENU
        print() # Added for one line of space between menus...
        menu_Specimen()
        option_Specimen = int(input("Enter a number for the Specimen information you would like to view: "))
        
        # Entering "0" breaks out of the while loop, prints the main menu options, then prompts the user to select an option from the main menu.
        while option_Specimen != 0:
            if option_Specimen == 1:
                print("\n" + "Entire Specimen Segment (SPM): " + "\n" + str(segment(hl7_split, "SPM")) + "\n")
            elif option_Specimen == 2:
                print("\n" + "2" + "\n")
            elif option_Specimen == 3:
                print("\n" + "3" + "\n")
            elif option_Specimen == 4:
                print("\n" + "4" + "\n")
            elif option_Specimen == 5:
                print("\n" + "5" + "\n")
            else:
                print("\n" + "Please enter a valid option.")

            # DISPLAY SPECIMEN MENU AFTER RESULT OF LAST MENU SELECTION
            menu_Specimen()
            option_Specimen = int(input("Enter a number for the corresponding Specimen information: "))
        else:
            # DISPLAY MAIN MENU AFTER OPTION "0" SELECTED IN PREVIOUS MENU TO GO BACK
            print() # Added for one line of space between menus...
            menu()
            option_Menu = int(input("Enter a number for the message section you would like to view: "))
    else:
        # DISPLAY MAIN MENU AFTER INVALID NUMBER ENTERED
        print("\n" + "Invalid option! You must enter a number between 1 and 6..." + "\n")
        menu()
        option_Menu = int(input("Enter a number for the message section you would like to view: "))    
else:
    # DISPLAY MAIN MENU AFTER OPTION "0" SELECTED IN PREVIOUS MENU TO GO BACK
    menu()
    option_Menu = int(input("Enter a number for the message section you would like to view: "))

# DISPLAY MESSAGE TO NOTIFY USER THEY HAVE EXITED THE HL7 PARSER AFTER OPTION "0" SELECTED IN MAIN MENU 
print("You have exited the HL7 Program.")

"""
The "hl7_segments(hl7_split)" function:
    1. Takes one argument, which is the variable "hl7_split".
    2. Creates a new dictionary assigned to the variable "hl7_dictionary".
    3. Iterates through the new dictionary using a "for" loop, checking for the "segment" variable.
    4. Defines the "segment" variable as the index of the items in the new dictionary, and assigns this to the variable "segment_split"
    5. Returns the entire new dictionary as a list split up into each segment of the original HL7 v2.5.1 message.
"""
"""
def hl7_segments(hl7_split):
    hl7_dictionary = dict(hl7 = hl7_split)
    for segment in hl7_dictionary:
        segment_split = hl7_dictionary[segment]
        
    #print(segment_split)
    #return segment_split
    print(hl7_dictionary)

# Assigns a variable "x" to call the hl7_segments(hl7_split) function.
hl7_segments(hl7_split)
"""
"""
def segment(hl7_split):
    newdict = {}
    for line in hl7_split:
        if line[0:3] not in newdict:
            newdict[line[0:3]] = []
            newdict[line[0:3]].append(line[3:])
        else:
            newdict[line[0:3]].append(line[3:])
            
    #pprint.pprint(newdict)
    pprint.pprint(newdict)

segment(hl7_split)

def segment(hl7_split):
    newdict = {}
    for segment in hl7_split:
        key = segment[0:3]
        value = segment[3:]

        if key not in newdict:
            newdict[key] = []
            newdict[key].append([field.split(caret) for field in value.split(pipe)][1:])
            
        else:
            newdict[key].append([field.split(caret) for field in value.split(pipe)][1:])

    #print(newdict["MSH"][0][2][0])
    return newdict["MSH"][0][2][0]
"""

"""
The "hl7_fields(hl7_segments(hl7_split))" function:
    1. Takes one argument, which is the result of the "hl7_segments(hl7_split)" function.
    2. Creates a new list assigned to the variable "segment_list".
    3. Iterates through the new list using a "for" loop, checking for the "field" variable.
    4. Defines the "field" variable as the index of the items in the new list, and assigns this to the variable "field_split"
    5. Returns the entire new list as a list split up into each field of the segment of the original HL7 v2.5.1 message.
"""
"""
def hl7_fields(x):
    x_split = x.split(pipe)
    segment_list = list(x_split)
    for field in segment_list:
        field_split = segment_list[field]
        
    print(field_split)
    #return field_split

# Call the hl7_fields(hl7_segments(hl7_split)) function.
hl7_fields(x)
"""
"""
segment_split = hl7.split(new_line)

hl7_dictionary = dict(hl7 = hl7_split)
for segment in hl7_dictionary:
    segment_split = hl7_dictionary[segment]
# convert to "return" instead of "print"
print(segment_split)


msh = hl7_split[0]
#pid = hl7_split[1]

msh_split = msh.split(pipe)
field = msh_split[3]

field_split = field.split(caret)
target = field_split[0]

#print(field)
#print(field_split)

#newdict = dict(hl7 = msh_split)
#print(newdict)

#newdict = dict(msh = msh_split)
#print(newdict)

#newdict = dict(field = field_split)
#print(newdict)

#print(target)
#print(*msh_split, sep="\n")
"""
"""
#, sep=new_line + new_line
for x in hl7_split:
    hl7_split[x] = segment
    
segment_split = segment.split(pipe)

#print(*hl7_split, sep="\n")
#print(*pid.split("|"), sep="\n")
#print(*pid.split("|"), sep="\n")

# print(testing.index("MSH"))
# print(testing.index("PID"))
# print(testing.index("SPM"))

# for y in testing:
#    y = testing.index("\n")
#    print(y)
"""
