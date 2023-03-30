# HL7_App_Functions.py
"""
This file holds several functions for the INF 360 VA Programming with Python Final Project (HL7 Parser App) by Jarrett Smolarkiewicz.
""" 

# The "files_menu()" function:
#     1. Creates a new list assigned to the variable "file_menu" containing each menu option as an item in the list.
#     2. Prints the entire "file_menu" list, with each menu option on a new line.
def files_menu():
    file_select = [
        "[1] message_01.hl7",
        "[2] message_02.hl7",
        "[3] message_03.hl7",
        "[0] Exit Program"]
    print("HL7 MESSAGE SELECT MENU")
    print(*file_select, sep="\n")
    
# The "menu()" function:
#     1. Creates a new list assigned to the variable "main_menu" containing each menu option as an item in the list.
#     2. Prints the entire "main_menu" list, with each menu option on a new line.
def menu():
    main_menu = [
        "[1] View Entire HL7 Message",
        "[2] Message Header",
        "[3] Patient Identification",
        "[4] Lab Order Information",
        "[5] Lab Result Information",
        "[6] Specimen Information",
        "[0] Select Another HL7 Message"]
    print("HL7 MESSAGE PARSER MENU")
    print(*main_menu, sep="\n")

# MAIN MENU OPTION 1: View Entire HL7 Message (There is no pre-defined function for this option. The code is within the "while" statement later in the program.)
# Choosing Option "1" from the Main Menu will display the entire HL7 Message, then display the Main Menu again and prompt the user to make another selection.

# MAIN MENU OPTION 2: Message Header
# The "message_header()" function:
#     1. Creates a new list assigned to the variable "message_header_info" containing a string of only the necessary extracted information from the Message Header segment (MSH).
#     2. Prints the entire "message_header_info" content as a formatted string that is much easier to read and understand.
def message_header(hl7_split):
    message_header_info = [
        "\n" + "Entire Message Header Segment (MSH): " + "\n" + str(segment(hl7_split, "MSH")) + "\n" +
        "\n" + "Sending Facility: " + str(component(hl7_split, "MSH", 4, 1).lower().title()).rjust(18) + 
        "\n" + "Receiving Facility: " + str(component(hl7_split, "MSH", 6, 1)) + "\n" +
        "\n" + "Message Type Information: " + (str(component(hl7_split, "MSH", 9, 3)) + 
            " (Message Structure)").rjust(15) + "\n" + (str(component(hl7_split, "MSH", 9, 1)) + 
            " (Message Code)").rjust(48) + "\n" + (str(component(hl7_split, "MSH", 9, 2)) + " (Trigger Event)").rjust(49) + "\n" +
        "\n" + "Message Version: " + "HL7 v" + str(field(hl7_split, "MSH", 12)) + "\n"]
    print("\n" + "MESSAGE HEADER INFORMATION")
    print(*message_header_info, sep="\n")

# MAIN MENU OPTION 3: Patient Identification
# The "patient_identification()" function:
#     1. Creates a new list assigned to the variable "patient_identification_info" containing a string of only the necessary extracted information from the Patient Identification segment (PID).
#     2. Prints the entire "patient_identification_info" content as a formatted string that is much easier to read and understand.
def patient_identification(hl7_split):
    patient_identification_info = [
        "\n" + "Entire Patient Identification Segment (PID): " + "\n" + str(segment(hl7_split, "PID")) + "\n" + 
        "\n" + "Patient Name: " + str(component(hl7_split, "PID", 5, 2)).rjust(10) + " " + str(component(hl7_split, "PID", 5, 1)) +
        "\n" + "Date of Birth: " + str(field(hl7_split, "PID", 7)[4:6]) + "-" + str(field(hl7_split, "PID", 7)[6:]) + "-" + str(field(hl7_split, "PID", 7)[0:4]) +
        "\n" + "Phone Number: " + "(".rjust(2) + str(component(hl7_split, "PID", 13, 6)) + ") " + str(component(hl7_split, "PID", 13, 7)[0:3]) + "-" + str(component(hl7_split, "PID", 13, 7)[3:]) +
        "\n" + "Address: " + str(component(hl7_split, "PID", 11, 1)).rjust(26) +
        "\n" +  str(component(hl7_split, "PID", 11, 3).lower().title()).rjust(21) + ", " + str(component(hl7_split, "PID", 11, 4)) + " " + str(component(hl7_split, "PID", 11, 5)) + "\n"] 
    print("\n" + "PATIENT IDENTIFICATION INFORMATION")
    print(*patient_identification_info, sep="\n")

