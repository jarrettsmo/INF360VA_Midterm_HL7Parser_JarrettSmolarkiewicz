"""
INF360 VA - Programming with Python
Jarrett Smolarkiewicz
Final Project
GitHub Link: https://github.com/jarrettsmo/INF360VA_Midterm_HL7Parser_JarrettSmolarkiewicz

FINAL GRADING RUBRIC:
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
FINAL TOTAL: 100 Points

FINAL PROJECT OVERVIEW - ALSO SEE EXPANDED FEATURES SECTION BELOW...
I currently work as a software developer at a firm called End Point. The division I am in works with public health clients that need solutions to standardize healthcare data
messages from diverse sources into a unified format that can be understood by the application we market to public health agencies (for conducting public health investigations).

The first part of the standardization process involves taking a healthcare data message in its raw form (like the message below, which is non-sensitive, generic data in HL7 v2.5.1 format),
and searching through it to find only the data that is needed, so that it can be processed by the rest of our application's workflow.

Here is what a raw HL7 v2.5.1 Message looks like... All the delimiter characters (|^~\&) can make this really difficult to understand and work with! 

MSH|^~\&|QLS^2.16.840.1.113883.3.165.2^ISO|QUEST WEST HILLS^05D0642827^CLIA|NV^2.16.840.1.114222.4.3.2.2.3.600.4^ISO|NVDOH^2.54.944.1.447329.0.2.400493^ISO|20220909040419.1651-0700||ORU^R01^ORU_R01|MET-ELRNV60-LV142381S-20220909-20220909 04:04:19.1651|P|2.5.1|||AL|AL|USA||||PHLabReport-Ack^^2.16.840.1.113883.9.11^ISO
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

EXPANDED FEATURES IN FINAL vs. MID-TERM PROJECT 
Mid-Term Version
   * My mid-term project was a basic app that parsed a single HL7 message (the one above), and returned only the data needed in a user-friendly, and much more human readbale format.
   * The mid-term only returned the first instance of all the "OBX" segments in the sample HL7 message above, followed by a count of how many total "OBX" segments are in that HL7 message.

Final Version
   * My final project expands the number of HL7 messages a user can parse through from 1 to 3 messages (all fabricated, non-sensitive data), which are selected by an additional menu.
   * The "HL7 MESSAGE PARSER MENU" returns the data from whichever HL7 message the user selects in the initial menu.
   * All relevant data from each "OBX" segment from the HL7 message the user initially selects is included when option "5" is selected in the "HL7 MESSAGE PARSER MENU".
   * Logging is included, and recorded in a file called "JarrettSmolarkiewiczFinalProject_HL7_App_Logs.txt".
   * The main functions are stored within the additional file called "JarrettSmolarkiewiczFinalProject_HL7_App_Functions.py", and imported at the start of this file, then called as "hl7_fn".
"""
# Importing logging and sys
import logging
import sys
# Imported logging file information
logging.basicConfig(filename='JarrettSmolarkiewiczFinalProject_HL7_App_Logs.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of Program')

# Primary HL7 App functions stored within file called "JarrettSmolarkiewiczFinalProject_HL7_App_Functions.py", and imported here, then called within this app as "hl7_fn".
# If "JarrettSmolarkiewiczFinalProject_HL7_App_Functions.py" is not found, the app will exit and inform the user why this happened, as well as storing it within the log file.
try: 
    import JarrettSmolarkiewiczFinalProject_HL7_App_Functions as hl7_fn
except:
    logging.critical("Missing HL7_App_Functions.py!")
    print("Missing HL7_Files_Menu_Function.py! Exiting the application...")
    sys.exit()

# Importing Path from the Path Library (pathlib)
from pathlib import Path
# This function reads the file selected by the user in the initial app menu.
def readHL7(p):
    fileHL7 = Path(p).read_text()
    return fileHL7
        
################################### Beginning of the HL7 Application... ###################################

while True:
    try:
        # DISPLAY HL7 MESSAGE SELECT MENU
        hl7_fn.files_menu()
        option_File = input("Enter a number between 0 - 2 for the HL7 message file you would like to view: ")
                    
        # SELECT message_01.hl7 FILE AND ASSIGN TO LOCAL VARIABLE hl7, THEN RUN THROUGH hl7_fn.menuLoop(hl7) FUNCTION TO PARSE THE MESSAGE CONTENTS FOR USER 
        if int(option_File) == 1:
            hl7 = readHL7("message_01.hl7")
            hl7_fn.menuLoop(hl7)
            continue
        # SELECT message_02.hl7 FILE AND ASSIGN TO LOCAL VARIABLE hl7, THEN RUN THROUGH hl7_fn.menuLoop(hl7) FUNCTION TO PARSE THE MESSAGE CONTENTS FOR USER 
        elif int(option_File) == 2:
            hl7 = readHL7("message_02.hl7")
            hl7_fn.menuLoop(hl7)
            continue
        # SELECT message_03.hl7 FILE AND ASSIGN TO LOCAL VARIABLE hl7, THEN RUN THROUGH hl7_fn.menuLoop(hl7) FUNCTION TO PARSE THE MESSAGE CONTENTS FOR USER 
        elif int(option_File) == 3:
            hl7 = readHL7("message_03.hl7")
            hl7_fn.menuLoop(hl7)
            continue
        elif int(option_File) == 0:
            # DISPLAY MESSAGE TO NOTIFY USER THEY HAVE EXITED THE HL7 APP AFTER OPTION "0" SELECTED IN MAIN MENU 
            break             
        else:
            # DISPLAY MAIN MENU AFTER INVALID NUMBER ENTERED
            print("\n" + "Invalid option! You must enter a number between 0 and 2..." + "\n")
            continue
    except:
        print("\n" + "Invalid option! You must enter a number between 0 and 2..." + "\n")
        continue

# DISPLAY MESSAGE TO NOTIFY USER THEY HAVE EXITED THE HL7 APP AFTER OPTION "0" SELECTED IN MAIN MENU 
print("You have exited the HL7 Program.")
logging.debug('End of Program')