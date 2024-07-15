# Hash tables are a data structure that maps keys to values using a hash function.

# Hash table using dictionary
hash_table = {}

# Insert key-value pairs
hash_table['key1'] = 'value1'
hash_table['key2'] = 'value2'
print("Hash table:", hash_table)

# Access value by key
print("Value for 'key1':", hash_table['key1'])

# Remove key-value pair
del hash_table['key2']
print("Hash table after deletion:", hash_table)
