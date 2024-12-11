class InMemoryDatabase:
  def __init__(self):
    self.db = dict()
    self.transaction = None
  
  def get(self, key):
    value = self.db.get(key)
    print(f'{key}: {value}')
    return value

  def put(self, key, value):
    if self.transaction is None: print('Can\'t put value: No transaction to put')
    else: 
      print("Put", key, "to", value)
      self.transaction[key] = value

  def begin_transaction(self):
    if self.transaction is not None: print('Can\'t begin transaction: transaction already started')
    else: 
      print("Started transaction")
      self.transaction = dict(self.db)

  def rollback(self):
    if self.transaction is None: print('Can\'t rollback transaction: No transaction to rollback')
    else: 
      print("Transaction rolled back")
      self.transaction = None

  def commit(self):
    if self.transaction is None: print('Can\'t commit transaction: No transaction to commit')
    else:
      print("Committed transaction")
      self.db.update(self.transaction)
      self.transaction = None

if __name__ == '__main__':
  db = InMemoryDatabase()

  db.get("A") # None
  db.put("A", 5) # No transaction to put
  db.begin_transaction() # Start new transaction
  db.put("A", 5) # Put A to 5
  db.get("A") # None
  db.put("A", 6) # Put A to 6
  db.commit() # Commit transaction
  db.get("A") # Returns 6
  db.commit() # No transaction to commit
  db.rollback() # No transaction to rollback
  db.get("B") # None
  db.begin_transaction() # Start new transaction
  db.put("B", 10) # Put B to 10
  db.rollback() # Reverts transaction
  db.get("B") # None because transaction was reverted

