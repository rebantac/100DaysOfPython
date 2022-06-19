from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Subject", ["Mathematics", "Physics", "Biology"])
table.add_column("Marks", ["100", "94", "98"])
table.align = "r"
print(table)
