# Import the csv module
import csv

class pycsv:
    def __init__(self, file):
        self.file = file
    
    def read_csv(self, columnHeaders="yes", columnNames=None):
        file = self.file
        table = {}
        print(file)
        # Read the csv file data
        with open(file, 'r') as csvFile:
            
            # New csvreader Object
            csvReader = csv.reader(csvFile)
            
            # If the parameter columnHeaders is yes
            if columnHeaders.lower() == "yes":
                # Assign the headers variable to the first row of the csv file
                headers = next(csvReader)
            # If the parameter columnHeaders is no
            elif columnHeaders.lower() == "no":
                # Create an empty list to store column names
                headers = []
                # Get the number of columns by counting the number of elements in the first row
                columnCount = len(next(csvReader))
                # For each column in the csv file
                for colNum in range(0, columnCount):
                    # Append a column name to the headers list
                    headers.append(f'col_{colNum}')

            # Declare the number of columns
            numCols = len(headers) 

            # Loop through each item in the first row and assign it to a key in your dictionary
            for colNum in range(0, numCols):
                table.update({headers[colNum]: None})
            

            # Establish globals variable for rows lists
            g = globals()

            # Create a row list for each row in the header
            for colNum in range(0, numCols):
                g[f'row_{colNum}'] = []

            # Loop through each row in the csv file
            for row in csvReader:
                # For each row use the length of the header row to determine how many columns there are
                for colNum in range(0, numCols):
                    # Append the value of each rowXcolumn to its respective list 
                    g[f'row_{colNum}'].append(row[colNum])
                    table.update({headers[colNum]: g[f'row_{colNum}']})
            
            #Declare the number of rows
            numRows = len(list(table.values())[0])
            
            # Create an empty column for the index
            headers = [""] + headers
            
            # Create new list for index row
            idx_row =[]
            # Add an index position number for each row
            for row in range(0, numRows):
                idx_row.append(row)
            
            # Add index row to table
            table.update({headers[0]: idx_row})
            
            # Re-declare the number of columns
            numCols = len(headers) 
            
            # Establist string variable for column layout string
            columnLayout = ""
            # For each column
            for col in range(0, numCols):
                # Check the length of the longest column and set the layout length
                if len(headers[col]) <= 0:
                    columnLayout += "{:<7}"
                elif len(headers[col]) <= 4:
                    columnLayout += "{:<12}"
                elif len(headers[col]) <= 10:
                    columnLayout += "{:<15}"
                elif len(headers[col]) <= 15:
                    columnLayout += "{:<20}"
                elif len(headers[col]) <= 20:
                    columnLayout += "{:<25}"
                elif len(headers[col]) <= 25:
                    columnLayout += "{:<30}"
                elif len(headers[col]) <= 30:
                    columnLayout += "{:<33}"
                    
            # Map the column names to the column layout
            print(columnLayout.format(*list(map(lambda x: x, headers))))

            # Print the first 5 rows of the of the csv file
            for row in range(0, 5):
                # Map the row data to the column layout
                print(columnLayout.format(*list(map(lambda x: table[x][row], headers))))
            # Print a separator
            separatorLayout = (numCols * "-")
            print(columnLayout.format(*str(separatorLayout)))
            # Print the last 5 rows of the csv file
            for row in range((numRows - 5), numRows):
                # Map the row data to the column layout
                print(columnLayout.format(*list(map(lambda x: table[x][row], headers))))
            # Describe the data
            print(f"\n{numRows} rows x {numCols - 1} columns")
            
            self.headers = headers
            self.table = table
            self.numCols = numCols - 1
            self.numRows = numRows
    
    def data(self):
        return self.table
    
    def count(self, axis='index'):
        if axis.lower() == "index":
            colNum = 0
            for col in self.headers[1:]:
                print("{:<10} {:<10}".format(col, len(list(self.table.values())[colNum])))
                colNum += 1
        elif axis.lower() == "columns":
            print(len(self.headers) - 1)

    def _sum(self, columnName=None):
        if columnName in self.headers[1:]:
            sumList = []
            for row in range(0, self.numRows):
                if self.table[columnName][row].lstrip('-').isnumeric():
                    sumList.append(int(self.table[columnName][row]))
            print("{:<10} {:<10}".format(columnName, sum(sumList)))
        else:
            for col in self.headers[1:]:
                sumList = []
                for row in range(0, self.numRows):
                    if self.table[col][row].lstrip('-').isnumeric():
                        sumList.append(int(self.table[col][row]))
                
                print("{:<10} {:<10}".format(col, sum(sumList)))
                        
            
    def diff(self, columnName=None):
        # Create a list to store difference values
        diffList = []
        # Create a dictionary to store the values of the difference between rows
        difference = {}
        
        # Create a rowNum variable to determine which row we are at
        rowNum = 0
        
        # Create a variable for the previous and current row equal to 0
        prevRow = 0
        currRow = 0
        
        # For each row in the table column
        for row in self.table[columnName]:
            # Skip the first row 
            rowNum += 1
            # Check if the row number is greater than 1
            if rowNum > 1:
                # Set the previous row
                prevRow = currRow
                # Set the current row
                currRow = int(row)
                # Append the difference for the current row to the list of difference 
                diffList.append(currRow - prevRow)
            # If the row number is less than 1
            else:
                # Set the previous row to 0
                prevRow = 0
                # Set the current row
                currRow = int(row)
        # Check if the column name is in the headers
        if columnName in self.headers:
            # Set the index of the difference table
            difference.update({self.headers[0]: self.table[self.headers[0]]})
            
            # Set the column of the difference table
            difference.update({columnName: diffList})
            
            # Set the number of columns
            numCols = len(list(difference.keys()))
            
            # Set the number of rows
            numRows = len(difference[columnName])
            
            # Map the column names to the column layout
            print("{:<10} {:<10}".format(*list(map(lambda x: x, list(difference.keys())))))
            
            # Print the first 5 rows of the table
            for row in range(0, 5):
                print("{:<10} {:<10}".format(difference[self.headers[0]][row], difference[columnName][row]))
                
            # Print a separator
            separatorLayout = (numCols * "-")
            print("{:<10} {:<10}".format(*str(separatorLayout)))
            
            # Print the last 5 rows of the csv file
            for row in range((numRows - 5), numRows):
                # Map the row data to the column layout
                print("{:<10} {:<10}".format(difference[self.headers[0]][row], difference[columnName][row]))
                
        print(f"\n Name: {columnName}, Length: {numRows + 1}")   
           