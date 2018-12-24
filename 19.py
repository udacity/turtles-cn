# # 19.列表和循环
# ## squiral.py
# 

# In[ ]:


import turtle

lengths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

dizzy = Turtle.Turtle()
dizzy.color("blue")
dizzy.width(5)

for length in lengths:
    dizzy.forward(length)
    dizzy.right(90)