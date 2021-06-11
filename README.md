# AmazonKilo

AmazonKilo is a library tool with small features for Amazon.

## Installation

Use the vcs [git](https://git-scm.com/downloads) to install AmazonKilo.

```
git clone https://github.com/CODPUD/AmazonKilo.git
```

After downloading install the requirement libraries
```bash
pip install -r requirements.txt
```

## Usage
Create a file main.py

```python
from AmazonKilo.amazonkilo import AmazonKilo

client = AmazonKilo("user-agent")
p = client.get_product_detail_by_url("product-link") #It gets information about a particular product
print(p.title) #prints the title
print(p.price) #prints the price
print(p.rating) #prints the rating 
```

```python
categories = client.get_categories() #It gets all existing categories
for c in categories:
    print(c.value) #Prints the value 
```

## TO-DO
- Search products by category
- Price tracker for multiple products
- Build a web app for tracking

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
