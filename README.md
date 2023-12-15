## 🏠 AirBnB Clone - The Console
Welcome to the AirBnB Clone project, which attempts to reproduce the functionality of the popular AirBnB platform for educational purposes.

By participating in this project, you will acquire important insight into key concepts and technologies used in software development.

## ⚙️ Project Progress

The project is ready to be used at console, please let us know if you faced any issues

## 💻 HBnB Console

The HBnB Console is a command-line interface for managing instances of various classes in the HBnB project. This console allows users to create, show, update, and delete instances of classes such as BaseModel, User, State, City, Amenity, Place, and Review.

### Getting Started

To use the HBnB Console, follow these steps:

Clone the Repository:
    
    git clone https://github.com/xWESOOOx/AirBnB_clone.git

Cd to repository directory:

    cd AirBnB_clone

Run the Console:

    ./console.py

This will start the HBnB Console, and you will see the prompt (hbnb).

### Available Commands

The following commands are available in the HBnB Console:

quit or CTRL-D: Exit the program.

    (hbnb) quit

create <class>: Create a new instance of the specified class and print its ID.

    (hbnb) create BaseModel

show <class> <id>: Show a string representation of an instance based on the class name and ID.

    (hbnb) show BaseModel 1234-5678

destroy <class> <id>: Delete an instance based on the class name and ID.

    (hbnb) destroy BaseModel 1234-5678

all: Display string representations of all instances.

    (hbnb) all

all <class>: Display string representations of all instances of a given class.

    (hbnb) all BaseModel

update <class> <id> <attribute_name> <attribute_value>: Update an instance based on the class name and ID by adding or updating an attribute.

    (hbnb) update BaseModel 1234-5678 name "Bob"

update <class> <id> <attribute_dict>: Update an instance based on the class name and ID by adding or updating attributes from given dictionary.

    (hbnb) update BaseModel 1234-5678 {"name": "Bob", "age": 31}

count <class>: Count the number of instances of a class.

    (hbnb) count BaseModel

Additional Notes

- The console supports some alternative syntaxes, such as `<class name>.<command>(<arguments>)`.

- Unknown commands will result in an error message.

Feel free to explore and manage your HBnB instances using the HBnB Console! If you encounter any issues or have suggestions for improvements, please let us know.
