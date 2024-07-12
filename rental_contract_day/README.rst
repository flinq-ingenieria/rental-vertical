Rental Contract Month
====================================================


Summary
-------

Extension of module rental_contract and rental_pricelist

Description
-----------

During longtime rentals, it is often required to write invoices in regular intervals.
This is possible with the contract module, which is here extended to support rental
use cases in extension to purchase and sale use cases.

If a product is rentable in months, the related rental service is automatically 
considered as a contract and linked to the standard customer contract template.
If you add this monthly rental service in a sale order and confirm it, a contract 
is automatically created.


Usage
-----

- Create a stockable product and mark it as rentable in months.
  The automatically created rental service has the flag 'Is a contract' = True.
- Create a sale order, add the rental service and confirm the order.
  A contract is automatically created.

This module is automatically installed when all of the following modules are installed in a database:

 - rental_contract
 - rental_pricelist


