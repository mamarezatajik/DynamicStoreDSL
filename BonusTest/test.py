import unittest
import requests

# Base URL of the Flask backend
BASE_URL = 'http://127.0.0.1:5000'

class TestStoreDSLBackend(unittest.TestCase):
    def setUp(self):
        """Clear any existing data before each test."""
        # Delete all products and users
        self._delete_all_products()
        self._delete_all_users()

    def _delete_all_products(self):
        """Helper function to delete all products."""
        products = requests.get(f"{BASE_URL}/listProducts").json()
        for product in products:
            requests.post(f"{BASE_URL}/deleteProduct", json={"command": f'deleteProduct("{product["id"]}")'})

    def _delete_all_users(self):
        """Helper function to delete all users."""
        users = requests.get(f"{BASE_URL}/listUsers").json()
        for user in users:
            requests.post(f"{BASE_URL}/deleteUser", json={"command": f'deleteUser("{user["id"]}")'})

    def test_create_and_list_products(self):
        """Test creating a product and listing it."""
        # Create a product
        response = requests.post(
            f"{BASE_URL}/createProduct",
            json={"command": 'createProduct("1", "Laptop", "999.99", "High-end gaming laptop", "Electronics")'}
        )
        self.assertEqual(response.status_code, 201)

        # List products
        response = requests.get(f"{BASE_URL}/listProducts")
        self.assertEqual(response.status_code, 200)
        products = response.json()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]["name"], "Laptop")

    def test_update_product(self):
        """Test updating a product."""
        # Create a product
        requests.post(
            f"{BASE_URL}/createProduct",
            json={"command": 'createProduct("1", "Laptop", "999.99", "High-end gaming laptop", "Electronics")'}
        )

        # Update the product
        response = requests.post(
            f"{BASE_URL}/updateProduct",
            json={"command": 'updateProduct("1", "Updated Laptop", "899.99", "Mid-range laptop", "Electronics")'}
        )
        self.assertEqual(response.status_code, 200)

        # Verify the update
        response = requests.get(f"{BASE_URL}/listProducts")
        products = response.json()
        self.assertEqual(products[0]["name"], "Updated Laptop")
        self.assertEqual(products[0]["price"], 899.99)

    def test_delete_product(self):
        """Test deleting a product."""
        # Create a product
        requests.post(
            f"{BASE_URL}/createProduct",
            json={"command": 'createProduct("1", "Laptop", "999.99", "High-end gaming laptop", "Electronics")'}
        )

        # Delete the product
        response = requests.post(
            f"{BASE_URL}/deleteProduct",
            json={"command": 'deleteProduct("1")'}
        )
        self.assertEqual(response.status_code, 200)

        # Verify deletion
        response = requests.get(f"{BASE_URL}/listProducts")
        products = response.json()
        self.assertEqual(len(products), 0)

    def test_create_and_list_users(self):
        """Test creating a user and listing it."""
        # Create a user
        response = requests.post(
            f"{BASE_URL}/createUser",
            json={"command": 'createUser("1", "John Doe", "john@example.com", "password123")'}
        )
        self.assertEqual(response.status_code, 201)

        # List users
        response = requests.get(f"{BASE_URL}/listUsers")
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]["user_name"], "John Doe")

    def test_update_user(self):
        """Test updating a user."""
        # Create a user
        requests.post(
            f"{BASE_URL}/createUser",
            json={"command": 'createUser("1", "John Doe", "john@example.com", "password123")'}
        )

        # Update the user
        response = requests.post(
            f"{BASE_URL}/updateUser",
            json={"command": 'updateUser("1", "John Doe Updated", "john_updated@example.com", "newpassword123")'}
        )
        self.assertEqual(response.status_code, 200)

        # Verify the update
        response = requests.get(f"{BASE_URL}/listUsers")
        users = response.json()
        self.assertEqual(users[0]["user_name"], "John Doe Updated")
        self.assertEqual(users[0]["user_email"], "john_updated@example.com")

    def test_delete_user(self):
        """Test deleting a user."""
        # Create a user
        requests.post(
            f"{BASE_URL}/createUser",
            json={"command": 'createUser("1", "John Doe", "john@example.com", "password123")'}
        )

        # Delete the user
        response = requests.post(
            f"{BASE_URL}/deleteUser",
            json={"command": 'deleteUser("1")'}
        )
        self.assertEqual(response.status_code, 200)

        # Verify deletion
        response = requests.get(f"{BASE_URL}/listUsers")
        users = response.json()
        self.assertEqual(len(users), 0)

    def test_update_stock(self):
        """Test updating product stock."""
        # Create a product
        requests.post(
            f"{BASE_URL}/createProduct",
            json={"command": 'createProduct("1", "Laptop", "999.99", "High-end gaming laptop", "Electronics")'}
        )

        # Update stock
        response = requests.post(
            f"{BASE_URL}/updateStock",
            json={"command": 'updateStock("1", "10")'}
        )
        self.assertEqual(response.status_code, 200)

        # Verify stock update
        response = requests.get(f"{BASE_URL}/checkStock", params={"product_id": "1"})
        self.assertEqual(response.json()["stock"], 10)

    def test_apply_discount(self):
        """Test applying a discount to a product."""
        # Create a product
        requests.post(
            f"{BASE_URL}/createProduct",
            json={"command": 'createProduct("1", "Laptop", "999.99", "High-end gaming laptop", "Electronics")'}
        )

        # Apply discount
        response = requests.post(
            f"{BASE_URL}/applyDiscount",
            json={"command": 'applyDiscount("1", "15.0")'}
        )
        self.assertEqual(response.status_code, 200)

        # Verify discount
        response = requests.get(f"{BASE_URL}/generateReport", params={"report_type": "products"})
        products = response.json()
        self.assertEqual(products[0]["discount"], 15.0)

if __name__ == '__main__':
    unittest.main()