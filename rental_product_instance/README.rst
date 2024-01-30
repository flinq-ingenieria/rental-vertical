Rental Product Instance
====================================================


Summary
-------

Add product instances identified by serial number as unique rented objects

Description
-----------

This module extends the product data model in order to mark them as unique product instances 
that are traced by serial number. You might have several instances of a product but they are 
in different conditions or are somehow unique like machines, vehicles or maybe 'used' products.

In order to track the condition history of a product instance you can add operating data, e.g.
you can save the mileage of vehicles or the operating hours of machines.


Usage
-----

- Install the module.
- Create a stockable product.
- Mark the product as product instance.
- Save the product and set an unique serial number.
  Hint: Make an inventory adjustment, if needed.
- Set a product category that can be configured to either use mileage or operating hours as condition.
- Go to the smartbutton for operating data, create the current condition and update it regularly.


