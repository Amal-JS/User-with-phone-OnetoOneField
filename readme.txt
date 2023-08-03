So, In this project we are doing a login page and which is different from the previous project
here we are using a 'OneToOne Field' .
There is  user model and an phone model .So phone model has a onetoone relationship
with user model , means one user has associted with one phone record.

So to implement this , When we are creating a user object we want to create a phone 
object too. So after creating the user object we want to pass the user instance 
reference  to phone to create the object . But here the challenge is that the user 
is created successfully but the phone object creation failed .
At that time you have an user object but no phone related to it , 
So due to this issue we want to implement a system which creates a user object and then 
checks with the phone object creation . If it fails then the user object want to be not 
saved to the database and vice versa.
If both opertion is successful then it want to work.

For this case we are using 'transaction.atomic()' fuctionallity . Which is simillar to
 the acid properties in database.

'with transaction.atomic()'

It allows you to perform a series of database operations as an atomic transaction.
An atomic transaction means that either all the database operations within the
context succeed and are committed to the database, or if any of them fail, the 
entire transaction is rolled back, and no changes are persisted to the database.

all the database operations within the with transaction.atomic() block are treated 
as a single transaction. If any of the database operations fail (raises an exception)
, the transaction will be rolled back, and no changes will be persisted to the 
database.

Using transaction.atomic() helps maintain data consistency and integrity, especially
 when dealing with complex operations involving multiple database queries. It ensures
  that either all operations succeed together, or none of them have any lasting 
  effect on the database.