# MAIN MENU OPTION 4: Lab Order Information
# The "lab_order()" function:
#     1. Creates a new list assigned to the variable "lab_order_info" containing a string of only the necessary extracted information from the Common Order (ORC) and Observation Request (OBR) segments.
#     2. Prints the entire "lab_order_info" content as a formatted string that is much easier to read and understand.
def lab_order(hl7_split):
    lab_order_info = [
        "\n" + "All Lab Order Segments: " + "\n" + 
        "\n" + "(ORC)" +  
        "\n" + str(segment(hl7_split, "ORC")) + "\n" + 
        "\n" + "(OBR)" +  
        "\n" + str(segment(hl7_split, "OBR")) + "\n" + 
        "\n" + "Ordering Facility Information: " + 
        "\n" + str(component(hl7_split, "ORC", 21, 1)).rjust(26) + 
        "\n" + "(".rjust(3) + str(component(hl7_split, "ORC", 23, 6)) + ") " + str(component(hl7_split, "ORC", 23, 7)[0:3]) + "-" + str(component(hl7_split, "ORC", 23, 7)[3:]) +
        "\n" + str(component(hl7_split, "ORC", 22, 1).lower().title()).rjust(15) + "\n" + str(component(hl7_split, "ORC", 22, 3).lower().title()).rjust(9) + ", " + str(component(hl7_split, "ORC", 22, 4)) + " " + str(component(hl7_split, "ORC", 22, 5)) + "\n" +
        "\n" + "Ordering Provider Information: " + 
        "\n" + str(component(hl7_split, "ORC", 12, 3)).rjust(7) + " " + str(component(hl7_split, "ORC", 12, 2)) +
        "\n" + str(component(hl7_split, "ORC", 12, 13)).rjust(5) + ": " + str(component(hl7_split, "ORC", 12, 1)) +
        "\n" + str(component(hl7_split, "ORC", 24, 1).lower().title()).rjust(15) + "\n" + str(component(hl7_split, "ORC", 24, 3).lower().title()).rjust(9) + ", " + str(component(hl7_split, "ORC", 24, 4)) + " " + str(component(hl7_split, "ORC", 24, 5)) + "\n" +
        "\n" + "Lab Order Information: " +
        "\n" + "Performing Lab: ".rjust(18) + str(component(hl7_split, "OBR", 3, 2).lower().title()).rjust(9) + 
        "\n" + "LOINC: ".rjust(9) + str(component(hl7_split, "OBR", 3, 1)).rjust(35) + 
        "\n" + "Description of Lab: ".rjust(22) + str(component(hl7_split, "OBR", 4, 5).lower().title()).rjust(19) + 
        "\n" + "Date/Time of Lab: ".rjust(20) + str(field(hl7_split, "OBR", 7)[4:6]).rjust(4) + "-" + str(field(hl7_split, "OBR", 7)[6:8]) + "-" + str(field(hl7_split, "OBR", 7)[0:4]) + " " + str(field(hl7_split, "OBR", 7)[8:10]) + ":" + str(field(hl7_split, "OBR", 7)[10:12]) + " UTC" + str(field(hl7_split, "OBR", 7)[12:]) + "\n"]
    print("\n" + "LAB ORDER INFORMATION MENU")
    print(*lab_order_info, sep="\n")

# MAIN MENU OPTION 5: Lab Result Information
# The "lab_results()" function:
#     1. Creates a new list assigned to the variable "lab_result_info" containing a string of the initial Observation Result (OBX) segment, as well as how many total OBX segments are in the message.
#     2. Prints the entire "lab_result_info" content as a formatted string that is much easier to read and understand.
def lab_results(hl7_split):
    lab_result_info = [
        "\n" + "Initial Lab Result Segment (OBX): " + "\n" + str(segment(hl7_split, "OBX")) + "\n" +
        "\n" + "Total Number of Lab Result Segments in Message: " + "\n"]
        # "\n" + "Total Number of Lab Result Segments in Message: " +  str(hl7.count("OBX")) + "\n"]
    print("LAB RESULT INFORMATION MENU")
    print(*lab_result_info, sep="\n")

