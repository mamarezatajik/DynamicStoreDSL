import requests

# Base URL of the Flask backend
BASE_URL = 'http://127.0.0.1:5000'

# Helper function to send requests
def send_request(endpoint, method='GET', data=None):
    url = f"{BASE_URL}/{endpoint}"
    if method == 'GET':
        response = requests.get(url, params=data)
    elif method == 'POST':
        response = requests.post(url, json=data)
    else:
        raise ValueError("Unsupported HTTP method")
    
    print(f"Response from {url}: {response.status_code}")
    if response.status_code == 200:
        print(response.json())
    return response

# Test flow
def test_flow():
    # Create a product
    print("\nCreating a product...")
    send_request('createProduct', method='POST', data={"command": 'createProduct("1", "Laptop", "999.99", "High-end gaming laptop", "Electronics")'})

    # List products
    print("\nListing products...")
    send_request('listProducts')

    # Update product stock
    print("\nUpdating product stock...")
    send_request('updateStock', method='POST', data={"command": 'updateStock("1", "10")'})

    # Check product stock
    print("\nChecking product stock...")
    send_request('checkStock', data={"product_id": "1"})

    # Apply discount to product
    print("\nApplying discount to product...")
    send_request('applyDiscount', method='POST', data={"command": 'applyDiscount("1", "15.0")'})

    # Generate product report
    print("\nGenerating product report...")
    send_request('generateReport', data={"report_type": "products"})

    # Create a user
    print("\nCreating a user...")
    send_request('createUser', method='POST', data={"command": 'createUser("1", "John Doe", "john@example.com", "password123")'})

    # List users
    print("\nListing users...")
    send_request('listUsers')

    # Update user
    print("\nUpdating user...")
    send_request('updateUser', method='POST', data={"command": 'updateUser("1", "John Doe Updated", "john_updated@example.com", "newpassword123")'})

    # Delete user
    print("\nDeleting user...")
    send_request('deleteUser', method='POST', data={"command": 'deleteUser("1")'})

    # List users after deletion
    print("\nListing users after deletion...")
    send_request('listUsers')

    # Delete product
    print("\nDeleting product...")
    send_request('deleteProduct', method='POST', data={"command": 'deleteProduct("1")'})

    # List products after deletion
    print("\nListing products after deletion...")
    send_request('listProducts')

if __name__ == '__main__':
    test_flow()