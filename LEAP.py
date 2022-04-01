import pwd  # import the password database
import grp  # import Unix group database
# import library for easily displaying tabular data
from prettytable import PrettyTable
import argparse  # import command-line parsing module
import socket  # import module provides access to the BSD socket interface
import os  # import os module
import sys  # import sys module to  interact with interpreter variables
import subprocess  # import module to allow to spawn new processes
import shlex  # import to write lexical analyzers for simple syntaxes resembles unix command
try:
    from shlex import quote
except ImportError:
    from pipes import quote

# class definination


class LocalEnum:
    def __init__(self):  # init the constructor
        pass

    # Function to handle elevate
    def elevate(self, show_console=True, graphical=True):
        args = [sys.executable] + sys.argv  # build the argument list
        args.insert(0, "sudo")  # append sudo
        params = ""  # init param
        for arg in args:
            params = params + " " + arg  # build a string param from list args
        # use shellex to convert the string to unix format
        params = shlex.split(params)
        subprocess.call(params)  # call subprocess to relaunch the shell
        return 0

    # Function to list system user with domain name
    def get_system_user_list(self):
        table = PrettyTable()  # init pretty table
        table.field_names = ["User name", "Group Name"]  # group the properties
        group_name = []
        for usr in pwd.getpwall():  # call getpwall and construct the table
            try:
                group_name = grp.getgrgid(usr[3])
            except KeyError:
                pass
            table.add_row([usr[0], group_name[0]])
        print(table)  # print the result
        return table.get_string

    # Function to do the ns_lookup
    def ns_lookup(self, domain_name):
        ip_list = []
        # use socket to look for ns_lookup
        ais = socket.getaddrinfo(domain_name, 0, 0, 0, 0)
        for result in ais:
            ip_list.append(result[-1][0])
        ip_list = list(set(ip_list))
        print(ip_list)  # printt the result
        return ip_list[0]

    # Function for main menu
    def menu(self):
        # get use input
        print("Choose the following options to enumerate system local: ")
        print("Enter '1' to show system users and groups: ")
        print("Enter '2' to show nslookup: ")
        print("Enter '3' to elevate: ")
        self.option = input(": ")
        if self.option == "1":
            self.get_system_user_list()  # if option is 1 go to use list
        if self.option == "2":
            print("Enter the domain name: ")
            domain_name = input(": ")
            self.ns_lookup(domain_name)  # if option is 1 go to domain name
        if self.option == "3":
            self.elevate()


# main method
if __name__ == "__main__":
    localenum = LocalEnum()
    parser = argparse.ArgumentParser()  # use argument parser to build command input
    parser.add_argument("enumerate")
    args = parser.parse_args()
    if args.enumerate:
        localenum.menu()
