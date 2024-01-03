import json

with open('company_data.json', 'r') as json_file:
    data = json.load(json_file)

company_name = data['company_name']
company_address = data['company_address']
employees = data['employees']

unit_stats = {}
total_employees = len(employees)

for employee in employees:
    unit = employee['unit']
    if unit not in unit_stats:
        unit_stats[unit] = 1
    else:
        unit_stats[unit] += 1

print(f'Tên công ty: {company_name}')
print(f'Địa chỉ: {company_address}')

print('-----Thống kê nhân viên theo đơn vị-----')
for index, (unit, count) in enumerate(unit_stats.items(), start=1):
    percentage = (count / total_employees) * 100
    print(f'{index}./Tên đơn vị: {unit}.')
    print(f'- Số nhân viên: {count}')
    print(f'- Tỷ lệ: {percentage:.2f}%.')

print(f'Tổng số nhân viên: {total_employees}')
