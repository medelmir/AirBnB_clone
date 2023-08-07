<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://drive.google.com/uc?export=view&id=1i2kE3R33n6PTvAkhp8XplQfzE31HvTOj" alt="Logo" 
  </a>

<h1 align="center">0x00. AirBnB clone - The console</h1>
</a> 

[Aziz Belkharmoudi](https://github.com/Abubacer/)  , 
[El Mir Mohammed](https://github.com//)
<div align="left">
</p>
<br />

<!-- ABOUT THE PROJECT -->
## About The Project
A team project to build our first full web application: a clone of [AirBnB](https://www.airbnb.com/).
1. Concepts:
   - [Python packages](https://intranet.alxswe.com/concepts/66)
   - [AirBnB clone](https://intranet.alxswe.com/concepts/74)
     
2. Learning Objectives:
   - How to create a Python package
   - How to create a command interpreter in Python using the cmd module
   - What is Unit testing and how to implement it in a large project
   - How to serialize and deserialize a Class
   - How to write and read a JSON file
   - How to manage datetime
   - What is an UUID
   - What is *args and how to use it
   - What is **kwargs and how to use it
   - How to handle named arguments in a function
     
3. We will use what we build during this project with all other following projects:
   - HTML/CSS templating, database storage, API, front-end integration…
     
4. Each task is linked and will help us to:
   - put in place a parent class (called BaseModel ) to take care of the initialization, serialization and
deserialization of our future instances
   - create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
   - create all classes used for AirBnB ( User , State , City , Place …) that inherit from BaseModel
   - create the first abstracted storage engine of the project: File storage
   - create all unittests to validate all our classes and storage engine
     
5. The console will perform the following tasks:
   - Create a new object (ex: a new User or a new Place)
   - Retrieve an object from a file, a database etc…
   - Do operations on objects (count, compute stats, etc…)
   - Update attributes of an object
   - Destroy an object
     
6. All the classes are handled by the Storage engine defined in the FileStorage class:
   - Every time the backend is initialized, the app instantiates an instance of FileStorage called storage.
   - The storage object is loaded/re-loaded from any class instances stored in the JSON file file.json.
   - As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
All the development and testing were run over an operating system Ubuntu 20.04 LTS using the programming language Python 3.8 The editors used were VIM 8.1, VSCode 1.6 Control version using Git 2.25 Style guidelines: pycodestyle (version 2.7.*) and PEP8.

<br />
<div align="left">
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&style=for-the-badge&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a><!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&style=for-the-badge&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a><!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Bash&style=for-the-badge&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a></a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&style=for-the-badge&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a></a><!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&style=for-the-badge&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&style=for-the-badge&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"><!-- vagrant --> <a href="https://www.vagrantup.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vagrant&style=for-the-badge&color=blue&logo=vagrant&logoColor=f2f2f2&labelColor=2F333A" alt="vagrant"><!-- py --> <a href="https://pypi.org/project/pycodestyle/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=pycodestyle&style=for-the-badge&color=blue&logo=python&logoColor=yellow&labelColor=2F333A" alt="Github">


<p align="right">(<a href="#readme-top">back to top</a>)</p>
</p>
</div>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation
1. Clone the repo

   ```sh
   git clone https://github.com/Abubacer/AirBnB_clone.git
   ```
2. Change to the AirBnb directory and run the command

   ```sh
   ./console.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
### Execution

1. In interactive mode
   
   ```sh
   $ ./console.py
   (hbnb) help

   Documented commands (type help <topic>):
   ========================================
   EOF  help  quit

   (hbnb)
   (hbnb)
   (hbnb) quit
   $
   ```
2. In Non-interactive mode
   
   ```sh
   $ echo "help" | ./console.py
   (hbnb)

   Documented commands (type help <topic>):
   ========================================
   EOF  help  quit
   (hbnb)
   $
   $ cat test_help
   help
   $
   $ cat test_help | ./console.py
   (hbnb)

   Documented commands (type help <topic>):
   ========================================
   EOF  help  quit
   (hbnb)
   $
   ```
## Usage

1. Start the console in interactive mode:

   ```sh
    $ ./console.py
    (hbnb)
   ```
2. Use help to see the available commands:

   ```sh
   (hbnb) help

   Documented commands (type help <topic>):
   ========================================
   EOF  all  count  create  destroy  help  quit  show  update

   (hbnb)
   ```
3. To quit the console:
   
   ```sh
   (hbnb) quit
   $
   ```

   ```sh
   $ ./console.py
   (hbnb) EOF
   $  
   ```
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage: Console Commands
The console supports the following commands:

1. create:
   - Creates a new instance of a given class.
   - Usage: ```create <class>```.
<br />

   ```sh
   $ ./console.py
   (hbnb) create BaseModel
   486be963-6fe5-437e-a200-b9892e8946b8
   (hbnb) quit
   $ cat file.json ; echo ""
   {"BaseModel.486be963-6fe5-437e-a200-b9892e8946b8": {"updated_at": "2023-08-07T2
   1:30:42.215277", "created_at": "2023-08-17T21:30:42.215277", "__class__": "Base
   Model", "id": "486be963-6fe5-437e-a200-b9892e8946b8"}}
   ```
   
2. show:
   - Prints the string representation of a class instance based on a given id.
   - Usage: ```show <class> <id>``` or ```<class>.show(<id>)```.
<br />

   ```sh
   $ ./console.py
  

   ```
3. destroy:
   - Deletes a class instance based on a given id. The storage file will be updated with the change.
   - Usage: ```destroy <class> <id>``` or ```<class>.destroy(<id>)```
<br />

   ```sh
   $ ./console.py
   
   ```
4. destroy:
   - Prints the string representations of all instances of a given class.
   - If no class name is provided, the command prints all instances of every class.
   - Usage: ```all``` or ```all <class>```or```<class>.all()```
<br />

   ```sh
   $ ./console.py
   
   ```
5. count:
   - Returns the number of instances of a given class.
   - Usage: ```count <class>``` or ```<class>.count()```
<br />

   ```sh
   $ ./console.py
   
   ```
6. update:
   - Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs.
   - Usage: ```update <class> <id> <attribute name> "<attribute value>"``` or ```<class>.update(<id>, <attribute name>, <attribute value>)``` or ```<class>.update( <id>, <attribute dictionary>)```.
<br />

   ```sh
   $ ./console.py
   
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Testing
All the tests are defined in the tests folder:
- Using unittest module
- Files and folders start with test_
- File extension .py

- To run tests in interactive mode

   ```sh
   echo "python3 -m unittest discover tests" | bash
   ```

- To run test suite simultaneously, in non-interactive mode

   ```sh
   python3 -m unittest discover tests
   ```
- To run a single test file, in non-interactive mode

   ```sh
   python3 unittest -m tests/test_console.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Documentation

1. Modules:

   ```sh
   python3 -c 'print(__import__("my_module").__doc__)'
   ```
2. Classes:

   ```sh
   python3 -c 'print(__import__("my_module").MyClass.__doc__)'
   ```
3. Functions:
   
   ```sh
   python3 -c 'print(__import__("my_module").my_function.__doc__)'
   ```
   ```sh
   python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
   ```
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Authors

- Aziz belkharmoudi
- ELMIR Mohammed


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Aziz belkharmoudi - [@Aziz](https://www.linkedin.com/in/azizdesign/) - azizdesignislife@gmail.com
ELMIR Mohammed - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Abubacer/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Abubacer/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
