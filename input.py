import mysql.connector
import pandas as pd
def get_accounts_data(excel_filename="", option=2):
    if option == 1:
        accounts_data = [('1',), ('1.1',), ('1.2',), ('1.2.1',), ('1.2.2',), ('1.3',), ('1.3.1',), ('1.3.1.1',),
                         ('1.3.1.3',)]
        return accounts_data

    else:
        try:
            accounts_data = pd.read_excel(excel_filename)
        except OSError:
            print('Could not read/open file', excel_filename)
        else:
            return accounts_data

        def get_ledger_data(excel_filename="", option=2):
            if option == 1:
                ledger_data = [('1.2.1', 7), ('1.2.2', 8), ('1.1', 1), ('1.2.2', 2), ('1.3.1.3', 10), ('1.3.1.3', 6),
                               ('1.3.1.1', 2), ('1.2.1', 4), ('1.2.1', 1), ('1.3.1.3', 6), ('1.2.1', 9),
                               ('1.3.1.3', 10), ('1.3.1.1', 8), ('1.3.1.3', 9), ('1.1', 1), ('1.3.1.1', 4),
                               ('1.2.2', 7), ('1.3.1.3', 7), ('1.2.1', 10), ('1.2.2', 9)]

                return ledger_data

            else:

                try:
                    ledger_data = pd.read_excel(excel_filename)
                except OSError:
                    print('Could not read/open file', excel_filename)
                else:
                    return ledger_data
