import pandas as pd
import csv
from input import get_ledger_data, get_accounts_data

class TreeNode:
      self.account = account
        self.level = len(account.split('.'))
        self.value = 0
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def fill_values(self, dictionary):
    if len(self.children) == 0:
        self.value = dictionary[self.account]
        # self.parent.value += self.value
    else:
        for child in self.children:
            child.fill_values(dictionary)
            self.value += child.value

    def extract_data(self, dic):
        dic[self.account] = self.value
        if self.children:
            for child in self.children:
                child.extract_data(dic)
def build_tree(accounts_data):
    root = TreeNode("root")

    def evaluate_data(prev, current):
        if prev.level < current.level:
            return prev.add_child(current)
        else:
            evaluate_data(prev.parent, current)

    for i in accounts_data.index:
        myObj = TreeNode(str(accounts_data['account'][i]))

        if myObj.level == 1:
            root.add_child(myObj)
            previous = myObj
        else:
            evaluate_data(previous, myObj)
            previous = myObj

    return root


def calculate_ledger(ledger_data):
    dictx = {}
    for i in ledger_data.index:
        if str(ledger_data['account'][i]) not in dictx:
            dictx[str(ledger_data['account'][i])] = ledger_data['value'][i]
        else:
            # dict[x['account'][i]] = dict.get(x['account'][i]) + x['value'][i]
            dictx[str(ledger_data['account'][i])] += ledger_data['value'][i]

    return dictx


def create_csv(data):
    f = open('chart_of_accounts.csv', "w", newline="")
    writer = csv.writer(f)

    for key in data:
        if key != 'root':
            writer.writerow([key, data[key]])
    f.close()
def build_tree_database(accounts_data):
    root = TreeNode("root")

    def evaluate_data(prev, current):
        if prev.level < current.level:
            return prev.add_child(current)
        else:
            evaluate_data(prev.parent, current)

    for element in accounts_data:
        myObj = TreeNode(str(element[0]))

        if myObj.level == 1:
            root.add_child(myObj)
            previous = myObj
        else:
            evaluate_data(previous, myObj)
            previous = myObj

    return root


def calculate_ledger_database(ledger_data):
    dictx = {}
    for element in ledger_data:
        if str(element[0]) not in dictx:
            dictx[str(element[0])] = element[1]
        else:
            dictx[str(element[0])] += element[1]

    return dictx


def main():
    excel_filename_chartofaccounts = 'chart_of_accounts.xlsx'
    excel_filename_generalledger = 'general_ledger.xlsx'
    option = 2

    if option == 2:
        root = build_tree(get_accounts_data(excel_filename_chartofaccounts, option))
        dictx = calculate_ledger(get_ledger_data(excel_filename_generalledger, option))
        root.fill_values(dictx)
        data = {}
        root.extract_data(data)
        create_csv(data)
    else:
        root = build_tree_database(get_accounts_data(excel_filename_chartofaccounts, option))
        dictx = calculate_ledger_database(get_ledger_data(excel_filename_chartofaccounts, option))
        root.fill_values(dictx)
        data = {}
        root.extract_data(data)
        create_csv(data)


main()