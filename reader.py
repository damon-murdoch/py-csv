# python csv library
import csv

# python system library
import sys

# Read the contents from the csv file into
# a list of tables and return it
def get_content(filepath,delim=","):

  try:

    # open the csv file
    with open(filepath) as f:

      # All headers excl. ID
      head = []

      # Lookup table
      # K = id (first row), 
      # V = all other elements
      table = {}

      # Create a csv reader object, using the provided (or default) 
      # delimiter character (what splits up the columns in each row)
      # And I honestly have no idea what the quotechar does sorry
      reader = csv.reader(f,delimiter=delim, quotechar='|')

      # Current row
      i = 0

      # Now we can loop over all of the rows
      for row in reader:

        # If we are on th first row (the headings)
        if i == 0:

          # Set the headings
          headings = row[1:]

        else: # We are on any other row

          # Key placeholder variable
          k = None

          # Hashtable (key-value table) value
          v = {}

          # Current Column
          j = 0

          # Loop over the columns
          for col in row:

            # If this is the first column (i.e. the key)
            if j == 0:

              # Set the key for this row to the value of the column
              k = col

              # Don't add it to the value

            else: # This is a value row, add it to the value

              # Create a key-value pair
              # in the hashtable with the key
              # as the row heading and the value
              # as the current column
              v[headings[j-1]] = col

            # Increment the column counter
            j += 1

          # If the key has been changed
          if k != None:
            
            # Add the row to the hashtable
            table[k] = v

        # Increment the row counter
        i += 1
    
      # Return the table to the calling process
      return table
      
  # This is far too generic, python supports specifying
  # specific exception types to handle but is fine for
  # this purpose
  except Exception as e:

    # Just tell the user what went wrong, 'e' is the 
    # error message
    print("Failed to read csv file'",csv,"':",e)

    return None

# This runs when the file is launched,
# but not if it is imported by another file
if __name__ == '__main__':

  # Get the arguments from the terminal, 
  # excluding the default argument (filename)
  args = sys.argv[1:]

  # If there is one (or more) arguments
  if len(args) > 0:

    # Loop over each argument
    for path in args:

      # Print the data converted to an object
      print(get_content(path))