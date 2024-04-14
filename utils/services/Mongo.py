import requests;
import motor.motor_asyncio;


class Mongo:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):

        self.mongoClient = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URL);
        self.db = self.mongoClient.get_database("ecommerce");
        self.products = self.db.get_collection("products");
        pass


    @staticmethod
    def get_instance():
        if not Mongo._instance:
            Mongo._instance = Mongo()
        return Mongo._instance

    async def get_data(self, action, filter):
        try:
            query = {
                "category": filter["category"] if filter.get("category") else None,
                "brand": filter["brand"] if filter.get("brand") else None,
                "model": filter["model"] if filter.get("model") else None,
                "stock": {"$gt": 0} if filter.get("availability") == "in stock" else 0 if filter.get("availability") == "out of stock" else None,
                "price": {
                    "$gte": 0,
                    "$lt": 100 if filter.get("price-range") == "0-100" else
                           200 if filter.get("price-range") == "100-200" else
                           300 if filter.get("price-range") == "200-300" else
                           400 if filter.get("price-range") == "300-400" else
                           500 if filter.get("price-range") == "400-500" else
                           600 if filter.get("price-range") == "500-600" else
                           700 if filter.get("price-range") == "600-700" else
                           800 if filter.get("price-range") == "700-800" else
                           900 if filter.get("price-range") == "800-900" else
                           1000 if filter.get("price-range") == "900-1000" else
                           {"$gte": 1000} if filter.get("price-range") else None
                } if filter.get("price-range") else None
            }
            
            # Avoid empty string values in the query
            query = {k: v for k, v in query.items() if v is not None and v != ""}


            # console.log("query", query)
            print(action, query)
            match action:
                # Que marcas de la categoria laptops se encuentran en stock
                case "brands_in_stock":
                    products = await self.products.distinct("brand", query);
                case "count_brands":
                    products = await self.products.distinct("brand", query);
                case "price":
                    products = await self.products.find(query).to_list(1000);
                case "recommend":
                    products = await self.products.find(query).to_list(1000);
                case "count_stock": # *DONE
                    products = await self.products.find(query).to_list(1000);
                case "specifications":
                    products = await self.products.find(query).to_list(1000);


            return products;
    

        except requests.exceptions.RequestException as e:
            # Handle exception here
            print("An error occurred:", e)
            return None
    
    async def add_product(self, product):
        try:
            new_product = await self.products.insert_one(product);
            return new_product;
        except requests.exceptions.RequestException as e:
            # Handle exception here
            print("An error occurred:", e)
            return None