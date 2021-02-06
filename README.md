# OCR_for_an_invoice

This is a python code to extract key value features from a given invoice using OCR.

The output involves :

- "The Squeezed text" - The invoice image text.
- The key features list.
- The output image which show important key features highlighted such as 
	Date, Invoice number, Amount due , Billing and Shipping address.


The pytessract function uses "image to string" function to extract the text from the invoice.
Using the "text.split()" function Name of the Reciepient and Contact phone number have
 been extracted. Using "partition()" function the Grand total value has been extracted.  
The next string is also outputto make it look better. The other features (that are considered
 important and neded to be displayed) have been detected in the invoice and highlighted(via 
a output image of the invoice) having boxes around them to ease it in real time applications.


All the extracted key features have been displayed on the output screen in the form of a list.
