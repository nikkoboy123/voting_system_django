from django.core.management.utils import get_random_secret_key

# Generate a random secret key
secret_key = get_random_secret_key()

# Print the generated secret key
print(secret_key)
