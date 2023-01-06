# Utility Start CSV to HORUS =================================
# Standard Tools
print("Text delimited CSV to HORUS format.")
import pandas as pd
# Input Agreement ============================================
sInputFileName=r"F:\MSC IT\Practical\DS\Prac2\Country_Code.csv"
InputData = pd.read_csv(sInputFileName,encoding="latin-1")
print('Input Data Values ===================================')
print(InputData)
# Processing Rules ===========================================
ProcessData=InputData
# Remove columns ISO-2-Code and ISO-3-CODE
ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-Code',axis=1,inplace=True)
# Rename Country and ISO-M49
ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)
# Set new Index
ProcessData.set_index('CountryName',inplace=True)
# Sort data by CurrencyName
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)
print("**************************************************************************")
print("ProcessData")
print(ProcessData)
OutputData=ProcessData
sOutputFileName =r"F:\MSC IT\Practical\DS\Prac2\HORUSCountry_Code.csv"
OutputData.to_csv(sOutputFileName, index = False)
print('CSV to HORUS - Done')