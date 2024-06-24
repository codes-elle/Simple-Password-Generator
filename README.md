# Password Generator

This Python script generates a random password with a specified length using a combination of ASCII letters, digits, and punctuation characters. The default length of the generated password is 10 characters.

## Features

- Generates a random password
- Utilizes ASCII letters, digits, and punctuation to enhance complexity
- Allows customization of the password length

## Requirements

- Python 3.x

## Usage

1. **Import the required modules:**

    ```python
    import random  # Provides the ability to create a random output
    import string  # Adds more complexity by including various character sets
    ```

2. **Define the `generate_pw` function:**

    ```python
    def generate_pw(length: int = 10):  # Sets the default password length to 10
        # Combine ASCII letters, digits, and punctuation characters
        alphabet = string.ascii_letters + string.digits + string.punctuation  
        # Randomly select characters from the alphabet to form the password
        password = "".join(random.choice(alphabet) for i in range(length)) 
        return password
    ```

3. **Generate and print a password:**

    ```python
    password = generate_pw()
    print(f"Generated password: {password}")
    ```

### Example

To generate a password with the default length of 10 characters, run the script:

```python
Generated password: aB3$dEf!Gh
```

To generate a password with a different length, pass the desired length as an argument to the `generate_pw` function:

```python
custom_length_password = generate_pw(15)
print(f"Generated password with custom length: {custom_length_password}")
```

## Customization

You can customize the length of the generated password by passing an integer argument to the `generate_pw` function. For example, to generate a password with a length of 12 characters:

```python
password = generate_pw(12)
print(f"Generated password: {password}")
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## Contact

For any questions or suggestions, please contact the repository owner.

---

Feel free to use, modify, and distribute this script as needed. Happy password generating!
