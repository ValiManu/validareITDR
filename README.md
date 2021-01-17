# validareITDR

## 1. change structure
* display stock in dashboard
* display user in dashboard
* sorting the store according to the logged in user

## 2. new app Transactions: branches => transactions
* database refactoring
    * Users (name, password, email)
    * Shops (name, address, user, shops_network)
    * Address (city, street, street_no)
    * Products (name, url_img, active_product)
    * ShopsNetwork (name, cif)
    * Promotional Campaign (name, start_date, end_date, shops_network, product, active_campaign)
    * Sales (ticket_no, ticket_date, shop, prize)
    * ProductsSold (sale, product, quantity)
    * Awards:Products (quantity, shop)
* developing the interface for entering the ticket number
* display products sold
* cleaning the static folder
* testing the first ajax request

## 3. ticket validation branches => ticket
* field validation
* form wizard manually restored
* the mechanics of awarding prizes according to the products sold
* display transactions in the dashboard

## 4. eng_version
* field display formatting
* change user interface in English
* change database logic
* zero prize stock management
* delete unnecessary files