# MAIN MENU OPTION 6: Specimen Information
# The "specimen()" function:
#     1. Creates a new list assigned to the variable "specimen_info" containing a string of only the necessary extracted information from the Specimen (SPM) segment.
#     2. Prints the entire "specimen_info" content as a formatted string that is much easier to read and understand.
def specimen(hl7_split):
    amp = str(component(hl7_split, "SPM", 2, 2)).find("&")
    specimen_info = [
        "\n" + "Entire Specimen Segment (SPM): " + "\n" + str(segment(hl7_split, "SPM")) + "\n" +
        "\n" + "Specimen Information: " +
        "\n" + "LOINC: ".rjust(9) + str(component(hl7_split, "SPM", 2, 2)[0:amp]).rjust(30) +
        "\n" + "SNOMED: ".rjust(10) + str(component(hl7_split, "SPM", 4, 1)).rjust(23) +
        "\n" + "Type: ".rjust(8) + str(component(hl7_split, "SPM", 4, 2)).rjust(41) + 
        "\n" + "Data/Time Collected: ".rjust(23) + str(field(hl7_split, "SPM", 17)[4:6]).rjust(3) + "-" + str(field(hl7_split, "SPM", 17)[6:8]) + "-" + str(field(hl7_split, "SPM", 17)[0:4]) + " " + str(field(hl7_split, "SPM", 17)[8:10]) + ":" + str(field(hl7_split, "SPM", 17)[10:12]) + " UTC" + str(field(hl7_split, "SPM", 17)[12:]) + "\n"]
    print("SPECIMEN INFORMATION MENU")
    print(*specimen_info, sep="\n")

# MAIN MENU OPTION 0: Exit (There is no pre-defined function for this option. The code is within a "while" statement later in the program.)
# Choosing Option "0" from the Main Menu will exit the HL7 Parser Program.

"""
FUNCTION TO RETURN ALL DATA WITHIN SPECIFIED HL7 SEGMENT(S)
The "segment(hl7_split, header)" function:
    1. Takes two arguments:
            - "hl7_split" is the original HL7 Message, split into segments, using the "\n" character as a delimiter.
            - "header" is a three character string that corresponds to the three character header of the segment(s) being used from the HL7 message.
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
            - "hl7_split" is the original HL7 Message, split into segments, using the "\n" character as a delimiter.
            - "header" is a three character string that corresponds to the three character header of the segment(s) being used from the HL7 message .
            - "field" is a list of items within the segment(s) from the original HL7 Message, split into fields, using the "|" character as a delimiter.
    2. Uses a conditional "if" statement to ensure that if the "MSH" or "Message Header" segment is selected using the function,
       the number passed to the "field" argument reflects the actual number convention for HL7 messages.
    3. Creates a new dictionary and assigns it to the variable "newdict".
    4. Iterates through the HL7 Message segment(s) identified by the "hl7_split" variable using a "for" loop, checking for the "segment" variable.
    5. Assigns the "key" for "newdict" to the first three characters of the selected HL7 message segment(s), which is the segment header.
    6. Assigns the "value" for "newdict" to the characters from position three through the rest of the string in the selected HL7 message segment(s).
    7. Uses another conditional "if" statement to ensure all occurances of a segment header (key), and the segment containing the header(s) (value)
       are included in a new list called "newdict[key]", by checking if they are in the list as the function iterates through the HL7 message.
       This part of the function also further splits the segments by "|" and "^" delimiters whether one or multiple segments are appended to the newly created list.
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
            newdict[key].append([field.split("^") for field in value.split("|")][1:])
            
        else:
            newdict[key].append([field.split("^") for field in value.split("|")][1:])

    return "".join(newdict[header][0][field])

"""
The "component(hl7_split, header, field, component)" function:
    1. Takes four arguments:
            - "hl7_split" is the original HL7 Message, split into segments, using the "\n" character as a delimiter.
            - "header" is a three character string that corresponds to the three character header of the segment(s) being used from the HL7 message .
            - "field" is a list of items within the segment(s) from the original HL7 Message, split into fields, using the "|" character as a delimiter.
            - "component" is a list of items within the field(s) from the original HL7 Message, split into components, using the "^" character as a delimiter.
    2. Uses a conditional "if" statement to ensure that if the "MSH" or "Message Header" segment is selected using the function,
       the number passed to the "field" argument reflects the actual number convention for HL7 messages.
    3. Creates a new dictionary and assigns it to the variable "newdict".
    4. Iterates through the HL7 Message segment(s) identified by the "hl7_split" variable using a "for" loop, checking for the "segment" variable.
    5. Assigns the "key" for "newdict" to the first three characters of the selected HL7 message segment(s), which is the segment header.
    6. Assigns the "value" for "newdict" to the characters from position three through the rest of the string in the selected HL7 message segment(s).
    7. Uses another conditional "if" statement to ensure all occurances of a segment header (key), and the segment containing the header(s) (value)
       are included in a new list called "newdict[key]", by checking if they are in the list as the function iterates through the HL7 message.
       This part of the function also further splits the segments by "|" and "^" delimiters whether one or multiple segments are appended to the newly created list.
    8. Returns only the pieces of the new list (newdict[key]), based on the arguments passed into the function.
    9. This function's arguments are designed to drilldown all the way to the "component" level when returning the result.
