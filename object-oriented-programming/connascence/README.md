# Connascence

| Strength        | Connascence Type |
| :-:             | :-:              |
| Weakest, Static | Name             |
|                 | Type             |
|                 | Meaning          |
|                 | Position         |
|                 | Algorithm        |
| Dynamic         | Execution        |
|                 | Timing           |
| Strongest       | Identity         |


<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Connascence](#connascence)
- [Why connascence matters?](#why-connascence-matters)
- [Static Connascences](#static-connascences)
    - [Connascence of name](#connascence-of-name)
    - [Connascence of type](#connascence-of-type)
        - [Statically typed languages](#statically-typed-languages)
        - [Dynamically typed languages](#dynamically-typed-languages)
    - [Connascence of Meaning](#connascence-of-meaning)
        - [Solution](#solution)
        - [Primitive numerical types or data types](#primitive-numerical-types-or-data-types)
    - [Connascence of Position](#connascence-of-position)
        - [In Data Structures](#in-data-structures)
        - [In Function Arguments](#in-function-arguments)
            - [Solution](#solution-1)
    - [Connascence of algorithm](#connascence-of-algorithm)
        - [In data transmission](#in-data-transmission)
        - [In Data Validation and Encoding](#in-data-validation-and-encoding)
            - [Example 1: Validations: Users not being able to register, but recieving no feedback as to why.](#example-1-validations-users-not-being-able-to-register-but-recieving-no-feedback-as-to-why)
            - [Example 2: The encoding being used i.e. .encode('utf8')](#example-2-the-encoding-being-used-ie-encodeutf8)
        - [In test code](#in-test-code)
- [Dynamic Connascence](#dynamic-connascence)
    - [Connascence of Execution](#connascence-of-execution)
        - [Connascence of timing](#connascence-of-timing)
    - [Connascence of Value](#connascence-of-value)
    - [Connascence of Identity](#connascence-of-identity)
- [Contranascence](#contranascence)

<!-- markdown-toc end -->

Why connascence matters?
========
Recall definition: More explicitly, I define two software elements A and B to be connascent if there is at least one change that could be made to A that would necessitate a change to B in order to preserve overall correctness.

More connascence means:
* harder to extend
* more chance of bugs
* slower to write in the first place


Static Connascences
========


## Connascence of name

* Multiple components must agree on the name of an entity. Method, class, parameters have names.

* If the name of a method changes, callers of that method must be changed to use the new name.

```python
class Request:

    def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False,
                 method=None):
        pass

    def set_proxy(self, host, type):
        pass
```
> -- *[Connascenceio][connascenceio]*

Changing the name of any part of this code will cause code that uses this class to break, including:

* Changing the class name from Request.
* Changing any of the method names (such as set_proxy).
* Changing the name of any of the parameters to either __init__ or set_proxy.

Connascence of name is unavoidable, since we refer to entities using labels. If we change the name of an entity when we declare it, we must also change all code that refers to that entity. For this reason, connascence of name is the **weakest** connascence. 

However, it also illustrates how important it is to name entities in code well.

[connascenceIO]: https://www.connascence.io

## Connascence of type

Connascence of type is when multiple components must agree on the type of an entity. 

### Statically typed languages 
These issues are often (but not always) **caught by the compiler**. Consider the following trivial C++ code:

```C++
std::string cost;

cost = 10.95; // OOPS!
```

### Dynamically typed languages
Dynamically typed languages typically suffer from less obvious instances of connascence of type. Consider a function that calculates your age, given your day, month, and year of birth:

```python
def calculate_age(birth_day, birth_month, birth_year):
    # do the calculation here:
```

How is this function supposed to be called? Here are a few different options:

```python
calculate_age(1, 9, 1984)
calculate_age(1, 9, 84)
calculate_age('1', '9', '1984')
calculate_age('1', 'September', '1984')
```

## Connascence of Meaning

Connascence of meaning is when **multiple components must agree on the meaning** of particular values. 

Consider some code that processes credit card payments. The following function might be used to determine if a given credit card number is valid or not:

```python
def is_credit_card_number_valid(card_number):
    # Check for 'test' credit card numbers:
    if card_number == "9999-9999-9999-9999":
        return True
    # Do normal validation:
    # ...
```

The problem here is that all parts of this system must agree that 9999-9999-9999-9999 is the test credit card number. If that value changes in one place, it must also change in another.

```python
def get_user_role(username):
    user = database.get_user_object_for_username(username)
    if user.is_admin:
        return 2
    elif user.is_manager:
        return 1
    else:
        return 0
```

Elsewhere, code might need to check that a given username is an administrator, like so:

```python
if get_user_role(username) != 2:
    raise PermissionDenied("You must be an administrator")
```
### Solution
Connascence of meaning can be improved to connascence of name by moving the **"magic values or variables"** to named constants, and referring to the constants instead of the values. However in doing so, we have increased the amount of connascence of name (since we now need a third location to store the constant).

### None as return value
Another common example of connascence of meaning is when None is used as a return value. This frequently occurs in functions that are tasked with finding an object. If that object isn't found, the function might return None.


```python
def find_user_in_database(username):
    return database.find_user(username=username) or None
```

```python
def find_user_in_database(username):
    try:
        return database.find_user(username=username) or None
    except DatabaseError:
        return None
```

The problem in both these cases is that a semantic meaning is being assigned to the None value. If multiple different meanings are assigned to the same None value in the same codebase, the programmer must remember which meaning applies to which case. 


This can be improved to connascence of name by returning an explicit object that represents the case in question:


```python
def find_user_in_database(username):
    try:
        return database.find_user(username=username) or ObjectNotFound
    except DatabaseError:
        return None
```

We still have connascence of meaning in the error case, but **at least the None value is no longer ambigous**. The error case could also be improved to connascence of name in a similar way.

### Primitive numerical types or data types
Another common example of connascence of meaning is when we use primitive numeric types to represent more complex values. Consider this line of code in a codebase that processes payments:


```
unit_cost = 49.95
```

49.95 can be yen, usd, aud or British pounds. The meaning is very vague.

It can be improved to connascence of type by creating a 'Cost' type that disallows operations between different currencies:

```python
unit_cost = Cost(49.95, 'USD')
```

This particular problem is often called "Primitive Obsession", and can be generically described as using primitive data types to represent more complex domains.

## Connascence of Position

### In Data Structures
For example, consider a function that retrieves a user's details.

```python
def get_user_details():
    # Returns a user's details as a list:
    # first_name, last_name, year_of_birth, is_admin
    return ["Thomas", "Richards", 1984, True]
```

This is a somewhat contrived example, but it's not uncommon to see data returned in lists or tuples. Elsewhere in the code we might need to perform some check on whether the user is an administrator or not:


```python
def launch_nukes(user):
    if user[3]:
        # actually launch the nukes
    else:
        raise PermissionDeniedError("User is not an administrator!")
```

These two functions are **linked by connascence of position**. 

If the order of the values in the user list ever changes, both locations must be updated (this example is particularly scary if someone were to update the user list to be [first_name, initials, last_name, year_of_birth, is_admin] without updating the check inside launch_nukes).

This connascence can be improved to connascence of name by turning the list into a **dictionary or class**. The following example shows how the above functions might look as a dictionary:

```python
def get_user_details():
    return {
        "first_name": "Thomas",
        "last_name": "Richards",
        "year_of_birth": 1984,
        "is_admin": True,
    }


def launch_nukes(user):
    if user['is_admin']:
        # actually launch the nukes
    else:
        raise PermissionDeniedError("User is not an administrator!")
```


We've **turned connascence of position into the weaker connascence of name**. This has also increased the **readability** of the get_user_details function - the explicit comment is no longer needed to document the order of the keys.

A similar solution is to use a class instead of a dictionary, and this can be beneficial if the structure being returned has **constraints or operations associated with it**.

### In Function Arguments

Connascence of position also frequently occurs in ***function argument lists***. Consider the following function declaration from a mythical email-sending utility library:

```python
def send_email(firstname, lastname, email, subject, body, attachments=None):
```

Code calling this send_email function must remember the order of arguments. Should that order ever change, all calling locations must also be updated. 

#### Solution
This example could also be improved to connascence of name by **passing a structured object** (a class or dictionary) instead of a number of parameters.

## Connascence of algorithm 

This occurs is when **multiple components must agree on a particular algorithm**.

### In data transmission

Connascence of algorithm frequently occurs when two entities must manipulate data in the same way. 

> if data is being transmitted from one service to another, some sort of **checksum algorithm** is commonly used. The sender and receiver must agree on which algorithm is to be used. If the sender changes the algorithm used, the receiver must change as well. <br />
> -- [Connascenceio][connascenceio]

### In Data Validation and Encoding
#### Example 1: Validations: Users not being able to register, but recieving no feedback as to why.

Consider a hypothetical piece of software that required users to provide a valid email address when creating an account. The software must validate that the email address is valid, but this might happen in several places, including:

* In a database model object.
* In a webapp 'controller' class method.
* In a form field in the front-end UI.

These pieces of code might well be in different languages, and will almost certainly be far apart from each other. The consequence of these algorithms being different might include users not being able to register, but recieving no feedback as to why.
### Example 2: The encoding being used i.e. .encode('utf8')

Another common example of connascence of algorithm is when unicode strings are written to disk. Imagine a hypothetical piece of software that writes a data string to a cache file on disk:


```python
def write_data_to_cache(data_string):
    with open('/path/to/cache', 'wb') as cache_file:
        cache_file.write(data_string.encode('utf8'))
```

```python
def write_data_to_cache(data_string):
    with open('/path/to/cache', 'wb') as cache_file:
        cache_file.write(data_string.encode('utf8'))
```
The connascence of algorithm here is that both functions must agree on the encoding being used. If the write_data_to_cache function changes to encrypt the data on disk (the data being stored is potentially sensitive), the read_data_from_cache must also be updated.


### In test code 
Test code often contains connascence of algorithm. Consider this hypothetical test:

The test assumes the actual algorithm uses md5 from hashlib
```python
def test_user_fingerprint(self):
    user = User.new(name="Thomi Richards")
    actual = user.fingerprint()
    expected = hashlib.md5(user.name).hexdigest()
    self.assertEqual(expected, actual)
```

This test is supposed to be testing that the 'fingerprint' method of the User class works as expected. However, it contains connascence of algorithm, which limits it's effectiveness. If the User class ever changes the way fingerprints are calculated, this test will fail.


Dynamic Connascence
========

## Connascence of Execution
Connascence of execution is when the **order of execution of multiple components is important**. 

Common examples include locking and unlocking resources, where locks must be acquired and released in the same order everywhere in the entire codebase.

Connascence of execution can also occur when using objects that encapsulate a **state machine**, and that state machine only allows certain operations in certain states. For example, consider a hypothetical EmailSender class that allows a caller to generate and send an email:

```python
email = Email()

# Email must be generated first
email.setRecipient("foo@example.comp")
email.setSender("me@mydomain.com")

# Then sent
email.send()

# Subject is set after sent? Connascence of execution
email.setSubject("Hello World")
```

The setSubject method cannot be called after the send method (at best it will do nothing). 

In this example the **locality of the coupling** is very low, but cases where the **locality** is very high can be much harder to find and fix (consider, for example a scenario where the last two lines are called on separate threads).

### Connascence of timing

Connascence of timing is when the timing of the execution of multiple components is important.

An example include if you have a interval running in the background and a function or method only runs when the user clicks a button exactly at the interval boundary.

Another example if you have a time class, two class that reads the time of the time class and they exchange functions based on their own individual readings of the time class.


## Connascence of Value

Connascence of value is when several values must change together. This frequently occurs between **production code and test code**. 

For example, consider an Article class, which represents a blog article. When it is instantiated, it is given some text contents, and its initial 'state' is 'draft':

```python
class ArticleState(Enum):
    Draft = 1
    Published = 2


class Article(object):

    def __init__(self, contents):
        self.contents = contents
        self.state = ArticleState.Draft

    def publish(self):
        # do whatever is required to publish the article.
        self.state = ArticleState.Published
```

Now imagine a hypothetical test that ensures that the publish method works:

```python
article = Article("Test Contents")
assert article.state == ArticleState.Draft
article.publish()
assert article.state == ArticleState.Published
```

The problem here is that the test **requires knowledge of the initial state** of the Article class: if the Article's initial state is ever changed, this test will break (this is arguably a bad test, since the first assertion has little to do with the intent of the test, but it's a common mistake). 

#### Improvement

This code can be improved by adding an InitialState label to ArticleClass, and changing both the Article class and the test to refer to that label instead:

```python
class ArticleState(Enum):
    Draft = 1
    Published = 2
    InitialState = Draft


class Article(object):

    def __init__(self, contents):
        self.contents = contents
        self.state = ArticleState.InitialState
```

The test now becomes:

```python
article = Article("Test Contents")
assert article.state == ArticleState.InitialState
article.publish()
assert article.state == ArticleState.Published
```

Should we need to change the state machine of the Article class, we can do so by changing the ArticleState enumeration:

```python
class ArticleState(Enum):
    Preproduction = 1
    Draft = 2
    Published = 3
    InitialState = Preproduction
```

We have effectively introduced a level of indirection between the Article class and its initial state value.


## Connascence of Identity

Connascence of identity is when multiple components must reference the same entity.

```java
public class Person {
  private String name;
  private Set<Person> parents;
  public Person(String name, Person parenta, Person parentb) {
    this.name = name;
    parents = new HashSet<Person>();
    parents.add(parenta);
    parents.add(parentb);
  }

  public Set <Person> getParents() {
    return parents;
  }

  public boolean isSibling(Person a) {
    for (Person parent : parents) {
      if (a.getParents().contains(parent)) {
        return true;
      }
    }
  return false;
  }
}
```

```java
public static void main(String[] args) {
  Person gina = new Person("Gina Meares", null, null);
  Person fred = new Person("Fred Meares", null, null);
  Person anna = new Person("Anna Meares", gina, fred);
  Person kerrie = new Person("Kerrie Meares", gina, fred);

  Person gina2 = new Person("Gina Meares", null, null);
  Person fred2 = new Person("Fred Meares", null, null);
  Person kerrie2 = new Person("Kerrie Meares", gina2, fred2);
}
```
Even though we have two Kerries, they are different classes and have different identity.

```java
if (anna.isSibling(kerrie)) {
  System.out.println("Sisters rule");
}

if (anna.isSibling(kerrie2)) {
  System.out.println("Duplicate sisters too?");
}
```

## Contranascence

When two things are required to be different This is a form of connascence

“Aliasing bugs” – an example fault type where contranascence has not been maintained.

```javascript
const GENRE_ACTION = 0;
const GENRE_DRAMA = 1;
```

[connascenceio]: https://connascence.io/
