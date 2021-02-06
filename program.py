import cv2
import pytesseract,re
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img=cv2.imread('invoice.jpg')
text = pytesseract.image_to_string(img, lang='eng')
print(text)



d = pytesseract.image_to_data(img, output_type=Output.DICT)
keys = list(d.keys())

n_boxes = len(d['text'])

print("-------KEY VALUE PAIRS FROM THE GIVEN INVOICE----------")
#date pattern
date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
    	if re.match(date_pattern, d['text'][i]):
	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	        print("Date             :   " ,d['text'][i])

#Invoice_number pattern
invnum_pattern = '^[0-9]{5}$'
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
    	if re.match(invnum_pattern, d['text'][i]):
	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	        print("Invoice Number   :   " ,d['text'][i])

Name="Rep."
Contact="Phone"
Payment="Terms"
words=text.split()
for i,w in enumerate(words):
    if w==Name:
        print("Name of the Rep. :   ",words[i+1])
    if w==Contact:
        print("Contact Phone    :   ",words[i+1])

#Amount_Due pattern
amount_pattern = '^(\$[0-9]+(.[0-9]+)?)'
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
    	if re.match(amount_pattern, d['text'][i]):
	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	        print("Amount Due       :   " ,d['text'][i])
	        break

#email pattern
email_pattern='\S+@\S+'
print("\nBilling and shipping mail address:")
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
    	if re.match(email_pattern, d['text'][i]):
	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	        print("  ",d['text'][i])



#Grand total Extraction
keyword='Grand Total'
b_k,keyword,a_k=text.partition(keyword)
print("\nGrand Total      : ", a_k)

img=cv2.resize(img,(660,740))          
cv2.imshow('img', img)
cv2.waitKey(0)
