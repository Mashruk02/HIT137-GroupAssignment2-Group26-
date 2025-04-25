HIT137 - Group Assignment 2
Semester 1, 2025
Course: HIT137 – Software Now 
Contributors
Group Members:
• Al-Mashruk Bhuiyan - S390782
• Vijaya Rama Krishna Datta Sai KANAPARTHI- S385673
• Alexander Uybenes- S334549
• Kavya sree sunkara- S386025
Table of Contents
• Introduction
• Assignment Questions
• Question 1
• Question 2
• Question 3
• Contributions
• Challenges and Solutions
Introduction
This repository includes all the code and supporting materials developed for Group Assignment 2 in the HIT137 course during Semester 1, 2025, at CAS-DAN13. The entire project has been built using Python.
Assignment Questions
Question 1
Develop a program that reads data from a file named raw_text.txt, applies a basic encryption technique to its contents, and saves the encrypted result into a new file called encrypted_text.txt. Additionally, implement functions to decrypt the encrypted text and verify the accuracy of the decryption.

Requirements:
• For lowercase letters:
  - If the letter is in first half of alphabet (a-m): shift forward by n * m
  - If the letter is in second half (n-z): shift backward by n + m
• For uppercase letters:
  - If the letter is in first half (A-M): shift backward by n
  - If the letter is in second half (N-Z): shift forward by m^2
• Special characters and numbers remain unchanged.
Question 2
Develop a program that processes temperature data gathered from various weather stations across Australia. The data is saved in multiple CSV files within a folder named "temperatures," with each file containing records for a specific year.

Tasks:
• Calculate the average temperatures for each season across all years and save to 'average_temp.txt'.
• Find the station(s) with the largest temperature range and save to 'largest_temp_range_station.txt'.
• Find the warmest and coolest station(s) and save to 'warmest_and_coolest_station.txt'.
Question 3
Develop a program that draws a recursive tree using the Turtle graphics module. The program should accept the following parameters from the user:
• Left and right branch angles
• Starting branch length
• Recursion depth
• Branch length reduction factor

Example: A tree with left branch at 30°, right at 35°, starting length of 120 pixels, reducing by 80% each time, for 7 levels.
Contributions
• Vijaya Rama Krishna Datta Sai KANAPARTHI Developed the encryption and decryption functions for Question 1.
• Kavya sree sunkara - Examined and handled the temperature data for Question 2.
• Al-Mashruk Bhuiyan- Created the recursive tree pattern generator for Question 3.
• Alexander Uybenes - Oversaw the project and combined the contributions from all team members.
Challenges and Solutions
•	Problem: Faced errors due to missing modules initially.  
Fix: Installed Homebrew, pip, and the cryptography modules to resolve the issues.


•	Problem: Encountered difficulties with temperature analysis because of incorrect file paths.  
•	Fix: Corrected the file paths in the code and reorganized the folders and files in VS Code explorer.

•	Problem: Ran into errors while working on the recursive tree pattern.  
•	Fix: Installed the Turtle graphics module on macOS using the terminal in VS Code.

•	Module Issues: Missing modules caused errors at the start.  
•	Fix: Installed pip and cryptography to get the necessary modules.

•	Path Errors: Couldn’t access CSV files due to wrong directory structure.  
•	Fix: Adjusted the file organization and validated paths in the code.

•	Turtle Graphics Issue: The Turtle module wasn’t functioning as expected on macOS.  
•	Fix: Installed the needed graphics libraries via the terminal in VS Code.
