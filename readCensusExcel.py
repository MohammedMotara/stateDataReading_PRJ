import openpyxl, pprint

print('Opening workbook...')

wb = openpyxl.load_workbook('Automation\pyhtonExampleProjects\stateDataReading_PRJ\censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}
print ('Reading rows...')

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value 
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    #Defining our data structure here
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {  'tracts': 0,
                                            'pop': 0
                                         })

    #incramenting the one census tract 
    countyData[state][county]['tracts'] +=1

    #incramenting the county pop by the population in the tract
    countyData[state][county]['pop'] +=int(pop)

# Writing data to .py file
print('Writing Results...')

resultFile = open('census2020.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')
