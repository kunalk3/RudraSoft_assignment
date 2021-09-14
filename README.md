## RudraSoft_assignment
Words count with alphabetical bucket, Extracting data from wikipedia and write to excel with words start with alphabets and count

## Problem statement
- Assume that there is a file "words.txt". This file may have at least 10000 Lines of Proper English Sentences.
- The Program should read the content optimally[we want to avoid memory issue if the content of the file is too large]
- After reading the content, and Two Excel files should be Generated.
- On Excel file should have name words.xlsx which shall have 26 columns[Col A, Col B, Col C ... Col Z]
- Any word that starts with the letter 'A' should be put in Col A.
- Any word that starts with the letter 'B' should be put in Col B and so on.
- Another Excel file should have the name word_count.xlsx. Here also there should be 26 columns but there shall only be 
  one value in each column. The Value is the word count for the corresponding letter. For example if we have 40 words 
  starting with letter 'A' then value under Col A of this file should be 40 and so on. 
