## ------------- Import Necessary Library ------------- ##
import pandas as pd
import wikipedia
import string, re, time

## ------------- Data Preparation ------------- ##
excel_words = 'words.xlsx'
ecxcel_word_count = 'word_count.xlsx'

search_input = input(str('Enter your search : ')) # Your search query (Ex: Coronavirus)
raw_data = wikipedia.page(search_input)
raw_data = raw_data.content
filter_data = re.sub('[^A-Za-z]+', ' ', raw_data) # Basic data cleaning

# Save extracted data to text file 'words.txt'
with open('words.txt', 'w', encoding = 'utf8') as output:
    output.write(filter_data)
time.sleep(3)


## ------------- File Reading And Processing------------- ##
file_name = 'words.txt'
file = open(file_name, 'r', encoding = 'utf8')
file_data_raw = file.read()
file.close()
print(f'Text File data :\n {file_data_raw}')


file_data_raw = file_data_raw.lower() # Lower the text
file_data_raw = re.sub('[^A-Za-z]+', ' ',file_data_raw) # Clean data once again after loading from file
data_words_list = file_data_raw.split() # Split into words by white space
print(f'Data after processing :\n {data_words_list}')


## ------------- Excel Automation ------------- ##
data_list = []

# Loop for checking the initial letter of words with alphabets
for data_element in string.ascii_lowercase: # Allow lowercase alphabets
    res = [element for element in data_words_list if element.startswith(data_element)]
    data_list.append(res) 


words = pd.DataFrame(data_list) # Convert list into Dataframe object 
words_data = (words.T) # Transpose the data (converting rows into columns)
words_count = pd.DataFrame(words_data.count()) # Count the occurances
words_count_data = words_count.T # Transpose the data (converting rows into columns)
    
# Save the excel files
words_data.to_excel(excel_words, index = False, header=False, sheet_name='words_alphabets') 
words_count_data.to_excel(ecxcel_word_count, index = False, header=False, sheet_name='words_count')

