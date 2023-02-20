#!/usr/bin/env python
# coding: utf-8

# In[69]:


import selenium
import pandas as pd
from selenium import webdriver
import requests


# In[70]:


driver = webdriver.Chrome(r"C:\Users\Raushan\Downloads\chromedriver_win32\chromedriver.exe")


# In[71]:


#driver = webdriver.Chrome("chromedriver.exe")


# In[72]:


page2 = requests.get('https://udyamregistration.gov.in/Udyam_Verify.aspx')
page2


# In[73]:


driver.get('https://udyamregistration.gov.in/Udyam_Verify.aspx')


# In[74]:


udyam_refno = driver.find_element('name',"ctl00$ContentPlaceHolder1$txtUdyamNo")
udyam_refno.send_keys("UDYAM-MH-01-0000002")
captcha = driver.find_element('name' , 'ctl00$ContentPlaceHolder1$txtCaptcha')
captcha.send_keys("LS21VS")
verify = driver.find_element('name' , 'ctl00$ContentPlaceHolder1$btnVerify')
verify.click()


# In[57]:


Udyam_info = []


# In[78]:


udyam_data = driver.find_element('xpath','//*[@id="divPrint"]/div/div/div')
udyam_data.text


# In[79]:


Udyam_info.append(udyam_data)


# In[80]:


Udyam_info


# In[47]:


get_ipython().system('pip install pytesseract')


# In[48]:


import cv2
import os,argparse
import pytesseract
from PIL import Image


# In[ ]:


# We import the necessary packages
#import the needed packages


#We then Construct an Argument Parser
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",
				required=True,
				help="Path to the image folder")
ap.add_argument("-p","--pre_processor",
				default="thresh",
				help="the preprocessor usage")
args=vars(ap.parse_args())

#We then read the image with text
images=cv2.imread(args["image"])

#convert to grayscale image
gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)

#checking whether thresh or blur
if args["pre_processor"]=="thresh":
	cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
if args["pre_processor"]=="blur":
	cv2.medianBlur(gray, 3)
	
#memory usage with image i.e. adding image to memory
filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

# show the output images
cv2.imshow("Image Input", images)
cv2.imshow("Output In Grayscale", gray)
cv2.waitKey(0)

