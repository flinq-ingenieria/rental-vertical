Rental Check Availability
====================================================


Summary
-------

Extends the sale_rental module for checking availability of the rented product.

Description
-----------

This module activates availability checks on stockable products related to rental services in
sale orders. In the base functionality only the total amount of products in stock is checked and user is
informed when the amount of products to rent out in a sale order is higher.

After the installation of this module the availability is checked in consideration of the total amount
of goods in stock and the amount of products used in concurrent sale orders at the certain desired timeframe.
In case of insufficient products in stock the user receives visual notification on respective sale order line
and can access the list of concurrent sale orders directly.


Usage
-----

To use this module, you need to:

#. Go to Rental Orders and create a new one.

#. Add a product available for being rented out in sale order line.

#. If there is not enough stock on hand to fullfil the order and
   possible concurrent ones the sale order line will be colorized.
   Yellow marks that there are concurrent quotations and red indicates
   concurrent orders.

#. To check the concurrent order for a critical sale order line just click
   on the inline button being displayed in the sale order line.

