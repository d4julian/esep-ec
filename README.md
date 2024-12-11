# ESEP Extra Credit Assignment
## Data Processing and Storage

### Setup/Instructions
- Clone the repository or just install the script
- Verify you have Python installed on your computer
- You can run the program with `python esep-ec.py`

### Example
```
# Instantiate the InMemoryDatabase
db = InMemoryDatabase()

# Begins the transaction
db.begin_transaction()

# Put value A: 1
db.put("A", 1)

# Commit changes
db.commit()

# Get value A
db.get("A") # returns 1
```
### Output
- `begin_transaction()` Started transaction
- `put("A", 1)` Put A to 1
- `db.commit()` Committed transaction
- `get("A")` A: 1

### Assignment Suggestions
I definitely believe this assignment was fun and helpful in reinforcing how you can use data structures in your code. In my opinion, I think this should become a future assignment. In my other classes they have used software such as Gradescope to automatically run test cases on the code, which could be a viable option. In addition, I think the instructions should specify whether to include only the library or include the test cases shown in the document. 