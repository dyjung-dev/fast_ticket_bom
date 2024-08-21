import gspread

# json 파일이 위치한 경로를 값으로 줘야 합니다.
json_file_path = "/home/dyjung/Downloads/fast-ticket-433003-e9462bf1136d.json"
gc = gspread.service_account(json_file_path)
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1mQbPgQ_AjMM84UJfr0n-8xE46Wh5rF2fTueezrQ6O5Y/edit?gid=1669634297#gid=1669634297"
doc = gc.open_by_url(spreadsheet_url)

worksheet = doc.worksheet("Form Responses 1")
val = worksheet.get('A2')
# worksheet.update('a1','자동화 끝!')
print(val)

