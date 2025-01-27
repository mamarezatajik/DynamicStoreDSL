# DSL for Online Store Management using ANTLR

This project implements a **Domain-Specific Language (DSL)** designed for managing an online store. The DSL simplifies operations such as creating, deleting, updating, and listing entities like products and users. The language is implemented using **ANTLR 4** and provides an efficient way for store administrators to manage their inventory, discounts, and more.

---

## Features

1. **Define Entities**: Allows defining new entities like `Product`, `Order`, and `Customer` with specific attributes.
2. **Create Entities**: Enables creating new instances of entities with specified values.
3. **Update Entities**: Supports updating attributes of existing entities.
4. **Delete Entities**: Facilitates deletion of entities using a unique identifier.
5. **List Entities**: Provides a list of all instances of a specific entity.
6. **Apply Discounts**: Simplifies applying discounts to products in the inventory.

---

## Usage

### Sample Input
Define a new product and create an instance:

```dsl
define {
    entity: product,
    attributes: { name: String, price: Float, stock: Integer }
}

create {
    entity: product,
    attributes: { name: "Laptop", price: 1200.0, stock: 50 }
}
```


├── Grammar
│   └── StoreDSL.g4        # ANTLR grammar file for the DSL
├── GeneratedCodes
│   ├── StoreDSLLexer.py   # Generated lexer
│   ├── StoreDSLParser.py  # Generated parser
├── CustomCodes
│   ├── interpreter.py     # Code for interpreting parsed inputs
│   ├── generator.py       # Code generator for the DSL
├── Visualization
│   ├── ast_visualizer.py  # Visualize the AST using networkx
│   ├── subtree_creator.py # Extract and visualize subtrees from the AST
├── tests
│   └── test_cases.dsl     # Example test cases for the DSL
└── main.py                # Main entry point for running the project