from kinetic_sdk import Keypair

alice_key = [205, 213, 7, 246, 167, 206, 37, 209, 161, 129, 168, 160, 90, 103, 198, 142, 83, 177, 214, 203, 80, 29, 71, 245,
     56, 152, 15, 8, 235, 174, 62, 79, 138, 198, 145, 111, 119, 33, 15, 237, 89, 201, 122, 89, 48, 221, 224, 71, 81,
     128, 45, 97, 191, 105, 37, 228, 243, 238, 130, 151, 53, 221, 172, 125]
alice_keypair = Keypair.from_byte_array(alice_key)
alice_account = 'ALisrzsaVqciCxy8r6g7MUrPoRo3CpGxPhwBbZzqZ9bA'
alice_token_account = 'Ebq6K7xVh6PYQ8DrTQnD9fC91uQiyBMPGSV6JCG6GPdD'

bob_account = 'BobQoPqWy5cpFioy1dMTYqNH9WpC39mkAEDJWXECoJ9y'
bob_token_account = '92gcR7aBdZDGvoC1cCSTSzQDediBZecy32B43mJtuUXT'
charlie_account = 'CharYfTvJSiH6LtDpkGUiVVZmeCn5Cenu2TzdJSbDJnG'

default_mint = 'MoGaMuJnB3k8zXjBYBnHxHG47vWcW3nyb7bFYvdVzek'
fee_payer = 'oWNEYV3aMze3CppdgyFAiEj9xUJXkn85es1KscRHt8m'
