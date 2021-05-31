import csv, os, logging
from logging.handlers import RotatingFileHandler
my_handler = RotatingFileHandler("./actimize_append.log", mode='a', encoding=None, delay=0)
my_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(funcName)s (%(lineno)d) %(message)s'))
l = logging.getLogger(__name__)
l.setLevel("INFO")
l.addHandler(my_handler)
# l.addHandler(logging.StreamHandler())
l.info("Script initialized")


def modify_txn(src_file, dest_file):
    file = open(src_file)
    csv_data = csv.reader(file, delimiter='|')
    dfile = open(dest_file, 'w+')
    writer = csv.writer(dfile, delimiter='|')
    writer.writerow(next(csv_data))  # Write the first row (header) as is
    
    pod1_substring = 'THERE_WAS_SOMETHING_HERE'
    valid_txn_codes = ['LOL', 'OMG', 'WTF',
                      'LMAO', 'TITS', 'GREAT']
                      
    for row in csv_data:
        if row[1].startswith(pod1_substring): # if ACCOUNT_KEY starts with pod1 ID
            l.info("txn ID: " + row[0] +  " has ACCOUNT_KEY start with pod1 ID: (" + row[1] + ")")
            continue # Skip this TXN ID
        if row[7].startswith(pod1_substring): # if OPP_ACCOUNT_KEY starts with pod1 ID
            l.info("txn ID: " + row[0] +  " has OPP_ACCOUNT_KEY start with pod1 ID: (" + row[7] + ")")
            continue # Skip this TXN ID
        if row[15] not in valid_txn_codes: # Check if TXN has valid TXN code
            l.info("txn ID: " + row[0] +  " txn code not valid: " + row[15])
            continue # Skip this TXN ID
        row[0] = row[0] + 'a' # Append A to the TXN ID
        
        writer.writerow(row) # Write this row to the new file
        
        
def main_function():
    src_file = "./POD02_TRANSACTIONS_V2_FULL.DAT"
    dest_file = "./POD02_TRANSACTIONS_V2_FULL.DAT.processed"
    modify_txn(src_file=src_file, dest_file=dest_file)
    
    
main_function()
