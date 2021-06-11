from AmazonKilo.amazonkilo import AmazonKilo

product_url = "https://www.amazon.com/Razer-DeathAdder-Essential-Gaming-Mouse/dp/B07Y693ND1/ref=sr_1_4?dchild=1&keywords=gaming+mouse&pd_rd_r=60436fb0-8eed-4824-801b-dd9d1a33a1a3&pd_rd_w=beS8N&pd_rd_wg=N8gvK&pf_rd_p=5811f97a-f703-4231-aa5f-c344167bfe13&pf_rd_r=G61GZQY648MJNEEM7MVC&qid=1623391428&sr=8-4"

def price_tracker(target):
    while 1:
        product = client.get_product_detail_by_url(product_url)
        if product.price <= target:
            print("You got a offer on the {0} for {1}. Check out the product {2}".format(product.title, product.price, product_url))

client = AmazonKilo("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")
price_tracker(31)