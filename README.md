# DSL for Online Store Management Using ANTLR

## Table of Contents

1. [Introduction](#introduction)
2. [Project Purpose and Problem Solved](#project-purpose-and-problem-solved)
3. [Features and Functionality](#features-and-functionality)
4. [Implementation Steps](#implementation-steps)
5. [Grammar Structure and Behavior](#grammar-structure-and-behavior)
6. [Input and Output Example](#input-and-output-example)
7. [Technologies and Tools Used](#technologies-and-tools-used)
8. [Setup and Usage](#setup-and-usage)
9. [File Structure](#file-structure)
10. [Contributing](#contributing)
11. [License](#license)

---

## Introduction

This project implements a **Domain-Specific Language (DSL)** for managing online stores using **ANTLR 4**. The DSL allows store managers to perform tasks such as creating, deleting, updating, and listing entities (e.g., products, customers) in a simple and efficient way. It also supports applying discounts and managing the attributes of entities.

---

## Project Purpose and Problem Solved

Managing an online store often involves repetitive and complex tasks such as:

1. Creating, updating, or deleting products and customers.
2. Applying discounts.
3. Managing inventory efficiently.

### Problems Addressed:

- **Complexity in coding:** Simplifies repetitive tasks with intuitive commands.
- **Error-prone operations:** Reduces errors by validating commands during parsing.
- **Customization limitations:** Offers a customizable DSL for store-specific needs.

### Benefits:

- Easy-to-use syntax for managing store entities.
- Fast execution of repetitive tasks.
- Clear feedback for incorrect commands.
- Extensible grammar for future features.

---

## Features and Functionality

### Core Features:

1. **Define Entities:**
   - Define new entities (e.g., `Product`, `Customer`, `Order`) with attributes.
2. **Create Entities:**
   - Add instances of defined entities with specific attribute values.
3. **Update Entities:**
   - Modify attributes of existing entities.
4. **Delete Entities:**
   - Remove entities using unique identifiers.
5. **List Entities:**
   - Retrieve a list of all entities of a specific type.
6. **Apply Discounts:**
   - Add discounts to products or other entities.

---

## Implementation Steps

1. **Designing the Grammar:**
   - Using **ANTLR 4**, the DSL grammar was designed to support commands like `create`, `delete`, `update`, and `list`.
2. **Generating Lexer and Parser:**
   - ANTLR 4 generated a lexer and parser for the defined grammar.
3. **Building an Abstract Syntax Tree (AST):**
   - Commands are parsed into an AST, which represents their logical structure.
4. **Interpreting Commands:**
   - The AST is traversed to execute the corresponding operations (e.g., database updates).
5. **Testing and Refinement:**
   - The DSL commands were tested for edge cases and improved for better usability and error handling.

---

## Grammar Structure and Behavior

### Core Grammar Rules:

1. **Define Command:**
   ```
   define {
       entity: entityName,
       attributes: { attributeName: type, ... }
   }
   ```
2. **Create Command:**
   ```
   create {
       entity: entityName,
       attributes: { attributeName: value, ... }
   }
   ```
3. **Delete Command:**
   ```
   delete {
       entity: entityName,
       id: uniqueId
   }
   ```
4. **Update Command:**
   ```
   update {
       entity: entityName,
       attributes: { attributeName: newValue, ... }
   }
   ```
5. **List Command:**
   ```
   list {
       entity: entityName
   }
   ```
6. **Discount Command:**
   ```
   discount {
       entity: entityName,
       percentage: value
   }
   ```

---

## Input and Output Example

### Input:

```
define {
    entity: product,
    attributes: { name: String, price: Float, stock: Integer }
}

create {
    entity: product,
    attributes: { name: "Laptop", price: 1200.0, stock: 50 }
}

list {
    entity: product
}
```

### Output:

- After defining and creating the product, running the `list` command will produce:

```
Product List:
1. Name: Laptop, Price: 1200.0, Stock: 50
```

---

## Technologies and Tools Used

- **ANTLR 4:** Lexer and parser generation.
- **Java/Python:** Backend for interpreting and executing commands.
- **SQLite/MySQL:** Database for storing entities.

---

## Setup and Usage

### Prerequisites:

- Install **Java (8 or later)**.
- Install **ANTLR 4**.

---

## File Structure

```
project-root/
|-- Grammar/                # Contains the DSL grammar (DSL.g4)
|-- GeneratedCodes/         # Contains code generated from the grammar
|-- CustomCodes/            # Custom implementations for interpreting commands
|-- Visualization/          # Modules for AST visualization
|-- README.md               # Documentation
|-- requirements.txt        # Python dependencies
|-- Main.py                 # Main entry point
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---