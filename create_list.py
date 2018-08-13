from state_list import get_state_list
from get_state import get_state
import pandas as pds

item = get_state_list()

state_list = get_state_list()

all_list = []

for state in state_list:
    print("Processing %s (%s)..." % (state_list[state], state))
    all_list += get_state(state, state_list[state])

result = pds.DataFrame(all_list, columns=["Name", "Call", "State", "Count"])
result.sort_values("Count", ascending=False, inplace=True)

writer = pds.ExcelWriter("result.xlsx", engine="xlsxwriter")

result.to_excel(writer, freeze_panes=(1, 1), sheet_name="ARRL VE List", index=False)

workbook = writer.book
worksheet = writer.sheets["ARRL VE List"]
worksheet.autofilter("A1:D1")

worksheet.set_column("A:A", 10)
worksheet.set_column("B:B", 25)
worksheet.set_column("C:C", 20)
worksheet.set_column("D:D", 5)

writer.save()
