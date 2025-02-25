# Password Generator

A simple password generator application that allows users to create secure and random passwords based on customizable criteria such as length, inclusion of uppercase letters, numbers, and special characters.

## Features

- Generate strong, random passwords
- Customize password length (default: 8-16 characters)
- Option to include/exclude:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Copy generated password to clipboard
- Responsive design for mobile and desktop

## Tech Stack

- **Language Used**: Python
- **Deployment**: GitHub Pages (optional)

## Project Structure

```
password-generator/
│
├── Pass-gen.py           # Main Python file
└── README.md            # Project documentation
```

## Getting Started

### Prerequisites

Ensure you have a web browser installed (any modern browser will do).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BorisagarRushabh/Password-Generator.git
   cd Password-Generator
   python3 pass-gen.py
   ```
   
## Usage

1. Open the application.
2. Customize the password generation criteria:
   - Set password length
   - Choose whether to include/exclude uppercase letters, numbers, and special characters
3. Click the "Generate Password" button to create a random password.
4. Copy the generated password to your clipboard using the "Copy" button.

## Future Improvements

- Add an option to save generated passwords.
- Implement strength indicators to show how secure the generated password is.
- Create a version that integrates with local storage to remember preferences.
- Add dark mode for the user interface.

## Contributing

Contributions are welcome! Feel free to submit pull requests to enhance the functionality of the project.
