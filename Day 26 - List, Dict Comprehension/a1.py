import pandas

stud_marks = {
    "name" : ["John", "Curtis", "Frank"],
    "marks" : [56, 45, 87],
}

stud_df = pandas.DataFrame(stud_marks)
print(stud_df)
# To access rows in DF:
for (index, row) in stud_df.iterrows():
    # print(row)
    print(row.name)