"""
def component(hl7_split, header, field, component):
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
            newdict[key].append([field.split("^") for field in value.split("|")][1:]) 
        else:
            newdict[key].append([field.split("^") for field in value.split("|")][1:])

    return newdict[header][0][field][component - 1]

# SANITIZE USER INPUT (Ensures user enters ONLY numbers 0 - 6 as menu items, or else keeps looping through prompt for a valid menu option until they do)
def menuLoop(hl7):
    
    # This part splits the entire HL7 v2.5.1 message assigned to the variable "hl7" into segments that are separated by the "\n" character. 
    hl7_split = hl7.split("\n") 

    while True:
        try:
            # DISPLAY MAIN MENU
            menu()
            option_Menu = input("Enter a number between 0 - 6 for the HL7 message information you would like to view: ")
                        
            # DISPLAY ENTIRE HL7 MESSAGE
            if int(option_Menu) == 1:
                print("\n" + "Entire HL7 Message: " + "\n" + hl7)
                continue
            # DISPLAY RAW MESSAGE HEADER SEGMENT (MSH) FOLLOWED BY NEATLY PRESENTED RELEVANT INFORMATION
            elif int(option_Menu) == 2:
                message_header(hl7_split)
                continue
            # DISPLAY RAW PATIENT IDENTIFICATION SEGMENT (PID) FOLLOWED BY NEATLY PRESENTED RELEVANT INFORMATION
            elif int(option_Menu) == 3:
                patient_identification(hl7_split)
                continue
            elif int(option_Menu) == 4:
                # DISPLAY RAW COMMON ORDER (ORC) AND OBSERVATION RESULT (OBR) SEGMENTS FOLLOWED BY NEATLY PRESENTED RELEVANT LAB ORDER INFORMATION
                lab_order(hl7_split)
                continue
            elif int(option_Menu) == 5:
                # DISPLAY ALL RAW LAB RESULT (OBX) SEGMENTS IN MESSAGE FOLLOWED BY NEATLY PRESENTED RELEVANT LAB RESULT INFORMATION FOR EACH SEGMENT
                lab_results(hl7_split)
                continue
            elif int(option_Menu) == 6:
                # DISPLAY RAW SPECIMEN SEGMENT (SPM) FOLLOWED BY NEATLY PRESENTED RELEVANT SPECIMEN INFORMATION
                specimen(hl7_split)
                continue
            elif int(option_Menu) == 0:
                # DISPLAY MESSAGE TO NOTIFY USER THEY HAVE EXITED THE HL7 PARSER AFTER OPTION "0" SELECTED IN MAIN MENU 
                break             
            else:
                # DISPLAY MAIN MENU AFTER INVALID NUMBER ENTERED
                print("\n" + "Invalid option! You must enter a number between 0 and 6..." + "\n")
                continue
        except:
            print("\n" + "Invalid option! You must enter a number between 0 and 6..." + "\n")
            continue